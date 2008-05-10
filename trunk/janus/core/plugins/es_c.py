'''

Eventscripts 2.0 Emulator

'''

import plugins.pyplugin
import path
import sys
class Plugin(plugins.pyplugin._SourcePlugin)
    def __init__(self,server):
        '''
            Server: the current server instance
        '''
        ipaths = ['D:\\SRCDS\\Server', 'D:\\SRCDS\\Server\\cstrike\\addons\\eventscripts\\_libs\\python', 'D:\\SRCDS\\Server\\cstrike\\addons\\eventsc
ripts\\_engines\\python\\Lib\\plat-win\\python25.zip', 'D:\\SRCDS\\Server\\cstrike\\addons\\eventscripts\\_engines\\python\\DLLs', 'D:\\SRCDS\\Server\
\cstrike\\addons\\eventscripts\\_engines\\python\\lib', 'D:\\SRCDS\\Server\\cstrike\\addons\\eventscripts\\_engines\\python\\lib\\plat-win', 'D:\\SRCD
S\\Server\\cstrike\\addons\\eventscripts\\_engines\\python\\lib\\lib-tk', 'D:\\SRCDS\\Server', 'D:\\SRCDS\\Server\\cstrike\\addons\\eventscripts\\_eng
ines\\python', 'D:\\SRCDS\\Server\\cstrike\\addons\\eventscripts\\_engines\\python\\lib\\site-packages', 'D:\\SRCDS\\Server\\cstrike\\addons\\eventscr
ipts', 'D:\\SRCDS\\Server\\cstrike/addons/eventscripts/_engines/python/Lib', 'D:\\SRCDS\\Server\\cstrike/addons/eventscripts/_engines/python/Lib/plat-
win', 'D:\\SRCDS\\Server\\cstrike/addons/eventscripts/_engines/python/Lib/site-packages', 'D:\\SRCDS\\Server\\cstrike/addons/eventscripts/_libs/python
']
        for ipath in 
            sys.path.append(server.dir / ipath)