# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta

shops = pd.read_csv('datasets/fairMarket-shops.csv')

print shops.tail(1)

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

#add the dates of shops creation to the days array
for shopDate in shops['Created on']:
    if isinstance(shopDate, basestring):
        shopDay = str.split(shopDate)[0]
        shopDayDatetime = datetime.strptime(shopDay, '%d/%m/%y')
        days.append(shopDayDatetime)

#count days frequency in days array
unique, counts = np.unique(days, return_counts=True)
countDays = dict(zip(unique, counts))
realCounts = []
for count in counts:
    realCounts.append(count-1)

#count the total acumulation of shops created in each days
totalCount = 0
globalCount = []
for k in realCounts:
    totalCount = totalCount + k
    globalCount.append(totalCount)

dates = countDays.values()
counts = countDays.values()

#plot the data
plt.title("New shops opened each day")
plt.plot(unique, realCounts)
plt.show()

plt.title("Total shops each day")
plt.plot(unique, globalCount)
plt.show()

plt.title("New shops and total shops each day")
plt.plot(unique, realCounts, label="new shops opened each day")
plt.plot(unique, globalCount, label="total shops each day")
plt.legend(loc='upper left')
plt.show()
