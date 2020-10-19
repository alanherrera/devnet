from ncclient import manager
import xmltodict

host = 'ios-xe-mgmt.cisco.com'
user = 'developer'
password = 'C1sco12345'

netconf_filter = """
 <filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
        <name>Gigabit1</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
    </interface>
  </interfaces-state>
</filter>
"""

#Uses managet.connect to connect to the device, stores the connection as m
with manager.connect(host=host, port=10000, username=user, password=password,hostkey_verify=False) as m:
    interface_netconf = m.get(netconf_filter)
    print('getting running config...')
    #print(interface_netconf)

#Stores the configuration 
interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]

guide = interface_python['interfaces']['interface']
#name = interface_python['interfaces']['interface']['name']['#text']
#enabled = interface_python['interfaces']['interface']['enabled']

#print("\n\n")
#print(guide)
#print("\n\n\n")

for dicts in guide:
    name = dicts['name']
    for key,value in dicts['ipv4'].items():
        if key == 'address':
            ip = value['ip']
        else:
            ip = 'No IP'
    for key,value in dicts.items():
        if key == 'description':
            descr = value
        else:
            descr = "No description"
    print(name)
    print(ip)
    print(descr)
    print('\n\n')

#if enabled == True:
    #print("\n")
    #print("The interface {} is enabled \n".format(name))

#else:
#    print("\n")
#    print("The interface {} is disabled \n".format(name))


    