from abc import ABC, abstractmethod
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class MultivariateAnalysisTemplate(ABC):
    def analyze(self, df: pd.DataFrame):
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)
    
    @abstractmethod
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        pass
    
    @abstractmethod
    def generate_pairplot(self, df: pd.DataFrame):
        pass
    
    
class SimpleMultivariateAnalysis(MultivariateAnalysisTemplate):
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        # plt.figure(figsize = (10, 6))
        sns.heatmap(df.corr(), annot = True, fmt = ".2f", cmap = "coolwarm", linewidths = 0.5)
        plt.title("Correlation heatmap")
        plt.show()
    
    def generate_pairplot(self, df: pd.DataFrame):
        sns.pairplot(df)
        plt.suptitle("Pair plot od selected features", y = 1.02)
        plt.show()
        
    # def generate_correlation_heatmap(self, df: pd.DataFrame, figsize: tuple) -> None:
    #     plt.figure(figsize = figsize)
    #     sns.heatmap(df.corr(), annot = True, fmt = ".2f", cmap = "coolwarm", linewidths = 0.5)
    #     plt.title("Correlation heatmap")
    #     plt.show()
    
class MultiVariateAnalysis:
    def __init__(self, strategy: MultivariateAnalysisTemplate):
        self.strategy = strategy
        
    def set_strategy(self, strategy: MultivariateAnalysisTemplate):
        self.strategy = strategy
        
    def execute_strategy(self, df: pd.DataFrame):
        self.strategy.analyze(df)
        

if __name__ == "__main__":
    df = pd.read_csv("extracted_data/AmesHousing.csv")
    
    selected_features = df[['SalePrice', 'Gr Liv Area', 'Overall Qual', 'Total Bsmt SF', 'Year Built']]
    
    multivariate_analyzer = SimpleMultivariateAnalysis()
    multivariate_analyzer.analyze(selected_features)
