
def my_function():
    print('This is my function!')
    print('A second string.')
    return


def my_function2(str1, str2):
    print(str1)
    print(str2)


def my_function3(name = 'Someone', age = 'Unknown'):
    print('My name is', name, 'and my age is', age)
    return


def my_function4(*people):
    for person in people:
        print('My name is', person)
    return


def do_math(num1, num2):
    return num1 + num2


my_function()
my_function2('This is argument1', 'This is argument2')
my_function2('Stringy', 'Hello World')
my_function3('Nick', 30)
my_function3()
my_function3(age=20)
my_function3(age=35, name='Chris')
my_function4('First', 'Second', 'Third', 'Fourth', 'Fifth')
my_function4()
my_function4('Test1', 'Test2')
math1 = do_math(1, 2)
math2 = do_math(30, 20.5)
print('First sum is', math1, 'and the second sum is', math2)
