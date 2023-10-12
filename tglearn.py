import numpy as np


class KNeighborsRegressor:
    def __init__(self, n_neighbors = 5):
        self.n_neighbors = n_neighbors

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for X_test in X_test:
            distances = np.sqrt(np.sum((X_test-self.X_train)**2, axis=1))
            indices = np.argsort(distances)[:self.n_neighbors]
            prediction = np.mean(self.y_train[indices])
            predictions.append(prediction)
            return np.array(prediction).reshape(-1, 1)
class LinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None

    def fit(self, X ,y):
        """
        Learning function
        :param X: Independent variable (2d array)
        :param y: dependent variable (2d array)
        :return: void
        """
        X_mean = np.mean(X)
        y_mean = np.mean(y)
        denominator =  np.sum(pow((X-X_mean),2))
        numerator = np.sum((X-X_mean)*(y-y_mean))

        self.slope = numerator/denominator
        self.intercept = y_mean-(self.slope * X_mean)

    def predict(self, X) -> list:
        """
        predict value for input
        :param X: new independent variable
        :return:predict value for input(2d array format)
        """
        return self.slope * np.array(X) + self.intercept
