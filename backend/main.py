#!/bin/python3
from db import *

PERSISTANCE_FILE="defcon_data.bd"

def main():
    # Load value from database
    defcon_value = load_defcon_value(PERSISTANCE_FILE)
    print(f"DEFCON {defcon_value}")
    print("Enter a new DEFCON value [1,5]\n0 to exit")
    
    # Loop for updating
    while True:
        try:
            print(f"DEFCON {defcon_value}")
            new_val = int(input("New value:"))
            if corretVal(new_val):
                store_defcon_value(PERSISTANCE_FILE, str(new_val))
                defcon_value=new_val
            elif new_val == 0: 
                exit(0)
            else: 
                raise ValueError
        except ValueError:
            print("incorrect value")
        
if __name__ == "__main__":
    main()