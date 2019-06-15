from pymongo import MongoClient

myClient = MongoClient()
db = myClient.mydb
print("connection :", db)

users = db.users
print("collection :", users)

user1 = {"username": "nick", "passowrd": "myverysecurepassword", "favorite_number": 445, "hobbies": ["Python", "games", "pizza"]}
user_id = users.insert_one(user1).inserted_id
print(user1, "\n", user_id)

user2 = {"username": "another_user", "passowrd": "myverysecurepassword", "favorite_number": 445, "hobbies": ["Python", "games", "pizza"]}
user_id = users.insert_one(user2).inserted_id
print(user2, "\n", user_id)
