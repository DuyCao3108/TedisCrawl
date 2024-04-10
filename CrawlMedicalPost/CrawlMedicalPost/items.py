# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class tamanhhospitalItem(Item):
    # define the fields for your item here like:
    website = Field()
    title = Field()
    url = Field()
    article = Field()
    

class doctortuanItem(Item):
    # define the fields for your item here like:
    website = Field()
    title = Field()
    url = Field()
    article = Field()

class suckhoedoisongItem(Item):
    # define the fields for your item here like:
    website = Field()
    title = Field()
    url = Field()
    article = Field()

class medlatecItem(Item):
    # define the fields for your item here like:
    website = Field()
    title = Field()
    url = Field()
    article = Field()
    
