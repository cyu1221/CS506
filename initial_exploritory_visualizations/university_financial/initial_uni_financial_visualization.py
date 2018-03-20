import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv("./../../data/university_financial/university_financial0116.csv")

cols = ['0102_RESEARCH','0203_RESEARCH','0304_RESEARCH','0405_RESEARCH','0506_RESEARCH',
		'0607_RESEARCH','0708_RESEARCH','0809_RESEARCH','0910_RESEARCH','1011_RESEARCH',
		'1112_RESEARCH','1213_RESEARCH','1314_RESEARCH','1415_RESEARCH','1516_RESEARCH']

df = df[cols]

X = df.mean().tolist()

bins = ['01-02','02-03','03-04','04-05','05-06',
	 '06-07','07-08','08-09','09-10','10-11',
	 '11-12','12-13','13-14','14-15','15-16']

plt.grid()
plt.bar(bins, X, align='center')

# labels
plt.title('Total amount of USD allocated to research accross post-secondary US educational institutions')
plt.xlabel('School year')
plt.ylabel('USD allocated to research')

plt.show()

print(X)