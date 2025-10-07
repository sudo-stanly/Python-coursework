import json
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

product_data = {
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

clear()
# input
print(" MARKETPLACE ".center(50, '='))
print("\nAvailable Markets:")
for marketplace, val in product_data.items():
    if isinstance(val, list):
        # print(val)
        for subelements in val:
            # print(subelements)
            if isinstance(subelements, dict):
                for key, val in subelements.items():
                    if key == 'id':
                        print(f"[{val}] ", end="")
                    if key == 'name':
                        print(f"{val}")
    
print()
marketID = int(input("Choose a market: "))
while True:
    
    product = input("[!] Place your products, f to quit: ")
    product_data["market"][marketID - 1]["products"].append(product)

    if product.lower() == 'f':
        break
    
# remove 'f'
product_data["market"][marketID - 1]["products"].pop()
    
# convert to json
convert_to_json = json.dumps(product_data)
print(convert_to_json)

# parse
parse = json.loads(convert_to_json)

# write json file
with open("product.json", "w") as f:
    json.dump(parse, f, indent=4)