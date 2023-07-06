import argparse

from db import *
from utils import *
from interactive import start_interactive
from server import start_server

defcon_db = None
BD_FILE="defcon_data.bd"

def main():
    #Argument parsing:
    parser = argparse.ArgumentParser(description="DEFCON server app")
    parser.add_argument('--server', required=False, help="Enable server mode?",action='store_true')
    args= parser.parse_args()
    
    serverMode=args.server

    # Start the backend:
    defcon_db = db_get_file(BD_ENV_VAR)
    
    # Run in desired mode:
    if serverMode:
        start_server(defcon_db)
    else:
        start_interactive(defcon_db)

if __name__ == "__main__":
    main()