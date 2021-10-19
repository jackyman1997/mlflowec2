import mlflow

from trainer.load_data import boston_data
from trainer.metrics import eval_metrics
from trainer.ml_utils import sklearn_split
from trainer.simple_predictor import DummyModel


mlflow.set_tracking_uri("http://127.0.0.1:5000")

if __name__ == "__main__":
    # load data
    X, y = boston_data(return_X_y=True)
    # Split the data into training and test sets. (0.75, 0.25) split.
    X_train, X_test, y_train, y_test = sklearn_split(X, y, test_size=0.25)

    # just rmb export mlflow tracking uri, put it into bashrc, and mlflow run . --experiment-name <name>

    # mlflow.run(uri="./mlruns") or mlflow.start_run()
    with mlflow.start_run(run_name="TRY"):
        model = DummyModel(alpha=1, l1_ratio=0.5)
        model.fit(X_train, y_train)
        # Pkl_Filename = "savethis.pkl"
        # with open(Pkl_Filename, 'wb') as file:
        #     pickle.dump(lr, file)
        mlflow.sklearn.log_model(
            model, "model", registered_model_name=f"{model.__name__}")
