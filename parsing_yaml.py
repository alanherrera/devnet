import yaml
from yaml import load, load_all

stream = open('sample.yaml', 'r')
documents = load_all(stream, Loader=yaml.FullLoader)

for doc in documents:
    y = 0
    for items in doc['people']:
        if y == 0:
            names = doc['people'][y]['FirstName']
        elif y == (len(doc['people']) - 1):
            names = names +" "+ "and"+" "+doc['people'][y]['FirstName']
        else:
            names = names +" "+","+" "+doc['people'][y]['FirstName']
        y = y + 1
    print("First names in the document are: {}".format(names))
    
def(test_merge_conflict)


LALALA