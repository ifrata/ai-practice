name =input("enter your name: ")
lname =input("enter your LAST name: ")
age =input("enter your age: ")
qualification =input("enter your qualification: ")
with open("bio","a") as d:
    d.write(name+'\n')
    d.write(lname+'\n')
    d.write(age+'\n')

    