
"""
Load Python variables from Javascript

Variables to load:
customer_budget
customer_home_preference
point_list

"""

from pyodide.http import open_url
from js import budget
from js import bedrooms
from js import pref_list
from js import window
from js import alert

import pandas as pd
import numpy as np
df= pd.read_csv(open_url("https://raw.githubusercontent.com/alechokcl/findmyborough-dataframe/main/dataframe.csv"))

df.rename(columns={'green_space': 'Number of Green Spaces', 'travel_bank': 'Travel Time to Bank Station', 'safety': 'Safety','school_density':'Number of Schools', 
                   'pub_number':'Number of Pubs', 'well_being_score':'Well Being Score','restaurant_number':'Number of Restaurants'}, inplace=True)


# convert pref_list items from integers to strings

pref_list = pref_list.split(",")

customer_budget = int(budget)
customer_home_preference = int(bedrooms)
point_list = pref_list

# error handling for missing variables
if customer_budget is None:
  window.location.href = "budget.html"

if customer_home_preference is None:
  window.location.href = "budget.html"

if point_list is None:
  window.location.href = "rank-points.html"

print(type(pref_list))

#checking whether entered budget is bigger than or equal to minimum average budget. If not asking user to enter their total budget for a house again.
checker = True

  if customer_home_preference == 1:
    if customer_budget < df['rent_per_month_1bed'].min():
      checker = True
      alert("Your budget is too low. Please enter a higher budget (total budget not per room)!")
      window.location.href = "budget.html"
    else:
      checker = False
      break

  elif customer_home_preference == 2:   
    if customer_budget < df['rent_per_month_2bed'].min():
      checker = True
      alert("Your budget is too low. Please enter a higher budget (total budget not per room)!")
      window.location.href = "budget.html"
    else:
      checker = False
      break

  elif customer_home_preference == 3:
    if customer_budget < df['rent_per_month_3bed'].min():
      checker = True
      alert("Your budget is too low. Please enter a higher budget (total budget not per room)!")
      window.location.href = "budget.html"
    else:
      checker = False
      break

  elif customer_home_preference == 4:
    if customer_budget < df['rent_per_month_4bed'].min():
      checker = True
      alert("Your budget is too low. Please enter a higher budget (total budget not per room)!")
      window.location.href = "budget.html"
    else:
      checker = False
      break

#filtering the boroughs according to their average rent to match with user's budget
if customer_home_preference == 1:
  df2=df.drop(["rent_per_month_2bed"], axis = 1)
  df2=df2.drop(["rent_per_month_3bed"], axis = 1)
  df2=df2.drop(["rent_per_month_4bed"], axis = 1)
elif customer_home_preference == 2:
  df2=df.drop(["rent_per_month_1bed"], axis = 1)
  df2=df2.drop(["rent_per_month_3bed"], axis = 1)
  df2=df2.drop(["rent_per_month_4bed"], axis = 1)
elif customer_home_preference == 3:
  df2=df.drop(["rent_per_month_1bed"], axis = 1)
  df2=df2.drop(["rent_per_month_2bed"], axis = 1)
  df2=df2.drop(["rent_per_month_4bed"], axis = 1)
elif customer_home_preference == 4:
  df2=df.drop(["rent_per_month_1bed"], axis = 1)
  df2=df2.drop(["rent_per_month_2bed"], axis = 1)
  df2=df2.drop(["rent_per_month_3bed"], axis = 1)

#customer_budget = int(input("Please enter your budget:"))

if customer_home_preference == 1:
  filtered_customer_list = df2.loc[(df2['rent_per_month_1bed'] <= customer_budget)]

elif customer_home_preference == 2:
  filtered_customer_list = df2.loc[(df2['rent_per_month_2bed'] <= customer_budget)]

elif customer_home_preference == 3:
  filtered_customer_list = df2.loc[(df2['rent_per_month_3bed'] <= customer_budget)]

elif customer_home_preference == 4:
  filtered_customer_list = df2.loc[(df2['rent_per_month_4bed'] <= customer_budget)]

#creating a list with column names 
columns = df2.columns
columns = list(columns)

#Dropping all the columns other than variable columns
columns.remove('Borough')
if customer_home_preference == 1:
  columns.remove('rent_per_month_1bed')

elif customer_home_preference == 2:
  columns.remove('rent_per_month_2bed')

elif customer_home_preference == 3:
  columns.remove('rent_per_month_3bed')

elif customer_home_preference == 4:
  columns.remove('rent_per_month_4bed')

'''print('Rate between 1 and 5 how important each of the following variables are for your accomodation (1 = not important and 5 = being essential')
for i in range (len(columns)):
  added_word = columns[i]
  added_word = str(added_word)
  customer_ranking = input("Please enter your point for " + added_word + ": ")
  point_list.append(customer_ranking)'''

new_matrix = filtered_customer_list[['Number of Green Spaces','Travel Time to Bank Station','Safety','Number of Schools','Number of Pubs','Well Being Score','Number of Restaurants']]
new_matrix.to_numpy()

vector = np.array(point_list,dtype=float)
matrix = np.array(new_matrix,dtype=float)

matrix_transpose = matrix.T
final_mark = np.dot(vector,matrix_transpose)
final_mark = final_mark.T
final_mark=list(final_mark)


x = filtered_customer_list.iloc[:, 0]
x = pd.DataFrame([x]).T
x['Points'] = final_mark
x_final = x.sort_values(by=['Points'], inplace=False, ascending=False)
final_list = x_final.head(3)
final_list = final_list.iloc[:,0:1]
final_list = final_list.values.tolist()

empty_list = []
for i in range(0,3):
  for j in range(0,1):
    final_result = final_list[i][j]
    empty_list.append(final_result)

#print("Top borough to live according to your choices :")

#for i in range(0,1):
  #print(empty_list[i])

borough = empty_list[0]

from js import window

if borough == "Barking and Dagenham":
  window.location.href = "boroughs/barking.html"

if borough == "Barnet":
  window.location.href = "boroughs/barnet.html"

if borough == "Bexley":
  window.location.href = "boroughs/bexley.html"

if borough == "Brent":
  window.location.href = "boroughs/brent.html"

if borough == "Bromley":
  window.location.href = "boroughs/bromley.html"

if borough == "Camden":
  window.location.href = "boroughs/camden.html"

if borough == "City of London":
  window.location.href = "boroughs/city.html"

if borough == "Croydon":
  window.location.href = "boroughs/croydon.html"

if borough == "Ealing":
  window.location.href = "boroughs/ealing.html"

if borough == "Enfield":
  window.location.href = "boroughs/enfield.html"

if borough == "Greenwich":
  window.location.href = "boroughs/greenwich.html"

if borough == "Hackney":
  window.location.href = "boroughs/hackney.html"

if borough == "Hammersmith and Fulham":
  window.location.href = "boroughs/hammersmith.html"

if borough == "Haringey":
  window.location.href = "boroughs/haringey.html"

if borough == "Harrow":
  window.location.href = "boroughs/harrow.html"

if borough == "Havering":
  window.location.href = "boroughs/havering.html"

if borough == "Hillingdon":
  window.location.href = "boroughs/hillingdon.html"

if borough == "Hounslow":
  window.location.href = "boroughs/hounslow.html"

if borough == "Islington":
  window.location.href = "boroughs/islington.html"

if borough == "Kensington and Chelsea":
  window.location.href = "boroughs/kensington.html"

if borough == "Kingston upon Thames":
  window.location.href = "boroughs/kingston.html"

if borough == "Lambeth":
  window.location.href = "boroughs/lambeth.html"

if borough == "Lewisham":
  window.location.href = "boroughs/lewisham.html"

if borough == "Merton":
  window.location.href = "boroughs/merton.html"

if borough == "Newham":
  window.location.href = "boroughs/newham.html"

if borough == "Redbridge":
  window.location.href = "boroughs/redbridge.html"

if borough == "Richmond upon Thames":
  window.location.href = "boroughs/richmond.html"

if borough == "Southwark":
  window.location.href = "boroughs/southwark.html"

if borough == "Sutton":
  window.location.href = "boroughs/sutton.html"

if borough == "Tower Hamlets":
  window.location.href = "boroughs/tower.html"

if borough == "Waltham Forest":
  window.location.href = "boroughs/waltham.html"

if borough == "Wandsworth":
  window.location.href = "boroughs/wandsworth.html"

if borough == "Westminster":
  window.location.href = "boroughs/westminster.html"

