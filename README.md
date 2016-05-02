# golfpool
This is a repository for the golfpool learning project

##Background
A freind of my runs a golf pool where you pick 8-9 players for each of the 4 major golf tournaments. Your team competes against others based on how much money your players win in aggregate for the tournament. The goal of this project is to automate this contest and eventually make it so there can be real time updates.  
##About the project
The project scrapes data from two different websites and writes the data back into a MySQL database hosted on Google Cloud. There is also an integration with Google Sheets and Google Forms to collect the picks.

The scraping is done using [Scrapy](http://doc.scrapy.org/en/latest/intro/tutorial.html) a python library. Here is the Scrapy architecture:

![Scarpy Architecture:](http://doc.scrapy.org/en/latest/_images/scrapy_architecture.png)

In this project I have two diffent spiders: 

1. one to pull the tounament results (GolfStats_results.py)
2. one to pull the offical world golf rankings (rank3.py)

Each of the spiders has a SQL pipeline to the MySQL database.

More details about the spiders and the project can be found in the [GettingStarted](https://github.com/richardson75/golfpool/blob/master/GettingStarted.md) file.




