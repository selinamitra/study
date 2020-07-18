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
iv1 = [df['ED01_01'],df['ED02_01'],df['ED03_01'], df['ED04_01'], df['ED05_01'],df['ED06_01'],df['ED07_01'], df['ED08_01']]
iv2 = [df['ED25_01'],df['ED26_01'],df['ED27_01'], df['ED28_01'], df['ED29_01'],df['ED30_01'],df['ED31_01'], df['ED32_01']]


## TOTAL MEAN OF A LIST
totalmean1 = 0
for v in iv1:
	mean = v.mean()
	totalmean1 = totalmean1 + mean
	#print('_______________________MEAN')
	#print(mean)

print('_______________________TOTAL MEAN1')
print(totalmean1 / 8)

totalmean2 = 0
for v in iv2:
	mean = v.mean()
	totalmean2 = totalmean2 + mean
	#print('_______________________MEAN')
	#print(mean)

print('_______________________TOTAL MEAN2')
print(totalmean2 / 8)


## LIST OF MEANS 1
meanlist1 = []

for v in iv1:
	mean = v.mean()
	#print('_______________________MEAN')
	#print(mean)
	meanlist1 = meanlist1 + [mean]

print('_______________________MEANlist1')
print(meanlist1)

## LIST OF MEANS 2
meanlist2 = []

for v in iv2:
	mean = v.mean()
	#print('_______________________MEAN')
	#print(mean)
	meanlist2 = meanlist2 + [mean]

print('_______________________MEANlist2')
print(meanlist2)

# Example of the Mann-Whitney U Test
from scipy.stats import mannwhitneyu
stat, p = mannwhitneyu(meanlist1, meanlist2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


"""
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

print('------------------------------------------------')
print('-------------------- Kruskal ---------------------')
# Example of the Kruskal-Wallis H Test
from scipy.stats import kruskal
stat, p = kruskal(iv[0],iv[1],iv[2],iv[3],iv[4],iv[5],iv[6],iv[7])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


#   VISUALIZATIONS FREQUENCES
for v in iv: 
	graph = v.plot(kind='hist',bins=[0,1,2,3,4,5,6,7,8,9])
	graph.set_xticklabels('')
	graph.set_xticks([1,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10], minor=True)
	graph.set_xticklabels(['','1','2','3','4','5','6','7','8','9'], minor=True)
	plt.title(v)
	plt.show(graph)
"""