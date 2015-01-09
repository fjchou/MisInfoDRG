from connection import dbConnection
from collections import Counter
from datetime import datetime, timedelta
import re

def _tweets_over_time(db_name, table_name, dateStart_str, dateEnd_str, date_increment, fname, adjust):

        db = dbConnection()
        db.create_mongo_connections(mongo_options=[db_name])