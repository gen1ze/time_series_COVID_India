import requests
from bs4 import BeautifulSoup
import ast
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import datetime as dt

URL = 'https://api.covid19india.org/data.json' 

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}

page = requests.get(URL,headers=headers)

soup = BeautifulSoup(page.content,'html.parser')
new_soup = ast.literal_eval(soup.get_text())  # to get dictionary

cts = new_soup['cases_time_series'] # cst is a list of dictionary
sw = new_soup['statewise']
tested = new_soup['tested']

daily_confirmed = []
daily_deceased = []
daily_recovered = []
total_confirmed = []
total_deceased = []
total_recovered = []
date = []
i = 0
while i < len(cts) :
    daily_confirmed.append(int(cts[i]['dailyconfirmed']))
    daily_deceased.append(int(cts[i]['dailydeceased']))
    daily_recovered.append(int(cts[i]['dailyrecovered']))
    total_confirmed.append(int(cts[i]['totalconfirmed']))
    total_deceased.append(int(cts[i]['totaldeceased']))
    total_recovered.append(int(cts[i]['totalrecovered']))
    date.append(cts[i]['date'])
    i += 1
start_date = dt.datetime(2020, 1, 30).date()
end_date = dt.datetime.now().date()
days = mdates.drange(start_date, end_date, dt.timedelta(days = 1))

plt.figure(1)
ax = plt.axes()
ax.set_facecolor('black')
plt.title('cumulative_data strting from jan 30')
plt.plot( days, total_confirmed, color = 'orange',label = 'total confirmed cases upto that date' )
plt.plot( days, total_recovered, color = 'green', label = 'total recovered cases upto that date ' )
plt.plot( days, total_deceased, color = 'red',label = 'total deceased cases upto that date' )
plt.legend()
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.xlim(start_date, end_date)
plt.gcf().autofmt_xdate()


plt.figure(2)
ax = plt.axes()
ax.set_facecolor('black')
plt.title('daily_data starting from jan 30 ')
plt.plot(days, daily_confirmed, color = 'orange', label = 'confirmed cases on that date')
plt.plot(days, daily_recovered, color = 'green', label = 'recovered cases on that date')
plt.plot(days, daily_deceased, color = 'red', label = 'deceased cases on that date')
plt.legend()
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate()
plt.show()


