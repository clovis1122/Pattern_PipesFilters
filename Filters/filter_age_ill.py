#!/usr/bin/env python

"""
This filter will proccess the file
and will deliver a file with two cells:
    [age | illness]
"""

import csv
import main
import filter_mean

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




    ####################################################################
    ###                         "main"                               ###
    ####################################################################

def __main__(file):
    doc = open(file,"rb")
    reader = csv.reader(doc)
    age_ill = open(main.new_path+'/age_ill.csv', 'wb')
    writer = csv.writer(age_ill)

    for row in reader:
        writer.writerow([row[4], row[5]])


    age_ill.close()
    doc.close()
    pipe_out(age_ill.name)
    # filter_mean.pipe_in(age_ill.name)
