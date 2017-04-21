import pandas as pd
import numpy as np

class DataLoader():

    def __init__(self,start,end,columns = None,look_back = 36,rolling = False):

        self.start_index = start
        self.end_index = end

        self.columns = columns

        self.train_data = None
        self.test_data = None


    def load_training(self):
        start = self.start_index
        end = self.end_index
        with pd.HDFStore("/Users/jpkotyla/Desktop/MachineLearning/Kaggle/TwoSigma/train.h5",
                         "r") as train:
            data = train.get("train")

        data = data[data.timestamp <= self.end_index]
        data = data[data.timestamp >= self.start_index]
        self.train_data = data

    def get_training(self):
        return self.train_data
