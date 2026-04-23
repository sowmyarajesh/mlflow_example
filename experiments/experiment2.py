'''
Example LLM experriment to demotrate how to mlflow to track llm experiments.
This script reads the mlflow server configuration from a config.yaml file, 
which should contain the host and port for the MLflow server.
The example LLM should use openai api to generate some text, and log the parameters and metrics to mlflow.  
'''
import mlflow
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
    mlflow.set_experiment('llm_experiment')
    ## use openai api to generate some text, and log the parameters and metrics to mlflow.
    mlflow.log_param("model", "gpt-3.5-turbo")
    mlflow.log_param("temperature", 0.7)
    mlflow.log_param("max_tokens", 100)
    # generate some text using openai api
    import openai
    openai.api_key = "your_openai_api_key"
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": "Write a haiku about mlflow."}],
        temperature=0.7,    
        max_tokens=100
    )
    generated_text = response['choices'][0]['message']['content']
    print(f"Generated Text: {generated_text}")
    mlflow.log_metric("response_length", len(generated_text))
    



if __name__ == "__main__":
    main()