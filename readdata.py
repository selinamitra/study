import pandas as pd
excel_file = pd.ExcelFile("data1/data_avap.xlsx")
sheet = pd.read_excel(excel_file)
print(sheet)