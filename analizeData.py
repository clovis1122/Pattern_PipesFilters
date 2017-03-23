#!/usr/bin/env python


"""
AnalizeData will take a directory as an input.
It will take all .csv files into a queue
and it will run the main function in a thread with a file
(this process will execute per 5 files, until queue gets empty)
"""

import sys
import os
import Queue
import threading
import main



#Pipe
def pipe_out(file):
    main.pipe_in(file)






directory = raw_input()

queue = Queue.Queue() #Files queue

if os.path.isdir(directory):
    # print("This directory exists")
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            queue.put(file)


else:
    print("Directory "+ directory +" does not exists")



while not queue.empty():
    if(queue.qsize()>=5):
        t1 = threading.Thread(target=main.pipe_in( pipe_out(queue.get()) ))
        t2 = threading.Thread(target=main.pipe_in( pipe_out(queue.get()) ))
        t3 = threading.Thread(target=main.pipe_in( pipe_out(queue.get()) ))
        t4 = threading.Thread(target=main.pipe_in( pipe_out(queue.get()) ))
        t5 = threading.Thread(target=main.pipe_in( pipe_out(queue.get()) ))
        join()
    else:
        while not queue.empty():
            t1 = threading.Thread(target=main.pipe_in( pipe_out(queue.get()) ))
