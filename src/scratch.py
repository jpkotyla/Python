from usefulThings import *

from mpi4py import MPI

def demo():
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    print 'Hello World (from proccess %d)' % comm.rank



name = "WikiPrices"

cols = [
        ('ticker','VARCHAR(100)'),
        ('date', 'DATETIME'),
        ('Open','float'),
        ('High', 'float'),
        ('Low', 'float'),
        ('Close', 'float'),
        ('Volume', 'float'),
        ('ExDividend', 'float'),
        ('SplitRate', 'float'),
        ('AdjOpen', 'float'),
        ('AdjHigh', 'float'),
        ('AdjLow', 'float'),
        ('AdjClose', 'float'),
        ('AdjVolume', 'float'),
        ('LoadDate','DATETIME')
        ]
pk = ['ticker','date']
nullable = []


query.create_tables("WikiPrices",cols, pk,nullable,con = query.get_fin_con())