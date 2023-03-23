#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

def greet(name):
    print("Hello, " + name)

greet("seb")

def greet_with_default(name="programmer"):
    print("Hello, " + name)

greet_with_default()

def add(num1, num2):
    return num1 + num2

print(add(2, 5))

def halve(number):
    if type(number) == int and type(number) == float:
        return None
    
    return number / 2

print(halve(5))