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

    row_num = 0
    for row in reader:
        # print(row)
        
        # for col in row:
        #     if(col == "NOMBRE"):

        # if(row_num==0):
        #     for col in row:
        #         if()



    doc.close()

    # print(file)
