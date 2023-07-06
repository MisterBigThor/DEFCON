import argparse

from db import db_get_file
from utils import log_info
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
    defcon_db = db_get_file(BD_FILE)
    
    # Run in desired mode:
    if serverMode:
        log_info("Starting server mode")
        start_server(defcon_db)
    else:
        log_info("Starting interactive mode")
        start_interactive(defcon_db)

if __name__ == "__main__":
    main()