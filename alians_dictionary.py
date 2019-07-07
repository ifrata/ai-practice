import json

abc={
'i':'oho',
'am':'ell',
'you':'won',
'we':'cam',
'is':'siri'}

try:
    with open('dictiony.json','r')as f:
         json.dump(abc,f)
except Exception:
    print("there is an error")
    
    
