import json
import xml.etree.ElementTree as ET
from collections import Counter


def read_json():
    with open("newsafr.json", encoding='utf-8-sig') as na:
        data = json.load(na)
        for v1 in data.values():
            x = []
            for v2 in v1['channel']['items']:
                a = v2['description'].split()
                for b in a:
                    if len(b) > 6:
                        x.append(b.lower())
        z1 = Counter(x).most_common(10)
        print(z1)


read_json()


def read_xml():
    tree = ET.parse(r"newsafr.xml")
    root = tree.getroot()
    items = root.findall("channel/item")
    y1 = []
    for item in items:
        x1 = (item.find("description").text).split()
        # y1 = []
        for x2 in x1:
            if len(x2) > 6:
                y1.append(x2.lower())
    v1 = Counter(y1).most_common(10)
    print(v1)

read_xml()