import json

jsonobj = json.load(open("sample.json"))


for value in jsonobj['people'][0].values():
    print(value)

y=0
for x in jsonobj['people']:
    for key,values in jsonobj['people'][y].items():
        print(key,values)

    y = y + 1 