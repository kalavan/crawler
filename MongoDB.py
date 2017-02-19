import pymongo
import db_access

client = pymongo.MongoClient("mongodb://%s:%s@ds037571.mlab.com:37571/targets"
                             % (db_access.db['user'], db_access.db['password']))
db = client.targets
collection = db.olx

for link in collection.find():
    print link['url']

