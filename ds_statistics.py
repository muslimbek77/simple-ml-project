import pandas as pd
import numpy as np

full_health_data = pd.read_csv("data.csv", header=0, sep=",")
full_health_data.dropna(axis=0,inplace=True)
full_health_data["Average_Pulse"] = full_health_data['Average_Pulse'].astype(float)
full_health_data["Max_Pulse"] = full_health_data["Max_Pulse"].astype(float)


Max_Pulse= full_health_data["Max_Pulse"]
percentile10 = np.percentile(Max_Pulse, 10)

print(percentile10)
