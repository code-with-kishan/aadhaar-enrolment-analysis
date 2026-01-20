from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_demand(X, y, future_X):
    """
    Train linear regression model and predict future demand.
    """
    if X is None or y is None or future_X is None:
        return None

    X = np.array(X).reshape(-1, 1)
    y = np.array(y)
    future_X = np.array(future_X).reshape(-1, 1)

    model = LinearRegression()
    model.fit(X, y)

    return model.predict(future_X)
