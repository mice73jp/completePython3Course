def add(num1, num2):
    return int(num1) + int(num2)


def subtract(num1, num2):
    return int(num1) - int(num2)


def multiply(num1, num2):
    return int(num1) * int(num2)


def divide(num1, num2):
    return int(num1) / int(num2)


menu_string = '''
Select operation.
1. Add
2. Subtract
3. Multiply
4. Divide
q. End
'''

while True:
    print(menu_string)
    choice = input('Enter choice(1/2/3/4/qQ): ')
    print('Debug : ', type(choice),  choice.isdigit())

    if choice.isdigit() and int(choice) in range(1, 4):
        firstNum = input('Enter first number: ')
        secondNum = input('Enter second number: ')
        if choice == '1':
            print(firstNum, '+', secondNum, '=', add(firstNum, secondNum))
        elif choice == '2':
            print(firstNum, '-', secondNum, '=', subtract(firstNum, secondNum))
        elif choice == '3':
            print(firstNum, '*', secondNum, '=', multiply(firstNum, secondNum))
        elif choice == '4':
            print(firstNum, '/', secondNum, '=', divide(firstNum, secondNum))
    elif choice.isalpha() and choice.lower() == 'q':
        break
    else:
        print('You chose wrong, please choose 1 - 4 or q/Q.')

