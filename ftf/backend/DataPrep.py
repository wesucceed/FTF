"""
Data Preprocessing Module

This module includes the class `DataPrep` and the functions that are defined inside it.
Each function will help with specific tasks in data preprocessing and getting the data ready for feature engineering 
and training the model. 
"""

# We are going to use resources that will help us with data manipulation. This includes the following libraries:
import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

class DataPrep:
    """
    List of functions in this file:

    `extract_date()`. This function uses Pandas' `to_datetime()` to convert the DataFrames' date to date format, 
    and then extracts year, month, day, and quarter from the modified date. 

    `handle_missing_data()`.  This function first takes the columns that has missing data, 
    then fits it into an iterative imputer, and takes the imputed data and puts it back to the DataFrame. 
    """
    
    def __init__(self, df):
        self.df = df

    def extract_date(self):
        """
        Extract the date from the DataFrame and merge the columns back into the DataFrame

        Parameters: 
            self.df (DataFrame): DataFrame containing the stock price data.

        Parameter constraints:
            Should have a column 'date'
            The format of the date should be valid

        Returns:
            DataFrame: The modified DataFrame with 'year', 'month', 'day, and 'quarter' added as new columns
        """
        # Setting the Date column to Panda's datetime format
        self.df['Date'] = pd.to_datetime(self.df['Date'])

        #Extracting the year and adding it after 'Date' column
        self.df['Year'] = self.df['Date'].dt.year
        index_date = self.df.columns.get_loc('Date')
        self.df.insert(index_date + 1, 'Year', self.df.pop('Year'))

        # Extracting the month and adding it after 'Year' column
        self.df['Month'] = self.df['Date'].dt.month
        index_year = self.df.columns.get_loc('Year')
        self.df.insert(index_year + 1, 'Month', self.df.pop('Month'))

        # Extracting the day and adding it after 'Month' column
        self.df['Day of Week'] = self.df['Date'].dt.dayofweek
        index_month = self.df.columns.get_loc('Month')
        self.df.insert(index_month + 1, 'Day of Week', self.df.pop('Day of Week'))

        # Extracting the quarter and adding it after 'Day' column
        self.df['Quarter'] = self.df['Date'].dt.quarter
        index_day = self.df.columns.get_loc('Day of Week')
        self.df.insert(index_day + 1, 'Quarter', self.df.pop('Quarter'))

        return self.df
    
    def handle_missing_data(self):
        """
        This function will check for any null values in our dataset and handles it with sklearn's iterative imputation

        Parameteres:
            self.df (DataFrame): DataFrame containing the stock price data.

        Returns:
            The modified DataFrame with all the missing values handled.
        """
        # Taking the columns containing missing values
        columns_with_missing_value = self.df.columns[self.df.isnull().any()].tolist()

        # Initiating an iterative imputer object as imputer
        imputer = IterativeImputer(max_iter=10, random_state=42)

        # Fitting the columns with missing values to the imputer
        imputer.fit(self.df[columns_with_missing_value])

        # Get the imputed data from the imputer and transforimg the columns with the imputed data
        imputed_data = imputer.fit_transform(self.df[columns_with_missing_value])

        # Replacing the columns with missing values with the columns containing imputed data
        self.df[columns_with_missing_value] = imputed_data

        return self.df