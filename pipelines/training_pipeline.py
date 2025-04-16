from steps.data_ingesttion_step import data_ingestion_step
from steps.handling_missing_values_step import handling_missing_values
from steps.feature_engineering_step import feature_engineering
from steps.outlier_detection_step import outlier_detection
from steps.data_splitter_step import data_splitter_step

from zenml import Model, pipeline

@pipeline(
    model = Model(
        # the name uniquelt identifies the model
        name = "prices_predictor"
    )
)

def ml_pipeline():
    """Define end-to-end machine learning pipeline"""
    
    # data ingestion step
    df_raw = data_ingestion_step(file_path = "data/archive.zip")
    
    # Handling missing values step
    df_filled = handling_missing_values(df_raw, method = "mean")
    
    # feature engineering
    df_transform = feature_engineering(
        df_filled,
        strategy = "log",
        features = ["Gr Liv Area", "SalePrice"]
    )
    
    # Outlier detection and handling the outliers
    outliers, df_cleaned = outlier_detection(df_transform)
    
    # Data splitting step
    X_train, X_test, y_train, y_test = data_splitter_step(df_cleaned, target_column = "SalePrice")
    
    return X_train, X_test, y_train, y_test
