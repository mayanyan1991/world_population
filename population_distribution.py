import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

df_raw = pd.read_csv('raw_data.csv') 
column_name = list(df_raw.columns)

#print(column_name)
#print(df_raw.shape)
#df_raw[df_raw["1961"].isnull()] return the whole row where certain column has missing value
#df_raw[df_raw.isnull().any(axis=1)] return the whole row if any missing value appears

#remove the row with missing data
df_dropna = df_raw.dropna()
#find out rows that are not countries and remove
list_remove = ['WLD','IBT','LMY','MIC','IBD','EAR','LMC',
               'UMC','EAS','LTE','EAP','TEA','SAS','TSA',
               'IDA','OED','HIC','SSF','TSS','SSA','IDX',
               'PST','LDC','PRE','FCS','ECS','HPC','LIC',
               'AFE','LCN','TLA','LAC','IDB','MEA','AFW',
               'TEC','EUU','ARB','MNA','ECA','TMN','NAC',
               'EMU','CEB','SST','OSS']

df_country = df_dropna.drop(df_dropna.loc
                               [df_dropna['Country Code'].
                                isin(list_remove)].index)

#find the largest number 
pop_max = df_country.iloc[:, 2:].max().max()
#find the smallest number
pop_min = df_country.iloc[:, 2:].min().min()
# define range
bins = 50

x = [math.log10(i) for i in list(df_country["1960"])]
y = [math.log10(i) for i in list(df_country["1980"])]

num_bins = [j for j in np.arange(0,10,0.2)] #bins can be a number or list

fig, axs = plt.subplots(1,2)
axs[0].hist(x, bins, density = True) # if two rows then axs[0,0]
axs[1].hist(y, bins, density = True)
plt.show() 
'''
fig, ax = plt.subplots() # subplots is covenient if having multiple figures 
# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=True)
ax.plot(bins)
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_title('')
plt.show()
'''