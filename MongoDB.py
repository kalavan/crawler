import pymongo

client = pymongo.MongoClient("mongodb://pblo28:test28@ds037571.mlab.com:37571/targets")
db = client.targets
print db
collection = db.olx
print collection

print collection.find_one({'author': 'test1'})

