import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.stats import friedmanchisquare
from scipy.stats import f_oneway
from scipy.stats import shapiro

#   READ FILE
df1 = pd.read_excel("data1/data_avap.xlsx")

#   SET FIRST COLUMN AS HEADER
headers = df1.iloc[0]
df  = pd.DataFrame(df1.values[1:], columns=headers)

#   SELECT SINGLE COLUMN
#column_x = df['ED01_01']

#   SELECT MULTIPLE COLUMNS
#column_xy = df[['ED01_01','REF']] OR column_xy = df.iloc[1:,[2,7]]

#   COUNT FREQUENCES
#counter = column_x.value_counts()

#	ARRAYS

##Valence
ratings1 = [df['ED33_01'],df['ED34_01'],df['ED35_01'], df['ED36_01'], df['ED37_01'],df['ED38_01'],df['ED39_01'], df['ED40_01']]
ratings2 = [df['ED01_01'],df['ED01_01'],df['ED01_01'], df['ED01_01'], df['ED01_01'],df['ED01_01'],df['ED01_01'], df['ED01_01']]

##Arousal
#ratings1 = [df['ED33_02'],df['ED34_02'],df['ED35_02'], df['ED36_02'], df['ED37_02'],df['ED38_02'],df['ED39_02'], df['ED40_02']]
#ratings2 = [df['ED01_02'],df['ED01_02'],df['ED01_02'], df['ED01_02'], df['ED01_02'],df['ED01_02'],df['ED01_02'], df['ED01_02']]

##Dominance
#ratings1 = [df['ED33_03'],df['ED34_03'],df['ED35_03'], df['ED36_03'], df['ED37_03'],df['ED38_03'],df['ED39_03'], df['ED40_03']]
#ratings2 = [df['ED01_03'],df['ED01_03'],df['ED01_03'], df['ED01_03'], df['ED01_03'],df['ED01_03'],df['ED01_03'], df['ED01_03']]

"""
#PRETESTS
#	GAUSSIAN DISTRIBUTION, MEAN, STANDARD DEVIATION (respective of one column in r: ratings)
for r in ratings1: 
	print('------------------------------------------------')
	#print(r)

	print('_______________________GD')
	data = r
	stat, p = shapiro(data)
	print('stat=%.3f, p=%.3f' % (stat, p))
	if p > 0.05:
		print('Probably Gaussian')
	else:
		print('Probably not Gaussian')

	mean = r.mean()
	print('_______________________MEAN')
	print(mean)

	sd = r.std()
	print('_______________________SD')
	print(sd)

	print('------------------------------------------------')
"""

## LIST OF MEANS 1
meanlist1 = []

for r in ratings1:
	mean = r.mean()
	#print('_______________________MEAN')
	#print(mean)
	meanlist1 = meanlist1 + [mean]

#print('_______________________LIST of MEANS (RATING 1)')
#print(meanlist1)

## LIST OF MEANS 2
meanlist2 = []

for r in ratings2:
	mean = r.mean()
	#print('_______________________MEAN')
	#print(mean)
	meanlist2 = meanlist2 + [mean]

#print('_______________________LIST of MEANS (RATING 2)')
#print(meanlist2)

#	TOTAL MEAN OF A LIST 
totalmean1 = 0

for r in ratings1:
	mean = r.mean()
	totalmean1 = totalmean1 + mean
	#print('_______________________MEAN')
	#print(mean)

print('_______________________TOTAL MEAN of RATING 1')
print(totalmean1 / 8)

totalmean2 = 0
for r in ratings2:
	mean = r.mean()
	totalmean2 = totalmean2 + mean
	#print('_______________________MEAN')
	#print(mean)

print('_______________________TOTAL MEAN of RATING 2')
print(totalmean2 / 8)


"""
#   VISUALIZATIONS FREQUENCES
for r in ratings1: 
	graph = r.plot(kind='hist',bins=[0,1,2,3,4,5,6,7,8,9])
	graph.set_xticklabels('')
	graph.set_xticks([1,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10], minor=True)
	graph.set_xticklabels(['','1','2','3','4','5','6','7','8','9'], minor=True)
	plt.title(r)
	plt.show(graph)
"""

#  MAIN TESTS
print('------------------------------------------------')
print('-------------------- WILCOXON ------------------')
from scipy.stats import wilcoxon
stat, p = wilcoxon(meanlist1, meanlist2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


"""
print('------------------------------------------------')
print('-------------- MANN-WHITNEY U TEST -------------')
from scipy.stats import mannwhitneyu
stat, p = mannwhitneyu(meanlist1, meanlist2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


print('------------------------------------------------')
print('------------------- Friedman -------------------')
stat, p = friedmanchisquare(ratings1, ratings2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


print('------------------------------------------------')
print('-------------------- ANOVA ---------------------')
from scipy.stats import f_oneway
stat, p = f_oneway(ratings[0], ratings[1], ratings[2])
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
stat, p = kruskal(ratings[0],ratings[1],ratings[2],ratings[3],ratings[4],ratings[5],ratings[6],ratings[7])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')
"""