"""
Feature Engineering Module

This module includes the class `FeatEng` and the functions that are defined inside it.
Each function will help with specific tasks in feature engineering and getting the dataset ready for training the model
or improving the model's performance. 
"""

#We are going to use resources that will help us with feature engineering. This includes the following libraries:
import pandas as pd
import numpy as np
import DataPrep


class FeatEng:
    """
    List of functions in this file:

    `volume_change()`. Extracts the percentage change in the `Volume` and adds it as a new column to the DataFrame. 

    `close_price_increase()`. Classifies if the price increased or not, 1 if it increased and 0 if it didn't, 
        then adds it to the DataFrame.

    `daily_range()`. Calculates the daily range of change by substracting the values of `Low` from `High` 
        and adds it to the DataFrame.

    `extract_changes()`. Executes the `volume_change()`, `close_price_increase()`, 
        and `daily_range()` altogether and modifies the DataFrame accordingly.

    `calculate_macd()`. Calculates the Mean Average Convergence Divergence (MACD) 
        and adds the features as new columns to the DataFrame.
    """

    # The constructor
    def __init__(self, df):
        self.df = df    

    # The definition of the function extract_changes
    def extract_changes(self):
        """ 
        Extracts the precentage, daily, and difference changes of high, low, volume, and close in the DataFrame. 

        Parameters: 
            self.df (DataFrame): DataFrame containing the stock price data.
        
        Parameter Constraints:
            Should have the columns high, low, volume, and close
        
        Returns:
            The modified DataFrame with the columns 'Daily Range', 'Volume Change', and 'Price Increase' added to previous DataFrame  
        """
        # Making a feature 'Daily Range' by substracting the elements low from high
        # and adding it after the 'Low' column        
        self.df = self.daily_range()

        # Making a feature 'Volume Change' by taking the percentage change in the volume
        # and adding it after 'Volume' column
        self.df = self.volume_change()

        # Making a feature 'Close Price Increase' by having a 1 if the price increase or 
        # a 0 if it did not. Adding it after 'Close' column
        self.df = self.close_price_increase()

        return self.df
    
    def volume_change(self):
        """ 
        Extracts the precentage change in the volume in the DataFrame. 

        Parameters: 
            self.df (DataFrame): DataFrame containing the stock price data.
        
        Parameter Constraints:
            Should have the column 'Volume'
        
        Returns:
            The modified DataFrame with the column 'Volume Change' added.  
        """
        # Making a feature 'Volume Change' by taking the percentage change in the volume
        # and adding it after 'Volume' column
        self.df['Volume Change'] = self.df['Volume'].pct_change()
        index_volume = self.df.columns.get_loc('Volume')
        self.df.insert(index_volume + 1, 'Volume Change', self.df.pop('Volume Change'))

        return self.df

    def close_price_increase(self):
        """ 
        Shows whether not the price increased in the close price of the DataFrame. 

        Parameters: 
        self.df (DataFrame): DataFrame containing the stock price data.
    
        Parameter Constraints:
        Should have the column 'Close'
    
        Returns:
        The modified DataFrame with the column 'Close Price Increase' added. 1 if the price increased and 0 if it did not.
        """
        # Making a feature 'Close Price Increase' by having a 1 if the price increase or 
        # a 0 if it did not. Adding it after 'Close' column
        self.df['Close Price Increase'] = (self.df['Close'] > self.df['Close'].shift(1)).astype(int)
        index_close = self.df.columns.get_loc('Close')
        self.df.insert(index_close + 1, 'Close Price Increase', self.df.pop('Close Price Increase'))

        return self.df
    
    def daily_range(self):
        """ 
        Extracts the 'Daily Range' change by substracting the elements of 'Low' from 'High' of the DataFrame. 

        Parameters: 
        self.df (DataFrame): DataFrame containing the stock price data.
    
        Parameter Constraints:
        Should have the columns 'High' and 'Low'
    
        Returns:
        The modified DataFrame with the column 'Daily Range' added.
        """
        # Making a feature 'Daily Range' by substracting the elements low from high
        # and adding it after the 'Low' column
        self.df['Daily Range'] = self.df['High'] - self.df['Low']
        index_low = self.df.columns.get_loc('Low')
        self.df.insert(index_low + 1, 'Daily Range', self.df.pop('Daily Range'))

        return self.df
    
    def calculate_macd(self, short_window=12, long_window=26, signal_window=9):
        """
        Calculate the Moving Average Convergence Divergence (MACD) indicator for a given DataFrame.

        Parameters:
            self.df (DataFrame): DataFrame containing the stock price data. It should have a 'Date' column and a 'Price' column.
            short_window (int): Number of days for the short-term moving average (default is 12).
            long_window (int): Number of days for the long-term moving average (default is 26).
            signal_window (int): Number of days for the signal line moving average (default is 9).

        Returns:
            The modified DataFrame containing the MACD, signal line, and MACD histogram.
        """
        # Calculate the short EMA
        self.df['shortEMA'] = self.df['Close'].ewm(span=short_window, adjust=False).mean()

        # Calulate the long EMA
        self.df['longEMA'] = self.df['Close'].ewm(span=long_window, adjust=False).mean()

        # Calculate the Mean Average Convergence Divergence
        self.df['MACD'] = self.df['shortEMA'] - self.df['longEMA']

        # Get the signal line
        self.df['signalLine'] = self.df['MACD'].ewm(span=signal_window, adjust=False).mean()

        # Calculate the MACD histogram
        self.df['MACD_histogram'] = self.df['MACD'] - self.df['signalLine']

        return self.df

