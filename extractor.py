#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 17:21:43 2017

@author: ale

extractor of views counts

rom lxml import etree
import xml.etree.ElementTree as ElementTree

CONTENT = "
<process id="process1">
 <log name="name1" device="device1"><![CDATA[timestamp value]]></log>
 <log name="name2" device="device2"><![CDATA[timestamp value, timestamp value, timestamp]]></log>
</process>
"

def parse_with_lxml():
    root = etree.fromstring(CONTENT)
    for log in root.xpath("//log"):
        print log.text

def parse_with_stdlib():
    root = ElementTree.fromstring(CONTENT)
    for log in root.iter('log'):
        print log.text

if __name__ == '__main__':
    parse_with_lxml()
    parse_with_stdlib()

"""

import xml.etree.ElementTree as ET
import json

file=open("iaBH1tIaCo8",'r')
f=file.read()
tree=ET.fromstring(f)
file.close()

#for item in tree.findall("graph_data"):
#    print (item.text)
text_data=tree.find("graph_data").text
data_dict=json.loads(text_data) 
viewcounts=data_dict["views"]["daily"]["data"]  