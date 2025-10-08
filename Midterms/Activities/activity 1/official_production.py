import json
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear()    

MARKET = {
        "market":[
        {
            "id":1,
            "name":"Legazpi City Centro Market",
            "products":[]
        },
        {
            "id":2,
            "name":"Ayala Malls Legazpi City",
            "products":[]
        }
    ]
}

customer = None
chosen_marketplace = None


# BEGIN PROGRAM
while True:
    try:
        # CHOOSE MARKETPLACE
        print("   MEAT MARKET   ".center(50, '=').rjust(5))   
        print() 
        for marketplace, val in MARKET.items():
            if isinstance(val, list):
                for subelements in val:
                    if isinstance(subelements, dict):
                        for key, val in subelements.items():
                            if key == 'id':
                                print(f"[{val}] ", end="")
                            if key == 'name':
                                print(f"{val}")
        print()
        customer = int(input("Choose a Marketplace or 0 to quit: "))
   
        if customer == 0:
            clear()
            print("\n[!] Program has ended!\n")
            break
        else:
            chosen_marketplace = customer
            customer = None
            
            # OPTIONS
            while True:
                clear()
                print("   PRODUCT MARKET   ".center(50, '=').rjust(5))   
                print() 
                for MARKETPLACE, market in MARKET.items():
                    if MARKETPLACE == "market":
                        if isinstance(market, list):
                            for ELEMENT, element in market[chosen_marketplace - 1].items():
                                if ELEMENT == "name":
                                    print(f"{element}:")
                print("[1] Add product\n[2] Remove Product\n[3] View Product\n[4] Quit".rjust(5))
                print()
                customer = int(input("choice: "))
                
                if customer == 4:
                    clear()
                    customer = None
                    chosen_marketplace = None
                    break
                else:
                    if customer == 1:
                        clear()
                        customer = None
                        
                        # ADD ITEMS
                        while True:
                            
                            print("   PRODUCT MARKET   ".center(50, '=').rjust(5))   
                            print() 
                            customer = input("Add item or 'F' to exit: ")
                            if customer.lower() == "f":
                                clear()
                                
                                # convert to json
                                convert_to_json = json.dumps(MARKET)
                                
                                # parse
                                parse = json.loads(convert_to_json)
                                
                                #write
                                with open("marketplace.json", "w") as f:
                                    json.dump(parse, f, indent=4)
                                
                                break
                            else:
                                clear()
                                for MRKT, market in MARKET.items():
                                    if MRKT == "market":
                                        if isinstance(market, list):
                                            for KEY, val in market[chosen_marketplace - 1].items():
                                                if KEY == "products":
                                                    if isinstance(val, list):
                                                            # if val.count(customer) == 0:
                                                            #     val.append(customer)
                                                            # else:
                                                            #     clear()
                                                            #     print("[!] Item is already in the list.")
                                                            val.append(customer)
                                                            
                                                            
                    elif customer == 2:
                        clear()
                        customer = None
                        
                        while True:
                            print("   PRODUCT MARKET   ".center(50, '=').rjust(5))  
                            
                            # parse json file 
                            with open("marketplace.json", "r") as f:
                                parsed_data =  json.load(f)

                            # print
                            selected_market = chosen_marketplace
                            for key, val in parsed_data.items():
                                if isinstance(val, list):
                                    if isinstance(val[selected_market - 1], dict):
                                        for INF, info in val[selected_market - 1].items():
                                            if INF == "products":
                                                if isinstance(info, list):
                                                    for INDEX, elements in enumerate(info, start=1):
                                                        print(f"[{INDEX}] {elements}")

                            # store products to remove           
                            products_to_remove = []
                            while True:
                                x = input("Select a product to remove, f to quit: ")
                                
                                if x.isdigit():
                                    if int(x) == 0:
                                        print("[!] 0 is not a valid selection.")
                                    else:
                                        for key, val in parsed_data.items():
                                            if isinstance(val, list):
                                                if isinstance(val[selected_market - 1], dict):
                                                    for INF, info in val[selected_market - 1].items():
                                                        if INF == "products":
                                                            if isinstance(info, list):
                                                                if products_to_remove.count(info[int(x) - 1]) == 0:
                                                                    products_to_remove.append(info[int(x) - 1])
                                                                    print(products_to_remove)
                                                                else:
                                                                    print("Product already in list to remove.")
                                else:
                                    if x.isalpha():
                                        if x.lower() == 'f':
                                            break
                            
                            # proceed to remove
                            for key, val in parsed_data.items():
                                if isinstance(val, list):
                                    if isinstance(val[selected_market - 1], dict):
                                        for INF, info in val[selected_market - 1].items():
                                            if INF == "products":
                                                if isinstance(info, list):
                                                    for elements_to_remove in products_to_remove:
                                                        info.remove(elements_to_remove)
                            
                            # update JSON
                            with open("marketplace.json", "w") as f:
                                json.dump(parsed_data, f, indent=4)
                            
                            clear()
                            print("[!] Product/s removed successfully!")
                            break

                    elif customer == 3:
                        clear()
                        customer = None
                        
                        # VIEW PRODUCTS
                        print("   PRODUCT MARKET   ".center(50, '=').rjust(5))   
                        print() 

                        # read JSON file
                        with open("marketplace.json", "r") as f:
                            parsed_data = json.load(f)
                        
                        selected_market = chosen_marketplace
                        print("   CURRENT PRODUCTS   ".center(50, '=').rjust(5))
                        for key, val in parsed_data.items():
                            if isinstance(val, list):
                                if isinstance(val[selected_market - 1], dict):
                                    for INF, info in val[selected_market - 1].items():
                                        if INF == "products":
                                            if isinstance(info, list):
                                                if len(info) == 0:
                                                    print("[!] No products available.")
                                                else:
                                                    for INDEX, elements in enumerate(info, start=1):
                                                        print(f"[{INDEX}] {elements}")
                                                        
                        y = input("Press 'F' to exit: ")
                        if y.lower() == 'f':
                            clear()
                            
    except:
        clear()
        print("[!] Invalid input. Input must be an integer.")
    