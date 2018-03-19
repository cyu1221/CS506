import os
import datetime
import pandas as pd

#List of file names
file_names = ['f1516_f3.csv','f1415_f3.csv','f1314_f3.csv','f1213_f3.csv','f1112_f3.csv','f1011_f3.csv','f0910_f3.csv',
			  'f0809_f3.csv','f0708_f3.csv','f0607_f3.csv','f0506_f3.csv','f0405_f3.csv','f0304_f3.csv','f0203_f3.csv',
			  'f0102_f3.csv','f0001_f3.csv','f9900f3.csv']

#Columns of intrest
colNames1316 = ['UNITID', 'F3A04', 'F3B01', 'F3B02', 'F3E02A1']
colNames0613 = ['UNITID', 'F3A04', 'F3B01', 'F3B02', 'F3E02']
colNames0506 = ['unitid', 'f3a04', 'f3b01', 'f3b02', 'f3e02']


dfs = [""]*17
for i in range(len(file_names)):
	print(file_names[i])
	dfs[i] = pd.read_csv(file_names[i], encoding='latin-1')
	if i < 3:
		dfs[i] = dfs[i][colNames1316]
	elif i < 10:
		dfs[i] = dfs[i][colNames0613]
	else:
		dfs[i] = dfs[i][colNames0506]

for i in range(len(file_names)):
	dfs[i].columns = ['UNITID', 'ASSETS', 'REVENUE', 'EXPENSES', 'RESEARCH']

for i in range(len(file_names)):
	dfs[i].columns = ['UNITID']+[file_names[i][1:5] + '_' + dfs[i].columns[j] for j in range(1,len(dfs[i].columns))]

for i in range(len(file_names)):
	dfs[i]['UNITID'] = dfs[i]['UNITID'].apply(lambda x: int(x))

df_result = dfs[0]
for i in range(1,len(dfs)):
	df_result = pd.merge(df_result, dfs[i], left_on='UNITID', right_on='UNITID', how='inner')


print(df_result)
df_result.to_csv('./for_profit9916.csv')















