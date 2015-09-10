# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from model import MyBlog, db_connect, create_myblog_table


class MyblogPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_myblog_table(engine)
        self.Session = sessionmaker(bind = engine)

    def process_item(self, item, spider):
        session = self.Session()
        myblog=MyBlog(**item)
        session.add(myblog)
        session.commit()

        return item
