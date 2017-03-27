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
import thread
import main
import filter_doc_pat

    ####################################################################
    ###                     FilterThread class                       ###
    ####################################################################
class filterThread(threading.Thread):
    def __init__(self, name, file):
        threading.Thread.__init__(self)
        self.name = name
        self.file = file

    def run(self):
        main.pipe_in(self.file)



    ####################################################################
    ###                         pipe out                             ###
    ####################################################################
def pipe_out(file):
    main.pipe_in(file)



    ####################################################################
    ###                         "main"                               ###
    ####################################################################

directory = raw_input()
filesQueue = Queue.Queue() #Files queue
c = 1


if os.path.isdir(directory):
    # print("This directory exists")
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            filesQueue.put(file)


else:
    print("Directory "+ directory +" does not exists")



while not filesQueue.empty():
    if(filesQueue.qsize()>=5):
        arch1 = filesQueue.get()
        arch2 = filesQueue.get()
        arch3 = filesQueue.get()
        arch4 = filesQueue.get()
        arch5 = filesQueue.get()
        t1 = filterThread("t1", arch1) #threading.Thread(target=main.pipe_in( pipe_out(filesQueue.get()) ))
        t2 = filterThread("t2", arch2) #threading.Thread(target=main.pipe_in( pipe_out(filesQueue.get()) ))
        t3 = filterThread("t3", arch3) #threading.Thread(target=main.pipe_in( pipe_out(filesQueue.get()) ))
        t4 = filterThread("t4", arch4) #threading.Thread(target=main.pipe_in( pipe_out(filesQueue.get()) ))
        t5 = filterThread("t5", arch5) #threading.Thread(target=main.pipe_in( pipe_out(filesQueue.get()) ))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
    else:
        while not filesQueue.empty():
            arch = filesQueue.get()
            t1 = filterThread("t"+str(c), arch)
            c=c+1
            t1.start()
