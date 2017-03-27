#!/usr/bin/env python

"""
This filter will proccess the file
and will deliver a file with two cells:
    [sex | illness]
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
    sex_ill = open('sex_ill.csv', 'wb')
    writer = csv.writer(sex_ill)

    for row in reader:
        # print row
        writer.writerow([row[5], row[3]])


    sex_ill.close()
    doc.close()
    pipe_out(sex_ill.name)
