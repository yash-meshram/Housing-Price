from src.handle_missing_values import MissingValueHandler, DropMissingValuesStrategy, FillMissingValuesStrategy
from zenml import step
import pandas as pd

@step
def handling_missing_values(df: pd.DataFrame, method: str = "mean", fill_value = None) -> pd.DataFrame:
    if method == "drop":
        handler = MissingValueHandler(DropMissingValuesStrategy(axis = 0))
    elif method in ["mean", "median", "mode", "constant"]:
        handler = MissingValueHandler(FillMissingValuesStrategy(method))
    else:
        raise ValueError(f"Unsupported missing value handling method: {method}.")
    
    df_cleaned = handler.execute_strategy(df)
    return df_cleaned