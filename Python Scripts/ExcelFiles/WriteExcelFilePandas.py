# Write to Excel file

# Some changes will be made to the data in the GCCFireStations file, make a copy fire_station_file

# you may need to run 'pip install xlsxwriter'

import shutil
import pandas as pd

shutil.copyfile('GCCFireStations.xlsx', 'WorkingFile.xlsx')

working_file_name = 'WorkingFile.xlsx'

# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Data': ['New Fire Station', 'text2', 'text 3', 'text 4', 'text 5', 'text 6']})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(working_file_name, engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='GCCFireStations')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
