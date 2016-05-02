import scrapy
from scrapy_golf.items import RankItem

class RankSpider(scrapy.Spider):
    name = "rank3"
    allowed_domains = ["owgr.com/"]
    start_urls = [
        "http://www.owgr.com/en/Ranking.aspx?pageNo=1&pageSize=10&country=All"
    ]

    """
    start_urls = [
        "http://www.owgr.com/en/Ranking.aspx?pageNo=1&pageSize=300&country=All",  
        "http://www.owgr.com/en/Ranking.aspx?pageNo=2&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=3&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=4&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=5&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=6&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=7&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=8&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=9&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=10&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=11&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=12&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=13&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=14&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=15&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=16&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=17&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=18&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=19&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=20&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=21&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=22&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=23&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=24&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=25&pageSize=300&country=All",
        "http://www.owgr.com/en/Ranking.aspx?pageNo=26&pageSize=300&country=All"
    ]
    """

    custom_settings = {
        'FEED_EXPORT_FIELDS': ["player3","rank", "tourn_id"],
        'ITEM_PIPELINES': ['scrapy_golf.pipelines.MySQLStorePipeline_Rank']
    }

    def __init__(self, *args, **kwargs): 
        super(RankSpider, self).__init__(*args, **kwargs) 

        self.tourn_id = [kwargs.get('tourn_id')] 

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        items =[]
        for sel in response.xpath("//*[@id='ranking_table']/div[2]/table/tr"):
            item = RankItem() 
            item['tourn_id'] = self.tourn_id
            item['player3'] = sel.xpath('td[5]/a/text()').extract()
            item['rank'] = sel.xpath('td[1]/text()').extract()
            items.append(item)

        return items