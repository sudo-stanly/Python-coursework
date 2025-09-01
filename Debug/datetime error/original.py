from datetime import datetime, timedelta

day = int(input("Enter Day/s: "))

def lab_func(bilang):
    noon = datetime.now - timedelta(days - bilang)
    ngayon = datetime.now
    if(noon < ngayon):
        print("Hindi na")
    else:(
        print("Oo pa yieee")
    )
    
    return lab_func

lab_func(day)