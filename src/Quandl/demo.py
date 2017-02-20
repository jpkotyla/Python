from mpi4py import MPI
import h5py
import Quandl
import pickle
import numpy as np

comm = MPI.COMM_WORLD
API_KEY = '_asM2hz4fixnHpU6KzNS'
Quandl.ApiConfig.api_key = API_KEY

names = pickle.load(open(r'names.p','rb'))

id = names[comm.rank]

print comm.rank

mydata = Quandl.get("WIKI/%s" % id)

pickle.dump(mydata,open(r'All_data_%s' %id,'wb'))
with h5py.File('collective_test.hdf5', 'a') as f:
    print id
    try:
        mydata = Quandl.get("WIKI/%s" % id)
        data = mydata['Open']
        f.create_group('%s' % id)
        f[id].create_dataset('open_prices', data = np.array(Quandl.get("WIKI/ABT")['Open'].values))
    except:
        print 'Missing Opening Data for %s' % id