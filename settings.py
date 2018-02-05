"""
Settings module for Reviews API.
"""

from os import environ
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

MONGO_HOST = environ.get('MONGO_HOST')
MONGO_PORT = environ.get('MONGO_PORT')
MONGO_DBNAME = environ.get('MONGO_DBNAME')


JSON = True
XML = False



#Schemas
reviews_schema = {
    "reviewerID": {'type':'string'},
    "asin": {'type':'string'},
    "reviewerName": {'type' : 'string'}, #"J. McDonald",
    "helpful": {'type':'list'}, # [2, 3],
    "reviewText": {'type':'string'}, #"I bought this for my husband who plays the piano. He is having a wonderful time playing these old hymns. The music is at times hard to read because we think the book was published for singing from more than playing from. Great purchase though!",
    "overall": {'type':'integer'}, #5.0,
    "summary": {'type':'string'}, #"Heavenly Highway Hymns",
    "unixReviewTime": {'type':'integer'}, #1252800000,
    "reviewTime": {'type':'date'} #"09 13, 2009"
}

reviews_config = {
    'schema':reviews_schema,
    'item_title':'Reviews For Androids Apps',
    'resource_methods': ['GET','POST']
}


DOMAIN = {
    'reviews':reviews_config
}
