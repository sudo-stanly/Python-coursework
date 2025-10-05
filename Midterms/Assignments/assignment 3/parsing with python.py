# this is where we will practice parsing an xml file using python
# i will parse the xml in the file "example.xml"
# this file has a tree of xml elements, root, child and subchild

# but first to visualize this first in a json form (dictionary for python):
data = {
    "date" : "10-05-2025",
    "stock_1": {
        "name":"Microsoft",
        "ticker":"MSFT",
        "price": 234.24,
        "currency": "USD"
    },
    "stock_2": {
        "name":"Apple",
        "ticker":"APPL",
        "price": 140.09,
        "currency": "USD"
    }
}
# this is how normally it would look in a json format. but in xml it would look like this:
"""
<data date="10-05-2025">
    <stock>
        <name>Microsoft</name>
        <ticker>MSFT</ticker>
        <price>234.24</price>
        <currency>USD</currency>
    </stock>
    <stock>
        <name>Apple</name>
        <ticker>APPL</ticker>
        <price>140.09</price>
        <currency>USD</currency>
    </stock>
</data>
"""

# to access an instance of with our json dictionary:
# we use bracket notation of key value pair or with for loop

# for loop printing all dictionary values
#* for keys in data:
#*     print(f"{keys} : {data[keys]}")

# notation:
#* print(data["date"]) #prints the date value by accessig the key pair
#* print(data["stock_1"]["name"]) # prints the key and pairs and value of the key

#* for loop:
#*  for key, value in data.items():
    
#*      if not isinstance(value,dict):
#*          print(f"{key} : {value}")
    
#*      if isinstance(value, dict):
#*          print(f"key : {key}")
#*          for stocks, info in value.items():
#*              print(f"\t{stocks} : {info}")
#*      print()
    
    
# but since we're going for xml:
# first we import the xml tree
import xml.etree.cElementTree as ET

# parse xml into element tree
# tree = ET.parse('xml_file.xml')
tree = ET.parse('./Midterms/Assignments/assignment 3/example.xml')
root = tree.getroot()

# root
#* print(root) # this prints the binary data and root tag itself : <Element 'data' at 0x79ee1569e2f0>
#* print(root.tag) # this prints the exact tag name of the root : data
#* print(len(root)) # this prints the length of the tag : which is 2 because it has 2 children inside of the root(parent)
#                  # by commenting or removing the other child, the length will be 1


# # accessing root child by using bracket notation:
#* print(root[0].tag) # this prints the first child of the root which is stock
#* print(len(root[0])) # this prints the length of the child which is 5 because it has subchildren of name, ticker, price, and currency



# another way to retrieve the xml file is by using for loop:
"""
    xml:
    * <data date="10-05-2025">
    *     <stock>
    *         <name>Microsoft</name>
    *         <ticker>MSFT</ticker>
    *         <price>234.24</price>
    *         <currency>USD</currency>
    *     </stock>
    *     <stock>
    *         <name>Apple</name>
    *         <ticker>APPL</ticker>
    *         <price>140.09</price>
    *         <currency>USD</currency>
    *     </stock>
    * </data>
"""
#* for child in root:
#*     # print(child[0].tag) 
#*     # print(child[0].text) 
#*     # ! print(f"{child[0].tag} : {child[0].text}")
    
#*     # explain: 
#*     # since we're using for loop we want to access the children inside the root
#*     # since we're looping over the children we then want to print the subchildren
#*     # with their tags and text(values) inside.
#*     #
#*     # we can change which access we want with the subchildren
#*     print(f"{child[1].tag} : {child[1].text}")






"""
    xml:
    * <data date="10-05-2025">
    *     <stock>
    *         <name>Microsoft</name>
    *         <ticker>MSFT</ticker>
    *         <price>234.24</price>
    *         <currency>USD</currency>
    *     </stock>
    *     <stock>
    *         <name>Apple</name>
    *         <ticker>APPL</ticker>
    *         <price>140.09</price>
    *         <currency>USD</currency>
    *     </stock>
    * </data>
"""
# if we want to access relative to the root tag:
#! first child element [0][]
#* print(root[0][0].tag) # prints name tag
#* print(root[0][0].text) # prints the value of the name tag
#*                       # the first notation we access [0][] the first element(child) which is is the stock
#*                       # and the first element [0][0] of that child the subchild is name

#* print(root[0][1].tag) # prints ticker tag
#* print(root[0][1].text) # prints value of ticker tag


# #! the 2nd child element [1][]
#* print(root[1][2].tag) # prints ticker tag
#* print(root[1][2].text) # prints value of ticker tag






"""
    xml:
    * <data date="10-05-2025">
"""
#getting the attributes next
print(root.attrib) # prints the attribute of the root: "date" then the value: 0-05-2025 : {'date': '10-05-2025'}




# another example is looping over the ticker tag, or iterating over multiple elements(subchildren) inside the child
#* for ticker in root.iter('ticker'):
#*     print(ticker.text)
# this searches for all the tickers within the root and iterating through them



# another imprortant function is by using the findall function
# find children with 'price' tag
# this only looks through direct children and does not look at any children or any below that.
#* print(len(root[0].findall('price')))
#* print(root[0].findall('price')[0].text)



# change price and remove currency (manipulate xml data)
root[0][2].text = "233"
root[1].remove(root[1][3])
tree.write('./Midterms/Assignments/assignment 3/example.xml')