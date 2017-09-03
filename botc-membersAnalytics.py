# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta

members = pd.read_csv('datasets/BotC.csv')

print members.head(1)

#generate the full set of days from the first date to the last in the dataset
months = []
days = []
dInit = date(2017, 6, 8)
dEnd = date(2017, 1, 9)
delta = dEnd - dInit
for i in range(delta.days+1):
    day = dInit + timedelta(days=i)
    dayString = day.strftime("%d/%m/%y")
    dayDatetime = datetime.strptime(dayString, '%d/%m/%y')
    days.append(dayDatetime)

#add the dates of shops creation to the days array
for memberDate in members['Date']:
    if isinstance(memberDate, basestring):
        memberDay = memberDate
        memberDayDatetime = datetime.strptime(memberDay, '%B %d, %Y')
        days.append(memberDayDatetime)

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
plt.title("New members registered each day")
plt.plot(unique, realCounts)
plt.show()

plt.title("Total members each day")
plt.plot(unique, globalCount)
plt.show()

plt.title("New members and total members each day")
plt.plot(unique, realCounts, label="new members registered each day")
plt.plot(unique, globalCount, label="total members each day")
plt.legend(loc='upper left')
plt.show()


# place of the account
places = []
for place in members["Place"]:
    if isinstance(place, basestring):
        places.append(place)

placesNames, placesCount = np.unique(places, return_counts=True)
plt.title("Membership places")
plt.pie(placesCount, labels=placesNames, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()
