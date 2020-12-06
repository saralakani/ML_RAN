#4gV5gRAN.data_exp
#Python code for data exploration
import pandas as pd
import numpy as np
#folder = r"C:\Users\SAHA\Documents\Git Repos\TimeSeries_ML"
#filename = "moving-closerfarcloser.csv"
data = pd.read_csv('moving-closerfarcloser.csv')
print(data.info())