from pymongo import MongoClient

# 기본 몽고 디비 연결
# client = MongoClient()

# 주소 혹은 포트 지정의 경우. 둘 다 같은 설정이다.
# client = MongoClient("localhost", 27017)
# client = MongoClient("mongodb://localhost:27017")

client = MongoClient()

# mytestdb가 존재재하 않더라도 연결됨(데이터 입력시 만들어지나??)
db = client.mytestdb

print("db content:", db)
