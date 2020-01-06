
from openpyxl import load_workbook

fire_station_file = "GCCFireStations.xlsx"

wb = load_workbook(filename = fire_station_file)

sheet_ranges = wb['GCCFireStations']

print(sheet_ranges['F2:F10'])
print(sheet_ranges['F2'].value)
