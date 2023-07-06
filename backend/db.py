from utils import *

# TODO: Tidy up this region
# BD_COLORS = {
#    1 : ('DEFCON1', 'white'), 2 : ('DEFCON2', 'red'),
#    3 : ('DEFCON3', 'yellow'),4 : ('DEFCON4', 'green'),
#    5 : ('DEFCON5', 'blue')
#}

BD_ENV_VAR='DEFCON_DB_PATH'
BD_FILE="defcon_data.bd"


def db_get_file(db_file:str) -> str:
    v = getEnvVar(BD_ENV_VAR)
    if v is not None:
        return pathAndFile(v, db_file)
    else: 
        return db_file

def create_new_bd(fName:str):
    with open(fName, 'x') as bd_file:
        record=getRecord("5")
        bd_file.write(record)
    print(f"{WARN} generated new BD with default value DEFCON5.")

def db_load_defcon(fName:str):
    if not fileExist(fName):
        log_info(f"can't find db file {fName}")
        create_new_bd(fName)

    with open(fName, mode='r') as bd_file:
        log_info(F"find db file, loading...")
        raw=""
        for line in bd_file.readlines():
            log_info(f"read DEFCON value: {line.strip()}")
            raw=line.split("->")[1]
        
        return raw

def db_store_defcon(fName:str, defcon:str):
    record=getRecord(defcon)
    with open(fName, 'a') as bd_file:
        bd_file.write(record)
        log_info(f"updated {record}")
        