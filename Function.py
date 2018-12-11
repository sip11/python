'''
from sys import argv
filename, f_name, x, y = argv

def add(x,y):
    print (f" {x} add {y}, the answer is", (int(x) + int(y)))

def multiply (x,y):
    return int(x)*int(y)

if f_name == "add" or f_name is "a":
    add(x,y)
if f_name == "multiply" or f_name is "m":
    print (f"{x} multiply {y}, the answer is", multiply(x,y))
'''

'''
from sys import argv
filename,  x, y = argv
prompt = '''
#Would you like to do Add or Multiply caculation?
#Input a for add , m for multiply or q for quit.
'''

instruction = input(prompt)

def add(x,y):
    print (f" {x} add {y}, the answer is", (int(x) + int(y)))

def multiply (x,y):
    return int(x)*int(y)

if instruction == "add" or instruction is "a":
    add(x,y)
if instruction == "multiply" or instruction is "m":
    print (f"{x} multiply {y}, the answer is", multiply(x,y))
if instruction == 'q':
    exit()

'''

prompt = '''
Please input a number
'''

x = input(prompt)
y = input(prompt)
def convert_numbers(s):
    while True:
        try:
            return int(s)
        except ValueError:
            s = input(prompt)
        else:
            break

x = convert_numbers(x)
y = convert_numbers(y)

prompt = '''
#Would you like to do Add or Multiply caculation?
#Input a for add , m for multiply or q for quit.
'''

def add(x,y):
    print (f" {x} add {y}, the answer is", (int(x) + int(y)))

def multiply (x,y):
    return int(x)*int(y)

instruction = input(prompt)

if instruction == "add" or instruction is "a":
    add(x,y)
if instruction == "multiply" or instruction is "m":
    print (f"{x} multiply {y}, the answer is {multiply(x,y)}.")
if instruction == 'q':
    exit()




















