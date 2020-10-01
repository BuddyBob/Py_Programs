 
import urllib.request
import datetime
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
urllib.request.urlretrieve(url, filename="time_series_covid19_deaths_global.csv")
