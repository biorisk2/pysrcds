#import core.logging as log
#import core.errors as error
from contrib.path import path
from contrib.configobj import ConfigObj

import os
import sys
import zipfile

# paths
root = path(os.getcwd())
serverpath = root / "servers"
datapath = root / "servers"

# append the server path
sys.path.append(serverpath)

class _SourceServer(object):

    def __init__(self,name,type):
        '''
            Setup the server, contains some generic stuff
        '''
        # basic setup - so that it works when un-subclassed
        self.type = type
        self.name = name
        self.dir = serverpath / name
        # test the server parent dir exists
        # servers/<name>
        if not self.dir.exists():
            # make it
            self.dir.mkdir(1)
            sys.path.append(self.dir)
        # now the specific server type directory is setup
        # eg servers/<name>/<type>
        self.dir = self.dir / type
        if not self.dir.exists():
            # make it
            self.dir.mkdir(1)
            # copy the default directory structure
            self._copy_default()
        # init some variables
        self.commandlist = {}  
        self.cvarlist = {}  
        # now load up the server
        self._load()
        
    def _load(self):
        # the directory is there so lets check it's structure and load from file
        # first create the defaults
        self._load_defaults()
        # then overwrite by loading the data
        self._load_from_directory()
            
       
    def _copy_default(self):
        '''
            Copies the server data from a source zip (first time setup)
                The path module makes this SO unbelievably easy!
        '''
        # path to the zip file with all the data in it
        srcdir = datapath / ("serversrc/%s.zip" % self.type)
        if srcdir.exists():
            # unzips the data.zip package
            z = zipfile.ZipFile(srcdir)
            for entry in z.namelist():
                fd = self.dir / entry
                if fd.count(".") == 0 and not fd.exists():
                    fd.mkdir(1)
                else:
                    # save the file
                    fd.write_bytes(z.read(entry))
        else:
            # needs error
            pass
        
    '''
        Umimplemented methods
    '''
    
    def _load_from_directory(self):
        pass
    def _parse_cfg(self,file):
        pass
    def _load_defaults(self):
        pass
        
    # this one parses a cfg file (the normal srcds cfg style) when passed a path() instance
    def parse_cfg(self,file):
        '''
            Runs through a cfg file and executes the commands / sets the cvars
        '''
        # iterate through the file
        for line in file.lines():
            # get run of newlines
            line=line.strip("\n")
            # continue if blank
            if line.startswith("//"): continue
            # split by spaces and get rid of empty elements
            elements = []
            for element in line.split(" "):
                if element != "":
                    elements.append(element)
            # ignore blank lines
            if len(elements) < 1: continue
            # check if it is a command
            cmd = self.command(elements[0])
            if cmd:
                cmd.fire(elements)
            # nope not a command
            else:
                # try setting a cvar
                # gotta have 2 elements for a proper cvar
                # should probably add an error here...
                if len(elements) < 2: continue
                # ok w'ere good so lets set a cvar!
                self.cvar(elements[0],elements[1])
    '''
        Server Commands handling
    '''
    def command(self,name,callback=None):
        pass
     
    class Command(object):
        def fire(self,argv):
            '''
                Fires the command
                    argv is an iterator with the arguments in it
            '''
            pass
    '''
        Server Cvar handling
    '''
    def cvar(self,name,value=None):
        # if we are just after the cvar then return the class instance
        if not value:
            # if it exists!
            if name in self.cvarlist:
                # log what we did (lvl 11 = really high up!)
                self._record(11,"Cvar %s instance requested" % name)
                # return the cvar instance finally
                return self.cvarlist[name]
        # well it wasn't there.. or we are meant to be creating the cvar
        # check that it is not a command first
        if name in self.commandlist:
            raise ServerError("Unable to create cvar %s, it already exists as a command")
        # so then! lets create the class instance
        temp = Cvar(name,value)
        # add it to the internal dictionary
        self.cvarlist[name] = temp
        # log what we did
        self._record(9,"Created Cvar %s" % name)
        # return it!
        return temp
        
    class Cvar(object):
        '''
         Internal class implementing an individual cva
            Adds important loggingand history info as well as the basic Cvar behaviour
        '''
        def __init__(self,name,value=None):
            # initialise variables
            self.name=name
            self.CvarHistory = []
            self.flags=={"public":0}
            # if a value was set initially then set it as such
            if value:
                self.set(value)
            # else set it to **empty**
            else:
                self.set("**empty**")
            # record what happened
            self._record("Created cvar")
            
        def set(self,value):
            # what are we doing?
            action = "Value change from %s to %s" % (self.value,value)
            # record it
            self._record(action)
            # set the cvar to a value
            self.value = value
            
        def makepublic(self):
            # what are we doing?
            action = "Made public"
            # record it
            self._record(action)
            # make it public
            self.flags["public"] = 1
            
        def _record(self,action):
            # record all the actions onm the cvar and log them at a huge level
            # record the action
            self.CvarHistory.append({"timestamp":int(time.time()),"action":action})
            # log the action
            logging.log(12,"Cvar (%s): %s" % (self.name,action))

            
            
            
            
    def tick(self):
        '''
            Server tick
        '''
        pass