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