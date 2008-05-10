from core.srcds import pyserver
from contrib.path import path
from contrib.configobj import ConfigObj

'''

    Setup and run a CounterStrike:Source server emulator

'''

class Server(pyserver._SourceServer):
    '''
        Sub class the main server class
    '''
    def __init__(self,name):
        # init the parent
        pyserver._SourceServer.__init__(self,name,"cstrike")
       
    