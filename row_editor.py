import pandas as pd

df = pd.read_excel('stats_shooting.xlsx')

rows_to_delete = df.index[25::26]  

df = df.drop(rows_to_delete)

df.to_excel('stats_shooting_modified.xlsx', index=False)