import pandas as pd
from abc import ABC, abstractmethod
from sklearn.model_selection import train_test_split
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

class DataSplitterStrategy(ABC):
    @abstractmethod
    def split_data(self, df: pd.DataFrame, target_column: str):
        pass
    
class SimpleTrainTestSplitStrategy(DataSplitterStrategy):
    def __init__(self, test_size, random_state):
        self.test_size = test_size
        self.random_state = random_state
        
    def split_data(self, df: pd.DataFrame, target_column: str):
        logging.info("Performing simple train-test strategy.")
        
        X = df.drop(columns = [target_column])
        y = df[target_column]
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size = self.test_size,
            random_state = self.random_state
        )
        logging.info(f"Simple train-test split completed with test size: {self.test_size}.")
        return X_train, X_test, y_train, y_test
    
class DataSplitter:
    def __init__(self, strategy: DataSplitterStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: DataSplitterStrategy):
        logging.info(f"Setting data splitter strategy: {strategy}.")
        self.strategy = strategy
    
    def split(self, df: pd.DataFrame, target_column: str):
        logging.info("Splitting data using the selected stratgey.")
        return self.strategy.split_data(df, target_column)
        