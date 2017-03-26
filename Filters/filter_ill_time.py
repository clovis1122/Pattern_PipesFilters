#!/usr/bin/env python

"""
This filter will proccess the file
and will deliver a file with three cells:
    [illness | start time | end time]
"""

import csv
    ####################################################################
    ###                         pipe in                              ###
    ####################################################################

def pipe_in(file):
    __main__(file)


    ####################################################################
    ###                         pipe out                             ###
    ####################################################################

# def pipe_out(file):




    ####################################################################
    ###                         "main"                               ###
    ####################################################################

def __main__(file):
    doc = open(file,"rb")
    reader = csv.reader(doc)
    ill_time = open('ill_time.csv', 'wb')
    writer = csv.writer(ill_time)

    for row in reader:
        # print row
        writer.writerow([row[5], row[6], row[7]])


    ill_time.close()
    doc.close()
