"""
    - This is a utility script to calculate distances between an Airbnb
        listing and an educational institute
    
    - This script has a User Defined Function (UDF) to calculate the required distance
    
    Input:
        None
    
    Output:
        None
    
    Usage:
        - No direct usage
        - Internally used by 'calculateDistance.py' script
"""

# Importing the required libraries
import os, sys
from pathlib import Path
from pyspark.sql import SparkSession, functions, types
from math import sin, cos, sqrt, atan2, radians

# Spark configurations
spark = SparkSession.builder.appName('Spark Distance Analysis Utility').getOrCreate()
spark.sparkContext.setLogLevel('WARN')
sc = spark.sparkContext

# Importing the 'constants' file
sc.addFile('../utils/constants.py')
import constants as constants

# Function to calculate distance between an Airbnb listing and an educational institute
@functions.udf(returnType=types.FloatType())
def calculate_Distance(listing_latitude, listing_longitude, institute_latitude, institute_longitude):
    
    institute_location = [institute_latitude, institute_longitude]
    
    lat1 = radians(institute_location[0])
    lon1 = radians(institute_location[1])
    lat2 = radians(float(listing_latitude))
    lon2 = radians(float(listing_longitude))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = constants.EARTH_RADIUS * c

    return round(distance, 2)
