from ncclient import manager
import xmltodict

router_list = ['10.10.1.1', '10.10.1.2', '10.10.4.2', '10.10.2.2']

user = 'admin'
password = 'admin'

ospf_filter = """
    <filter>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <router>
                <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                </ospf>
            </router>
        </native>
    </filter>
    """

ospf_config_filter = """
    <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <router>
                <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                    <id>{proc_id}</id>
                    <network>
                        <ip>{net_range}</ip>
                        <mask>{net_mask}</mask>
                        <area>{net_area}</area>
                    </network>
                </ospf>
            </router>
        </native>
    </config>
"""


for ip_router in router_list:
    with manager.connect(host=ip_router, port=830, username=user, password=password,hostkey_verify=False) as m:
        ospf_netconf = m.get(ospf_filter)
        ospf_python = xmltodict.parse(ospf_netconf.xml)["rpc-reply"]["data"]

        if ospf_python is not None:
            for key,values in ospf_python["native"]["router"].items():
                if key == "ospf":
                    print("\n\nThe router {} has OSPF already configured: ".format(ip_router))
                    pid=ospf_python["native"]["router"]["ospf"]["id"]
                    #rid=ospf_python["native"]["router"]["ospf"]["router-id"]
                    net=ospf_python["native"]["router"]["ospf"]["network"]["ip"]
                    print("PID: {}\nNetwork: {}\n".format(pid,net))
                else:
                    print("OSPF is not configured")
        else:
            print("Router {} has no routing configured".format(ip_router))

    with manager.connect(host=ip_router, port=830, username=user, password=password,hostkey_verify=False) as m:
        netconf_ospf = ospf_config_filter.format(proc_id="10",net_range="10.10.0.0",net_mask="0.0.255.255",net_area="0")
        config_ospf = m.edit_config(netconf_ospf, target="running")


    with manager.connect(host=ip_router, port=830, username=user, password=password,hostkey_verify=False) as m:
        ospf_netconf = m.get(ospf_filter)
        ospf_python = xmltodict.parse(ospf_netconf.xml)["rpc-reply"]["data"]

        if ospf_python is not None:
            for key,values in ospf_python["native"]["router"].items():
                if key == "ospf":
                    print("\n\nThe router {} was configured succesfully, current config: ".format(ip_router))
                    pid=ospf_python["native"]["router"]["ospf"]["id"]
                    #rid=ospf_python["native"]["router"]["ospf"]["router-id"]
                    net=ospf_python["native"]["router"]["ospf"]["network"]["ip"]
                    print("PID: {}\nNetwork: {}\n".format(pid,net))
                else:
                    print("OSPF is not configured")
        else:
            print("We were not able to configure Router {}\n".format(ip_router))
