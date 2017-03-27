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
    counter;

    for key in mean_dictionary:
        x.append(key)
        y.append(mean_dictionary.get(key))
        counter++

    Xvar = range(counter)
    plt.bar(Xvar, y, align='center', alpha=0.5)
    plt.xlabel('Elemento')
    plt.ylabel('Frecuencia')
    plt.title('Frecuencia del elemento')
    plt.xticks(Xvar,x)
    plt.savefig('hist_filter_'+file.name)