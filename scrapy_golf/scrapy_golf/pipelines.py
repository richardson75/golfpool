# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

#Pipelines for the golf project 

class MySQLStorePipeline_Results(object):
  def __init__(self):
    self.conn = MySQLdb.connect(user='root', passwd='root', db='pga', host='146.148.92.23', charset="utf8", use_unicode=True)
    self.cursor = self.conn.cursor()

  def process_item(self, item, spider):

    try:
        self.cursor.execute("""INSERT INTO LOAD_RESULTS (TOURN_ID, PLAYER_NAME, PLAYER_FINISH, PLAYER_PAYOUT, START_URL) VALUES (%s, %s, %s, %s, %s)""", 
          (item['tourn_id'], item['player'][0].encode('utf-8'), item['place'][0].encode('utf-8'), item['payout'][0].encode('utf-8'),item['url_id']))
        self.conn.commit()

# WHEN THE PAYOUT IS ZERO YOU GET AN INDEX ERROR
    except IndexError:
        self.cursor.execute("""INSERT INTO LOAD_RESULTS (TOURN_ID, PLAYER_NAME, PLAYER_FINISH, PLAYER_PAYOUT, START_URL) VALUES (%s, %s, %s,%s, %s)""", 
          (item['tourn_id'], item['player'][0].encode('utf-8'), item['place'][0].encode('utf-8'), '0',item['url_id']))
        self.conn.commit()

    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])


    return item


class MySQLStorePipeline_Rank(object):
  def __init__(self):
    self.conn = MySQLdb.connect(user='root', passwd='root', db='pga', host='146.148.92.23', charset="utf8", use_unicode=True)
    self.cursor = self.conn.cursor()

  def process_item(self, item, spider):
    
    try:
        self.cursor.execute("""INSERT INTO LOAD_RANK (TOURN_ID, PLAYER_NAME, PLAYER_WGR) VALUES (%s, %s, %s)""", 
          (item['tourn_id'], item['player3'][0].encode('utf-8'), item['rank'][0].encode('utf-8')))
        self.conn.commit()    

    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])


    return item