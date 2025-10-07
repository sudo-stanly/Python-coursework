import json

product_data = {
    "market":[
        {
            "id":1,
            "products":[]
        },
        {
            "id":2,
            "products":[]
        }
    ]
}

# input
marketID = 1
product_data["market"][marketID - 1]["products"].append("apple")
print(product_data["market"][marketID - 1]["products"])

# convert to json
convert_to_json = json.dumps(product_data)
print(convert_to_json)

# parse
parse = json.loads(convert_to_json)

# write json file
with open("product.json", "w") as f:
    json.dump(parse, f)