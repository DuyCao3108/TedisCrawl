# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from CrawlMedicalPost.items import *
import re

def processing_article(article):
    valid_article = [sentence for sentence in article if "\n" not in sentence]
    joined_article = " ".join(valid_article)
    return joined_article

class CrawlMedicalPostPipeline:
    def process_item(self, item, spider):
        if isinstance(item, tamanhhospitalItem):
            self.process_tamanhhospitalItem(item, spider)
        elif isinstance(item, doctortuanItem):
            self.process_doctortuanItem(item, spider)
        elif isinstance(item, suckhoedoisongItem):
            self.process_suckhoedoisongItem(item, spider)
        elif isinstance(item, medlatecItem):
            self.process_medlatecItem(item, spider)
        elif isinstance(item, vinmecItem):
            self.process_vinmecItem(item, spider)
        return item
    
    def process_doctortuanItem(self, item, spider):
        adapter = ItemAdapter(item)
        joined_article = processing_article(adapter['article'])
        adapter['article'] = joined_article
        adapter['website'] = "doctortuan"

        # print(adapter.items())
        return item
    
    def process_suckhoedoisongItem(self, item, spider):
        adapter = ItemAdapter(item)
        joined_article = processing_article(adapter['article'])
        adapter['article'] = joined_article
        adapter['website'] = "suckhoedoisong"

        # print(adapter.items())
        return item
    
    def process_medlatecItem(self, item, spider):
        adapter = ItemAdapter(item)
        joined_article = processing_article(adapter['article'])
        adapter['article'] = joined_article
        adapter['website'] = "medlatec"

        # print(adapter.items())
        return item

    def process_tamanhhospitalItem(self, item, spider):
        adapter = ItemAdapter(item)
        joined_article = processing_article(adapter['article'])
        adapter['article'] = joined_article
        adapter['website'] = "tamanhhospital"

        # print(adapter.items())
        return item
        
    def process_vinmecItem(self, item, spider):
        adapter = ItemAdapter(item)
        joined_article = processing_article(adapter['article'])
        adapter['article'] = joined_article
        adapter['title'] = re.sub(r'\W+', ' ', adapter['title'])
        adapter['website'] = "vinmec"

        # print(adapter.items())
        return item