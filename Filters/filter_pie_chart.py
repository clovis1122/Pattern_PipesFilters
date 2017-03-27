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
    # Here I should iterate the frequency_dictionary_queue
    while not main.mean_dictionary_queue.empty():
        __main__(main.mean_dictionary_queue.get())



    ####################################################################
    ###                         pipe out                             ###
    ####################################################################

# def pipe_out(mean_dictionary):




def __main__(mean_dictionary):

    x = []
    y = []
    explode = []
    for key in mean_dictionary:
        x.append(key)
        y.append(mean_dictionary.get(key))
        explode.append(0)



    fig1, ax1 = plt.subplots()
    ax1.pie(y, explode=explode, labels=x, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.savefig('test.jpeg')
    # plt.show()
