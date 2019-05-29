import requests

my_data = {"name": "Mick", "email": "nicktest@yahoo.com"}

# "https://www.w3schools.com/php/demo_form_post.php"
# 위의 폼에 데이터를 넣은 결과와 같은 것을 아래의 코드로 실행
r = requests.post("https://www.w3schools.com/php/welcome.php", data=my_data)

print("Status Code :", r.status_code)
print("===============")
print(r.text)

resultFile = open("./postResult.html", "w+")
resultFile.write(r.text)

