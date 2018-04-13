import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# For each school make a vector x = [<year>_delta_grants, <year>_delta_expenses, <year>_delta_research, <year>_delta_assets, type]

df_financial = pd.read_csv("./../../data/university_financial/university_financial0116.csv", index_col=0)

print(df_financial.columns)