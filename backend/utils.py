from os.path import isfile, join
from os import getenv
import datetime

#LOG:
INFO="INFO:"
WARN="WARN:"
log_info    = lambda msg : print(f"{INFO} {msg}") 
log_warn    = lambda msg : print(f"{WARN} {msg}") 

#ENV Fx:
existEnv    = lambda env_var : (getenv(env_var) != None)
getEnvVar   = lambda env_var : getenv(env_var)

#FILE MANAGEMENT Fx:
fileExist   = lambda fName : isfile(fName)
pathAndFile = lambda p, fName : join(p,fName)

#APP Fx:
corretVal   = lambda val : 1 <= val and val <= 5
recordDate  = lambda : datetime.datetime.now().strftime("%x %X")
getRecord   = lambda record : recordDate() + " -> " + record + "\n"