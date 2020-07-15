import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.stats import friedmanchisquare
from scipy.stats import f_oneway
from scipy.stats import shapiro

#   READ FILE
df1 = pd.read_excel("data1/data_avap.xlsx")
#print(df1)

#   SET FIRST COLUMN AS HEADER
headers = df1.iloc[0]
df  = pd.DataFrame(df1.values[1:], columns=headers)
#print(df)

#   SELECT SINGLE COLUMN
#column_x = df['ED01_01']
#print(column_x)

#   SELECT MULTIPLE COLUMNS
###column_xy = df.iloc[1:,[2,7]]
#column_xy = df[['ED01_01','REF']]
#print(column_xy)

#   COUNT FREQUENCES
#counter = column_x.value_counts()
#print('--------------- COUNTS ---------------')
#print(counter)

#	ARRAY: INDEPENDET VARIABLES
iv = [df['ED01_01'],df['ED01_02'],df['ED01_03']]

#	GAUSSIAN DISTRIBUTION, MEAN, STANDARD DEVIATION
for v in iv: 
	print('------------------------------------------------')
	#rating1 = df['ED01_01']
	print(v)

	print('_______________________GD')
	data = v
	stat, p = shapiro(data)
	print('stat=%.3f, p=%.3f' % (stat, p))
	if p > 0.05:
		print('Probably Gaussian')
	else:
		print('Probably not Gaussian')

	mean = v.mean()
	print('_______________________MEAN')
	print(mean)

	sd = v.std()
	print('_______________________SD')
	print(sd)


print('------------------------------------------------')
print('------------------- Friedman -------------------')
stat, p = friedmanchisquare(iv[0], iv[1], iv[2])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')
print('------------------------------------------------')
print('-------------------- ANOVA ---------------------')
from scipy.stats import f_oneway
stat, p = f_oneway(iv[0], iv[1], iv[2])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')
print('------------------------------------------------')


#   VISUALIZATIONS FREQUENCES
for v in iv: 
	graph = v.plot(kind='hist',bins=[0,1,2,3,4,5,6,7,8,9])
	graph.set_xticklabels('')
	graph.set_xticks([1,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10], minor=True)
	graph.set_xticklabels(['','1','2','3','4','5','6','7','8','9'], minor=True)
	plt.show(graph)