# srcds launcher

print "## PySrcds by Errant ##" 
import sys
import os

# add paths to import .locations
sys.path.append(os.getcwd()+"/contrib")
sys.path.append(os.getcwd()+"/core")

# imports
import launcher

type = raw_input("Start server type: ")

server = launcher.startServer(type)
