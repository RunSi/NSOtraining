#!/usr/bin/env python

import logging
from lxml import etree
from ncclient import manager
from ncclient.xml_ import *
import sys
import xml.dom.minidom

# the variables below assume the user is leveraging the
# network programmability lab and accessing csr1000v
# use the IP address or hostname of your CSR1000V device
HOST = 'ios-xe-mgmt.cisco.com'
# use the NETCONF port for your CSR1000V device
PORT = 10000
# use the user credentials for your CSR1000V device
USER = 'root'
PASS = 'C!sc0123'
MODULE_NAME = 'ietf-ipv4-unicast-routing'


# create a main() method
def main():
    """Main method that prints netconf capabilities of remote device."""
    with manager.connect(host=HOST, port=PORT, username=USER, password=PASS,
                         hostkey_verify=False, device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as m:

        # print YANG module
        print('***Saving the YANG Module***')
        data = m.get_schema('ietf-ipv4-unicast-routing')
        xml_doc = xml.dom.minidom.parseString(data.xml)
        yang_module = xml_doc.getElementsByTagName("data")

        # save the YANG module to a file
        with open(MODULE_NAME, mode='w+') as f:
            f.write(yang_module[0].firstChild.nodeValue)

if __name__ == '__main__':
    sys.exit(main())
