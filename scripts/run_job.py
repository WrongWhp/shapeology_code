from sys import argv
from os import getpid,system
from os.path import isfile
from time import sleep
import datetime


def getLock(lockfile):
    try:
        l=open(lockfile, 'x')
        return l
    except FileExistsError:
        return None

scripts=argv[1]
stem=argv[2]

lockfilename=stem+'.lock'
logfilename=stem+'.log'

lockfile=getLock(lockfilename)
if not lockfile is None:

    command='python3 %s/extractPatches.py %s > %s'%(scripts,stem,logfilename)
    # put some info into the log/lock file
    now = datetime.datetime.now()
    print('pid=',getpid(), file=lockfile)
    print('start time=',now.isoformat(), file=lockfile)
    print('command=',command, file=lockfile)
    
    system(command)
    sleep(1)
else:
    print(lockfilename,'exists, skipping')
