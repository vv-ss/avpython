import numpy as np
from xgboost.sklearn import XGBRegressor as Model
import csv
import pandas as pd

# Read X from .csv
#X = np.array([[18, 24, 18, 0], [18, 24, 2, 0], [15, 23, 3, 0]])
#y = [14, 40, 25, 30]
#model = LinearRegression().fit(X, y)
#print(model.score(X, y))
#print(model.predict(np.array([[15, 25, 0, 0]])))


def read_csv_file():
    with open("Bewaesserung.csv", 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
    data = pd.read_csv('Bewaesserung.csv', index_col=False, header=0, delimiter=';')
    print(data.columns)
    (min_temp, max_temp, moisture, rain, water) = data['min_temp'], data['max_temp'], data['moisture_sun'], data['rain'], data['water']
    print(min_temp, max_temp, moisture, rain)
    y = moisture[1:]
    X = np.array([min_temp[1:], max_temp[1:], rain[1:], water[1:], moisture[:-1]])
    X = np.transpose(X)
    model = Model().fit(X, y)
    print(model.score(X, y))
    print(model.predict(np.array([[15, 35, 0, 12, 5]])))
read_csv_file()

