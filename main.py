#!/usr/bin/env python

"""
This module will recieve a file, and ...
(here start our diagram)
"""

import threading
import filter_ins_pac


def pipe_in(file):
    __main__(file)




def pipe_out(file):
    # filter_ins_pac.pipe_in(file)
    t1 = threading.Thread(target= filter_ins_pac.pipe_in(file))




def __main__(file):
    pipe_out(file)
