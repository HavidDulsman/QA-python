#!/usr/bin/env python3.8

import maths

def add(number_1,number_2):
    return number_1 + number_2

def subtract(number_1,number_2):
    if maths == "-":
        return number_1 - number_2

def multiply(number_1,number_2):
    if maths == "*":
        return number_1 * number_2
   
def divide(number_1,number_2):
    if maths == "/":
        return number_1 / number_2

def modular(number_1,number_2):
    if maths == "%":
        return number_1 % number_2

session = True
while session:
    number_1 = int(input("enter first number: "))
    maths = input("enter operation: ")
    number_2 = int(input("enter second number: "))

    if maths == "+":
        print(add(number_1, number_2))
    elif maths == "-":
        print(subtract(number_1, number_2))
    elif maths == "*":
        print(multiply(number_1,number_2))
    elif maths == "/":
        print(divide(number_1,number_2))
    elif maths == "%":
        print(modular(number_1, number_2))
    
    ask = input("Do you want to continue? (y/n) ")

    if ask == "n":
        session = False
    else:
        pass