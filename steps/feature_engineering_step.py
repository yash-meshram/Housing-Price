from src.feature_engineering import FeatureEngineering, LogTransformation, StandardScaling, MinMaxScaling, OneHotEncoding
import pandas as pd
from zenml import step

@step
def feature_engineering(df: pd.DataFrame, strategy: str = "log", features: list = []) -> pd.DataFrame:
    if strategy == "log":
        engineering = FeatureEngineering(LogTransformation(features))
    elif strategy == "standard_scaling":
        engineering = FeatureEngineering(StandardScaling(features))
    elif strategy == "minmax_scaling":
        engineering = FeatureEngineering(MinMaxScaling(features))
    elif strategy == "onehot_encoding":
        engineering = FeatureEngineering(OneHotEncoding(features))
    else:
        raise ValueError(f"Unsuppoerting feature engineering strategy: {strategy}")
    df_transformed = engineering.excute_strategy(df)
    return df_transformed