import pymongo
import datetime

myClient = pymongo.MongoClient()
users = myClient.mydb.users

print(users)

start_time = datetime.datetime.now()
listDocs = users.find({"username": "nick"})
print("No index :", datetime.datetime.now() - start_time)

for item in listDocs:
    print("item :", item)

index_name = users.create_index([("username", pymongo.ASCENDING)])
print("index_name :", index_name)
sorted(list(users.index_information()))

start_time = datetime.datetime.now()
listDocs = users.find({"username": "nick"})
print("Index :", datetime.datetime.now() - start_time)

for item in listDocs:
    print("item :", item)

users.drop_index(index_name)
