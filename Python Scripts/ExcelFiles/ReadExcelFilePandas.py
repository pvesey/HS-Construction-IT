# Read Excel File

# https://data.gov.ie/dataset/galway-fire-stations/resource/63d20282-b314-46cf-8e91-ade73a7fc2de
# Galway Fire Stations - converted to .xlsx

# **** Note you must install xlrd first.
# ***  run 'pip install pandas' - you shouold only need to do this once

# Information availale here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html

import pandas as pd

# Give the location of the file
fire_station_file = ("GCCFireStations.xlsx")

data = pd.read_excel(open(fire_station_file, 'rb'), sheet_name='GCCFireStations')

print(data)

data = pd.read_excel(fire_station_file, index_col=None, na_values=['NA'], usecols = "E:I,L")
print(data)
