import requests
from io import BytesIO
from PIL import Image

# http://www.weeky.es/wp-content/uploads/2017/03/la-milonga-flamenca.jpg
# https://i.ytimg.com/vi/E-PJ84f1jvI/maxresdefault.jpg
# https://i.ytimg.com/vi/ZVx_1My7Z6o/maxresdefault.jpg
r = requests.get("https://i.ytimg.com/vi/ZVx_1My7Z6o/maxresdefault.jpg")

print("Status Code :", r.status_code )

# r.content is byte data
image = Image.open(BytesIO(r.content))

path = "./downloaded_image." + image.format
print(image.size, image.format, image.mode)

try:
    image.save(path, image.format)
except IOError:
    print("Can not save image.")
