from gen_closed import GenClosed as gen
from json_to_pandas import WeatherFrame as WF
import fetch_active
import pandas as pd
import datetime
import json
import os
import pytz
import requests
import sys

current_year = datetime.datetime.now().year
years = list(range(1990, current_year + 1))

dataframe_list =[]
for x in years:
    try:
        url ='http://www.nhc.noaa.gov/gis/archive_besttrack_results.php?year='+ str(x)
        weather_df = gen.generate_closed_storms(url)
        #print(weather_df)
        dataframe_list.append(weather_df)
    except Exception as e:
        print(e)
        continue
    
combined_df = pd.concat(dataframe_list, ignore_index=True)
CUR_DIR = os.path.dirname(os.path.realpath('output'))
filename = 'stormdata.xlsx' 
print ('Creating File: %s' % filename)
                
                # Write out file
#combined_df = pd.concat(dataframe_list, ignore_index=True)

# Write to Excel
filepath = os.path.join(CUR_DIR, 'output', filename)
combined_df.to_excel(filepath, index=False)
#pd.ExcelWriter(filepath,dataframe_list)
print(dataframe_list)