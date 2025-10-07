import json

product_data = {
    "products":[]
}

while True:
    x = input("Enter Product, f to exit: ")
    product_data["products"].append(x)
    
    if x.lower() == 'f':
        break
    
print(product_data["products"])

# convert to json
convert_to_json = json.dumps(product_data)
print(convert_to_json)

#parse
y = json.loads(convert_to_json)
print(y)

# write/generate json file
with open("product.json", "w") as f:
    json.dump(y, f)
    
    
# read file
with open("product.json", "r") as f:
    data = json.load(f)
print("reading: ", data)