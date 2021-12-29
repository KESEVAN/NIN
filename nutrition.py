import sklearn
import joblib
import pandas as pd
import random
import numpy as np
import decimal
from operator import add, sub, mul

classifier =joblib.load("NIN.pkl")


nin_db = "NIN_Db_final.xlsx" # Path to the Excel file
df = pd.read_excel(nin_db)
# df.head()
group = df.drop(columns=['Common name'])
group = group.rename(columns={'Food Group':'name'})
factor = pd.factorize(group['name'],sort=True)
group.name= factor[0]
definitions = factor[1]

path_to_data = "MEN.xlsx" # Path to the Excel file
df_men = pd.read_excel(path_to_data)
# print(df_men.head())
path_to_data = "WOMEN.xlsx" # Path to the Excel file
df_women = pd.read_excel(path_to_data)
df_women.head()


    

def Rand(start, end, num):
    res = []
 
    for j in range(num):
        res.append(float(decimal.Decimal(random.randrange(start, end))/100))
 
    return res

def women(age):
    if int(age) in range(11,14):
        op = df_women.iloc[:1,1:]
    elif int(age) in range(15,18):
        op = df_women.iloc[1:2,1:]
    elif int(age) in range(19,24):
        op = df_women.iloc[2:3,1:]
    elif int(age) in range(25,51):
        op = df_women.iloc[3:4,1:]
    elif int(age) > 51:
        op = df_women.iloc[4:5,1:]
    return op.values

def men(age):
    if int(age) in range(11,14):
        op = df_men.iloc[:1,1:]
    elif int(age) in range(15,18):
        op = df_men.iloc[1:2,1:]
    elif int(age) in range(19,24):
        op = df_men.iloc[2:3,1:]
    elif int(age) in range(25,51):
        op = df_men.iloc[3:4,1:]
    elif int(age) > 51:
        op = df_men.iloc[4:5,1:]
    return op.values

def preference(pre,prefer):
    ingredients = []
    # pref = input("Enter Preference:")
    pref = prefer
    for i in pre:
        q = definitions[i]
        op = df.loc[df['Food Group'] == q]

        column = op[pref]
        max_value = column.max()
        m = op.loc[df[pref] == max_value]
        x = m.iloc[:,:1].values
        ingredients.append(x[0][0])
    return ingredients

def norm(pr,m):
    pr = pr
    for i in range(15):
        b = Rand(100,300,1)
        m *= b
        pred = classifier.predict(m)
        if pred not in pr:
            pr.append(pred[0])
    return pr

# if __name__ == '__main__':
#     main()

def start(a,g,p):
    pr=[]
    age = a
    gen = g
    prefer = p
    if gen == 'M':
        m = men(int(age))
        pred  = classifier.predict(m)
        pr.append(pred[0])
        m_norm = norm(pr,m)
        # for i in m_norm:
        #     print(definitions[i])
    else:
        w = women(int(age))
        pred  = classifier.predict(w)
        pr.append(pred[0])
        w_norm = norm(pr,w)
        # for i in w_norm:
        #     print(definitions[i])

    result = preference(pr,prefer)
    return result
