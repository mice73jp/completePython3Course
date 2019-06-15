from pymongo import MongoClient
import datetime

myClient = MongoClient()
db = myClient.mydb
Users = db.users

current_date = datetime.datetime.now()
print("current_date :", current_date)

old_date = datetime.datetime(2009, 8, 11)
print("old_date :", old_date)

# uid = Users.insert_one({"username": "ffie", "date": current_date})
# print("uid :", uid)

cnt = Users.count_documents({"date": {"$exists": True}})
print("Date Exist Cnt :", cnt)

cnt = Users.count_documents({"date": {"$lte": old_date}})
print("Date Lte Cnt :", cnt)

cnt = Users.count_documents({"date": {"$gte": old_date}})
print("Date Gte Cnt :", cnt)

cnt = Users.count_documents({"username": {"$ne": "yetanother"}})
print("Username ne Cnt :", cnt)

list = Users.find({"username": {"$ne": "yetanother"}})
for oneItem in list:
    print("doc :", oneItem)
    print("username :", oneItem["username"])
