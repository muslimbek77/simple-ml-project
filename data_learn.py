import pandas as pd

d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

df = pd.DataFrame(data=d)

print(df)

count_column = df.shape[1]
print("count_column: ",count_column)

count_row = df.shape[0]
print("count_row: ", count_row)

data = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
print("data: ", data)
Average_pulse_max = max(data)
Average_pulse_min = min(data)
print ("Average_pulse_max: ",Average_pulse_max)
print ("Average_pulse_min: ",Average_pulse_min)


import numpy as np
Average_calorie_burnage = np.mean(data)
print("Average_calorie_burnage:",Average_calorie_burnage)



import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")

print(health_data)
print(health_data.head())

health_data.dropna(axis=0,inplace=True)

print(health_data)

print(health_data.info())

health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)

print (health_data.info())
print(health_data.describe())
