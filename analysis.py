import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fulldf = pd.read_excel('data.xls', 'Data Set')

# Sort dataset by committee
fulldf.sort_values(by=['Committe'], ascending = True, inplace = True)
# print(fulldf)

# Average expenditure by committee
committee_average = fulldf.pivot_table(values='Cost', index='Committe', aggfunc= np.mean)
# committee_average.plot(kind = 'bar')
# plt.show()
# print(committee_average)

# Total costs per committee
committee_total = fulldf.pivot_table(values = 'Cost', index = 'Committe', aggfunc = np.sum)
# committee_total.plot(kind = 'bar')
# plt.show()
# print(committee_total)

# -- Committee Specific Data (Using Smalltown Records as Example) --

# Retrieve smalltown records
smalltown = fulldf.loc[(fulldf['Committe']=='Small Town Records'), ['Committe', 'Date', 'Line Item', 'Cost']]
# print(smalltown)

# Plot monthly transactions
smalltown.sort_values(by = 'Date',ascending = True, inplace = True)
smalltown['Month'] = smalltown['Date'].dt.month
smalltown_monthly = smalltown.pivot_table(values = 'Cost', index = 'Month', aggfunc = np.sum)
smalltown_monthly.plot(kind = 'bar')
plt.show()
