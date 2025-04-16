import logging
from abc import ABC, abstractmethod
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
import numpy as np

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

class FeatureEngineeringStrategy(ABC):
    @abstractmethod
    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        pass
    
# log transformation - reduce the screwness in data - we can find it by dist plot- if a feature is screw then we can apply log transformation
class LogTransformation(FeatureEngineeringStrategy):
    def __init__(self, features):
        self.features = features
        
    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Applying log transformation to features: {self.features}")
        df[self.features] = np.log1p(df[self.features])         #log1p handles log(0) by calculating log(1+x)
        logging.info("Log transformation completed.")
        return df
    
# This strategy applies standard scaling (z-score normalization) to features, centering them around zero with unit variance.
class StandardScaling(FeatureEngineeringStrategy):
    def __init__(self, features):
        self.features = features
        self.scaler = StandardScaler()
    
    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Applying standard scaling to features: {self.features}")
        df[self.features] = self.scaler.fit_transform(df[self.features])
        logging.info("Standard scaling completed.")
        return df
    
class MinMaxScaling(FeatureEngineeringStrategy):
    def __init__(self, features):
        self.features = features
        self.scaler = MinMaxScaler()
        
    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Applying min max scaling to features: {self.features}")
        df[self.features] = self.scaler.fit_transform(df[self.features])
        logging.info("Min max scaling completed.")
        return df
    
class OneHotEncoding(FeatureEngineeringStrategy):
    def __init__(self, features):
        self.features = features
        self.encoder = OneHotEncoder(sparse = False, drop = "first")
        
    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Applying one hot encoding to features: {self.features}.")
        
        # applying one hot encoding to features
        df_encoded = self.encoder.fit_transform(
            df[self.features],
            columns = self.encoder.get_feature_names_out(self.features)
        )
        
        # droping the feature columns from df
        df.drop(columns = self.features, inplace = True)
        df.reset_index(drop = True)
        
        # adding the encoded columns to the df
        df = pd.concat([df, df_encoded], axis = 1)
        
        logging.info("One hot encoding completed.")
        return df
        
        
class FeatureEngineering:
    def __init__(self, strategy: FeatureEngineeringStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: FeatureEngineeringStrategy):
        logging.info(f"Setting the feature engineering strategy: {strategy}")
        self.strategy = strategy
        
    def excute_strategy(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Applying feature engineering strategy: {self.strategy}")
        return self.strategy.apply_transformation(df)