import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class EnergyModel:
    def __init__(self, data_path='energy_data.csv'):
        self.data = pd.read_csv(data_path)
        self.models = {}

    def preprocess(self):
        df = self.data.copy()
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        df['dayofweek'] = pd.to_datetime(df['timestamp']).dt.dayofweek
        df.drop(['timestamp'], axis=1, inplace=True)
        X = df.drop('energy_consumption', axis=1)
        y = df['energy_consumption']
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_models(self):
        X_train, X_test, y_train, y_test = self.preprocess()

        # Linear Regression
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        self.models['linear'] = lr

        # Decision Tree
        dt = DecisionTreeRegressor()
        dt.fit(X_train, y_train)
        self.models['Decision Tree'] = dt

        # Neural Network
        nn = Sequential([
            Dense(64, input_dim=X_train.shape[1], activation='relu'),
            Dense(64, activation='relu'),
            Dense(1)
        ])
        nn.compile(optimizer='adam', loss='mse')
        nn.fit(X_train, y_train, epochs=50, batch_size=10, verbose=0)
        self.models['Neural Network'] = nn

        # Evaluation 
        for name, model in self.models.items():
            pred = model.predict(X_test) if name != 'nn' else model.predict(X_test).flatten()
            rmse = np.sqrt(mean_squared_error(y_test, pred))
            print(f'{name} RMSE: {rmse:.2f}')

    def predict(self, model_name, input_data):
        model = self.models.get(model_name)
        if not model:
            raise ValueError("Model not found")
        if model_name == 'nn':
            return model.predict(np.array([input_data])).flatten()[0]
        else:
            return model.predict([input_data])[0]