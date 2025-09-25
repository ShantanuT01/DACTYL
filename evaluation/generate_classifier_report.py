import pandas as pd
from libauc.metrics import pauc_roc_score
from sklearn.metrics import roc_auc_score, average_precision_score, roc_curve
import numpy as np
np.int = np.int64
from collections import defaultdict
# constants

TPAUC = "tpAUC"
PAUC = "pAUC"
AUC = "AUC"
AP = "AP"
METRIC_COLS = [TPAUC, PAUC, AUC, AP]

TARGET = "target"
DOMAIN = "domain"
MODEL = "model"
HUMAN = "human"
CATEGORY = "category"
META_LLAMA_321B = "meta-llama/Llama-3.2-1B-Instruct"
ADVERSE_FPR = 0.3
ADVERSE_TPR = 0.4

NON_ADVERSE_FPR = 0.05
NON_ADVERSE_TPR = 0.8

REAL = "-real-"
FAKE = "-fake-"
REAL_CATEGORY = "real"
NEWS_OUTLET = "news_outlet"
TOPIC = "topic"
CLASSIFIERS = ["piratexx", "binoculars","desklib","e5lora","daigt","fakespot","mage","pangram","superannotate"]
CLASSIFIERS_PRETTY_NAMES = ["AICD","Binoculars","Desklib","e5-LoRA","DAIGT","Fakespot","MAGE","Pangram","SuperAnnotate"]
CLASSIFIERS = dict(zip(CLASSIFIERS, CLASSIFIERS_PRETTY_NAMES))
DACTYL_TRAINED_CLASSIFIERS = {'dactyl-bert-tiny-finetuned': 'BERT Tiny(DXO)', 'dactyl-bert-tiny-pretrained': 'BERT Tiny(BCE)', 'dactyl-tinybert-finetuned': 'TinyBERT(DXO)', 'dactyl-tinybert-pretrained': 'TinyBERT(BCE)', 'dactyl-distilroberta-base-finetuned': 'distilRoBERTa-base(DXO)', 'dactyl-distilroberta-base-pretrained': 'distilRoBERTa-base(BCE)', 'dactyl-modernbert-base-finetuned': 'ModernBERT-base(DXO)', 'dactyl-modernbert-base-pretrained': 'ModernBERT-base(BCE)', 'dactyl-deberta-v3-large-finetuned': 'DeBERTa-V3-large(DXO)', 'dactyl-deberta-v3-large-pretrained': 'DeBERTa-V3-large(BCE)'}
CLASSIFIER = "Classifier"
DOMAINS = ["tweets","reviews","abstracts","news","student_essays","RedditWritingPrompts"]
DOMAIN_PRETTY_NAMES =  ["Tweets","Reviews","Abstracts","News","Essays","CW"]
DOMAINS = dict(zip(DOMAINS, DOMAIN_PRETTY_NAMES))

def get_predictions_for_classifier(classifier):
    if classifier in CLASSIFIERS:
        non_adv_df = pd.read_parquet(f"nonadversarial-results/baselines/{classifier}-results.parquet")
        adv_df = pd.read_parquet(f"adversarial-results/baselines/{classifier}-results.parquet")
    else:
        non_adv_df = pd.read_parquet(f"nonadversarial-results/dactyl-trained/{classifier}-results.parquet")
        adv_df = pd.read_parquet(f"adversarial-results//dactyl-trained/{classifier}-results.parquet")
    non_adv_df = non_adv_df.dropna(subset=[f"{classifier}_pred"])
    adv_df = adv_df.dropna(subset=[f"{classifier}_pred"])
    return non_adv_df, adv_df

def get_ood_predictions_for_classifier(classifier):
    ood_df = pd.read_parquet(f"ood-results/{classifier}-results.parquet")
    ood_df = ood_df.dropna(subset=[f"{classifier}_pred"])
    return ood_df


def compute_metrics(max_fpr, min_tpr, y_true, y_pred):
    tpauc = pauc_roc_score(y_true=y_true, y_pred=y_pred, max_fpr=max_fpr, min_tpr=min_tpr)
    pauc = roc_auc_score(y_true=y_true, y_score=y_pred, max_fpr=max_fpr)
    ap = average_precision_score(y_true=y_true, y_score=y_pred,pos_label=1)
    auc = roc_auc_score(y_true=y_true, y_score=y_pred)

    return {
        TPAUC: tpauc,
        PAUC: pauc,
        AP: ap,
        AUC: auc
    }

def compute_metrics_by_llm_factor(column, df, score_col):
    human_df = df[df.target == 0]
    ai_df = df[df.target == 1]
    groups = ai_df.groupby(column)
    results = list()
    for group, sf in groups:
        eval_df = pd.concat([sf, human_df])
        y_true = eval_df.target
        y_pred = eval_df[score_col]
        result = compute_metrics(NON_ADVERSE_FPR, NON_ADVERSE_TPR, y_true, y_pred)
        result[column] = group
        results.append(result)
    results = pd.DataFrame(results)
    results = results[[column] + METRIC_COLS]
    results[METRIC_COLS] *= 100
    results = results.sort_values(METRIC_COLS)
    return results.round(2)

def compute_metrics_by_domain_and_model(df, score_col):
    human_df = df[df.target == 0]
    ai_df = df[df.target == 1]
    groups = ai_df.groupby([DOMAIN, MODEL])
    results = list()
    for group, sf in groups:
        human_df_set = human_df[(human_df.domain == group[0])]
        eval_df = pd.concat([sf, human_df_set])
        y_true = eval_df.target
        y_pred = eval_df[score_col]
        result = compute_metrics(NON_ADVERSE_FPR, NON_ADVERSE_TPR, y_true, y_pred)

        result[DOMAIN] = group[0]
        result[MODEL] = group[1]

        results.append(result)
    results = pd.DataFrame(results)
    results = results[[DOMAIN, MODEL] + METRIC_COLS]
    results[METRIC_COLS] *= 100
    results = results.sort_values(METRIC_COLS)
    return results

def compute_metrics_by_factor(column, df, score_col):
    categories = df.groupby(column)
    results = list()
    for category, cdf in categories:
        y_true = cdf[TARGET]
        y_pred = cdf[score_col]
        result = compute_metrics(NON_ADVERSE_FPR, NON_ADVERSE_TPR, y_true, y_pred)
        result[column] = category
        results.append(result)
    results = pd.DataFrame(results)
    results = results[[column] + METRIC_COLS]
    results[METRIC_COLS] *= 100
    #results = results.sort_values(METRIC_COLS)
    return results.round(2)

    
def tweets_report(tweets_df,score_col):
    # block by troll category
    return compute_metrics_by_factor(CATEGORY, tweets_df, score_col)


def reviews_report(reviews_df, score_col):
    star_ratings = list()
    for category in reviews_df[CATEGORY]:
        star_ratings.append(int(category.split("-")[-1]))
    reviews_df["stars"] = star_ratings
    return compute_metrics_by_factor("stars", reviews_df, score_col)
   
def abstracts_report(abstracts_df, score_col):
    return compute_metrics_by_factor(CATEGORY, abstracts_df, score_col)


def news_report(news_df, score_col):
    # split by real vs fake, news topic, and news outlet
    reals = list()
    topics = list()
    news_outlets = list()
    for _, row in news_df.iterrows():
        if row[TARGET] == 1:
            found = None
            if row[CATEGORY].find(REAL) >= 0:
                reals.append("real")
                found = REAL
            elif row[CATEGORY].find(FAKE) >= 0:
                reals.append("fake")
                found = FAKE
            topic, news_outlet = row[CATEGORY].replace("ISOT/","").split(found)
            topics.append(topic)
            news_outlets.append(news_outlet)
        else:
            if row[CATEGORY].find(REAL[0:-1]) >= 0:
                reals.append("real")
                found = REAL
            elif row[CATEGORY].find(FAKE[0:-1]) >= 0:
                reals.append("fake")
                found = FAKE
            topic = row[CATEGORY].replace("ISOT/","").replace(found[0:-1],"").strip()
            topics.append(topic)
            news_outlets.append(None)

    news_df[REAL.strip("-")] = reals
    news_df["topic"] = topics
    news_df["news_outlet"] = news_outlets
    categories_to_split_on = [REAL.strip("-"),"topic","news_outlet"]
    results_dfs = [compute_metrics_by_factor(col, news_df, score_col) for col in categories_to_split_on[0:2]]
    results_dfs.append(compute_metrics_by_llm_factor("news_outlet", news_df, score_col))
    return results_dfs

def get_domain_performance(pred_df, score_col):
    return compute_metrics_by_factor(DOMAIN, pred_df, score_col)

def student_essays_report(essay_df, score_col):
    subset = list()
    for category in essay_df[CATEGORY]:
        if category.lower().find("ellipse") == 0:
            subset.append("ELLIPSE")
        elif category.lower().find("ivy") == 0:
            subset.append("Ivy Panda")
        else:
            raise Exception(category)
    essay_df["subset"] = subset
    subsets = essay_df.groupby("subset")
    ellipse_frame = subsets.get_group("ELLIPSE")
    ivy_panda_frame = subsets.get_group("Ivy Panda")
    human_ellipse, ai_ellipse = ellipse_frame[ellipse_frame.target == 0], ellipse_frame[ellipse_frame.target == 1]
    #print(len(human_ellipse), len(ai_ellipse))
    human_ivy, ai_ivy = ivy_panda_frame[ivy_panda_frame.target == 0], ivy_panda_frame[ivy_panda_frame.target == 1]
    #print(len(human_ivy), len(ai_ivy))
    test1 = pd.concat([human_ellipse, ai_ivy])
    test1["subset"] = "ELLIPSE(Human)+\nIvy Panda (AI)"
    test2 = pd.concat([human_ivy, ai_ellipse])
    test2["subset"] = "Ivy Panda(Human)+\nELLIPSE (AI)"
    essay_df = pd.concat([essay_df,test1, test2])
    return compute_metrics_by_factor("subset", essay_df, score_col)

def adversarial_report(adversarial_df, non_adversarial_df, score_col):
    df = adversarial_df
    non_df = non_adversarial_df
    non_df = non_df[non_df.target == 0]
    adv_df = pd.concat([df, non_df])
    domains = adv_df.groupby(DOMAIN)
    rows = list()
    for domain, ddf in domains:
        models = ddf[MODEL].unique()
        for model in models:
            if model == HUMAN:
                continue
            sf = pd.concat([ddf[ddf.target == 0], ddf[ddf.model == model]])
            row = compute_metrics(ADVERSE_FPR, ADVERSE_TPR, sf[TARGET],sf[score_col])
            row[DOMAIN] = domain
            row[MODEL] = model
            rows.append(row)
    results = pd.DataFrame(rows)
    results = results[[MODEL, DOMAIN] + METRIC_COLS]
    results = results.sort_values([DOMAIN] + METRIC_COLS)
    results[METRIC_COLS] *= 100
    return results.round(2)

def get_difference_from_cpt_and_base(results, metric):
    domains = results.groupby(DOMAIN)
    row = dict()
    for domain, df in domains:
        cpt = df[df[MODEL].str.contains("fine-tuned")][metric].values[0]
        base = df[df[MODEL].str.contains("meta-llama/")][metric].values[0]
        row[DOMAINS[domain]] = cpt - base
    return row

def get_non_adversarial_performance(df, score_col):
    df = df.dropna(subset=[score_col])
    df["classifier"] = score_col.replace("_pred","")
    overall = compute_metrics_by_factor("domain", df, score_col)
    return overall

def make_classifier_report(classifier_name):
    non_adv_df, adv_df = get_predictions_for_classifier(classifier)
    score_col = f"{classifier_name}_pred"
    adv_df = adv_df.dropna(subset=[score_col])
    non_adv_df = non_adv_df.dropna(subset=[score_col])
    lines = list()
    lines.append(f"# {classifier_name} - DACTYL Results\n\n")
    lines.append(f"Unless otherwise specified, TPAUC is {NON_ADVERSE_FPR * 100}% FPR and {NON_ADVERSE_TPR * 100}% TPR.\n\n")
    lines.append(f"## Overall\n\n")
    
    non_adv_df["dataset"] = "test"
    adv_df["dataset"] = "test-finetuning"   
    one_b_df = adv_df[adv_df.model == "meta-llama/Llama-3.2-1B-Instruct"] 
    one_b_df["dataset"] = "test-1b-no-finetuning"
    all_data = pd.concat([non_adv_df, adv_df[adv_df.model != "meta-llama/Llama-3.2-1B-Instruct"], one_b_df])
    overall = compute_metrics_by_llm_factor("dataset", all_data, score_col)
    #all_data = pd.concat([non_adv_df, adv_df[adv_df.model != "meta-llama/Llama-3.2-1B-Instruct"]])
    lines.append(overall.to_markdown(index=False)+"\n")
    lines.append("### Domain Performance\n\n")
    lines.append(get_domain_performance(all_data, score_col).to_markdown(index=False) + "\n\n")
    lines.append("### Model Performance\n\n")
    lines.append(compute_metrics_by_llm_factor(MODEL, all_data, score_col).sort_values(METRIC_COLS).to_markdown(index=False) +"\n\n")
    
    lines.append("## Nonadversarial Results\n\n")
    lines.append("### Domain\n\n")
    lines.append(get_domain_performance(non_adv_df, score_col).to_markdown(index=False) + "\n\n")
    lines.append("### Tweets\n\n")
    lines.append(tweets_report(non_adv_df[non_adv_df.domain == "tweets"], score_col).to_markdown(index=False) +"\n\n")

    lines.append("### Reviews\n\n")
    lines.append(reviews_report(non_adv_df[non_adv_df.domain == "reviews"], score_col).to_markdown(index=False) +"\n\n")

    lines.append("### Abstracts\n\n")
    lines.append(abstracts_report(non_adv_df[non_adv_df.domain == "abstracts"], score_col).to_markdown(index=False) +"\n\n")

    lines.append("### News\n\n")
    news_results = [rdf.to_markdown(index=False) +"\n\n" for rdf in news_report(non_adv_df[non_adv_df.domain == "news"], score_col)]
    lines.extend(news_results)
    
    lines.append("### Student Essays\n\n")
    lines.append(student_essays_report(non_adv_df[non_adv_df.domain == "student_essays"], score_col).to_markdown(index=False) + "\n\n")
    
    lines.append("## Adversarial Results\n\n")
    lines.append(f"TPAUC is {ADVERSE_FPR * 100}% FPR and {ADVERSE_TPR * 100}% TPR.\n\n")
    adv_report = adversarial_report(adv_df, non_adv_df, score_col).sort_values(METRIC_COLS)
    lines.append(adv_report.to_markdown(index=False) + "\n\n")
    check = "✅"
    x_mark = "❌" 
  
    
    model_order = adv_report[MODEL].to_list()
    base_model_order = list(adv_report[[MODEL, DOMAIN]].values)
    base_model_order = [list(arr) for arr in base_model_order]
    top_row = {"Type": "Finetuned"}
    bottom_row = {"Type": "Base"}
    for domain in ["tweets","reviews","abstracts","news","student_essays","RedditWritingPrompts"]:
        finetuned_rank = model_order.index(f"USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-{domain}-testing")
        base_rank = base_model_order.index([META_LLAMA_321B, domain])
        if finetuned_rank < base_rank:
            top_row[domain] = check
            bottom_row[domain] = x_mark
        else:
            bottom_row[domain] = check
            top_row[domain] = x_mark

    lines.append(pd.DataFrame([top_row, bottom_row]).to_markdown(index=False)+"\n\n")
    
    
    with open(f"reports/{classifier_name}.md",'w+') as f:
        f.writelines(lines)


if __name__ == "__main__":
    NON_ADVERSE_TPR = 0.8
    for classifier in DACTYL_TRAINED_CLASSIFIERS:
        make_classifier_report(classifier)
    NON_ADVERSE_TPR = 0.5
    for classifier in CLASSIFIERS:
        make_classifier_report(classifier)