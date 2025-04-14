from src.handle_missing_values import DropMissingValuesStrategy
from zenml import step
import pandas as pd

@step
def handling_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    handler = DropMissingValuesStrategy(axis = 0)
    df_cleaned = handler.handle(df)
    return df_cleaned
    