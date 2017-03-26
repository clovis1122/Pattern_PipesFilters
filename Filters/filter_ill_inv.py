#!/usr/bin/env python

"""
This filter will proccess the file
and will deliver a file with two cells:
    [illness | invoice]
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
    ill_inv = open('ill_inv.csv', 'wb')
    writer = csv.writer(ill_inv)

    for row in reader:
        # print row
        writer.writerow([row[5], row[8]])


    ill_inv.close()
    doc.close()

    #Send the file trought the pipe_out
