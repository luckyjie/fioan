from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from myblog.items import MyblogItem

class MyblogSpider(CrawlSpider):
    name = 'spider'
    allowed_domain = ['blog.csdn.net']
    start_urls = ['http://blog.csdn.net/jiangjieqazwsx']

    rules = [
        Rule(LinkExtractor(allow=r'/jiangjieqazwsx/article/list/\d+')),
        Rule(LinkExtractor(allow=r'/jiangjieqazwsx/article/details/\d+'), callback="parse_item"),
    ]

    def parse_item(self, response):
        sel = Selector(response)
        item = MyblogItem()

        item['title'] = sel.xpath('//*[@class="link_title"]/a/text()').extract()[0]

#        item['title'] = sel.xpath('//*[@class="link_title"]/a/text()').extract()[0].encode('utf-8')
        item['time'] = sel.xpath('//*[@class="link_postdate"]/text()').extract()[0]
        item['read'] = sel.xpath('//*[@class="link_view"]/text()').re(r'\d+')[0]
#        print "***************"
#        print item['title']
#        print item['time']
#        print item['read']
#        print '##############'
        return item
