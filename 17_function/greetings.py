# Functions need to be declared first
def greeting(name):
    print('Hello', name)


def addition(a, b):
    return a + b


def main():
    name1 = input('Enter your name:\n')
    greeting(name1)
    name2 = input('Enter another name:\n')
    greeting(name2)

    number1 = float(input('Enter a number: '))
    number2 = float(input('Enter another number: '))
    result = addition(number1, number2)
    print('The result is', result)


main()
