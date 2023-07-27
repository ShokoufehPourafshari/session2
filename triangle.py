a = int(input("please enter a: "))
b = int(input("please enter b: "))
c = int(input("please enter c: "))

op1 = a + b
if op1 > c:
    show = ("Congratulations you have a triangle!")
else:
    show = ("Sorry, try different numbers")
op2 = a + c
if op2 > b:
    show = ("Congratulations you have a triangle!")
else:
    show = ("Sorry, try different numbers")
op3 = b + c
if op3 > a:
    show = ("Congratulations you have a triangle!")
else:
    show = ("Sorry, try different numbers")
print (show)