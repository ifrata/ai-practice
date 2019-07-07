""" for i in range(10):
    print("*"*(5-abs(i-5)))


def calcuate_taxes(percent):
    def actual_tax(salary):
        return salary*percent
    return actual_tax


faa=calcuate_taxes(0.30)
print(faa)
#print(faa(50000)) """



""" print("------------------------(pattren 1)------------------------")
n =abs(int(input("Enter Number of Rows: ")))
for row in range(1,n):
    for j in range(row):
        print(j,end="")
    print()
     
     
 """


class human():
    self.abc="ghgj"
    def __init__(self,name="ifra"):
        self.name=name
        print("hello i am " )
print(human.abc)
h2=human("hhj")
