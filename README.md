# kill_python_processes

Note:

You might need to install "future" python module using the command

"$sudo pip install future"


----------------------------------------


This program is used to kill python processes 
so that instead of me typing ps -ano then kill -9 each time as below

ibrahim@khorwat:~/Desktop$ ps -ano

  PID TTY          TIME CMD
  
 4507 pts/10   00:00:00 python3
 
 4508 pts/12   00:00:00 python
 
 4509 pts/8    00:00:00 python
 
 4510 pts/5    00:00:00 ps
 

Then

ibrahim@khorwat:~/Desktop$kill -9 4507

ibrahim@khorwat:~/Desktop$kill -9 4508

ibrahim@khorwat:~/Desktop$kill -9 4509


i just use one command that is supported using python2 and python3

----------------------------------------

For python 2.7 use the below command

ibrahim@khorwat:~/Desktop$ python kill_python.py 

 loading processes using ps -ano
 
 parsing over python processes ...
 
4473

4476

4477

4478

Killed

----------------------------------------

for python 3 use the below command


ibrahim@khorwat:~/Desktop$ python3 kill_python.py 

 loading processes using ps -ano
 
 parsing over python processes ...
 
b'4464'

b'4465'

b'4466'

b'4467'

Killed

