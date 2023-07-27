import math
op = input('''please select one of the options below:
sin
cos
tan
cot
factorial
radical
''')
x = int(input('Please Enter x: '))
if op == "sin":
    print (math.sin(x))
if op == "cos":
    print (math.cos(x))
if op == "tan":
    print (math.tan(x))
if op == "cot":
    print (math.cot(x))
if op == "factorial":
    print (math.factorial(x))
if op == "radical":
    print (math.sqrt(x))