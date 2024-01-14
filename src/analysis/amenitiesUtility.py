"""
    This utility script is used for analysis of amenities available for all listings

    Input:
        None

    Output:
        None

    Usage:
        - No direct usage 
        - Internally used by 'analyzeAmenities.py' script
"""

# Importing the required libraries
import os, sys
from pathlib import Path
from pyspark.sql import SparkSession, functions, types
from math import sin, cos, sqrt, atan2, radians

# Spark configurations
spark = SparkSession.builder.appName('Spark Amenities Analysis Utility').getOrCreate()
spark.sparkContext.setLogLevel('WARN')
sc = spark.sparkContext

# Function to calculate the total number of amenities for all listings
@functions.udf(returnType=types.IntegerType())
def no_Of_Amenities(amenity_list):

    amenities_cleaned = amenity_list.replace("[" , "")
    amenities_cleaned = amenities_cleaned.replace("]" , "")
    amenities_list = amenities_cleaned.split(",")
    num_ameneties = len(amenities_list)

    return num_ameneties

# Function to calculate the number of essential amenities out of the total amenities available
@functions.udf(returnType=types.IntegerType())
def essential_Amenities(amenity_list):

    essential = ['heat' , 'washer' , 'dryer' , 'wifi' , 'fan' , 'alarm' , 'hot water' , 'workspace' , 'dishes and silverware' , 'microwave']
    amenities_cleaned = amenity_list.replace("[" , "")
    amenities_cleaned = amenities_cleaned.replace("]" , "")
    
    essential_Count = 0
    
    for amenity in essential:
        
        if amenity in amenities_cleaned.lower():
            essential_Count += 1

    return essential_Count
