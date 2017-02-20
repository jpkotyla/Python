
import pandas as pd
from pandas import DataFrame,Series,date_range
import statsmodels.tsa.stattools as tsa
import matplotlib.pyplot as plt


all_data = DataFrame.from_csv(r'/Users/jpkotyla/Desktop/MachineLearning/Kaggle/Witon//train.csv')


with pd.HDFStore("/Users/jpkotyla/Desktop/MachineLearning/Kaggle/TwoSigma/train.h5", "r") as train:
    df = train.get("train")









