# this file launches the server...

from core.srcds import srcds_cstrike

def startServer(type):
    '''
        Start server of type "type"
    '''
    return srcds_cstrike.Server(type)