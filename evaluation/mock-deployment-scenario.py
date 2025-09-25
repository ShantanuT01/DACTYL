import pandas as pd
from sklearn.metrics import roc_curve, precision_recall_curve, f1_score
import numpy as np
from generate_classifier_report import META_LLAMA_321B, get_ood_predictions_for_classifier
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, f1_score
from torcheval.metrics.functional import binary_recall_at_fixed_precision, binary_precision
import torch

# Implementation optimized from Krishna et al, 2023.
def get_threshold_for_fixed_fpr(y_true, y_score, max_fpr):
    fpr, tpr, thresholds = roc_curve(y_true, y_score)
    target_index = np.searchsorted(fpr, max_fpr)
    if fpr[target_index] > max_fpr:
        target_index -= 1
    return thresholds[target_index], fpr[target_index], tpr[target_index]

def get_threshold_for_recall_at_fixed_precision(y_true, y_score, min_precision):
    recall, threshold = binary_recall_at_fixed_precision(target=torch.tensor(y_true.values), input=torch.tensor(y_score.values),min_precision=min_precision)
    recall = recall.item()
    precision = binary_precision(input=torch.tensor(y_score.values), target=torch.tensor(y_true.values), threshold=threshold).item()
    return threshold.item(), recall, precision




def get_results_by_roc_curve(y_true, y_score,max_fpr, y_true_test, y_scores_test):
    # use roc curve on validation set in this case our test set
    threshold, fpr_test, tpr_test = get_threshold_for_fixed_fpr(y_true, y_score, max_fpr)
    y_pred_test = [1 if score >= threshold else 0 for score in y_score]
    y_pred = [1 if score >= threshold else 0 for score in y_scores_test]
    precision_test = precision_score(y_true=y_true, y_pred=y_pred_test) * 100
    recall_test = recall_score(y_true=y_true, y_pred=y_pred_test) * 100
    f1_test = f1_score(y_true=y_true, y_pred=y_pred_test, average='macro') * 100

    precision = precision_score(y_true=y_true_test, y_pred=y_pred) * 100
    recall = recall_score(y_true=y_true_test, y_pred=y_pred) * 100
    f1 = f1_score(y_true=y_true_test, y_pred=y_pred, average='macro') * 100

    cm = confusion_matrix(y_true=y_true_test, y_pred=y_pred)
    fpr = (cm[0][1]/np.sum(cm[0, :])) * 100
    return {
        "Method": f"TPR@FPR={max_fpr * 100}%",
        "Test FPR": fpr_test*100,
        "Test TPR/Recall": tpr_test*100,
        "Test Precision": precision_test,
        "Test TPR/Recall": recall_test,
        "Test macro-F1": f1_test,
        "Precision": precision,
        "TPR/Recall": recall,
        "Macro-F1 Score": f1,
        "FPR": fpr,
        "Threshold": threshold*100,
        "CM": list(cm)
    }




def get_results_given_threshold(y_true, y_score,threshold, y_true_test, y_scores_test):
    # use roc curve on validation set in this case our test set
    #threshold, fpr_test, tpr_test = threshold_at_fixed_fpr(y_true, y_score, max_fpr)
    y_pred_test = [1 if score >= threshold else 0 for score in y_score]
    y_pred = [1 if score >= threshold else 0 for score in y_scores_test]
    precision_test = precision_score(y_true=y_true, y_pred=y_pred_test) * 100
    recall_test = recall_score(y_true=y_true, y_pred=y_pred_test) * 100
    f1_test = f1_score(y_true=y_true, y_pred=y_pred_test, average='macro') * 100
    cm = confusion_matrix(y_true=y_true, y_pred=y_pred_test)
    fpr_test = (cm[0][1] / np.sum(cm[0, :])) * 100
    tpr_test = (cm[1][1] / np.sum(cm[1, :])) * 100
    precision = precision_score(y_true=y_true_test, y_pred=y_pred) * 100
    recall = recall_score(y_true=y_true_test, y_pred=y_pred) * 100
    f1 = f1_score(y_true=y_true_test, y_pred=y_pred, average='macro') * 100

    cm = confusion_matrix(y_true=y_true_test, y_pred=y_pred)
    fpr = (cm[0][1]/np.sum(cm[0, :])) * 100
    return {
        "Method": f"Threshold={threshold * 100}",
        "Test FPR": fpr_test,
        "Test Precision": precision_test,
        "Test TPR/Recall": tpr_test,
        "Test macro-F1": f1_test,
        "Precision": precision,
        "TPR/Recall": recall,
        "Macro-F1 Score": f1,
        "FPR": fpr,
        "Threshold": threshold*100,
        "CM": list(cm)
    }


def get_results_by_prc_curve(y_true, y_score,min_precision, y_true_test, y_scores_test):
    # use roc curve on validation set in this case our test set
    threshold,recall_test, precision_test = get_threshold_for_recall_at_fixed_precision(y_true, y_score, min_precision)
    y_pred_test = [1 if score >= threshold else 0 for score in y_score]
    cm = confusion_matrix(y_true=y_true, y_pred=y_pred_test)
    fpr_test = (cm[0][1] / np.sum(cm[0, :])) * 100
    #tpr_test = (cm[1][1] / np.sum(cm[1, :])) * 100
    f1_test = f1_score(y_true=y_true, y_pred=y_pred_test, average='macro') * 100

    y_pred = [1 if score >= threshold else 0 for score in y_scores_test]
    precision = precision_score(y_true=y_true_test, y_pred=y_pred) * 100
    recall = recall_score(y_true=y_true_test, y_pred=y_pred) * 100
    f1 = f1_score(y_true=y_true_test, y_pred=y_pred, average='macro') * 100

    cm = confusion_matrix(y_true=y_true_test, y_pred=y_pred)
    fpr = (cm[0][1]/np.sum(cm[0, :])) * 100
    return {
        "Method": f"Recall@Precision>={min_precision * 100}%",
        "Test Precision": precision_test*100,
        "Test FPR": fpr_test,
        "Test TPR/Recall": recall_test*100,
        "Test macro-F1": f1_test,
        "Precision": precision,
        "TPR/Recall": recall,
        "Macro-F1 Score": f1,

        "FPR": fpr,
        "Threshold": threshold*100,
        "CM": list(cm)
    }


if __name__ == "__main__":
    ood_df = get_ood_predictions_for_classifier("dactyl-modernbert-base-pretrained")
    ood_df = ood_df[ood_df.model != META_LLAMA_321B]
    score_col = "dactyl-modernbert-base-pretrained_pred"
    dress_aig = ood_df[ood_df.dataset == "dress+aig-asap"]
    dactyl_essays = ood_df[(ood_df.dataset == "dactyl") & (ood_df.domain == "student_essays")]
    test_scores = [(0.05, 0.95), (0.01, 0.99)]
    results = list()
    results.append(get_results_given_threshold(dactyl_essays.target, dactyl_essays[score_col], 0.5, dress_aig.target, dress_aig[score_col]))
    for scores in test_scores:
        results.append(get_results_by_roc_curve(dactyl_essays.target, dactyl_essays[score_col], scores[0], dress_aig.target, dress_aig[score_col]))
        results.append(get_results_by_prc_curve(dactyl_essays.target, dactyl_essays[score_col], scores[1], dress_aig.target,
                                       dress_aig[score_col]))


    ood_df = get_ood_predictions_for_classifier("dactyl-deberta-v3-large-finetuned")
    ood_df = ood_df[ood_df.model != META_LLAMA_321B]
    score_col = "dactyl-deberta-v3-large-finetuned_pred"
    dress_aig = ood_df[ood_df.dataset == "dress+aig-asap"]
    dactyl_essays = ood_df[(ood_df.dataset == "dactyl") & (ood_df.domain == "student_essays")]
    results.append(get_results_given_threshold(dactyl_essays.target, dactyl_essays[score_col], 0.5, dress_aig.target,
                                               dress_aig[score_col]))
    for scores in test_scores:
        results.append(
            get_results_by_roc_curve(dactyl_essays.target, dactyl_essays[score_col], scores[0], dress_aig.target,
                                     dress_aig[score_col]))
        results.append(
            get_results_by_prc_curve(dactyl_essays.target, dactyl_essays[score_col], scores[1], dress_aig.target,
                                     dress_aig[score_col]))
    results = pd.DataFrame(results)
    classifiers = ["MB-BCE"] * 5 + ["DV3L-DXO"] * 5
    results["Classifier"] = classifiers
    dactyl_results = results[["Classifier","Method","Test FPR","Test TPR/Recall","Test Precision","Test macro-F1","Threshold"]].round(2)
    daa_results = results[["Classifier","Method","Threshold","FPR","TPR/Recall","Precision", "Macro-F1 Score"]].round(2)


    print(dactyl_results.to_markdown(index=False))
    print(daa_results.to_markdown(index=False))
