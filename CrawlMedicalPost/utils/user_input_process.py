import time
from utils.constant import WEBSITE_TO_CRAWL, BASEURL_WEBSITE_TO_CRAWL
from utils.process_websites import *

def get_user_input():
    keyword = input("What keywords to search?")
    max_article = input("What is the max number of articles to crawl?")
    from_websites = WEBSITE_TO_CRAWL

    inputDict = {
        "keyword": keyword,
        "max_article": max_article,
        "from_websites": from_websites,
    }

    return inputDict

def get_url_from_input(inputDict):
    from_websites = inputDict['from_websites']
    start_urls = []
    
    # convert to url
    for from_website in from_websites:
        if from_website == "vinmec": 
            start_url = ""
            start_urls.append(start_url)

        elif from_website == "nhathuoclongchau": 
            ntLongChau_processor = ntLongChau(inputDict)
            start_url = ntLongChau_processor.create_start_url()
            start_urls.append(start_url)

        elif from_website == "hellobacsi": 
            helloBacsi_processor = helloBacsi(inputDict)
            start_url = helloBacsi_processor.create_start_url()
            start_urls.append(start_url)
        
        elif from_website == "medlatec": 
            medlatec_processor = medlatec(inputDict)
            start_url = medlatec_processor.create_start_url()
            start_urls.append(start_url)
        
        elif from_website == "suckhoedoisong": 
            suckhoedoisong_processor = suckhoedoisong(inputDict)
            start_url = suckhoedoisong_processor.create_start_url()
            start_urls.append(start_url)

        elif from_website == "youmed": 
            youmed_processor = youmed(inputDict)
            start_url = youmed_processor.create_start_url()
            start_urls.append(start_url)

        elif from_website == "doctortuan": 
            doctortuan_processor = doctortuan(inputDict)
            start_url = doctortuan_processor.create_start_url()
            start_urls.append(start_url)

        elif from_website == "tamanhhospital": 
            tamanhhospital_processor = tamanhhospital(inputDict)
            start_url = tamanhhospital_processor.create_start_url()
            start_urls.append(start_url)

    inputDict['start_urls'] = start_urls
    
    return inputDict


    