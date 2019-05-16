import re

string = "'I AM NOT YELLING', she said. Though we knew it to not be true."
print(string)

new = re.sub('[A-Z]', '', string)
print(new)

new = re.sub('[a-z]', '', string)
print(new)

new = re.sub('[.,\']', '', string)
print(new)

new = re.sub('[.,\'a-z]', '', string)
print(new)

new = re.sub('[.,\'a-zA-Z]', '', string)
print(new)

new = re.sub('[.,\'A-Z]', '', string)
print(new)

new = re.sub('[.,\'A-Z+" "]', '', string)
print(new)

new = re.sub('[.,\'A-Z" "]', '', string)
print(new)

string = string + "6 298 -345"
print(string)

new = re.sub('[^0-9]', '', string)
print(new)

