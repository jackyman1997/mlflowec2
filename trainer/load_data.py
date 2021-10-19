from numpy import ndarray
from sklearn.datasets import load_boston
from numpy import ndarray
import typing


def boston_data() -> typing.Tuple[ndarray]:
    ''' Return load_boston(return_X_y=True)
    '''
    return load_boston(return_X_y=True)


if __name__ == "__main__":
    print(boston_data()[0])
