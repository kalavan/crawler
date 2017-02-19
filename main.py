import db_access
from pymongo import MongoClient, collection
from PageSweeper import loop_through_olx

status = "NEW"
statusFieldName = "status"
urlFieldName = "url"
olxURL = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/?page=1"
mongoUrl = 'mongodb://%s:%s@ds037571.mlab.com:37571/targets' % (db_access.db['user'], db_access.db['password'])

def fulfillDatabaseWithOlxLinks(olxLinks, mongoUrl, urlFieldName, statusFieldName, status):
    client = MongoClient(mongoUrl)
    db = client.targets
    olx = db.olx

    existing = olx.find()
    existingLinks = [x[urlFieldName] for x in existing]
    print "In database exist: %s links" % len(existingLinks)
    toAdd = [{urlFieldName: x,
              statusFieldName: status} for x in olxLinks if x not in existingLinks]
    numOfLinksToAdd = len(toAdd)
    print "%s url's will be added" % numOfLinksToAdd
    olx.insert_many(toAdd)
    print "Now in database are: %s links" % olx.count()
    return numOfLinksToAdd

def doWork():
    numOfAddedLinks = 1
    tryNo = 1
    while numOfAddedLinks > 0:
        links = loop_through_olx(olxURL)
        print "Try no: %s. Found no of links: %s" % (tryNo, len(links))
        numOfAddedLinks = fulfillDatabaseWithOlxLinks(links, mongoUrl, urlFieldName,statusFieldName, status)
        tryNo += 1

doWork()