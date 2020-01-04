# Read Excel File

# https://data.gov.ie/dataset/galway-fire-stations/resource/63d20282-b314-46cf-8e91-ade73a7fc2de
# Galway Fire Stations - converted to .xlsx

# **** Note you must install xlrd first.
# ***  run 'pip install xlrd' - you shouold only need to do this once

import xlrd

# Give the location of the file
fire_station_file = ("GCCFireStations.xlsx")

wb = xlrd.open_workbook(fire_station_file)
sheet = wb.sheet_by_index(0)

fire_station_name = sheet.cell_value(2, 5)

print(fire_station_name)
