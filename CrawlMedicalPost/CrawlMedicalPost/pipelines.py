# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

def processing_article(article):
    valid_article = [sentence for sentence in article if "\n" not in sentence]
    joined_article = " ".join(valid_article)
    return joined_article

class tamanhhospital_pipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        joined_article = processing_article(adapter['article'])
        adapter['article'] = joined_article

        print(adapter.items())
        
