from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class BivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame):
        pass


class NumericalVsNumericalAnalysis(BivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        # Scatter plot
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=feature1, y=feature2)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()


class CategoricalVsNumericalAnalysis(BivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        # Box plot
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x=feature1, y=feature2)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()


class BivariateAnalysis:
    def __init__(self, strategy: BivariateAnalysisStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: BivariateAnalysisStrategy):
        self.strategy = strategy

    def execute_strategy(self, df: pd.DataFrame, feature1: str, feature2: str):
        self.strategy.analyze(df, feature1, feature2)


if __name__ == "__main__":
    df = pd.read_csv("extracted_data/AmesHousing.csv")

    bivariate_analyzer = BivariateAnalysis(NumericalVsNumericalAnalysis())
    bivariate_analyzer.execute_strategy(df, "Gr Liv Area", "SalePrice")

    bivariate_analyzer.set_strategy(CategoricalVsNumericalAnalysis())
    bivariate_analyzer.execute_strategy(df, "Overall Qual", "SalePrice")
