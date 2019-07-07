import csv
# with open('data.csv','r') as f:
#     students=csv.reader(f)
#     for student in students:
#         print(student)

students=[

["name","age","education"],
["abc","24","bscs"],
["xyz","20","accp"]

]

with open('bb.csv','a',newline='') as xx:
    writer=csv.writer(xx,delimiter='|')
    for student in students:
        writer.writerow(student)