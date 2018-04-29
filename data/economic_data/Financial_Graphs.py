''' Financial Graphs 1992-2018 '''


import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter, MonthLocator, YearLocator

years = YearLocator()  # every year
months = MonthLocator()  # every month
yearsFmt = DateFormatter('%Y')

quotes = pd.read_csv('TNX_log_returns.csv',
                     index_col=0,
                     parse_dates=True,
                     infer_datetime_format=True)

dates = quotes.index
opens = quotes['Log Returns']

fig, ax = plt.subplots()
ax.plot_date(dates, opens, '-')

# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
ax.autoscale_view()


# format the coords message box
def price(x):
    return '$%1.2f' % x


ax.fmt_xdata = DateFormatter('%Y-%m-%d')
ax.fmt_ydata = price
ax.grid(True)

fig.autofmt_xdate()
plt.title('Logged Percent Change CBOE 10yr Bond Yields')
plt.show()

