from gen_closed import GenClosed as gen
from json_to_pandas import WeatherFrame as WF
import fetch_active
import pandas as pd
import datetime

current_year = datetime.datetime.now().year
years = list(range(1990, current_year + 1))

dataframe_list =[]
for x in years:
    url ='http://www.nhc.noaa.gov/gis/archive_besttrack_results.php?year='+ str(x)
    weather_df = gen.generate_closed_storms(url)
    #print(weather_df)
    dataframe_list.append(weather_df)
    
dataframe_list= pd.concat(dataframe_list)

print(dataframe_list)