

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn import tree
from sklearn.datasets import load_iris

import os
import sys
import h5py

f = h5py.File("mytestfile.hdf5", "w")

TEST_PATH = '/Users/jpkotyla/Desktop/MachineLearning/Kaggle/AnimalShelter/test.csv'
TRAIN_PATH = '/Users/jpkotyla/Desktop/MachineLearning/Kaggle/AnimalShelter/train.csv'

train = pd.DataFrame.from_csv(TRAIN_PATH)
test = pd.DataFrame.from_csv(TEST_PATH)

# import pdb;pdb.set_trace()


train['AgeMonths'] = train['AgeuponOutcome'].dropna().apply(lambda x: int(str(x).split(' ')[0])
                if ('month' in str(x).split(' ')[1])
                else 12*int(str(x).split(' ')[0])).reindex(train.index)

train['OutcomeType']

# X = [[features for observation 1],[features for observation 2]...[features for observation n]]
# Y = [Response1,Response2,Response3,...,Response n ]
X = [[0, 0], [1, 1], [.5,3]]
Y = [0,1,1]


clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

clf.predict([[2.,1.]])