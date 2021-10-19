# mlflowec2

# Run locally
Start VENV on both terminals (one for server, one for runs): 
```
conda activate ./venv
```
Run `mlflow` server, [explanation](https://stackoverflow.com/questions/63255631/mlflow-invalid-parameter-value-unsupported-uri-mlruns-for-model-registry-s): 
``` 
mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./artifacts \
    --host 0.0.0.0
```
Set `MLFLOW_TRACKING_URI` environment variable: 
```
export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
```
Then on the next terminal: 
```
mlflow run .
```

# Issues
## zshrc fucked
Sometimes `mlflow` is not found, solutions: 
- make sure VENV with mlflow is started at BOTH terminals
- edit `~/.zshrc `
    1. add this in `~/.zshrc `
        ```
        export PATH=$HOME/bin:/usr/local/bin:$PATH
        export PATH=$HOME/miniconda3/bin/:$PATH
        ```
    2. do
        ```
        conda init zsh
        ```
## 