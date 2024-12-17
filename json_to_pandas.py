from bs4 import BeautifulSoup 
import json
import os
import pytz
import requests
import sys
import xml.etree.ElementTree
import pandas as pd

class WeatherFrame(): 
    
    def get_dataframe(json_data):
        #print(json_data)
        if isinstance(json_data, str):
            try:
                json_data = json.loads(json_data)
                print("valid JSON string")
                df = pd.json_normalize(
                json_data['features'], 
                record_path=None,
                meta=[
                'properties.title',
                'properties.lat', 
                'properties.lng',
                'properties.storm_name',
                'properties.storm_number',
                'properties.basin',
                'properties.storm_type',
                'properties.intensity_mph',
                'properties.intensity_kph',
                'properties.pressure',
                'properties.datetime',
                ['geometry', 'type'],
                ['geometry', 'coordinates']
            ]
        )

                df = df[df['geometry.type'] == 'Point']
                #print(df)
                return df
            except json.JSONDecodeError:
                print("Invalid JSON string")
            return None
        
        

        
    
if __name__ == "__main__":
    pass