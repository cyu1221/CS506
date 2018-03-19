import os
import datetime
import pandas as pd

#List of file names
file_names = ['f1516_f1a.csv','f1415_f1a.csv','f1314_f1a.csv','f1213_f1a.csv','f1112_f1a.csv','f1011_f1a.csv','f0910_f1a.csv',
			  'f0809_f1a.csv','f0708_f1a.csv','f0607_f1a.csv','f0506_f1a.csv','f0405_f1a.csv','f0304_f1a.csv','f0203_f1a.csv',
			  'f0102_f1a.csv']

#Columns of intrest
colNames0616 = ['UNITID', 'F1A18', 'F1D01', 'F1D02', 'F1C021']
colNames0106 = ['unitid', 'f1a18', 'f1d01', 'f1d02', 'f1c021']

dfs = [""]*15
for i in range(len(file_names)):
	print(file_names[i])
	dfs[i] = pd.read_csv(file_names[i], encoding='latin-1')
	if i < 10:
		dfs[i] = dfs[i][colNames0616]
	else:
		dfs[i] = dfs[i][colNames0106]

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

df_result.to_csv('./public0116.csv')
