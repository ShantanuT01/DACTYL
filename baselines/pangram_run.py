from dotenv import load_dotenv
load_dotenv()
import os
import time
from pangram import Pangram
from tqdm import tqdm
import pandas as pd

if __name__ == "__main__":
    pangram_client = Pangram(api_key=os.environ["PANGRAM_API_KEY"])
    df = pd.read_parquet("finetuned-texts.parquet")
    results = list()
    batch_size = 32
    ids = df["id"].to_list()
    texts = df["text"].to_list()
    for i in tqdm(range(0, len(texts), batch_size)):
        results.extend(pangram_client.batch_predict(texts[i:i+batch_size]))
        pangram_results = pd.DataFrame(results)
        pangram_results["id"] = ids[0:len(pangram_results)]
        pangram_results.to_json(f"pangram-results.json",index=False,orient="records",indent=4)