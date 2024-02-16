#!/usr/bin/env python
# coding: utf-8

# In[7]:


import argparse
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# In[16]:


parser = argparse.ArgumentParser()

parser.add_argument('month', type= str)
parser.add_argument('year',type= str)
args = parser.parse_args()


list_month = list(args.month)
status_month = 0

for i in list_month:
    try:
        if isinstance(int(i), int):
            status_month += 1
    except ValueError:
        status_year = 0
assert status_month == 2, 'month is integer'

list_year = list(args.year)
status_year = 0

for j in list_year:
    try:
        if isinstance(int(j), int):
            status_year += 1
    except ValueError:
        status_year = 0

assert status_year == 4, 'year is integer'

month = args.month
year = args.year
try:
    df_orders = pd.read_excel(fr"C:\Users\Артур\Downloads\outcome_{month}.{year}.xlsx", index_col = 0)

except FileNotFoundError:
    print("File not found((")

else:
    df_orders["Дата"]
    [int(x.split()[0]) for x in df_orders['Дата']]
    df_orders["День"] = [int(x.split()[0]) for x in df_orders['Дата']]

    fig,ax = plt.subplots(constrained_layout = True)

    sns.barplot(
        data=df_orders,
        x="Сумма",
        y="Категория",
        orient = "h",
        estimator="sum",
        errorbar=None,
        hue = 'Категория',
        ax=ax
    )

    plt.title(f'График зависимости Категории от трат {month}.{year}', fontsize=15)
    plt.show()


# In[ ]:




