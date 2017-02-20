#Numerical/TS
import numpy as np
import pandas as pd
import scipy as sci

from pandas import Series,TimeSeries,DataFrame
import datetime as dt
import matplotlib.pyplot as plt

#ML
import sklearn as skl

#OperatingSystems
import os
import sys

#Dates/Time
import datetime as dt
import time as time

# Read/Write
import cPickle as pickle
import h5py


def to_datetime(s):
    if type(s)==str:
        assert len(s)== 8
        return dt.datetime(int(s[:4]),int(s[4:6]),int(s[6:]))
    else:
        assert type(s) == int
        return to_datetime(str(s))

def multiThread(func_name, n_threads = 4):
    import os
    os.system('mpiexec -n %d python %s' % (n_threads,func_name))