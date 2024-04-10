from CrawlMedicalPost.spiders.crawl_medical_post import MedicalPostSpider
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import sys

def main(keyword, max_article):
    configure_logging({"LOG_FORMAT": "%(levelname)s: %(message)s"})
    runner = CrawlerRunner(
        settings={
            "FEEDS": {
                './storage/data.json': {'format': 'json'}
            },
            'SCRAPEOPS_API_KEY': 'c77ada02-6767-4b0e-bd5d-38aea43c9431',
            'SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT': 'https://headers.scrapeops.io/v1/user-agents',
            'SCRAPEOPS_FAKE_USER_AGENT_ENABLED': True,
            'SCRAPEOPS_NUM_RESULTS': 20,
            'ROBOTSTXT_OBEY': False,
            'DOWNLOADER_MIDDLEWARES': {
                'CrawlMedicalPost.middlewares.ScrapeOpsFakeUserAgentMiddleware': 725,
            },
            'EXTENSIONS': {
                "scrapy.extensions.closespider.CloseSpider": 200,
            },
            'ITEM_PIPELINES': {
                "CrawlMedicalPost.pipelines.CrawlMedicalPostPipeline": 300,
            }
        }
    )
    d = runner.crawl(MedicalPostSpider, keyword = keyword, max_article = max_article)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


if __name__ == "__main__":
    keyword = sys.argv[1]
    max_article = sys.argv[2]
    main(keyword, max_article)