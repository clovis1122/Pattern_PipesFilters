#!/usr/bin/env python

"""
This filter will proccess the file
and will deliver a file with two cells:
    [illness | invoice]
"""

import csv
import main
# import filter_mean

    ####################################################################
    ###                         pipe in                              ###
    ####################################################################

def pipe_in(file):
    __main__(file)


    ####################################################################
    ###                         pipe out                             ###
    ####################################################################

def pipe_out(file):
    main.mean_analize_queue.put(file)
    #File is sent to mean queue




    ####################################################################
    ###                         "main"                               ###
    ####################################################################

def __main__(file):
    doc = open(file,"rb")
    reader = csv.reader(doc)
    ill_inv = open('ill_inv.csv', 'wb')
    writer = csv.writer(ill_inv)

    for row in reader:
        # print row
        writer.writerow([row[5], row[8]])


    ill_inv.close()
    doc.close()
    pipe_out(ill_inv.name)

    # filter_mean.pipe_in(ill_inv.name)
    #Send the file trought the pipe_out
