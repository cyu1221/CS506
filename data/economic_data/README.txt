The Data Files are as follows:

^DJI.csv 
^GSPC.csv
^IXIC.csv
^RUT.csv

^TNX.csv

	Obtained from 
	https://finance.yahoo.com/lookup/

	The rows contain weekly data with the variables Date, Open, High, Low, Close, Adj Close, 	Volume. In the case of ^TNX.csv, the non-date columns represent yields on the 10-year CBOE 	bond with no Volume data. 

CPI_PurchPower.csv
Unemployment.csv

	Obtained from
 	https://fred.stlouisfed.org/series/CUUR0000SA0R
	https://fred.stlouisfed.org/series/LNU04027662
	
	The rows contain monthly data with a single variable representing the relative purchasing 	power of the consumer dollar and the unemployment rate for college graduates having a 	bachelor’s degree or higher, aged 25 and above. 

All Data files contain data from 1992-2018

Financial_Graphs.py plots a timeseries with formatted gridlines
Financial_Graphsbook.ipynb creates graphs of all of the data files
