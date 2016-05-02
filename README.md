# golfpool
This is a repository for the golfpool project

##About the project
The project scrapes data from two different websites and writes the data back into a MySQL database

The scraping is done using Scrapy here are some details on the two spiders:

##golfstats_results
This hits the website *http://www.golfstats.com/* to pull in the results for a tournement

The location where the sprider will crawl defined by the start_url passed in as an argument a var for the trournament (tourn_id) is also passed in and written to the database.

### Here is how you call the spider:
scrapy crawl golfstats_results -a start_url="http://www.golfstats.com/search/?yr=2016&tournament=Masters&player=&tour=Majors&submit=go" -a tourn_id=201601

This crawls the 2016 masters results:
	http://www.golfstats.com/search/?yr=2016&tournament=Masters&player=&tour=Majors&submit=go
and puts the tourn_id as 201601. 

This spider writes to the table LOAD_RESULTS in a MySQL database

##rank3
This hits http://www.owgr.com/en/Ranking.aspx, the start_urls are defined in the spider

### Here is how you call 
scrapy crawl rank3 -a tourn_id=201601

This spider uses a pipeline to write to LOAD_RANK in the MySQL database




