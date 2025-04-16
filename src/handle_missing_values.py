import logging      # use to log the information
from abc import ABC, abstractmethod
import pandas as pd

# setting up logging configuration
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

class MissingValueHandlingStrategy(ABC):
    @abstractmethod
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        pass
    
class DropMissingValuesStrategy(MissingValueHandlingStrategy):
    def __init__(self, axis = 0, thresh = None):
        # axis (int): 0 to drop rows with missing values, 1 to drop columns with missing values.
        # thresh (int): The threshold for non-NA values. Rows/Columns with less than thresh non-NA values are dropped.
        self.axis = axis
        self.thresh = thresh
        
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Dropping missing values with axis = {self.axis} and thresh = {self.thresh}.")
        df_cleaned = df.dropna(axis = self.axis, thresh = self.thresh)
        logging.info("Missing values dropped.")
        return df_cleaned

class FillMissingValuesStrategy(MissingValueHandlingStrategy):
    def __init__(self, method = "mean", fill_value = None):
        self.method = method
        self.fill_value = fill_value
        
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Filling the missing values using method: {self.method}.")
        
        if self.method == "mean":
            numerical_columns = df.select_dtypes(include = "number").columns
            df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].mean())
        elif self.method == "median":
            numerical_columns = df.select_dtypes(include = "number").columns
            df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].median())
        elif self.method == "mode":
            df = df.fillna(df.mode().iloc[0])
        elif self.method == "constant":
            df = df.fillna(self.fill_value)
        else:
            logging.warning(f"Unknown method '{self.method}'. No missing values handled.")
        logging.info("Missing values filled.")
        return df
    
class MissingValueHandler:
    def __init__(self, strategy: MissingValueHandlingStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: MissingValueHandlingStrategy):
        logging.info(f"Setting missing value handler strategy: {strategy}")
        self.strategy = strategy
    
    def execute_strategy(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Excuting missing value handler strategy: {self.strategy}")
        return self.strategy.handle(df)