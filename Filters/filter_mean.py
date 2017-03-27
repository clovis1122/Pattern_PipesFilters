#!/usr/bin/env python

"""
This filter will proccess the file
and will deliver a file with two cells:
    [illness | invoice]
"""

import os
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

def pipe_out(mean_dictionary):
    #Send the mean_dictionary to the main mean_dictionary_queue

    main.mean_dictionary_queue.put(mean_dictionary)


def mean_age_ill(file):
    #Format: Age | Ill
    dictionary={}
    dictionary_frec={}

    mean_dictionary = {}

    doc = open(file,"rb")
    reader = csv.reader(doc)

    #skips first row
    next(reader)


    for row in reader:

        if not row[1] in dictionary:
            dictionary[row[1]] = 0
            dictionary_frec[row[1]] = 1

        dictionary[row[1]] = (int(dictionary.get(row[1]))+int(row[0]))
        dictionary_frec[row[1]] += 1

            #Testing dictionary and dictionary_frec

    # for key in dictionary:
    #     print key, dictionary[key]
    #
    # print(" ")
    #
    # for key in dictionary_frec:
    #     print key, dictionary_frec[key]

    for key in dictionary:
        sum_age = dictionary.get(key)
        cant_age = dictionary_frec.get(key)

        mean_dictionary[key] = (sum_age/cant_age)

    #Testing mean dictionary
    # for key in mean_dictionary:
    #     print key, mean_dictionary[key]


    #Returning mean_dictionary
    pipe_out(mean_dictionary)



def mean_ill_inv(file):
        #Format: ill | invoice
        dictionary={}
        dictionary_frec={}

        mean_dictionary = {}

        doc = open(file,"rb")
        reader = csv.reader(doc)

        #skips first row
        next(reader)


        for row in reader:

            if not row[0] in dictionary:
                dictionary[row[0]] = 0
                dictionary_frec[row[0]] = 1

            dictionary[row[0]] = (int(dictionary.get(row[0]))+int(row[1]))
            dictionary_frec[row[0]] += 1

        #         Testing dictionary and dictionary_frec
        #
        # for key in dictionary:
        #     print key, dictionary[key]
        #
        # print(" ")
        #
        # for key in dictionary_frec:
        #     print key, dictionary_frec[key]
        for key in dictionary:
            sum_invoices = dictionary.get(key)
            cant_invoices = dictionary_frec.get(key)

            mean_dictionary[key] = (sum_invoices/cant_invoices)


        # Testing mean dictionary
        # for key in mean_dictionary:
        #     print key, mean_dictionary[key]

        # Returning mean_dictionary
        pipe_out(mean_dictionary)


def __main__(file):

    doc = open(file,"rb")
    reader = csv.reader(doc)

    if(file == "age_ill.csv"):
        doc.close()
        mean_age_ill(file)

    elif(file == "ill_inv.csv"):
        doc.close()
        mean_ill_inv(file)
