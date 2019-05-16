numbers = ['Nick', 'Someone', 'Another Person']

for item in numbers:
    print('This persons name is', item)

run = True
current = 1

while run:
    if current == 20:
        run = False
    else:
        print(current)
        current += 1
