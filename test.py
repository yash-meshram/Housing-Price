import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Start an MLflow run
with mlflow.start_run():
    # Train a model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Log parameters
    mlflow.log_param("n_estimators", model.n_estimators)
    mlflow.log_param("max_depth", model.max_depth)

    # Log metrics
    accuracy = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", accuracy)

    # Create an input example (1 sample with the same number of features as the model expects)
    input_example = np.array([[5.1, 3.5, 1.4, 0.2]])  # Example input for the Iris dataset

    # Log the model with input example
    mlflow.sklearn.log_model(model, "model", input_example=input_example)

print("Model training and logging complete.")