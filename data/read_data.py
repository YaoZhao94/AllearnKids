from data import food_data_wrangling as w
import pandas as pd



directory = './fd_data/advanced'

result = w.get_data(directory)

df = pd.DataFrame()
df['Food'] = result[0]
df['Allergy'] = result[1]
df['Summary'] = result[2]
df['url'] = result[3]


df.to_csv('advanced.csv',index=False)
print(df)