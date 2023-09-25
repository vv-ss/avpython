import numpy as np
from sklearn.linear_model import LinearRegression
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
    y = moisture
    X = np.array([min_temp, max_temp, rain, water])
    X = np.transpose(X)
    model = LinearRegression().fit(X, y)
    print(model.score(X, y))
    print(model.predict(np.array([[15, 25, 0, 0]])))
    print(X)
read_csv_file()

