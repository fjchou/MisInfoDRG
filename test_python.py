from pymongo import MongoClient
from datetime import datetime
import re


client = MongoClient('z')
db = client.boston
collection = db.tweets
tweets = db.tweets


def rumors_over_time():
        filename = raw_input('file name (be careful not to overwrite): ')
        title = "%s.csv" % filename
        f = open(title, 'w')    #create new csv
        f.write('time,count\n')
        inc = 30
        searchterm_re = re.compile("falseflag", re.IGNORECASE)
        for i in range(16,17):          #15-23 (day)
                for j in range(0,2):   #0-24 (hour)
                        for k in range(0,60,inc):
                                dateStart = datetime(2013,04,i,j,k)
                                dateEnd = datetime(2013,04,i,j,(k+(inc-1)),59)
                                print "time: %s,%s" % (dateStart,dateEnd)
                                tweet_count = tweets.find({"text": searchterm_re, "created_ts":{"$gte":dateStart,"$lte":dateEnd}}).count()
                                result = '"%s"\t%d\n' % (dateStart,tweet_count)
                                f.write(result)

rumors_over_time()