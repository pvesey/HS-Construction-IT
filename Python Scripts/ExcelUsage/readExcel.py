from openpyxl import Workbook
import openpyxl

filename = "hello_again.xlsx"

workbook = openpyxl.load_workbook(filename)

sheet = workbook.active

cell = sheet.cell(row=1, column=1)

print(cell.value)

