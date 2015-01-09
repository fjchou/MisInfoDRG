from connection import dbConnection
from collections import Counter
from datetime import datetime, timedelta
import re
from random import randint

def _get_random_tweets(db_name, table_name, fname, number):

        db = dbConnection()
        db.create_mongo_connections(mongo_options=[db_name])

        f = open(fname, 'w')

        reggie = re.compile("cnn", re.IGNORECASE)

        result = "time\ttext\n"

        # two, three, 2, 3, gunmen, terrorist
        count_data = int(db.m_connections[db_name].find({ "text": reggie }).count())
        raw_data = db.m_connections[db_name].find({ "text": reggie }, {"created_at":1, "text":1, "_id":0 })

        for i in range(0, (number-1)):
                        r = randint(0, (count_data-1))
                result += "%s\t%s\n" % (raw_data[r]["created_at"], raw_data[r]["text"])

        result = result.encode('ascii', 'ignore')
        f.write(result)

def get_random_tweets():
        _get_random_tweets("sydneysiege", "tweets", "anyfile.txt", 100)

def main():
        _get_random_tweets("sydneysiege", "tweets", "anyfile.txt", 100)

if __name__ == "__main__":
    get_random_tweets()