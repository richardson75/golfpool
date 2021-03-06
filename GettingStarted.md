#Getting Started with Scrapy

######Creating a new project:
$ scrapy startproject scrapy_golf

##Spider: golfstats_results
This hits the website *http://www.golfstats.com/* to pull in the results for a specific tournement

##### Example Start URLS:
1. 2016 Masters: http://www.golfstats.com/search/?yr=2016&tournament=Masters&player=&tour=Majors&submit=go
2. 2015 US Open: http://www.golfstats.com/search/?yr=2015&tournament=U.S.+Open&player=&tour=Majors&submit=go

#####crawl examples (note 2 arguments -> start_url and tourn_id)
```python
scrapy crawl golfstats_results -a start_url="http://www.golfstats.com/search/?yr=2016&tournament=Masters&player=&tour=Majors&submit=go" -a tourn_id=201601
```

```python
scrapy crawl golfstats_results -a start_url="http://www.golfstats.com/search/?yr=2015&tournament=U.S.+Open&player=&tour=Majors&submit=go" -a tourn_id=201502
```

The results use the pileline: __SQLStorePipeline_Results__ which writes to LOAD_RESULTS

##Spider: rank3
This hits *http://www.owgr.com/en/Ranking.aspx*, the start_urls are defined in the spider

##### Here is how you call
``` python
scrapy crawl rank3 -a tourn_id=201601
```

This spider uses the __MySQLStorePipeline_Rank__ pipeline to write to LOAD_RANK in the MySQL database


