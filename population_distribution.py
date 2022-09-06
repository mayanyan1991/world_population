import pandas as pd

df_raw = pd.read_csv('raw_data.csv') 
column_name = list(df_raw.columns)

print(column_name)

print(df_raw.shape)














