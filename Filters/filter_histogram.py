# !/usr/bin/env python

"""
This module will recieve a file, and ...
(here start our diagram)
"""

import main
import matplotlib.pyplot as plt

    ####################################################################
    ###                         pipe in                              ###
    ####################################################################

def pipe_in(file):
    while not main.mean_dictionary_queue.empty():
        __main__(main.mean_dictionary_queue.get())



    ####################################################################
    ###                         pipe out                             ###
    ####################################################################

# def pipe_out(mean_dictionary):




def __main__(mean_dictionary):

    x = []
    y = []

    for key in mean_dictionary:
        x.append(key)
        y.append(mean_dictionary.get(key))
