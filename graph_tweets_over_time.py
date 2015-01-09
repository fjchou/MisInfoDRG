from connection import dbConnection
from collections import Counter
from datetime import datetime, timedelta
import re

def _tweets_over_time(db_name, table_name, dateStart_str, dateEnd_str, date_increment, fname, adjust):

        db = dbConnection()
        db.create_mongo_connections(mongo_options=[db_name])

        f = open(fname, 'w')

        dateStart = datetime.strptime(dateStart_str, "%Y-%m-%d %H:%M:%S")
        dateEnd = datetime.strptime(dateEnd_str, "%Y-%m-%d %H:%M:%S")
        print "time: %s, %s" % (dateStart, dateEnd)

        time1 = dateStart

        result = "time\tnum_tweets\n"

        timenow = datetime.now()
        print "%s" % (timenow)
        while (time1 < dateEnd):
                time2 = time1 + timedelta(seconds=date_increment)
                p_time = time1 + timedelta(seconds=adjust)

                raw_data = db.m_connections[db_name].find({
                    "created_ts":{
                        "$gte":time1,
                        "$lt":time2
                    }}).count()


                print "%s\t%d" % (time2, raw_data)
                result += "%s\t%d\n" % (time2, raw_data)

                f.write(result)

                time1 = time2

def tweets_over_time():
        _tweets_over_time("sydneysiege", "tweets", "2014-12-15 15:50:00", "2014-12-15 15:55:00", 1, "tweets_over_time_sydney.txt", 0)

def main():
        _tweets_over_time("sydneysiege", "tweets", "2014-12-15 15:50:00", "2014-12-15 15:55:00", 1, "tweets_over_time_sydney.txt", 0)

if __name__ == "__main__":
    tweets_over_time()