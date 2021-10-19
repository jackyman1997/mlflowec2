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

# Run with Docker


# Custom hyperparamaters
This is one of the improvements that needs to be done. Currently, it is done by hard coded argparse and for loops.  
## usage
1. Edit `MLproject` entry_points
```
entry_points:
  main: 
    command: "python3 main.py --alpha=\"0.1 0.5 1 2\" --l1_ratio=\"0 0.25 0.5 0.75 1\"" 
```
PS. here you can see the are strings with spaces as separations, ugly right?
2. check if `main.py` agrees with those flats and args 
3. run 
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
## hard coded hyperparameter optimisation
- `GridSearchCV` might help with the for loops
- use json for saving hyperparameter
- issues with model registry
- work with multiple models? even NNs? 
