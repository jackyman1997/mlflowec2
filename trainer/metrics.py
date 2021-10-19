import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import typing


def eval_metrics(
        actual: typing.Union[list, np.ndarray],
        pred: typing.Union[list, np.ndarray]
) -> tuple:
    # Expected sequence or array-like, got <class 'float'>
    if isinstance(actual, float) or isinstance(actual, int):
        actual = [actual]
    if isinstance(pred, float) or isinstance(pred, int):
        pred = [pred]
    # metrics
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


if __name__ == "__main__":
    print(eval_metrics(actual=18.9, pred=19))
