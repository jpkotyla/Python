from usefulThings import *

from mpi4py import MPI

def demo():
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    print 'Hello World (from proccess %d)' % comm.rank
