#!/bin/python3
from db import *


def start_interactive(db_file):

    # Load value from database
    defcon_value = db_load_defcon(db_file)
    print(f"DEFCON {defcon_value}")
    print("Enter a new DEFCON value [1,5]\n0 to exit")
    
    # Loop for updating from the user
    while True:
        try:
            print(f"DEFCON {defcon_value}")
            user_val = int(input("New value:"))
            if corretVal(user_val):
                db_store_defcon(db_file, str(user_val))
                defcon_value=user_val
            elif user_val == 0: 
                exit(0)
            else: 
                raise ValueError
        except ValueError:
            print("incorrect value")
        
if __name__ == "__main__":
    start_interactive()