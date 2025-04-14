from src.ingest_data import DataIngestorFactory
import pandas as pd
from zenml import step


@step
def data_ingestion_step(file_path: str) -> pd.DataFrame:
    file_extension = ".zip"

    # Get the appropriate DataIngestor
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    # Ingest the data
    df = data_ingestor.ingest(file_path)
    return df
