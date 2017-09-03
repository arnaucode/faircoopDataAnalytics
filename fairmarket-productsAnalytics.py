# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import mpld3
from mpld3 import plugins, utils

from datetime import datetime, date, timedelta

products = pd.read_csv('datasets/fairMarket-products.csv')

#print products.tail(1)

#generate the full set of days from the first date to the last in the dataset
months = []
days = []
dInit = date(2015, 5, 04)
dEnd = date(2017, 8, 31)
delta = dEnd - dInit
for i in range(delta.days+1):
    day = dInit + timedelta(days=i)
    dayString = day.strftime("%d/%m/%y")
    dayDatetime = datetime.strptime(dayString, '%d/%m/%y')
    days.append(dayDatetime)

#add the dates of products creation to the days array
for productDate in products['Creado en']:
    if isinstance(productDate, basestring):
        productDay = str.split(productDate)[0]
        productDayDatetime = datetime.strptime(productDay, '%d/%m/%y')
        days.append(productDayDatetime)

#count days frequency in days array
unique, counts = np.unique(days, return_counts=True)
countDays = dict(zip(unique, counts))
realCounts = []
for count in counts:
    realCounts.append(count-1)

#count the total acumulation of products created in each days
totalCount = 0
globalCount = []
for k in realCounts:
    totalCount = totalCount + k
    globalCount.append(totalCount)

dates = countDays.values()
counts = countDays.values()

#plot the data
plt.title("New products published each day")
plt.plot(unique, realCounts)
plt.show()

plt.title("Total products in FairMarket each day")
plt.plot(unique, globalCount)
plt.show()

plt.title("New products and total products each day")
plt.plot(unique, realCounts, label="new products offered each day")
plt.plot(unique, globalCount, label="total products in FairMarket each day")
plt.legend(loc='upper left')
plt.show()




# now, product categories analytics
categories = []
for category in products["Categoría pública/Display Name"]:
    if isinstance(category, basestring):
        categories.append(category)

categoriesNames, categoriesCount = np.unique(categories, return_counts=True)
plt.title("Products categories")
plt.pie(categoriesCount, labels=categoriesNames, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
mpld3.show()
