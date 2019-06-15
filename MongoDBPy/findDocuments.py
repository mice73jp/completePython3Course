from pymongo import MongoClient

myClient = MongoClient()
db = myClient.mydb
users = db.users

# cnt = users.find({}).count()
cnt1 = users.count_documents({"favorite_number": 445})
print("Cnt1 :", cnt1)
cnt2 = users.count_documents({"favorite_number": 445, "username": "yetanother"})
print("Cnt2 :", cnt2)
