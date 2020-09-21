import xmltodict


#Get the xml file and open it
stream = open('sample.xml', 'r')

#Parse the XML file into a Dict
xml = xmltodict.parse(stream.read())

for e in xml["People"]["Person"]:
    for key, value in e.items():
        if key == "FirstName":
            FN = value
        if key == "Email":
            EM = value
    print("The person {} has the email {}".format(FN, EM))
    
