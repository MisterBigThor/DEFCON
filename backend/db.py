from os.path import isfile
import datetime

INFO="INFO:"
WARN="WARN:"

defcon_data = {
    1 : ('DEFCON1', 'white'), 2 : ('DEFCON2', 'red'),
    3 : ('DEFCON3', 'yellow'),4 : ('DEFCON4', 'green'),
    5 : ('DEFCON5', 'blue')
}


fileExist   = lambda fName : isfile(fName)
corretVal   = lambda val : 1 <= val and val <= 5
recordDate  = lambda : datetime.datetime.now().strftime("%x %X")
getRecord   = lambda defcon : recordDate() + " -> " + defcon + "\n"

def create_new_bd(fName:str):
    with open(fName, 'x') as bd_file:
        record=getRecord("5")
        bd_file.write(record)
    print(f"{WARN} generated new BD with default value DEFCON5.")

def load_defcon_value(fName:str):
    if not fileExist(fName):
        print(f"{WARN} can't find db file, creating new one.")
        create_new_bd(fName)

    with open(fName, mode='r') as bd_file:
        print(f"{INFO} find db file, loading...")
        raw=""
        for line in bd_file.readlines():
            print(f"{INFO} read DEFCON value:", line.strip())
            raw=line.split("->")[1]
        
        return raw

def store_defcon_value(fName:str, defcon:str):
    record=getRecord(defcon)
    with open(fName, 'a') as bd_file:
        bd_file.write(record)
        print(f"{INFO} updated {record}")
        