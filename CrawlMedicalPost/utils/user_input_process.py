import time
from utils.constant import WEBSITE_TO_CRAWL, BASEURL_WEBSITE_TO_CRAWL

def get_user_input():
    keyword = input("What keywords to search?")
    max_article = input("What is the max number of articles to crawl?")
    from_websites = list(filter(lambda x: x == "nhathuoclongchau", WEBSITE_TO_CRAWL))

    inputDict = {
        "keyword": keyword,
        "max_article": max_article,
        "from_websites": from_websites,
    }

    return inputDict

def get_url_from_input(inputDict):
    from_websites = inputDict['from_websites']
    keyword = inputDict['keyword']
    start_urls = []
    
    # convert to url
    for from_website in from_websites:
        base_url = BASEURL_WEBSITE_TO_CRAWL[from_website]
        
        if from_website == "vinmec": 
            start_url = ""
            start_urls.append(start_url)
        elif from_website == "nhathuoclongchau": 
            start_url = base_url
            keyword_splited = keyword.split(" ")
            start_url += keyword_splited[0]

            if len(keyword_splited) <= 1: start_url 
            else:
                for character in keyword_splited[1:]:
                    start_url += f"+{character}"

            start_urls.append(start_url)
        elif from_website == "hellobacsi": 
            start_url = ""
            start_urls.append(start_url)

    inputDict['start_urls'] = start_urls
    
    return inputDict


    