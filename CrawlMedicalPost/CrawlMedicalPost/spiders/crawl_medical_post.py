import scrapy
from utils.user_input_process import get_user_input, get_url_from_input

class MedicalPostSpider(scrapy.Spider):
    name = "medicalpost"

    def start_requests(self):
        # get user input
        inputDict = get_user_input()
        # convert to url
        inputDict_with_url = get_url_from_input(inputDict)
        # get url 
        urls = inputDict_with_url['start_urls']
        # start crawling on urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response)
        print("done")
        
        
        
        # for quote in response.css("div.quote"):
        #     yield {
        #         "text": quote.css("span.text::text").get(),
        #         "author": quote.css("small.author::text").get(),
        #         "tags": quote.css("div.tags a.tag::text").getall(),
        #     }



 