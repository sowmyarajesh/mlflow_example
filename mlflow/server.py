'''
Script to start the inital mlflow server. 
This is used by the mlflow server command, and can also be used to start the server from a Python script.
Read config from config.yaml file, and start the mlflow server with the specified host and port.
'''
import argparse
import mlflow   



def read_config(config_path):
    import yaml
    import os
    from pathlib import Path
    config = {}
    APP_ROOT = Path(__file__).parents[1]
    with open(APP_ROOT / 'config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    return config

def start():
    config = read_config('config.yaml')
    if config is None:
        raise ValueError("Config file is empty or not found.")
    elif config.get('mlflow_host') is None or config.get('mlflow_port') is None:
        raise ValueError("Config file must contain 'mlflow_host' and 'mlflow_port' keys.")
    
    mlflow.server.start_server(host=config['mlflow_host'], port=config['mlflow_port'])

if __name__ == '__main__':
    start()
