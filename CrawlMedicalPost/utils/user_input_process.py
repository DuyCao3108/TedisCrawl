import time
from constant import WEBSITE_TO_CRAWL

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







    