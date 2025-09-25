from binoculars import Binoculars
import pandas as pd
from tqdm import tqdm

if __name__ == "__main__":
    print("Starting to create binoculars")
    bino = Binoculars()
    print("Created binoculars object")
    df = pd.read_parquet("complete_test_set.parquet")
    df = df[df.dataset == "dactyl"]

    texts = df["text"].to_list()
    y_pred = list()
    for i in tqdm(range(0,len(df), 8)):
        y_pred.extend(bino.compute_score(texts[i:i+8]))  
    df["binoculars_pred"] = y_pred
    df[["id","binoculars_pred","target","model","domain","category","dataset"]].to_csv(f"predictions/binoculars-results.csv",index=False)