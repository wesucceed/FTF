# Import yahoo finance library for getting the data
import yfinance as yf

# Import packages for data manipulation
import numpy as np
import pandas as pd
import FeatEng as fe
import DataPrep as dp

# Not Final
import DataVis as dv

# DataExtract module
import DataExtract as de

# Import candidate models for the project
from xgboost import XGBRegressor, XGBClassifier

# Import packages for data visualization 
import matplotlib.pyplot as plt

# Import packages for metrics
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# This lets us see all the columns, preventing Jupyter from redacting them.
pd.set_option('display.max_columns', None)

# Here, "MSFT" and "1y" will be our input from the user, here they are put for testing purpose
dataset = de.DataExtract("MSFT")

df = dataset.dataset("1yr")

print(df)



#df0 = pd.

# Isolate X variable
#X = df.drop(columns = ['Price', 'Date'])
#X.head()