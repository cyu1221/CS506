import os
import datetime
import pandas as pd

#List of file names
file_names = ['f1516_f2.csv','f1415_f2.csv','f1314_f2.csv','f1213_f2.csv','f1112_f2.csv','f1011_f2.csv','f0910_f2.csv',
			  'f0809_f2.csv','f0708_f2.csv','f0607_f2.csv','f0506_f2.csv','f0405_f2.csv','f0304_f2.csv','f0203_f2.csv',
			  'f0102_f2.csv','f0001_f2.csv','f9900f2.csv']

#Columns of intrest
colNames0616 = ['UNITID', 'F2A06', 'F2B01', 'F2B02', 'F2E021']
colNames9906 = ['unitid', 'f2a06', 'f2b01', 'f2b02', 'f2e021']

dfs = [""]*17
for i in range(len(file_names)):
	print(file_names[i])
	dfs[i] = pd.read_csv(file_names[i], encoding='latin-1')
	if i < 10:
		dfs[i] = dfs[i][colNames0616]
	else:
		dfs[i] = dfs[i][colNames9906]

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
df_result.to_csv('./not_for_profit9916.csv')

