import pymongo
import datetime
client = pymongo.MongoClient('localhost', 27017)

todaydetail = datetime.datetime.today()
db = client.testDB

co = db.testCollection
day = "./photo/" + todaydetail.strftime("%Y%m%d-%H%M") + ".jpeg"
co.insert_one({"path":day, "year":todaydetail.year, "month":todaydetail.month, "day":todaydetail.day ,"time":todaydetail.strftime("%H%M"), "hour":todaydetail.hour, "min":todaydetail.minute})
for data in co.find():
    print(data)