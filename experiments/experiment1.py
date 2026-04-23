'''
This is a sample experiment script that demonstrates how to use MLflow for tracking machine learning experiments. 
It includes code for setting up the MLflow client, creating an experiment, and logging parameters and metrics.
The script reads the MLflow server configuration from a config.yaml file, which should contain the host and port for the MLflow server, 
as well as the name of the experiment to be created or used.

'''
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn import datasets
from sklearn.model_selection import train_test_split
import yaml
from pathlib import Path

def read_config(config_path):
    config = {}
    APP_ROOT = Path(__file__).parents[1]
    with open(APP_ROOT / 'config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    return config

def main():
    config = read_config('config.yaml')
    mlflow.set_tracking_uri(f"{config['mlflow_host']}:{config['mlflow_port']}")
    mlflow.set_experiment(config['experiment_name'])
    
    # Load dataset
    data = datasets.load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    
    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Log parameters and metrics
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("random_state", 42)
    
    predictions = model.predict(X_test)
    mse = np.mean((predictions - y_test) ** 2)
    print(f"Mean Squared Error: {mse}")
    mlflow.log_metric("mse", mse)   

if __name__ == "__main__":
    main()