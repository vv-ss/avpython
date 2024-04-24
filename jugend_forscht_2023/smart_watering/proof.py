import json
from urllib.request import urlopen
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import onnxruntime as rt
from warnings import simplefilter

# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

sess = rt.InferenceSession("model.onnx", providers=["CPUExecutionProvider"])
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name
TROCKEN_NFK = 21
plot_watering = []
plot_optimal_watering = []


def predict(X_test):
    x = (sess.run([label_name], {input_name: X_test})[0])
    # print('X_test ', X_test, ' Prediction = ', x[0][0])
    return x[0][0]


# three files, 2020.csv, 2021.csv, 2022.csv
# in each row, write min temp, max temp, precipitation for dates between 01-07 to 31-08
# DONE!

def make_files():
    for year in range(2019, 2023):
        file_year = open(str(year) + '.csv', 'w')
        file_year.write('Datum ; min_temp ; max_temp ; precip \n')
        for month in range(7, 9):
            for day in range(1, 32):
                date = str(year) + '-' + '{:02}'.format(month) + '-' + '{:02}'.format(day)
                file_year.write(date)
                j = urlopen('https://api.worldweatheronline.com/premium/v1/past-weather.ashx?q=Munich&date=' +
                            date + '&key=13442c01219a44a882f122116232011&format=json&tp=24')
                j_obj = json.load(j)
                print(j_obj)
                min_temp = str(j_obj['data']['weather'][0]['mintempC'])
                max_temp = str(j_obj['data']['weather'][0]['maxtempC'])
                precip = str(j_obj['data']['weather'][0]['hourly'][0]['precipMM'])
                file_year.write(' ; ' + min_temp + ' ; ' + max_temp + ' ; ' + precip + '\n')


# write file information in arrays
def read_csv_file(year):
    # with open(str(year) + '.csv', 'r') as file:
    #    csv_reader = csv.reader(file)
    #    for row in csv_reader:
    #        print(row)
    data = pd.read_csv(str(year) + '.csv', index_col=False, header=0, delimiter=' ; ', engine='python')
    (mi_temp, ma_temp, rain) = data['min_temp'], data['max_temp'], data['rain']
    return mi_temp, ma_temp, rain


def optimale_giessmenge(min_temp, max_temp, regen, heute_bodenfeuchte):
    if heute_bodenfeuchte > TROCKEN_NFK:
        return 0
    else:
        for i in range(0, 20):
            morgen_bodenfeuchte = predict(np.array([[min_temp[0], max_temp[0],
                                                     regen[0] + i, round(heute_bodenfeuchte)]]))
            if morgen_bodenfeuchte < TROCKEN_NFK:
                continue
            uebermorgen_bodenfeuchte = predict(np.array([[min_temp[1], max_temp[1],
                                                          regen[1] + 0, round(morgen_bodenfeuchte)]]))
            if uebermorgen_bodenfeuchte < TROCKEN_NFK:
                continue
            tag3_bodenfeuchte = predict(
                np.array([[min_temp[2], max_temp[2], regen[2] + 0, round(uebermorgen_bodenfeuchte)]]))
            if tag3_bodenfeuchte >= TROCKEN_NFK:
                return i
        return 20


# calculating total water for tw cases. See at the end of code
def calculate_total_water(min_temp_array, max_temp_array, rain_array, amount=None):
    morning_moisture = 40
    total_water = 0
    for i in range(len(min_temp_array) - 2):
        min_temp = min_temp_array[i]
        max_temp = max_temp_array[i]
        raining = rain_array[i]
        # if enough water
        if morning_moisture >= TROCKEN_NFK:
            watering = 0
            if amount is None:
                plot_optimal_watering.append(total_water + watering)
            else:
                plot_watering.append(total_water + watering)
        # if water needed
        else:
            if amount is not None:
                watering = amount
                plot_watering.append(total_water + watering)
            else:
                watering = optimale_giessmenge(min_temp_array[i:i + 3].array, max_temp_array[i:i + 3].array,
                                               rain_array[i:i + 3].array, morning_moisture)
                plot_optimal_watering.append(total_water + watering)
            total_water += watering
        morning_moisture = predict(np.array([[min_temp, max_temp, raining + watering, round(morning_moisture)]]))
    return total_water


def plot_graph(min_temp_array, max_temp_array, rain_array, year):
    # add two y-axis
    fig, ax1 = plt.subplots()
    # define timeline
    x_points = np.array(range(len(min_temp_array) - 2))
    # define ax2
    ax2 = ax1.twinx()
    # get data
    y_points_max_temp = max_temp_array[:-2]
    y_points_min_temp = min_temp_array[:-2]
    y_points_rain = np.cumsum(rain_array[:-2])
    data1 = [y_points_max_temp, y_points_min_temp]
    data2 = [plot_watering, plot_optimal_watering, y_points_rain]
    # plot and show lines and legend
    ax1.plot(x_points, data1[1], label="min Temperatur", linestyle="dotted")
    ax1.plot(x_points, data1[0], label="max Temperatur", linestyle="dotted")
    ax2.plot(x_points, data2[2], label="Niederschlag", color="blue", linestyle="-.")
    ax2.plot(x_points, data2[1], label="optimierte Bewaesserung", color="green")
    ax2.plot(x_points, data2[0], label="verschwenderische Bewaesserung", color="red")
    # add titles
    plt.title('Beweis, dass optimiertes Bewaessern Wasser spart :' + str(year))
    ax1.set_ylabel('Temperatur (in Grad C°)')
    ax2.set_ylabel('Niederschlag und Gießmenge (in mm)')
    plt.xlabel('Tage')
    # legend
    ax1.legend(loc="upper left", fontsize='x-small')
    ax2.legend(loc="upper right", fontsize='x-small')
    # fix axis size
    ax1.set_ylim(0, max(max_temp_array[:-2]) + 6)
    ax2.set_ylim(0, max(y_points_rain + plot_watering))
    plt.show()


for years in range(2019, 2023):
    mi_temp, ma_temp, rain = read_csv_file(years)
    plot_watering = []
    plot_optimal_watering = []
    # run model with fixed watering
    case_1 = calculate_total_water(mi_temp, ma_temp, rain, 20)
    case_2 = calculate_total_water(mi_temp, ma_temp, rain)
    plot_graph(mi_temp, ma_temp, rain, years)
    print('\033[1;34;40m Proof our model saves water')
    print('\033[1;32m year', years, ' Water Case 1:', case_1)
    # run model with optimized watering
    print('\033[1;32m Water Case 2:', case_2)
    print('\033[1;37m')
    print('\033[1;34;40m Saved water:', case_1 - case_2, '->', (case_1 - case_2) * 100 // case_1, '% \n')

# call model with above data to calculate next day moisture
# use model to find optimal watering
# -> optimale Gießmenge

# plot data
