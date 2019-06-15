from pymongo import MongoClient
import datetime

myClient = MongoClient()

db = myClient.mydb
users = db.users

dataUsers = [{"username": "third", "passowrd": "12345"}, {"username": "red", "passowrd": "blue"}, {"username": "nick", "date": datetime.datetime.now()}, {"username": "ticke", "date": datetime.datetime.now()}, {"username": "yetanother", "passowrd": "myverysecurepassword", "favorite_number": 445}, {"username": "yetanother", "passowrd": "myverysecurepassword", "favorite_number": 445}]
inserted = users.insert_many(dataUsers)

print("inserted :", inserted)
print("ids :", inserted.inserted_ids)
