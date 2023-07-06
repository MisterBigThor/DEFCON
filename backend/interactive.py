#!/bin/python3
from db import *
from utils import *

BD_FILE="defcon_data.bd"

def main():
    db_file=check_env(BD_FILE)

    # Load value from database
    defcon_value = load_defcon_value(db_file)
    print(f"DEFCON {defcon_value}")
    print("Enter a new DEFCON value [1,5]\n0 to exit")
    
    # Loop for updating
    while True:
        try:
            print(f"DEFCON {defcon_value}")
            user_val = int(input("New value:"))
            if corretVal(user_val):
                store_defcon_value(db_file, str(user_val))
                defcon_value=user_val
            elif user_val == 0: 
                exit(0)
            else: 
                raise ValueError
        except ValueError:
            print("incorrect value")
        
if __name__ == "__main__":
    main()