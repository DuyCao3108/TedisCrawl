import subprocess
import json
import pandas as pd


def Scraper(keyword, max_article, scrape_out_dirname):
    # generate relative paths
    scrape_out_loc_json = f"./storage/{scrape_out_dirname}/data.json"
    scrape_out_loc_csv = f"./storage/{scrape_out_dirname}/data.csv"    
    # run subprocess
    result = subprocess.run(["python", "./CrawlMedicalPost/main.py", keyword, max_article, scrape_out_loc_json], check=True)
    if result.returncode != 0 :
        print("Error: The subprocess returned a non-zero exit code.")
        return False
    else: 
        with open(scrape_out_loc_json, "r") as file:
                    json_string = file.read()
                    decoded_data = json.loads(json_string)
                    pd.DataFrame(decoded_data).to_csv(scrape_out_loc_csv)
        return True
    
    