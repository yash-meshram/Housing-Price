from zenml import step
from src.outlier_detection import OutlierDector, ZScoreOutlierDetection, IQROutlierDetection
import pandas as pd
from typing import Tuple


@step
def outlier_detection(df: pd.DataFrame, strategy = "zscore", method = "remove") -> Tuple[pd.DataFrame, pd.DataFrame]: 
    if df is None:
        raise ValueError("Input data must be a non-null pandas DataFrame.")
    
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input data must be pandas DataFrame.")
    
    df_numeric = df.select_dtypes(include = [int, float])
    
    if strategy == "zscore":
        outlier_detector = OutlierDector(ZScoreOutlierDetection(threshold = 3))
        outliers = outlier_detector.detect_outlier(df_numeric)
        df_cleaned = outlier_detector.handle_outlier(df_numeric, method)
    elif strategy == "IQR":
        outlier_detector = OutlierDector(IQROutlierDetection())
        outliers = outlier_detector.detect_outlier(df_numeric)
        df_cleaned = outlier_detector.handle_outlier(df_numeric, method)
        
    return outliers, df_cleaned
        