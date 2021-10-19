import mlflow
import argparse

from trainer.load_data import boston_data
from trainer.metrics import eval_metrics
from trainer.ml_utils import sklearn_split
from trainer.simple_predictor import DummyModel
from tools.utils import argparse_to_dict


# export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
mlflow.set_tracking_uri("http://127.0.0.1:5000")


if __name__ == "__main__":
    # load data
    X, y = boston_data()

    # argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--split', type=float, default=0.25)
    parser.add_argument('--alpha', type=str, nargs="+", default=[1.0])
    parser.add_argument('--l1_ratio', type=str, nargs="+", default=[0.5])
    flags = parser.parse_args()
    kwargs = argparse_to_dict(flags)
    # for multiple inputs in mlflow
    if type(kwargs["alpha"][0]) is str:
        kwargs["alpha"] = list(map(float, kwargs["alpha"][0].split()))
    if type(kwargs["l1_ratio"][0]) is str:
        kwargs["l1_ratio"] = list(map(float, kwargs["l1_ratio"][0].split()))

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = sklearn_split(
        X, y, test_size=kwargs["split"], random_state=kwargs["seed"])

    # mlflow run, those forloops maybe replaced by grid search cv
    for alpha in kwargs["alpha"]:
        for l1_ratio in kwargs["l1_ratio"]:
            # mlflow.run(uri="./mlruns") or mlflow.start_run()
            with mlflow.start_run(run_name="TRY"):
                # train model
                model = DummyModel(alpha=alpha, l1_ratio=l1_ratio)
                model.fit(X_train, y_train)
                # get pred
                y_pred = model.predict(X_test)
                # eval results
                (rmse, mae, r2) = eval_metrics(y_test, y_pred)
                # record
                mlflow.log_param("alpha", alpha)
                mlflow.log_param("l1_ratio", l1_ratio)
                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("r2", r2)
                mlflow.log_metric("mae", mae)
                # model registry
                mlflow.sklearn.log_model(
                    model, "model", registered_model_name=f"DUMMYMODEL")
                # save model
                # Pkl_Filename = "savethis.pkl"
                # with open(Pkl_Filename, 'wb') as file:
                #     pickle.dump(lr, file)

    # just rmb export mlflow tracking uri, put it into bashrc, and mlflow run . --experiment-name <name>
