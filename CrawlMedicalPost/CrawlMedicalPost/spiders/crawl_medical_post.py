import scrapy
import math
from utils.user_input_process import get_user_input, get_url_from_input, get_current_website_info
from utils.process_websites import get_query_keyword
from CrawlMedicalPost.items import CrawlmedicalpostItem

class MedicalPostSpider(scrapy.Spider):
    name = "medicalpost"

    def start_requests(self):
        # get user input
        inputDict = get_user_input()
        # convert to url
        inputDict_with_url = get_url_from_input(inputDict)
        self.inputDict_with_url = inputDict_with_url
        # get url 
        urls = inputDict_with_url['start_urls']
        print("=========== PROCESSING START URLs =========")
        print(urls)
        # start crawling on urls
        for url in urls:
            current_web_info = get_current_website_info(url)
            yield scrapy.Request(url=url, callback=self.parse, meta = current_web_info)

    def parse(self, response):
        print("=========== RECEIVED RESPONSE FROM =========")
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
            
            article_urls = response.css("div.box-category-item > a::attr(href)").getall()
            current_base_url = response.meta['current_base_url']

            for article_url in article_urls:
                full_article_url = current_base_url + article_url
                response.meta['full_article_url'] = full_article_url
                print(f"Full article url: {full_article_url}")
                yield scrapy.Request(url = full_article_url, callback = self.parse_articles, meta = response.meta)

            # GET OTHER PAGES
            number_of_articles = int(response.css("#admwrapper > div.main > div.list__content > div.list__search-page > div > p > span::text").get())
            number_of_article_per_page = 24
            number_of_pages = math.ceil(number_of_articles/number_of_article_per_page)

            query_keyword = get_query_keyword(
                                            from_web = response.meta['current_web'], 
                                            keyword = self.inputDict_with_url['keyword']
                                            )

            for num_page in range(2, number_of_pages + 1):
                next_page_url = "https://suckhoedoisong.vn/timeline/search.htm?keywords={}&page={}".format(query_keyword, num_page)
                print(f"Next page url: {next_page_url}")
                yield scrapy.Request(url = next_page_url, callback = self.parse, meta = response.meta)

        elif response.meta['current_web'] == "medlatec":
            
            article_urls = response.css("div.search-wrapper > div.post-list div.post-item-info > div.post-item-details a::attr(href)").getall()
            current_base_url = response.meta['current_base_url']

            for article_url in article_urls:
                full_article_url = current_base_url + article_url
                response.meta['full_article_url'] = full_article_url
                print(f"Full article url: {full_article_url}")
                yield scrapy.Request(url = full_article_url, callback = self.parse_articles, meta = response.meta)

            # GET NEX PAGES
            doHaveMoreThanOnePage = response.css("li.page-item.active") != None
            doReachTheEndPage = len(response.css("li.page-item.active + span + li.disabled.page-item")) > 0

            if doHaveMoreThanOnePage == True and doReachTheEndPage == False: 
                next_page_url = response.css("li.page-item.active + li.page-item > a::attr(href)").get()
                full_next_page_url = current_base_url + next_page_url
                response.meta['full_next_page_url'] = full_next_page_url
                print(f"Full next page url: {full_next_page_url}")
                yield scrapy.Request(url = full_next_page_url, callback = self.parse, meta = response.meta)

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
            Article['article'] = response.css("#ftwp-postcontent ::text").extract()
            
            yield Article

        elif response.meta['current_web'] == "suckhoedoisong":
            Article = CrawlmedicalpostItem()
            Article['url'] = f"this is a url of {response.url}"
            Article['title'] = response.css("h1.detail-title::text").get()
            Article['article'] = "this is a article"
            
            yield Article
        
        elif response.meta['current_web'] == "medlatec":
            Article = CrawlmedicalpostItem()
            Article['url'] = f"this is a url of {response.url}"
            Article['title'] = response.css("div.block-posts-single > h1::text").get()
            Article['article'] = "this is a article"
            print(Article)   
            yield Article

        

        

        



 