#!/usr/bin/env python

"""
This filter will proccess the file
and will deliver a file with two cells:
    [age | illness]
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

# def pipe_out(file):




    ####################################################################
    ###                         "main"                               ###
    ####################################################################

def __main__(file):
    doc = open(file,"rb")
    reader = csv.reader(doc)
    age_ill = open('age_ill.csv', 'wb')
    writer = csv.writer(age_ill)

    for row in reader:
        writer.writerow([row[5], row[3]])


    age_ill.close()
    doc.close()
