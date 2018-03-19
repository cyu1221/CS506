import os
import datetime
import pandas as pd

#List of file names
file_names = ['./sfa1516.csv','./sfa1415.csv','./sfa1314.csv','./sfa1213.csv','./sfa1112.csv','./sfa1011.csv','./sfa0910.csv',
			  './sfa0809.csv','./sfa0708.csv','./sfa0607.csv','./sfa0506.csv','./sfa0405.csv','./sfa0304.csv','./sfa0203.csv',
			  './sfa0102.csv','./sfa0001s.csv','./sfa9900s.csv']

#Columns of intrest
colNames0616 = ['UNITID', 'ANYAIDN', 'LOAN_A', 'LOAN_N', 'FGRNT_N', 'FGRNT_A', 'SGRNT_N', 'SGRNT_A', 'IGRNT_N', 'IGRNT_A']
colNames9906 = ['unitid', 'anyaidn', 'loan_a', 'loan_n', 'fgrnt_n', 'fgrnt_a', 'sgrnt_n', 'sgrnt_a', 'igrnt_n', 'igrnt_a']


# Poor formating on sfa0910.csv, must be processed individualy
data = []
for s in open('./sfa0910.csv', 'r'):
	l = []
	line = s.split(',')
	l.append(line[0])
	l.append(line[60])
	l.append(line[122])
	l.append(line[116])
	l.append(line[76])
	l.append(line[82])
	l.append(line[100])
	l.append(line[106])
	l.append(line[108])
	l.append(line[114])
	data.append(l)

cols = data.pop(0)
df = pd.DataFrame(data, columns=cols)

# making all files into a list of dataframes 
dfs = [""]*17
for i in range(len(file_names)):
	if i == 6:
		continue
	dfs[i] = pd.read_csv(file_names[i], encoding='latin-1')
	if i < 10:
		dfs[i] = dfs[i][colNames0616]
	else:
		dfs[i] = dfs[i][colNames9906]

dfs[6] = df

# set lower case column names to upper
for i in range(len(file_names)):
	dfs[i].columns = ['UNITID']+[file_names[i][5:9] + '_' + dfs[i].columns[j].upper() for j in range(1,len(dfs[i].columns))]

for i in range(len(file_names)):
	dfs[i]['UNITID'] = dfs[i]['UNITID'].apply(lambda x: int(x))


df_result = dfs[0]
for i in range(1,len(dfs)):
	df_result = pd.merge(df_result, dfs[i], left_on='UNITID', right_on='UNITID', how='inner')

print(df_result)

df_result.to_csv('./sfa9916.csv')

