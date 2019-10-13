import pandas as pd
import re
import records



df = pd.read_excel('./VCAMS_Indicator_7_7a.xlsx', index_col=0)

gk = df.groupby('LGA')

df_1 = pd.DataFrame()

for x in gk.groups:
    if re.findall('victoria',x):
        next
    else:


        df_1 = df_1.append(gk.get_group(x))
df_1.reset_index(level = 0, inplace = True)


db = records.Database('mysql://root:ECC12345$@mydatabase.cn2pbhimebqz.ap-southeast-2.rds.amazonaws.com/food_recall')



for index,x in df_1.iterrows():
    query = "INSERT INTO vcams(year,LGA,numerator,denominator,indicator) VALUES (\"" + str(x['Year']) + "\",\"" + x['LGA'] + "\",\"" + str(x['Numerator']) + "\",\"" + str(x['Denominator']) + "\",\"" + str(x['Indicator']) + "\")"
    query = query.encode('latin-1', 'ignore')
    query = query.decode("utf-8")
    db.query(query)



row = db.query("SELECT * FROM vcams;")




