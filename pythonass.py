# 1. write a simple calculator that tkes in two numbers and aan operator as input ad prints out the result
'''
try:
    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))
   
    if op == "*":
        print(num1 * num2)
    elif op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("Invalid operator")  
except ValueError:
    print("Invalid input")
'''


# 2. write a code that reads the input and identifies whether it's a prime number or not
'''
from math import *

num = int(input("Enter a number: "))
for no in range(2, num):
    if num % no == 0:
        print(str(num) + " is a not a prime number")
        break
else:
    print(str(num) + " is a prime number")
'''
#4 number guessing game where the user gets 5 chances to guess a randomly generated number between 1 and 100
'''
import random
def guessganme():
    nog = 0
    ans = ""
    Rand = random.randint(1,10)
    while nog !=5 and ans != Rand:
        ans = int(input("Enter your guess from 1 to 10: "))
        nog +=1
    if ans == Rand:
        print("YOU ARE CORRECT")
    else:
        print("YOU ARE WRONG, THE ANSWER IS " + str(Rand))
guessganme()
'''
#5 write a function that checks if a string is a palindrome
'''
ans = input("Enter a word: ")
if ans[0] == ans[-1] and ans[1] == ans[-2]:
     print(ans + " is a palindrome")
elif ans[2] == ans[-3] and ans[3] == ans [-4]:
      print(ans + " is a palindrome")
else:
    print(ans + " is not a palindrome")
'''

#6 create a function that takes a list of numbers and returns the average, min and max
'''
import numpy
def AMM():
    print("This machine compares two values and sees if they are similar")

    list_of_nos = input("Enter list of numbers separated by spaces: ").split()
    numbers = list(map(float, list_of_nos))
    print("The average of the numbers inputed is ",numpy.average(numbers))
    print("The maximum of the numbers inputed is ", max(numbers))
    print("The minimum of the numbers inputed is ", min(numbers))

AMM()
'''

'''
def DC(a, b):
    if a == b:
        print(True)
    else:
        print(False)
inpu1 = input("enter value a: ")
inpu2 = input("Enter value b: ")
DC(inpu1, inpu2)
'''



