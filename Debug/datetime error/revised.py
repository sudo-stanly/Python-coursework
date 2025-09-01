import datetime
from datetime import datetime, timedelta

day = int(input("Enter Day/s: "))

def lab_func(num_of_days):
    
    before = datetime.now() - timedelta(num_of_days)
    after = datetime.now()
    print(f"before\t:\t{before}\nafter\t:\t{after}")
    
    marital_status_hahahah = "Hindi na" if before < after else "Oo pa yieee"
    print(marital_status_hahahah)
    
    return lab_func

lab_func(day)