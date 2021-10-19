from sklearn.linear_model import ElasticNet


class DummyModel():
    def __init__(self, *args, **kwargs):
        self.model = ElasticNet(*args, **kwargs)

    def fit(self, *args, **kwargs):
        self.model.fit(*args, **kwargs)
