#!/usr/bin/env python

"""
This filter will proccess the file
and will deliver a file with two cells:
    [insurance | patient]
"""

import csv
import main

    ####################################################################
    ###                         pipe in                              ###
    ####################################################################

def pipe_in(file):
    __main__(file)


    ####################################################################
    ###                         pipe out                             ###
    ####################################################################

def pipe_out(file):
    main.files_to_analize.put(file)





    ####################################################################
    ###                         "main"                               ###
    ####################################################################

def __main__(file):
    doc = open(file,"rb")
    reader = csv.reader(doc)
    ins_pat = open('ins_pat.csv', 'wb')
    writer = csv.writer(ins_pat)

    for row in reader:
        # print row
        writer.writerow([row[2], row[0]])


    pipe_out(ins_pat.name)
    ins_pat.close()
    doc.close()

    #Send the file trough out the pipe_out
