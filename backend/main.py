import argparse

from db import db_get_file
from utils import log
from interactive import start_interactive
from server import start_server

global verboseMode 
defcon_db = None
BD_FILE="defcon_data.bd"

def main():
    #Argument parsing:
    parser = argparse.ArgumentParser(description="DEFCON server app")
    parser.add_argument('--server', required=False, help="Enable server mode?",action='store_true')
    parser.add_argument('--verbose', required=False, help="Be verbose?", action='store_true')
    args= parser.parse_args()
    
    serverMode  = args.server
    verboseMode = args.verbose

    # Start the App:
    defcon_db = db_get_file(BD_FILE)
    if not verboseMode :
        log[0] = lambda _ : None
        log[1] = lambda _ : None
        log[2] = lambda _ : None
    
    # Run in desired mode:
    if serverMode:
        log[0]("Starting server mode")
        start_server(defcon_db)
    else:
        log[0]("Starting interactive mode")
        start_interactive(defcon_db)

    log[0]("Finish app")
if __name__ == "__main__":
    main()