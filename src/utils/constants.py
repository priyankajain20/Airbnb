"""
    This script contains all the constants used in the Project

    Input:
        None

    Output:
        None
    
    Usage:
        - Supply values to several executable files
        - No direct usage / execution
"""

# Data download URL and specified directory to download data for Vancouver 
DATA_BASE_URL_VANCOUVER = "http://data.insideairbnb.com/canada/bc/vancouver/2022-09-10/"
DATA_DIRECTORY_VANCOUVER = "../../rawData/vancouver/"

# Data download URL and specified directory to download data for Toronto 
DATA_BASE_URL_TORONTO = "http://data.insideairbnb.com/canada/on/toronto/2022-09-07/"
DATA_DIRECTORY_TORONTO = "../../rawData/toronto/"

# Constants for all compressed files
LISTING_DETAILED = "listings.csv.gz"
CALENDAR_DETAILED = "calendar.csv.gz"
REVIEW_DETAILED = "reviews.csv.gz"

# Constants for all summary files
LISTING_SUMMARY = "listings.csv"
REVIEW_SUMMARY = "reviews.csv"

# Constants for Neighbourhood related data files
NEIGHBOURHOODS = "neighbourhoods.csv"
NEIGHBOURHOODS_GEO = "neighbourhoods.geojson"

# Radius of Earth in 'km' to calculate distances
EARTH_RADIUS = 6371

"""
    Latitudes and Longitudes for Educational Institutes in Vancouver
"""

# Simon Fraser University
VAN_SFU_LAT = 49.278
VAN_SFU_LON = -122.919

# British Columbia Institute of Technology
VAN_BCIT_LAT = 49.248
VAN_BCIT_LON = -123.001

# University of British Columbia
VAN_UBC_LAT = 49.260
VAN_UBC_LON = -123.245

# Langara College
VAN_LAN_LAT = 49.224
VAN_LAN_LON = -123.108

# Vancouver Community College
VAN_VCC_LAT = 49.281
VAN_VCC_LON = -123.110

# Columbia College
VAN_COL_LAT = 49.271
VAN_COL_LON = -123.094

# University Canada West
VAN_UCW_LAT = 49.275
VAN_UCW_LON = -123.130

"""
    Latitudes and Longitudes for Educational Institutes in Toronto
"""

# University of Toronto
TOR_UOT_LAT = 43.674
TOR_UOT_LON = -79.351

# York University
TOR_YU_LAT = 43.773
TOR_YU_LON = -79.501

# Humber College
TOR_HUM_LAT = 43.730
TOR_HUM_LON = -79.606

# George Brown College
TOR_GBC_LAT = 43.677
TOR_GBC_LON = -79.403

# Victoria University
TOR_VU_LAT = 43.667
TOR_VU_LON = -79.392
