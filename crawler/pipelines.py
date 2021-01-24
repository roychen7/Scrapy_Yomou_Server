# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from uuid import UUID


MongoClient = pymongo.MongoClient
client = MongoClient("localhost", 27017)
db = client.yomou


# intercept result to save it to mongodb 'htmlpages' collection
class CrawlerPipeline:
    def process_item(self, item, spider):
        # convert UUID string to mongo-compatible repr
        # see https://stackoverflow.com/a/60404331
        uuid = UUID(spider.uuid)

        # add html to entry with specified UUID in db
        query = {"uuid": uuid}
        update = {"$set": {"html": item.get("res")}}
        db.documents_document.update_one(query, update)

        return item
