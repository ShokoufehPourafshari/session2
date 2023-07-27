print ("please follow up the instructure")
first_name = input ("enter your first name: ")
last_name = input ("enter your last name: ")
biology = int(input("enter your biology score: "))
geology = int(input("enter your geology score: "))
mathematics = int(input("enter your mathematics score: "))
average = (biology + geology + mathematics)/3
if average >= 17:
    print ("Greate!")
if 12 <= average < 17:
    print ("Normal")
if average < 17:
    print ("I'm sorry nut you are faild")