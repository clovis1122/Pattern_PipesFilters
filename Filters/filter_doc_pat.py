#!/usr/bin/env python

"""
This filter will proccess the file
and will deliver a file with two cells:
    [doctor | patient]
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
    doc_pat = open('doc_pat.csv', 'wb')
    writer = csv.writer(doc_pat)

    for row in reader:
        # print row
        writer.writerow([row[0], row[9]])


    doc_pat.close()
    doc.close()

    #Send the file trough out the pipe_out
