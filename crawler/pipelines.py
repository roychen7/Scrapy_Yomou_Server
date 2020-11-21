# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
MongoClient = pymongo.MongoClient

# intercept result to save it to mongodb 'htmlpages' collection
class CrawlerPipeline:
    def process_item(self, item, spider):
        client = MongoClient("localhost", 27017)
        db = client.yomou
        unique_id = spider.unique_id
        id = db.htmlpages.insert_one({
            "unique_id": unique_id,
            "html": item.get('res')
        }).inserted_id
        print(id)

        return item
