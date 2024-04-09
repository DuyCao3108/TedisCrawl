import scrapy
from utils.user_input_process import get_user_input, get_url_from_input, get_current_website_info
from CrawlMedicalPost.items import CrawlmedicalpostItem

class MedicalPostSpider(scrapy.Spider):
    name = "medicalpost"

    def start_requests(self):
        # get user input
        inputDict = get_user_input()
        # convert to url
        inputDict_with_url = get_url_from_input(inputDict)
        # get url 
        urls = inputDict_with_url['start_urls']
        print(urls)
        # start crawling on urls
        for url in urls:
            current_web_info = get_current_website_info(url)
            yield scrapy.Request(url=url, callback=self.parse, meta = current_web_info)

    def parse(self, response):
        print("===========RECEIVED RESPONSE FROM=========")
        print(response.meta['current_web'])

        if response.meta['current_web'] == "doctortuan":
            
            article_urls = response.css("body > div.container-5.w-container > div > div a::attr(href)").getall()
            current_base_url = response.meta['current_base_url']

            for article_url in article_urls:
                full_article_url = current_base_url + article_url
                response.meta['full_article_url'] = full_article_url
                print(f"Full article url: {full_article_url}")
                yield scrapy.Request(url = full_article_url, callback = self.parse_articles, meta = response.meta)

        elif response.meta['current_web'] == "tamanhhospital":
            
            article_urls = response.css("body > div.container > div > div.col-sm-12.col-xs-12 > div a::attr(href)").getall()

            for article_url in article_urls:
                full_article_url = article_url
                response.meta['full_article_url'] = full_article_url
                yield scrapy.Request(url = full_article_url, callback = self.parse_articles, meta = response.meta)

        elif response.meta['current_web'] == "suckhoedoisong":
            pass
            
        elif response.meta['current_web'] == "medlatec":
            pass
        
            pass
    
    
    
    def parse_articles(self, response):
        print("=========== SCRAPING ITEMS FROM=========")
        print(response.meta['full_article_url'])

        if response.meta['current_web'] == "doctortuan":
            Article = CrawlmedicalpostItem()
            Article['url'] = f"this is a url of {response.url}"
            Article['title'] = response.css("h1.blog-post-title::text").get()
            Article['article'] = "this is a article"
            print(Article)   
            yield Article

        elif response.meta['current_web'] == "tamanhhospital":
            Article = CrawlmedicalpostItem()
            Article['url'] = f"this is a url of {response.url}"
            Article['title'] = response.css("div.title > h1::text").get()
            Article['article'] = "this is a article"
            print(Article)   
            yield Article

        elif response.meta['current_web'] == "suckhoedoisong":
            pass
        
        elif response.meta['current_web'] == "medlatec":
            pass

        

        

        



 