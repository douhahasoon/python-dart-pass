'''
Q:Write a program that takes an Integer (0 < x <= 10) then takes X integers one
after another, after inputting all those numbers, you should print 'N is odd' or 'N
is even' depending on each N that was received. Your whole program should be
implemented using a single function.
! You don't have to check for cases that breaks your code.

'''


def odd_even():
    value = int(input("enter X value:"))
    numbers = []
    for i in range(value):
        num = int(input())
        numbers.append(num)

    for x in numbers:
        if x % 2 == 0:
            print(f'{x} is even ')
        elif x % 2 != 0:
            print(f'{x} is odd')


odd_even()
