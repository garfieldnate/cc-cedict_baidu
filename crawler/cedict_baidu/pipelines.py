# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from redis import Redis
import logging
logger = logging.getLogger(__name__)


r = Redis()
redis_queue = "cedict_baidu"


class CedictBaiduPipeline:
    def process_item(self, item, spider):
        r.rpush(redis_queue, str(item))
        logger.info(f"Writing result to redis: {dict(item)}")
        return item
