import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# file on university financial data
df = pd.read_csv("./../../data/university_financial_aid/sfa9916_with_types.csv")


#purchesing power per dollar to convert USD to same value
df_PPD = pd.read_csv("./../../data/economic_data/CPI_PurchPower.csv") 

dates = ['2000-01-01', '2001-01-01', '2002-01-01', '2003-01-01', '2004-01-01', '2005-01-01', 
		 '2006-01-01', '2007-01-01', '2008-01-01', '2009-01-01', '2010-01-01', '2011-01-01', 
		 '2012-01-01', '2013-01-01', '2014-01-01', '2015-01-01', '2016-01-01', '2018-01-01']

df_PPD = df_PPD.loc[(df_PPD['DATE'].isin(dates))]

PPD = df_PPD['CUUR0000SA0R'].tolist()

base_year_2018 = PPD[len(PPD)-1]
PPD = PPD[:len(PPD)-1]

adjustments = [val/base_year_2018 for val in PPD]


def extractVariableStatistics(df, varName, yearFirst, numYears, adjustments, mean):
	#generate column names
	_cols = [varName]*numYears
	yearFall   = int(yearFirst[:2])
	yearSpring = int(yearFirst[2:])
	for i in range(numYears):
		_cols[i]   = str(yearFall).zfill(2) + str(yearSpring).zfill(2) + "_" + _cols[i]
		yearFall   = 0 if yearFall   == 99 else yearFall+1
		yearSpring = 0 if yearSpring == 99 else yearSpring+1
	
	_all			= df[_cols]
	_public			= df.loc[(df['TYPE'] == 'public'), _cols]
	_not_for_profit = df.loc[(df['TYPE'] == 'not-for-profit'), _cols]
	_for_profit 	= df.loc[(df['TYPE'] == 'for-profit'), _cols]

	result_all            = _all.sum().tolist()
	result_public         = _public.sum().tolist()
	result_not_for_profit = _not_for_profit.sum().tolist()
	result_for_profit     = _for_profit.sum().tolist()

	if adjustments != []:
		result_all            = [result_all[i]*adjustments[i] for i in range(len(result_all))]
		result_public         = [result_public[i]*adjustments[i] for i in range(len(result_public))]
		result_not_for_profit = [result_not_for_profit[i]*adjustments[i] for i in range(len(result_not_for_profit))]
		result_for_profit     = [result_for_profit[i]*adjustments[i] for i in range(len(result_for_profit))]


	if mean == True:
		n_non_zero_all            = _all.astype(bool).sum(axis=0)
		n_non_zero_public         = _public.astype(bool).sum(axis=0)
		n_non_zero_not_for_profit = _not_for_profit.astype(bool).sum(axis=0)
		n_non_zero_for_profit     = _for_profit.astype(bool).sum(axis=0)

		result_all            = [result_all[i]/n_non_zero_all[i] for i in range(len(result_all))]
		result_public         = [result_public[i]/n_non_zero_public[i] for i in range(len(result_public))]
		result_not_for_profit = [result_not_for_profit[i]/n_non_zero_not_for_profit[i] for i in range(len(result_not_for_profit))]
		result_for_profit     = [result_for_profit[i]/n_non_zero_for_profit[i] for i in range(len(result_for_profit))]

	return (result_all, result_public, result_not_for_profit, result_for_profit)



n_receiving_aid        = extractVariableStatistics(df, 'ANYAIDN', '9900', 17, [], False)

n_loans                = extractVariableStatistics(df, 'LOAN_N', '9900', 17, [], False)
avg_loan_amount        = extractVariableStatistics(df, 'LOAN_A', '9900', 17, adjustments, True)

n_fed_grant            = extractVariableStatistics(df, 'FGRNT_N', '9900', 17, [], False)
avg_fed_grant_amount   = extractVariableStatistics(df, 'FGRNT_N', '9900', 17, adjustments, True)

n_state_grant          = extractVariableStatistics(df, 'SGRNT_N', '9900', 17, [], False)
avg_state_grant_amount = extractVariableStatistics(df, 'SGRNT_N', '9900', 17, adjustments, True)


n_uni_grant	           = extractVariableStatistics(df, 'IGRNT_N', '9900', 17, [], False)
avg_uni_grant_amount   = extractVariableStatistics(df, 'IGRNT_N', '9900', 17, adjustments, True)



bins = ['99-00','00-01','01-02','02-03','03-04','04-05',
		'05-06','06-07','07-08','08-09','09-10','10-11',
	 	'11-12','12-13','13-14','14-15','15-16']

plt.figure(figsize=(8,7))
plt.title('Total number of students reciving\nany kind of financial aid')
plt.xlabel('School year')
plt.ylabel('number of students')
plt.plot(range(17),n_receiving_aid[0], label='all')
plt.plot(range(17),n_receiving_aid[1], label='public')
plt.plot(range(17),n_receiving_aid[3], label='for-profit')
plt.plot(range(17),n_receiving_aid[2], label='not-for-profit')
plt.legend()
plt.xticks(range(17), bins, rotation='vertical')
plt.savefig('./tot_n_receiving_aid.png')




plt.figure(figsize=(8,7))
plt.title('Total number of students taking loans')
plt.xlabel('School year')
plt.ylabel('number of students')
plt.plot(range(17),n_loans[0], label='all')
plt.plot(range(17),n_loans[1], label='public')
plt.plot(range(17),n_loans[3], label='for-profit')
plt.plot(range(17),n_loans[2], label='not-for-profit')
plt.legend()
plt.xticks(range(17), bins, rotation='vertical')
plt.savefig('./tot_n_receiving_loan.png')

plt.figure(figsize=(8,7))
plt.title('Average loan amount to students \ntaking up loans (CPI adjusted)')
plt.xlabel('School year')
plt.ylabel('USD (2018 CPI adjusted)')
plt.plot(range(17),avg_loan_amount[0], label='all')
plt.plot(range(17),avg_loan_amount[1], label='public')
plt.plot(range(17),avg_loan_amount[3], label='for-profit')
plt.plot(range(17),avg_loan_amount[2], label='not-for-profit')
plt.legend()
plt.xticks(range(17), bins, rotation='vertical')
plt.savefig('./avg_loan_amount.png')



plt.figure(figsize=(8,7))
plt.title('Total number of students receiving federal grants')
plt.xlabel('School year')
plt.ylabel('number of students')
plt.plot(range(17),n_fed_grant[0], label='all')
plt.plot(range(17),n_fed_grant[1], label='public')
plt.plot(range(17),n_fed_grant[3], label='for-profit')
plt.plot(range(17),n_fed_grant[2], label='not-for-profit')
plt.legend()
plt.xticks(range(17), bins, rotation='vertical')
plt.savefig('./tot_n_receiving_fed_grants.png')

plt.figure(figsize=(8,7))
plt.title('Average federal grant amount to\nstudents receiving it (CPI adjusted)')
plt.xlabel('School year')
plt.ylabel('USD (2018 CPI adjusted)')
plt.plot(range(17),avg_fed_grant_amount[0], label='all')
plt.plot(range(17),avg_fed_grant_amount[1], label='public')
plt.plot(range(17),avg_fed_grant_amount[3], label='for-profit')
plt.plot(range(17),avg_fed_grant_amount[2], label='not-for-profit')
plt.legend()
plt.xticks(range(17), bins, rotation='vertical')
plt.savefig('./avg_fed_grant_amount.png')



plt.figure(figsize=(8,7))
plt.title('Total number of students receiving state or local grants')
plt.xlabel('School year')
plt.ylabel('number of students')
plt.plot(range(17),n_state_grant[0], label='all')
plt.plot(range(17),n_state_grant[1], label='public')
plt.plot(range(17),n_state_grant[3], label='for-profit')
plt.plot(range(17),n_state_grant[2], label='not-for-profit')
plt.legend()
plt.xticks(range(17), bins, rotation='vertical')
plt.savefig('./tot_n_receiving_state_or_local_grants.png')

plt.figure(figsize=(8,7))
plt.title('Average state or local grant amount to\nstudents receiving it (CPI adjusted)')
plt.xlabel('School year')
plt.ylabel('USD (2018 CPI adjusted)')
plt.plot(range(17),avg_state_grant_amount[0], label='all')
plt.plot(range(17),avg_state_grant_amount[1], label='public')
plt.plot(range(17),avg_state_grant_amount[3], label='for-profit')
plt.plot(range(17),avg_state_grant_amount[2], label='not-for-profit')
plt.legend()
plt.xticks(range(17), bins, rotation='vertical')
plt.savefig('./avg_state_or_local_grant_amount.png')



plt.figure(figsize=(8,7))
plt.title('Total number of students receiving institutional grants')
plt.xlabel('School year')
plt.ylabel('number of students')
plt.plot(range(17),n_uni_grant[0], label='all')
plt.plot(range(17),n_uni_grant[1], label='public')
plt.plot(range(17),n_uni_grant[3], label='for-profit')
plt.plot(range(17),n_uni_grant[2], label='not-for-profit')
plt.legend()
plt.xticks(range(17), bins, rotation='vertical')
plt.savefig('./tot_n_receiving_institutional_grants.png')

plt.figure(figsize=(8,7))
plt.title('Average institutional grant amount to\nstudents receiving it (CPI adjusted)')
plt.xlabel('School year')
plt.ylabel('USD (2018 CPI adjusted)')
plt.plot(range(17),avg_uni_grant_amount[0], label='all')
plt.plot(range(17),avg_uni_grant_amount[1], label='public')
plt.plot(range(17),avg_uni_grant_amount[3], label='for-profit')
plt.plot(range(17),avg_uni_grant_amount[2], label='not-for-profit')
plt.legend()
plt.xticks(range(17), bins, rotation='vertical')
plt.savefig('./avg_institutional_grant_amount.png')
