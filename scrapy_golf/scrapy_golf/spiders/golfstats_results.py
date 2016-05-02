import scrapy
from scrapy_golf.items import ResultsItem


class GolfstatsResults(scrapy.Spider):
    name = "golfstats_results"
    allowed_domains = ["golfstats.com"]
    custom_settings = {
        'FEED_EXPORT_FIELDS': ["player","place","payout"],
        'ITEM_PIPELINES': ['scrapy_golf.pipelines.MySQLStorePipeline_Results']
        }

    def __init__(self, *args, **kwargs): 
        super(GolfstatsResults, self).__init__(*args, **kwargs) 

        self.start_urls = [kwargs.get('start_url')] 
        self.tourn_id = [kwargs.get('tourn_id')] 

    def parse(self, response):
        items =[]
        for sel in response.xpath('//tbody/tr'):
            item = ResultsItem() 
            item['url_id'] = self.start_urls  
            item['tourn_id'] = self.tourn_id
            item['player'] = sel.xpath('td[1]/a[1]/text()').extract()
            item['place'] = sel.xpath('td[3]/text()').extract()
            item['payout'] = sel.xpath('td[13]/text()').extract()
            items.append(item)

        return items