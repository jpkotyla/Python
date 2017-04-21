from __future__ import print_function
import numpy as np
import h5py
import time
import matplotlib.pyplot as plt
from datetime import date,timedelta
import pandas as pd
import cPickle as pickle
import os
import sys

DATA_PATH = r'/Users/jpkotyla/Python/src/hdf5_testing//'
TESTDIR = r'/Users/jpkotyla/Python/src/hdf5_testing//'

def write_test(num = 20):
    all_dat = [np.random.normal(0, 1, size=(250, 1100)) for i in range(num)]

    try:
        os.system('rm '+DATA_PATH+' *.h5')
        os.system('rm ' + DATA_PATH + ' *.p')
    except:
        pass

    start = time.time()
    with h5py.File(DATA_PATH+'data.h5','w') as df:
        g1 = df.create_group('group1')
        for d in range(num):
            g1.create_dataset('dataset'+str(d),data = all_dat[d])
    end = (time.time() - start)

    pickle_time = time.time()
    [pickle.dump(all_dat[i],open(r'/Users/jpkotyla/Python/src/hdf5_testing//test_'+str(i)+'.p','wb')) for i in range(num)]
    pickle_end = time.time() - pickle_time

    s = pd.Series(index = pd.Index([i for i in range(num)]),data = [all_dat[i] for i in range(num)])
    single_pick_time = time.time()
    pickle.dump(s, open(r'/Users/jpkotyla/Python/src/hdf5_testing//single.p', 'wb'))
    end_single = time.time() - single_pick_time
    return (end,pickle_end,end_single,num)


def read_test(num = 20):
    start = time.time()
    with h5py.File(DATA_PATH + 'data.h5', 'r') as df:
        g1 = df.get('group1')

        for d in range(num):
            rands = g1.get('dataset'+str(d))
    end = time.time() - start

    pickle_time = time.time()
    for i in range(num):
        res = pickle.load(open(r'/Users/jpkotyla/Python/src/hdf5_testing//test_'+str(i)+'.p','rb'))
    pickle_end = time.time() - pickle_time

    # single_pick_time = time.time()
    # res2 = pickle.load(s, open(r'/Users/jpkotyla/Python/src/hdf5_testing//single.p', 'wb'))
    # end_single = time.time() - single_pick_time

    return (end,pickle_end,num)


def write_speed(num):
    all_speeds = {i:write_test(i) for i in range(1,num)}
    return all_speeds

def read_speed(num):
    all_speeds = {i:read_test(i) for i in range(1,num)}
    return all_speeds

def plot_speeds(speed_dict,nums = 20,write = True):
    if (write):
        hd_times,multi_times,single_time,n = ([speed_dict[i][j] for i in range(1,nums)] for j in range(4))
        return pd.DataFrame(index = pd.Index(n),data = {'HD':hd_times,'Multi':multi_times,'Single':single_time})
    else:
        hd_times, multi_times, n = ([speed_dict[i][j] for i in range(1, nums)] for j in range(3))
        return pd.DataFrame(index=pd.Index(n), data={'HD': hd_times, 'Multi': multi_times})

def single_speed():
    start = time.time()
    rand = pickle.load(open(r'/Users/jpkotyla/Python/src/hdf5_testing//single.p','rb'))
    end = time.time()-start
    return end


def get_sizes():
    files = os.listdir(TESTDIR)
    multi_size = [np.sum([os.path.getsize(TESTDIR+file) for file in files[5:i] if 'test' in file]) for i in range(6,len(files))]
    return pd.Series(data = multi_size,index = pd.Index([i-5 for i in range(6,len(files))]))


test = pd.Series(np.random.normal(2,1,size=2000))

test_bin = test.apply(lambda x: -1 if x<0 else 1)


changes = (abs(test_bin - test_bin.shift(1))/2.0)
c_changes = changes.cumsum()