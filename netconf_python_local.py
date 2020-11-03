from ncclient import manager
import xmltodict

host = '10.10.1.2'
user = 'admin'
password = 'admin'

netconf_filter = """
 <filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
    </interface>
  </interfaces-state>
</filter>
"""
config_filter = """
<config>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
        <name>{inter_name}</name>
        <description>{inter_descr}</description>
    </interface>
  </interfaces>
</config>
"""
#Uses managet.connect to connect to the device, stores the connection as m
with manager.connect(host=host, port=830, username=user, password=password,hostkey_verify=False) as m:
    interface_netconf = m.get(netconf_filter)
    print('getting running config...')
    #print(interface_netconf)

#Stores the configuration 
interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]

guide = interface_python['interfaces']['interface']

print("Printing current interfaces...\n")
print("    -Interface-      -IP-     -Description-")
for dicts in guide:
    name = dicts['name']
    for key,value in dicts['ipv4'].items():
        if key == 'address':
            ip = value['ip']
        else:
            ip = 'None     '
    for key,value in dicts.items():
        if key == 'description':
            descr = value
            break
        else:
            descr = "Empty"
    
    print(name + "   " + ip + "   " + descr)

print("\n\nModifying interfaces description using Netconf\n\n")


with manager.connect(host=host, port=830, username=user, password=password,hostkey_verify=False) as m:
    for interfaces in guide:
        netconf_config = config_filter.format(inter_name=interfaces["name"],inter_descr="Configured by NETCONF")
        interface_config = m.edit_config(netconf_config, target="running")
        
print("Results after modifying the interfaces\n\n\n")



with manager.connect(host=host, port=830, username=user, password=password,hostkey_verify=False) as m:
    interface_netconf_after = m.get(netconf_filter)
    print('getting running config...')
    #print(interface_netconf)

#Stores the configuration 
interface_python_after = xmltodict.parse(interface_netconf_after.xml)["rpc-reply"]["data"]

guide_after = interface_python_after['interfaces']['interface']

print("Printing current interfaces...\n")
print("    -Interface-      -IP-     -Description-")
for dicts_after in guide_after:
    name = dicts_after['name']
    for key,value in dicts_after['ipv4'].items():
        if key == 'address':
            ip = value['ip']
        else:
            ip = 'None     '
    for key,value in dicts_after.items():
        #print("La llave en el after es: {} y el valor es {}".format(key,value))
        if key == 'description':
            descr = value
            break
        else:
            descr = "Empty"
    
    print(name + "   " + ip + "   " + descr)
