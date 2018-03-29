import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# file on university type from financial file
df_type = pd.read_csv("./../university_financial/university_financial0116.csv", index_col='Unnamed: 0')
df_type = df_type[['UNITID', 'TYPE']]

# retrieve sfa data
df_sfa = pd.read_csv("./sfa9916.csv", index_col='Unnamed: 0')

# merge on id
df_result = pd.merge(df_type, df_sfa, left_on='UNITID', right_on='UNITID', how='inner')

# save to file
df_result.to_csv('./sfa9916_with_types.csv')
