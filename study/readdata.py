import pandas as pd
import matplotlib.pyplot as plt

excel_file = pd.ExcelFile("data1/data_avap.xlsx")
df = pd.read_excel(excel_file)
#print(df)

# auf mehrere Spalten a,b zugreifen
#column_xy = df.iloc[:,[0,1]]
#print(column_xy)

# rating row - column
rating = df.iloc[1:, 6:7]
print(rating)

mean = rating.mean()
print('--------------- MEAN ---------------')
print(mean)

sd = rating.std()
print('---------------- SD ----------------')
print(sd)
