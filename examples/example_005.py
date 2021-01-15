from subprocess import check_output
import os

def get_pid(name):
    return check_output(["pidof", "-s", name])


print(get_pid("sshd"))
###############################################

import psutil

process_status = [ proc for proc in psutil.process_iter() if proc.name() == 'sshd' ]
if process_status:
    for current_process in process_status:
        print("Process id is %s, name is %s, staus is %s"%(current_process.pid, current_process.name(), current_process.status()))
else:
    print("Process name not valid", 'process_name')
    
res = psutil.net_connections("tcp")
for c in res:
    print(c)
    
for proc in psutil.process_iter(['pid', 'name', 'username', 'status']):
    print(proc.info)