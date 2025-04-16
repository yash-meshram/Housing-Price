import numpy as np
import pandas as pd
import logging
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import seaborn as sns

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

class OutlierDetectionStrategy(ABC):
    @abstractmethod
    def detect_outlier(self, df: pd.DataFrame) -> pd.DataFrame:
        pass
    
# Z-score = (X - mean) / std.
# abs(z-score) > threshold   --> outlier
class ZScoreOutlierDetection(OutlierDetectionStrategy):
    def __init__(self, threshold = 3):
        self.threshold = threshold
        
    def detect_outlier(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Detecting outlier using z-score method.")
        z_score = np.abs((df - df.mean()) / df.std())
        outliers = z_score > self.threshold
        logging.info(f"Outlier detected with z-score threshold: {self.threshold}.")
        return outliers
    
    
# IQR = Interquartile Range
# Q1 = 1st quartile = 25% from smaller to larger number
# Q3 - 3rd quartile = 75% from smaller to larger number
# IQR = Q3 - Q1
# outlier < Q1 - 1.5*IQR <= Acceptable range <= Q3 + 1.5*IQR < outlier
class IQROutlierDetection(OutlierDetectionStrategy):
    def detect_outlier(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Deecting outlier using IQR method.")
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        outliers = (df < Q1 - 1.5*IQR) | (Q3 - 1.5*IQR < df)
        logging.info("Outlier detected using the IQR method.")
        return outliers
        
        
class OutlierDector:
    def __init__(self, strategy: OutlierDetectionStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: OutlierDetectionStrategy):
        logging.info(f"Setting the outlier detection strategy: {strategy}.")
        self.strategy = strategy
    
    def detect_outlier(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Excuting outlier detection strategy.")
        return self.strategy.detect_outlier(df)
    
    def handle_outlier(self, df: pd.DataFrame, method = "remove", **kwargs) -> pd.DataFrame:
        outliers = self.detect_outlier(df)
        
        if method == "remove":
            logging.info("Removing outliers from the dataset.")
            df = df[(~outliers).all(axis = 1)]
        elif method == "cap":
            logging.info("Capping the outliers in the dataset.")
            df = df.clip(
                lower = df.quantile(0.01),
                upper = df.quantile(0.99),
                axis = 1
            )
        else:
            logging.warning(f"Unknown method {method}. No outlier handing performed.")
            
        logging.info("Outlier handling completed.")
        return df
    
    def visualize_outlier(self, df: pd.DataFrame, features):
        logging.info(f"Visualizing outlier for features: {features}.")
        for feature in features:
            plt.figure(figsize = (10, 6))
            sns.boxplot(x = df[feature])
            plt.title(f"Boxplot for {feature}")
            plt.show()
        logging.info("Outlier visualization completed.")