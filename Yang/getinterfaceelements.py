"""
    Original
    Netconf python example by yang-explorer (https://github.com/CiscoDevNet/yang-explorer)
    Modified
    S. Hart

    Running script: (save as example.py)
    > python getinterfaceelements.py -a 64.103.37.51 -u root -p C\!sc0123 --port 10000
    need to hash out the ! with \
"""

import lxml.etree as ET
from argparse import ArgumentParser
from ncclient import manager
from ncclient.operations import RPCError
import sys

count = 0

payload = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
<interface>
</interface>
</interfaces>
</filter>
"""

if __name__ == '__main__':



    parser = ArgumentParser(description='Usage:')

    # script arguments
    parser.add_argument('-a', '--host', type=str, required=True,
                        help="Device IP address or Hostname")
    parser.add_argument('-u', '--username', type=str, required=True,
                        help="Device Username (netconf agent username)")
    parser.add_argument('-p', '--password', type=str, required=True,
                        help="Device Password (netconf agent password)")
    parser.add_argument('--port', type=int, default=830,
                        help="Netconf agent port")
    parser.add_argument('--node', type=str,
    					help="xml element from tree to display")
    args = parser.parse_args()

    # connect to netconf agent
    with manager.connect(host=args.host,
                         port=args.port,
                         username=args.username,
                         password=args.password,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'name': 'csr'}) as m:

        # execute netconf operation
        try:
            response = m.get(payload).xml
            myxml = response.encode('UTF-8')
            data = ET.fromstring(myxml)
        except RPCError as e:
            data = e._raw

        # beautify output
        #print(ET.tostring(data, pretty_print=True))
		
		
        if args.node is not None:
		        for node in data.findall(args.node):
        	            print (node.text)
        		
        else:
        	print ("no namespace and element defined")
    
    

#'.//{urn:ietf:params:xml:ns:yang:ietf-ip}ip'


#note need to test for args.node before connecting to device, otherwise connection
#is superflous
