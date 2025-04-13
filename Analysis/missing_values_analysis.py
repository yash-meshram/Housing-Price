from abc import ABC, abstractmethod
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class MissingValuesAnalysisTemplate(ABC):
    def analyze(self, df: pd.DataFrame):
        self.identify_missing_values(df)
        self.visualize_missing_values(df)

    @abstractmethod
    def identify_missing_values(self, df: pd.DataFrame):
        pass

    @abstractmethod
    def visualize_missing_values(self, df: pd.DataFrame):
        pass


class SimpleMissingValuesAnalysis(MissingValuesAnalysisTemplate):
    def identify_missing_values(self, df: pd.DataFrame):
        print("\nMissing values count by columns:")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])

    def visualize_missing_values(self, df: pd.DataFrame):
        missing_values = df.isnull().sum()  # .sort_values(ascending=False)
        # missing_values = missing_values[missing_values > 0]
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 16), sharex=True, gridspec_kw={"hspace": 0.02})

        print("\nVisualizing missing values:")
        sns.barplot(x=missing_values.index, y=missing_values.values, ax=ax1)
        # plt.xticks(rotation=90)
        ax1.bar_label(ax1.containers[0], rotation=90, padding=3)

        sns.heatmap(df.isnull(), cbar=False, cmap="viridis", ax=ax2)
        plt.show()


if __name__ == "__main__":
    df = pd.read_csv("extracted_data/AmesHousing.csv")

    missing_value_analyzer = SimpleMissingValuesAnalysis()
    missing_value_analyzer.analyze(df)
