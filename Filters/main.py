# !/usr/bin/env python

"""
This module will recieve a file, and ...
(here start our diagram)
"""

import threading
import Queue
import filter_ins_pat
import filter_age_ill
import filter_ill_time
import filter_sex_ill
import filter_ill_inv
import filter_doc_pat
import filter_mean
import filter_frequency
import filter_histogram
import filter_pie_chart






    ####################################################################
    ###                         pipe in                              ###
    ####################################################################

def pipe_in(file):
    __main__(file)


    ####################################################################
    ###                         pipe out                             ###
    ####################################################################

def pipe_out(file):

    # filter_ins_pac.pipe_in(file)
    t1 = threading.Thread(target= filter_ins_pat.pipe_in(file))
    t2 = threading.Thread(target= filter_age_ill.pipe_in(file))
    t3 = threading.Thread(target= filter_ill_time.pipe_in(file))
    t4 = threading.Thread(target= filter_sex_ill.pipe_in(file))
    t5 = threading.Thread(target= filter_ill_inv.pipe_in(file))
    t6 = threading.Thread(target= filter_doc_pat.pipe_in(file))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()

    ####################################################################
    ###                         "main"                               ###
    ####################################################################

def __main__(file):
    pipe_out(file)


    """Maybe those whiles are going to be moved to pipe_out"""

    # Sending files to filter_frequency

    while not files_to_analize.empty():
        file = files_to_analize.get()
        filter_frequency.pipe_in(file)


    # Sending files to filter_mean
    while not mean_analize_queue.empty():
        file = mean_analize_queue.get()
        filter_mean.pipe_in(file)


    # Sending files to filter_histogram
    d=0
    while not mean_dictionary_queue.empty():
        d+=1
        dictionary = mean_dictionary_queue.get()
        filter_histogram.pipe_in(dictionary,d)
        # filter_pie_chart.pipe_in(dictionary) #This one should extract from the frequency_dictionary_queue
        # mean_dictionary_queue.get())


    # Sending freq_files to filter_histogram
    c=0
    while not freq_dictionary_queue.empty():
        c+=1
        dictionary = freq_dictionary_queue.get()
        filter_histogram.pipe_in(dictionary,c)






files_to_analize = Queue.Queue()        # Files for frequency analysis
mean_dictionary_queue = Queue.Queue()   # Files to generate histograms based on mean
freq_dictionary_queue = Queue.Queue()   # Files to generate histograms based on freq
mean_analize_queue = Queue.Queue()      # Files for mean analysis
