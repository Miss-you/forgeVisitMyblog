#! /usr/bin/env python
#coding=utf-8
import time, os, sched 
    
schedule = sched.scheduler(time.time, time.sleep) 
    
def perform_command(cmd, inc): 
    os.system(cmd) 
        
def timming_exe(cmd, inc = 60): 
    while True :
        schedule.enter(inc, 0, perform_command, (cmd, inc)) 
        schedule.run() 
            
#os.system("/usr/bin/python visitMyBlog.py")
print("visit my blog every 6 hours ") 
timming_exe("/usr/bin/python visitMyBlog.py", 21600)
