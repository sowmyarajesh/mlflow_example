# mlflow_example
Example project to learn and try out mlflow 

## Get Started 

To get started with this project

### Enable Virtual environment

If the environment does not exists, create one with the command:
    ```python -m venv .venv```

Activate the environment:
    windows: ```.venv/Scripts/Activate```
    Mac/Linux: ```source .venv/bin/activate```

Install the required libraries if not already:
    ```pip install -r requirements.txt```


### Start mlflow server
Start the mlflow server in the terminal
```mlflow server```

The server listens to ```http://localhost:5000``` by default. 

If the server needs to be accessed in other machines in the intranet.

```mlflow server --host 0.0.0.0```

If port has to be changed

```mlflow server --port 2030 --host 0.0.0.0```
