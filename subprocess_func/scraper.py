import subprocess
import json
import pandas as pd


def Scraper(keyword, max_article):
    result = subprocess.run(["python", "./CrawlMedicalPost/main.py", keyword, max_article], check=True)
    if result != 0 :
        print("Error: The subprocess returned a non-zero exit code.")
        return False
    else: 
        with open("storage/data.json", "r") as file:
                    json_string = file.read()
                    decoded_data = json.loads(json_string)
                    pd.DataFrame(decoded_data).to_csv("storage/data.csv")
        return True
    
    