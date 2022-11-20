# -*- coding: utf-8 -*-
"""Copy of ML sta

Originally made on Google Colab. Developed by Lara Tekbas, Zeynep Mertan, Manual Perez and Max Riffi-Aslett
Transposed into Python for web for FindMyBorough by Alex Choi

"""
import numpy as np

import pandas as pd
df= pd.read_csv("/content/drive/MyDrive/dataframe_final.csv")

df

customer_home_preference = int(input("Please enter how many bedrooms you need:"))

if customer_home_preference == 1:
  df.drop(columns=['rent_per_month_2bed', 'rent_per_month_3bed', 'rent_per_month_4bed'], axis=1)
elif customer_home_preference == 2:
  df.drop(columns=['rent_per_month_1bed', 'rent_per_month_3bed', 'rent_per_month_4bed'], axis=1)
elif customer_home_preference == 3:
  df.drop(columns=['rent_per_month_1bed', 'rent_per_month_2bed', 'rent_per_month_4bed'], axis=1)
elif customer_home_preference == 4:
  df.drop(columns=['rent_per_month_1bed', 'rent_per_month_2bed', 'rent_per_month_3bed'], axis=1)

df

customer_budget = int(input("Please enter your budget:"))

filtered_customer_list = df.loc[(df['rent_per_month'] <= customer_budget)]

filtered_customer_list

columns = df.columns
columns = list(columns)
columns.remove('Borough')
columns.remove('rent_per_month')
columns

ranking_list = []
print('Rate between 1 and 5 how important each of the following variables are for your accomodation (1 = not important and 5 = being essential')
for i in range (len(columns)):
  added_word = columns[i]
  added_word = str(added_word)
  customer_ranking = input("Please enter your ranking for " + added_word + ": ")
  ranking_list.append(customer_ranking)
ranking_list

new_matrix = filtered_customer_list[['green_space','travel_bank','safety','school_density','pubs','well_being_score']]
new_matrix

type(new_matrix)

new_matrix.to_numpy()

import numpy as  np

vector = np.array(ranking_list,dtype=float)
matrix = np.array(new_matrix,dtype=float)

matrix_transpose = matrix.T

final_mark = np.dot(vector,matrix_transpose)
final_mark = final_mark.T

final_mark=list(final_mark)

print(final_mark)

x = filtered_customer_list.iloc[:, 0]
x = pd.DataFrame([x]).T
x['Points'] = final_mark
x

x_final = x.sort_values(by=['Points'], inplace=False, ascending=False)
print(x_final)

final_list = x_final.head(3)
final_list