#Element tree library that comes embedded into Python, not recommended
#import xml.etree.ElementTree as ET

#lxml is the preferred tool to use when working with XML files
from lxml import etree as ET

stream = open('sample.xml', 'r')

xml = ET.parse(stream)

#Gets the root element of the Document
root = xml.getroot()

#Prints each element "e" inside the root (People). In case of sample.xml, prints each Person.
for e in root:

    #Prints each element of the root (or each in Person if using sample.xml).
    print(ET.tostring(e))
    
    #Prints a blank space
    print("")

    #Prints the ID of the person that was printed.
    print(e.get("Id"))