#!/usr/bin/env python

"""
This filter will proccess the file
and will deliver a dictionary with the frecuency:
    [frecuencykey | count]
"""


import csv
from filecmp import cmp
from collections import Counter
#import main

    ####################################################################
    ###                         pipe in                              ###
    ####################################################################

#def pipe_in(file):
#    __main__(file)


    ####################################################################
    ###                         pipe out                             ###
    ####################################################################

#def pipe_out(mean_dictionary):
#    #Send the mean_dictionary to the main mean_dictionary_queue
#    main.mean_dictionary_queue.put(mean_dictionary)



def F_sex_ill(reader):
    f = []
    m = []
    for row in reader:
        print row
        if (row[1] =="M"):
            m.append(row[0])
        else:
            f.append(row[0])

    male_frec = Counter(m)
    fem_frec = Counter(f)
    #    pipe_out(male_frec)
    #    pipe_out(fem_frec)
    return male_frec, fem_frec

def F_ins_pat(reader):
    ins = []
    for row in reader:
        ins.append(row[0])
    ins_frec = Counter(ins)
    #pipe_out(ins_frec)
    return ins_frec



#def F_ill_time(reader):
#    jan = []
#    feb = []
#    mar = []
##        #01-12-2016 < date1 < 31-12-2016
#        if ((01-01-2017 < row[1] < 31-01-2017) == True):
#            jan.append(row[0])
#        elif ((01-02-2017 < row[1]  < 28-02-2017) == True):
#            feb.append(row[0])
#        elif ((01-03-2017 < row[1]  < 31-03-2017) == True):
#            mar.append(row[0])
#        else:
#            print "Klk ta pasan2"
#    jan_frec = Counter(jan)
#    feb_frec = Counter(feb)
#    mar_frec = Counter(mar)
#    #    pipe_out(male_frec)
#    #    pipe_out(fem_frec)
#    print jan_frec
#    print feb_frec
#    print mar_frec


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
