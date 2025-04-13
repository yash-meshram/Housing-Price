from abc import ABC, abstractmethod
import pandas as pd


class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        pass


class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        print("\nData types and non-null counts:")
        print(df.info())


class SummaryStatisticInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        print("\nSummary statistics (Numerical features):")
        print(df.describe())
        print("\nSummary statistics (Categorical features):")
        df.describe(include=["O"])


class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        self.strategy = strategy

    def excute_strategy(self, df: pd.DataFrame):
        self.strategy.inspect(df)


if __name__ == "__main__":
    # load data
    df = pd.read_csv("../extracted_data/AmesHousing.csv")

    # Initialize data inspector with a specific strategy
    data_inspector = DataInspector(
        DataTypesInspectionStrategy()
    )  # setting the strategy
    data_inspector.excute_strategy(df)  # excuting the strategy

    # changing the strategy
    data_inspector.set_strategy(SummaryStatisticInspectionStrategy())
    data_inspector.excute_strategy(df)
