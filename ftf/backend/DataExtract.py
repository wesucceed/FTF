import yfinance as yf
import pandas as pd

class DataExtract:

    def __init__(self, name):
        assert isinstance(name, str)
        self.name=name
        
        

    def dataset(self, history):
        """
        Creates a dataset with the company name and a duration of 'history'

        Parameters:
            history (str): 1d, 5d, 1mo, 3mo, 6mo, 1yr,

        Returns:
            df0 (Dataset): an original dataset of the company
        """
        assert isinstance(self.name, str)
        assert isinstance(history, str)

        ticker = yf.Ticker(ticker="MSFT")
        data = ticker.history(history)

        df0 = pd.DataFrame(data)

        return df0


