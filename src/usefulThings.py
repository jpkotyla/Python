import pandas as pd
import numpy as np
from pandas import Series,TimeSeries,DataFrame
import h5py

import datetime as dt

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





