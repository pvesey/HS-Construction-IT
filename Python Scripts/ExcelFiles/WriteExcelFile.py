# Write to Excel file

# Some changes will be made to the data in the GCCFireStations file, make a copy fire_station_file

import shutil

shutil.copyfile('GCCFireStations.xlsx', 'WorkingFile.xlsx')
