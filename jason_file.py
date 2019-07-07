import json
# with open('student.json','w')as f:
#     lst=['inam','ali','4388']
#     di={'name':'ifra','age':'24'}
#     json.dump(di,f)


with open('student.json','r')as f:
    data=json.load(f)
    print(data)