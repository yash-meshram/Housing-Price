from abc import ABC, abstractmethod
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype, is_object_dtype, is_categorical_dtype, is_bool_dtype

class UnivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature: str):
        pass
    
class NumericalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature: str):
        if is_numeric_dtype(df[feature]):
            plt.figure(figsize = (10, 6))
            sns.histplot(df[feature], kde = True, bins = 30)
            plt.title(f"Distribution of {feature}")
            plt.xlabel(feature)
            plt.ylabel("Frequency")
            plt.show()
        else:
            print(f"{feature} is not a numerical feature")
    
class CategoricalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature: str):
        if is_object_dtype(df[feature]) or is_categorical_dtype(df[feature]) or is_bool_dtype(df[feature]):
            plt.figure(figsize = (10, 6))
            order = df[feature].value_counts().index
            sns.countplot(data = df, x = feature, palette = "muted", order = order)
            plt.title(f"Distribution of {feature}")
            plt.xlabel(feature)
            plt.ylabel("Count")
            plt.xticks(rotation = 90)
            plt.show()
        else:
            print(f"{feature} is not a categorical feature")
    
class UnivariateAnalyzer:
    def __init__(self, strategy: UnivariateAnalysisStrategy):
        self.strategy = strategy
        
    def set_strategy(self, strategy: UnivariateAnalysisStrategy):
        self.strategy = strategy
        
    def excute_strategy(self, df: pd.DataFrame, feature: str):
        self.strategy.analyze(df, feature)
        

if __name__ == "__main__":
    df = pd.read_csv("extracted_data/AmesHousing.csv")
    
    univariate_analyzer = UnivariateAnalyzer(NumericalUnivariateAnalysis())
    univariate_analyzer.excute_strategy(df, "SalePrice")
    
    univariate_analyzer.set_strategy(CategoricalUnivariateAnalysis())
    univariate_analyzer.excute_strategy(df, "Neighborhood")