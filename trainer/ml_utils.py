from sklearn.model_selection import train_test_split
import typing


def sklearn_split(
        *arrays,
        test_size=None,
        train_size=None,
        random_state=None,
        shuffle=True,
        stratify=None
) -> typing.List[typing.Union[typing.Sequence, typing.Any, list]]:
    '''Returns train_test_split \n
    All args same as train_test_split
    '''
    kwargs = locals()
    arrays = kwargs.pop("arrays", None)
    return train_test_split(*arrays, **kwargs)


if __name__ == "__main__":
    print(sklearn_split([1, 2, 3, 4, 5], [
          0.1, 0.2, 0.3, 0.4, 0.5], test_size=0.2))
    print(train_test_split([1, 2, 3, 4, 5], [
          0.1, 0.2, 0.3, 0.4, 0.5], test_size=0.2))
