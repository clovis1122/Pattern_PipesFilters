#!/usr/bin/env python
"""
This filter will proccess the file
and will deliver a dictionary with the frecuency:
    [frecuencykey | count]
"""


import csv
from filecmp import cmp
from collections import Counter
from datetime import datetime as dt
import main

    ####################################################################
    ###                         pipe in                              ###
    ####################################################################

def pipe_in(file):
   __main__(file)


    ####################################################################
    ###                         pipe out                             ###
    ####################################################################

def pipe_out(frec_dictionary):
   #Send the frec_dictionary to the main
   main.freq_dictionary_queue.put(frec_dictionary)


def F_sex_ill(reader):
    f = []
    m = []
    for row in reader:
        print row
        if (row[1] =="M"):
            m.append(row[0])
        else:
            f.append(row[0])

    male_frec = dict(Counter(m))
    fem_frec = dict(Counter(f))
    pipe_out(male_frec)
    pipe_out(fem_frec)
    # return male_frec, fem_frec

def F_ins_pat(reader):
    ins = []
    for row in reader:
        ins.append(row[0])
    ins_frec = dict(Counter(ins))
    pipe_out(ins_frec)
    # return ins_frec

def F_ill_time(reader):
    spring = []
    summer = []
    fall = []
    winter = []
    for row in reader:
        datenow = dt.strptime(row[1], "%d/%m/%Y")
        if ((dt.strptime("22/12/2016", "%d/%m/%Y") <= datenow <= dt.strptime("20/03/2017", "%d/%m/%Y")) == True):
            winter.append(row[0])
        elif ((dt.strptime("21/03/2016", "%d/%m/%Y") <= datenow <= dt.strptime("21/06/2016", "%d/%m/%Y")) == True):
            spring.append(row[0])
        elif ((dt.strptime("22/06/2016", "%d/%m/%Y") <= datenow <= dt.strptime("23/09/2016", "%d/%m/%Y")) == True):
            summer.append(row[0])
        elif ((dt.strptime("24/09/2016", "%d/%m/%Y") <= datenow <= dt.strptime("21/12/2016", "%d/%m/%Y")) == True):
            fall.append(row[0])
        else:
            print "Klk ta pasan2"

    winter_frec = dict(Counter(winter))
    spring_frec = dict(Counter(spring))
    summer_frec = dict(Counter(summer))
    fall_frec = dict(Counter(fall))

    pipe_out(winter_frec)
    pipe_out(spring_frec)
    pipe_out(summer_frec)
    pipe_out(fall_frec)

    # return winter_frec
    # return spring_frec
    # return summer_frec
    # return fall_frec



def __main__(file):
    #file parameter
    doc = open(file,"rb")
    reader = csv.reader(doc)

    #skips first row
    next(reader)

    if (cmp(file, "ins_pat.csv") == True):
        F_ins_pat(reader)
    elif (cmp(file, "ill_time.csv") == True):
        F_ill_time(reader)
    elif (cmp(file, "sex_ill.csv") == True):
        F_sex_ill(reader)
    else:
        print "Klk ta pasan2"


    doc.close()
