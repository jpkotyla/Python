
from mpi4py import MPI
comm = MPI.COMM_WORLD

import h5py
import quandl
import pickle
import numpy as np

API_KEY = '_asM2hz4fixnHpU6KzNS'

quandl.ApiConfig.api_key = API_KEY

names = pickle.load(open(r'names.p','rb'))

id = names[comm.rank]

print comm.rank

mydata = quandl.get("WIKI/%s" % id)

pickle.dump(mydata,open(r'All_data_%s' %id,'wb'))
with h5py.File('collective_test.hdf5', 'a') as f:
    print id
    try:
        mydata = quandl.get("WIKI/%s" % id)
        data = mydata['Open']
        f.create_group('%s' % id)
        f[id].create_dataset('open_prices',data = np.array(quandl.get("WIKI/ABT")['Open'].values))
    except:
        print 'Missing Opening Data for %s' % id