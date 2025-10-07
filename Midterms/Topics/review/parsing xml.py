import xml.etree.cElementTree as ET

tree = ET.parse('./Midterms/Topics/review/example.xml')
root = tree.getroot()

# print(f"{root[0][0].tag}")
for child in root:
    print(child[0].tag)
    print(child[0].text)
    print()
    
# xml tree as indexed list
#  [ <element_1><subelement>...</subelement><element_1/>, <element_1><subelement>...</subelement><element_1/> ]
#! 0                                                      1

