from src.data_splitter import DataSplitter, SimpleTrainTestSplitStrategy
import pandas as pd
from zenml import step
from typing import Tuple

@step
def data_splitter_step(df: pd.DataFrame, target_column: str, test_size = 0.2, random_state = 42) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    data_splitter = DataSplitter(SimpleTrainTestSplitStrategy(test_size, random_state))
    X_train, X_test, y_train, y_test = data_splitter.split(df, target_column)
    return X_train, X_test, y_train, y_test