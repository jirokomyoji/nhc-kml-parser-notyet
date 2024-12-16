from gen_closed import GenClosed as gen

import fetch_active




years= [2020,2021,2022,2023,2024]


for x in years:
    url ='http://www.nhc.noaa.gov/gis/archive_besttrack_results.php?year='+ str(x)
    gen.generate_closed_storms(url)