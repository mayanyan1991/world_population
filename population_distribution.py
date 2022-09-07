import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import math
import numpy as np
import matplotlib.animation as manimation

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


# Define the meta data for the movie
FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie', artist='YM',
                comment='histogram of population distribution')
writer = FFMpegWriter(fps=10, metadata=metadata)

# Initialize the movie
fig, ax = plt.subplots()

# Update the frames for the movie
with writer.saving(fig, "movie.mp4", 200):
    for year in column_name[2:]:
        ax.clear() # clean the previous figure
        ax.set_ylim(0,0.7) # set the figure properties
        ax.set_xlim(0,10)
        ax.set_xlabel('log10')
        ax.set_ylabel('percentage')
        ax.text(1, 0.5, 'year = ' + year)
        #plot
        pop_year = [math.log10(i) for i in list(df_country[year])]
        pop_year_max = max(pop_year)
        pop_year_min = min(pop_year)
        pop_range = np.linspace(pop_year_min, pop_year_max, 100)
        a_estimate, loc_estimate, scale_estimate = stats.skewnorm.fit(pop_year)
        pdf_skewnorm = stats.skewnorm.pdf(pop_range, a_estimate,
                                          loc = loc_estimate,
                                          scale = scale_estimate)
        plt.plot(pop_range, pdf_skewnorm)
        plt.hist(pop_year, num_bins, density = True)
        writer.grab_frame()
