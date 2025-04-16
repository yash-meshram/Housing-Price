import os
import zipfile
from abc import ABC, abstractmethod
import pandas as pd


class DataIngestor(ABC):
    """
    Abstract base class for data ingestion.
    """

    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        """
        Ingest data from the specified file path.
        """
        pass


class ZipDataIngester(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Extract the .zip file and
        store the extracted data in new folder and
        read the .csv file."""

        # Ensure the file is .zip
        if not file_path.endswith(".zip"):
            raise ValueError("Provided file is not a .zip file.")

        # Extract the .zip file in the new folder
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall("extracted_data")

        # find the .csv file in extracted_data
        extracted_files = os.listdir("extracted_data")
        csv_files = [file for file in extracted_files if file.endswith(".csv")]

        if len(csv_files) == 0:
            raise FileNotFoundError("No .csv file in the extracted data.")
        if len(csv_files) > 1:
            raise ValueError(
                "Multible .csv files found. PLease specify which one to use."
            )

        # csv file path
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        # read the csv file
        df = pd.read_csv(csv_file_path)  # DataFrame

        return df


# Factory for DataIngestors
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        if file_extension == ".zip":
            return ZipDataIngester()
        else:
            raise ValueError(
                f"No data ingestor is available for file extension: {file_extension}"
            )


# Example usage
if __name__ == "__main__":
    file_path = "data/archive.zip"

    file_extension = os.path.splitext(file_path)[1]

    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    df = data_ingestor.ingest(file_path)

    print(df.head())
