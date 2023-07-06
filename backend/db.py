from utils import *

BD_ENV_VAR='DEFCON_DB_PATH'
DEFAULT_BD_FILE="defcon_data.bd"

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
    log[1](f"generated new BD with default value DEFCON5.")

def db_load_defcon(fName:str):
    if not fileExist(fName):
        log[0](f"can't find db file {fName}")
        create_new_bd(fName)

    with open(fName, mode='r') as bd_file:
        log[0](f"find db file, loading...")
        raw=""
        for line in bd_file.readlines():
            log[0](f"read DEFCON value: {line.strip()}")
            raw=line.split("->")[1]
        
        return raw

def db_store_defcon(fName:str, defcon:str):
    record=getRecord(defcon)
    with open(fName, 'a') as bd_file:
        bd_file.write(record)
        log[0](f"update {record}")
        