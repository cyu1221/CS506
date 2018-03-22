import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# file on university financial data
df = pd.read_csv("./../../data/university_financial/university_financial0116.csv")



#purchesing power per dollar to convert USD to same value
df_PPD = pd.read_csv("./../../data/economic_data/CPI_PurchPower.csv") 

dates = ['2002-01-01', '2003-01-01', '2004-01-01', '2005-01-01', '2006-01-01', '2007-01-01',
		 '2008-01-01', '2009-01-01', '2010-01-01', '2011-01-01', '2012-01-01', '2013-01-01',
		 '2014-01-01', '2015-01-01', '2016-01-01', '2018-01-01']

df_PPD = df_PPD.loc[(df_PPD['DATE'].isin(dates))]

PPD = df_PPD['CUUR0000SA0R'].tolist()

base_year_2018 = PPD[len(PPD)-1]
PPD = PPD[:len(PPD)-1]

adjustments = [val/base_year_2018 for val in PPD]




#research

# relevant columns for research
cols_research = ['0102_RESEARCH','0203_RESEARCH','0304_RESEARCH','0405_RESEARCH','0506_RESEARCH',
		'0607_RESEARCH','0708_RESEARCH','0809_RESEARCH','0910_RESEARCH','1011_RESEARCH',
		'1112_RESEARCH','1213_RESEARCH','1314_RESEARCH','1415_RESEARCH','1516_RESEARCH']

research = df[['TYPE']+cols_research]


reserch_all = df[cols_research]
research_public = research.loc[(research['TYPE'] == 'public'), cols_research]
research_for_profit = research.loc[(research['TYPE'] == 'for-profit'), cols_research]
research_not_for_profit = research.loc[(research['TYPE'] == 'not-for-profit'), cols_research]

research_sum_all = reserch_all.sum().tolist()
research_public_sum_all = research_public.sum().tolist()
research_for_profit_sum_all = research_for_profit.sum().tolist()
research_not_for_profit_sum_all = research_not_for_profit.sum().tolist()

research_all_n_non_zero = research.astype(bool).sum(axis=0)
research_public_n_non_zero = research.astype(bool).sum(axis=0)
research_for_profit_n_non_zero = research.astype(bool).sum(axis=0)
research_not_for_profit_n_non_zero = research.astype(bool).sum(axis=0)

research_all_mean_non_zero = [research_sum_all[i]/research_all_n_non_zero[i] for i in range(len(research_sum_all))]
research_public_mean_non_zero = [research_public_sum_all[i]/research_public_n_non_zero[i] for i in range(len(research_public_sum_all))]
research_for_profit_mean_non_zero = [research_for_profit_sum_all[i]/research_for_profit_n_non_zero[i] for i in range(len(research_for_profit_sum_all))]
research_not_for_profit_mean_non_zero = [research_not_for_profit_sum_all[i]/research_not_for_profit_n_non_zero[i] for i in range(len(research_not_for_profit_sum_all))]

research_sum_all_adjusted = [research_sum_all[i]*adjustments[i] for i in range(len(research_sum_all))]
research_public_sum_all_adjusted = [research_public_sum_all[i]*adjustments[i] for i in range(len(research_public_sum_all))]
research_for_profit_sum_all_adjusted = [research_for_profit_sum_all[i]/adjustments[i] for i in range(len(research_for_profit_sum_all))]
research_not_for_profit_sum_all_adjusted = [research_not_for_profit_sum_all[i]/adjustments[i] for i in range(len(research_not_for_profit_sum_all))]


bins = ['01-02','02-03','03-04','04-05','05-06',
	 '06-07','07-08','08-09','09-10','10-11',
	 '11-12','12-13','13-14','14-15','15-16']

plt.title('Total amount of USD allocated to research\naccross post-secondary US educational institutions')
plt.xlabel('School year')
plt.ylabel('USD allocated to research')
plt.plot(bins,research_sum_all, label='all')
plt.plot(bins,research_public_sum_all, label='public')
plt.plot(bins,research_for_profit_sum_all, label='for-profit')
plt.plot(bins,research_not_for_profit_sum_all, label='not-for-profit')
plt.legend()
plt.show()

plt.title('Mean amount of USD allocated to research accross\npost-secondary US educational institutions doing research')
plt.xlabel('School year')
plt.ylabel('USD allocated to research')
plt.plot(bins,research_all_mean_non_zero, label='all')
plt.plot(bins,research_public_mean_non_zero, label='public')
plt.plot(bins,research_for_profit_mean_non_zero, label='for-profit')
plt.plot(bins,research_not_for_profit_mean_non_zero, label='not-for-profit')
plt.legend()
plt.show()

#Make graph adjusted for inflation:
plt.title('Total amount of USD (CPI adjusted) allocated to research\naccross post-secondary US educational institutions')
plt.xlabel('School year')
plt.ylabel('USD allocated to research')
plt.plot(bins,research_sum_all_adjusted, label='all')
plt.plot(bins,research_public_sum_all_adjusted, label='public')
plt.plot(bins,research_for_profit_sum_all_adjusted, label='for-profit')
plt.plot(bins,research_not_for_profit_sum_all_adjusted, label='not-for-profit')
plt.legend()
plt.show()



#Revenue

# relevant columns for revenue
cols_revenue = ['0102_REVENUE','0203_REVENUE','0304_REVENUE','0405_REVENUE','0506_REVENUE',
		'0607_REVENUE','0708_REVENUE','0809_REVENUE','0910_REVENUE','1011_REVENUE',
		'1112_REVENUE','1213_REVENUE','1314_REVENUE','1415_REVENUE','1516_REVENUE']

revenue = df[['TYPE']+cols_revenue]


reserch_all = df[cols_revenue]
revenue_public = revenue.loc[(revenue['TYPE'] == 'public'), cols_revenue]
revenue_for_profit = revenue.loc[(revenue['TYPE'] == 'for-profit'), cols_revenue]
revenue_not_for_profit = revenue.loc[(revenue['TYPE'] == 'not-for-profit'), cols_revenue]

revenue_sum_all = reserch_all.sum().tolist()
revenue_public_sum_all = revenue_public.sum().tolist()
revenue_for_profit_sum_all = revenue_for_profit.sum().tolist()
revenue_not_for_profit_sum_all = revenue_not_for_profit.sum().tolist()


revenue_all_n_non_zero = revenue.astype(bool).sum(axis=0)
revenue_public_n_non_zero = revenue.astype(bool).sum(axis=0)
revenue_for_profit_n_non_zero = revenue.astype(bool).sum(axis=0)
revenue_not_for_profit_n_non_zero = revenue.astype(bool).sum(axis=0)

revenue_all_mean_non_zero = [revenue_sum_all[i]/revenue_all_n_non_zero[i] for i in range(len(revenue_sum_all))]
revenue_public_mean_non_zero = [revenue_public_sum_all[i]/revenue_public_n_non_zero[i] for i in range(len(revenue_public_sum_all))]
revenue_for_profit_mean_non_zero = [revenue_for_profit_sum_all[i]/revenue_for_profit_n_non_zero[i] for i in range(len(revenue_for_profit_sum_all))]
revenue_not_for_profit_mean_non_zero = [revenue_not_for_profit_sum_all[i]/revenue_not_for_profit_n_non_zero[i] for i in range(len(revenue_not_for_profit_sum_all))]

revenue_sum_all_adjusted = [revenue_sum_all[i]*adjustments[i] for i in range(len(revenue_sum_all))]
revenue_public_sum_all_adjusted = [revenue_public_sum_all[i]*adjustments[i] for i in range(len(revenue_public_sum_all))]
revenue_for_profit_sum_all_adjusted = [revenue_for_profit_sum_all[i]/adjustments[i] for i in range(len(revenue_for_profit_sum_all))]
revenue_not_for_profit_sum_all_adjusted = [revenue_not_for_profit_sum_all[i]/adjustments[i] for i in range(len(revenue_not_for_profit_sum_all))]


plt.title('Total revenue accross \n post-secondary US educational institutions')
plt.xlabel('School year')
plt.ylabel('USD')
plt.plot(bins,revenue_sum_all, label='all')
plt.plot(bins,revenue_public_sum_all, label='public')
plt.plot(bins,revenue_for_profit_sum_all, label='for-profit')
plt.plot(bins,revenue_not_for_profit_sum_all, label='not-for-profit')
plt.legend()
plt.show()

plt.title('Mean revenue accross \n post-secondary US educational institutions')
plt.xlabel('School year')
plt.ylabel('USD')
plt.plot(bins,revenue_all_mean_non_zero, label='all')
plt.plot(bins,revenue_public_mean_non_zero, label='public')
plt.plot(bins,revenue_for_profit_mean_non_zero, label='for-profit')
plt.plot(bins,revenue_not_for_profit_mean_non_zero, label='not-for-profit')
plt.legend()
plt.show()

plt.title('Total amount of USD (CPI adjusted) revenue\naccross post-secondary US educational institutions')
plt.xlabel('School year')
plt.ylabel('USD allocated to revenue')
plt.plot(bins,revenue_sum_all_adjusted, label='all')
plt.plot(bins,revenue_public_sum_all_adjusted, label='public')
plt.plot(bins,revenue_for_profit_sum_all_adjusted, label='for-profit')
plt.plot(bins,revenue_not_for_profit_sum_all_adjusted, label='not-for-profit')
plt.legend()
plt.show()




# assets
# relevant columns for assets
cols_assets = ['0102_ASSETS','0203_ASSETS','0304_ASSETS','0405_ASSETS','0506_ASSETS',
		'0607_ASSETS','0708_ASSETS','0809_ASSETS','0910_ASSETS','1011_ASSETS',
		'1112_ASSETS','1213_ASSETS','1314_ASSETS','1415_ASSETS','1516_ASSETS']

assets = df[['TYPE']+cols_assets]


reserch_all = df[cols_assets]
assets_public = assets.loc[(assets['TYPE'] == 'public'), cols_assets]
assets_for_profit = assets.loc[(assets['TYPE'] == 'for-profit'), cols_assets]
assets_not_for_profit = assets.loc[(assets['TYPE'] == 'not-for-profit'), cols_assets]

assets_sum_all = reserch_all.sum().tolist()
assets_public_sum_all = assets_public.sum().tolist()
assets_for_profit_sum_all = assets_for_profit.sum().tolist()
assets_not_for_profit_sum_all = assets_not_for_profit.sum().tolist()

assets_all_n_non_zero = assets.astype(bool).sum(axis=0)
assets_public_n_non_zero = assets.astype(bool).sum(axis=0)
assets_for_profit_n_non_zero = assets.astype(bool).sum(axis=0)
assets_not_for_profit_n_non_zero = assets.astype(bool).sum(axis=0)

assets_all_mean_non_zero = [assets_sum_all[i]/assets_all_n_non_zero[i] for i in range(len(assets_sum_all))]
assets_public_mean_non_zero = [assets_public_sum_all[i]/assets_public_n_non_zero[i] for i in range(len(assets_public_sum_all))]
assets_for_profit_mean_non_zero = [assets_for_profit_sum_all[i]/assets_for_profit_n_non_zero[i] for i in range(len(assets_for_profit_sum_all))]
assets_not_for_profit_mean_non_zero = [assets_not_for_profit_sum_all[i]/assets_not_for_profit_n_non_zero[i] for i in range(len(assets_not_for_profit_sum_all))]

assets_sum_all_adjusted = [assets_sum_all[i]*adjustments[i] for i in range(len(assets_sum_all))]
assets_public_sum_all_adjusted = [assets_public_sum_all[i]*adjustments[i] for i in range(len(assets_public_sum_all))]
assets_for_profit_sum_all_adjusted = [assets_for_profit_sum_all[i]/adjustments[i] for i in range(len(assets_for_profit_sum_all))]
assets_not_for_profit_sum_all_adjusted = [assets_not_for_profit_sum_all[i]/adjustments[i] for i in range(len(assets_not_for_profit_sum_all))]


plt.title('Total assets accross\npost-secondary US educational institutions')
plt.xlabel('School year')
plt.ylabel('USD ')
plt.plot(bins,assets_sum_all, label='all')
plt.plot(bins,assets_public_sum_all, label='public')
plt.plot(bins,assets_for_profit_sum_all, label='for-profit')
plt.plot(bins,assets_not_for_profit_sum_all, label='not-for-profit')
plt.legend()
plt.show()

plt.title('Mean amount of assets accross\npost-secondary US educational institutions')
plt.xlabel('School year')
plt.ylabel('USD')
plt.plot(bins,assets_all_mean_non_zero, label='all')
plt.plot(bins,assets_public_mean_non_zero, label='public')
plt.plot(bins,assets_for_profit_mean_non_zero, label='for-profit')
plt.plot(bins,assets_not_for_profit_mean_non_zero, label='not-for-profit')
plt.legend()
plt.show()

plt.title('Total amount of USD (CPI adjusted) assets\naccross post-secondary US educational institutions')
plt.xlabel('School year')
plt.ylabel('USD allocated to assets')
plt.plot(bins,assets_sum_all_adjusted, label='all')
plt.plot(bins,assets_public_sum_all_adjusted, label='public')
plt.plot(bins,assets_for_profit_sum_all_adjusted, label='for-profit')
plt.plot(bins,assets_not_for_profit_sum_all_adjusted, label='not-for-profit')
plt.legend()
plt.show()




#Expences
# relevant columns for expenses
cols_expenses = ['0102_EXPENSES','0203_EXPENSES','0304_EXPENSES','0405_EXPENSES','0506_EXPENSES',
		'0607_EXPENSES','0708_EXPENSES','0809_EXPENSES','0910_EXPENSES','1011_EXPENSES',
		'1112_EXPENSES','1213_EXPENSES','1314_EXPENSES','1415_EXPENSES','1516_EXPENSES']

expenses = df[['TYPE']+cols_expenses]


reserch_all = df[cols_expenses]
expenses_public = expenses.loc[(expenses['TYPE'] == 'public'), cols_expenses]
expenses_for_profit = expenses.loc[(expenses['TYPE'] == 'for-profit'), cols_expenses]
expenses_not_for_profit = expenses.loc[(expenses['TYPE'] == 'not-for-profit'), cols_expenses]

expenses_sum_all = reserch_all.sum().tolist()
expenses_public_sum_all = expenses_public.sum().tolist()
expenses_for_profit_sum_all = expenses_for_profit.sum().tolist()
expenses_not_for_profit_sum_all = expenses_not_for_profit.sum().tolist()


expenses_all_n_non_zero = expenses.astype(bool).sum(axis=0)
expenses_public_n_non_zero = expenses.astype(bool).sum(axis=0)
expenses_for_profit_n_non_zero = expenses.astype(bool).sum(axis=0)
expenses_not_for_profit_n_non_zero = expenses.astype(bool).sum(axis=0)

expenses_all_mean_non_zero = [expenses_sum_all[i]/expenses_all_n_non_zero[i] for i in range(len(expenses_sum_all))]
expenses_public_mean_non_zero = [expenses_public_sum_all[i]/expenses_public_n_non_zero[i] for i in range(len(expenses_public_sum_all))]
expenses_for_profit_mean_non_zero = [expenses_for_profit_sum_all[i]/expenses_for_profit_n_non_zero[i] for i in range(len(expenses_for_profit_sum_all))]
expenses_not_for_profit_mean_non_zero = [expenses_not_for_profit_sum_all[i]/expenses_not_for_profit_n_non_zero[i] for i in range(len(expenses_not_for_profit_sum_all))]

expenses_sum_all_adjusted = [expenses_sum_all[i]*adjustments[i] for i in range(len(expenses_sum_all))]
expenses_public_sum_all_adjusted = [expenses_public_sum_all[i]*adjustments[i] for i in range(len(expenses_public_sum_all))]
expenses_for_profit_sum_all_adjusted = [expenses_for_profit_sum_all[i]/adjustments[i] for i in range(len(expenses_for_profit_sum_all))]
expenses_not_for_profit_sum_all_adjusted = [expenses_not_for_profit_sum_all[i]/adjustments[i] for i in range(len(expenses_not_for_profit_sum_all))]


plt.title('Total expenses accross\npost-secondary US educational institutions')
plt.xlabel('School year')
plt.ylabel('USD ')
plt.plot(bins,expenses_sum_all, label='all')
plt.plot(bins,expenses_public_sum_all, label='public')
plt.plot(bins,expenses_for_profit_sum_all, label='for-profit')
plt.plot(bins,expenses_not_for_profit_sum_all, label='not-for-profit')
plt.legend()
plt.show()

plt.title('Mean amount of expenses accross\npost-secondary US educational institutions')
plt.xlabel('School year')
plt.ylabel('USD')
plt.plot(bins,expenses_all_mean_non_zero, label='all')
plt.plot(bins,expenses_public_mean_non_zero, label='public')
plt.plot(bins,expenses_for_profit_mean_non_zero, label='for-profit')
plt.plot(bins,expenses_not_for_profit_mean_non_zero, label='not-for-profit')
plt.legend()
plt.show()

plt.title('Total amount of USD (CPI adjusted) expenses\naccross post-secondary US educational institutions')
plt.xlabel('School year')
plt.ylabel('USD allocated to expenses')
plt.plot(bins,expenses_sum_all_adjusted, label='all')
plt.plot(bins,expenses_public_sum_all_adjusted, label='public')
plt.plot(bins,expenses_for_profit_sum_all_adjusted, label='for-profit')
plt.plot(bins,expenses_not_for_profit_sum_all_adjusted, label='not-for-profit')
plt.legend()
plt.show()


exit()








