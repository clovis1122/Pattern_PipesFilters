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

def pipe_in(dict,num):
    # while not main.mean_dictionary_queue.empty():
        # dict = main.mean_dictionary_queue.get()
    __main__(dict,num)



    ####################################################################
    ###                         pipe out                             ###
    ####################################################################

# def pipe_out(mean_dictionary):




def __main__(dicc, name):

    x = []
    y = []
    counter = 0
    plt.hold(False)

    for key in dicc:
        x.append(key)
        y.append(dicc.get(key))
        counter+=1

    Xvar = range(counter)
    plt.bar(Xvar, y, align='center', alpha=0.5)
    plt.xlabel('Elemento')
    plt.ylabel('Frecuencia')
    plt.title('Frecuencia del elemento')
    plt.xticks(Xvar,x)
    stra = main.new_path+"/hist_"+str(name)+".jpeg"
    plt.savefig(stra)
