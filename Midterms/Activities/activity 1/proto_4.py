import json
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

MARKETPLACE = {
    "market":[
        {
            "id":1,
            "name":"LCC",
            "products":[]
        },
        {
            "id":2,
            "name":"Ayala",
            "products":[]
        }
    ]
}

# removing a product?

# first get the json and parse
with open("product.json", "r") as f:
    parsed_data =  json.load(f)
print(f"{type(parsed_data)} : {parsed_data}")

# acess data
#! print(parsed_data["market"][0])

# print
selected_market = 1
for key, val in parsed_data.items():
    if isinstance(val, list):
        #* print(val[selected_market - 1])
        if isinstance(val[selected_market - 1], dict):
            for INF, info in val[selected_market - 1].items():
                #* print(INF)
                if INF == "products":
                   if isinstance(info, list):
                    #* print(info)
                    for INDEX, elements in enumerate(info, start=1):
                        print(f"[{INDEX}] {elements}")

#store products to remove           
products_to_remove = []
while True:
    x = input("Select a product to remove, f to quit: ")
    
    if x.isdigit():
        for key, val in parsed_data.items():
            if isinstance(val, list):
                if isinstance(val[selected_market - 1], dict):
                    for INF, info in val[selected_market - 1].items():
                        if INF == "products":
                            if isinstance(info, list):
                            #!   print(info[0])
                            #!   products_to_remove.append(info[int(x)])
                            #!   print(products_to_remove)
                                if products_to_remove.count(info[int(x)]) == 0:
                                    products_to_remove.append(info[int(x)])
                                    print(products_to_remove)
                                else:
                                    print("Product already in list to remove.")
    else:
        if x.isalpha():
            if x.lower() == 'f':
                break
            
#proceed to remove
for key, val in parsed_data.items():
    if isinstance(val, list):
        if isinstance(val[selected_market - 1], dict):
            for INF, info in val[selected_market - 1].items():
                if INF == "products":
                   if isinstance(info, list):
                      for elements_to_remove in products_to_remove:
                          info.remove(elements_to_remove)
                          
# update
with open("product.json", "w") as f:
    json.dump(parsed_data, f, indent=4)