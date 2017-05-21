
from __future__ import print_function
import os, subprocess


# loading the result of the "ps -ano" command
# example:
# ibrahim@khorwat:~$ ps -ano
#  PID TTY          TIME CMD
# 3979 pts/8    00:00:00 python
# 3982 pts/5    00:00:00 ps

def kill_py_processes():
        '''killing python processes''' 
        print(" loading processes using ps -ano")
        output = subprocess.check_output( ["ps","-ano"] ).split(b"\n")

        print(" parsing over python processes ...")
        for i in output:
                if 'python' in str(i): 
                        process = i.split()[-4]
                        os.system("kill -9 " + process.decode('utf-8') )
        


if __name__ == '__main__':
        kill_py_processes()
