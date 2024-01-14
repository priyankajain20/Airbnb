"""
    - This script acts as a helper script for the 'dataCleaning.py' file

    - It contains all the User Defined Functions (UDFs) for cleaning and processing the data

    Input:
        None

    Output:
        None
    
    Usage:
        - No direct usage
        - Internally used by 'dataCleaning.py' script
"""

# Importing the required libraries
from pyspark.sql import SparkSession, functions, types
import math

# Function to clean the 'bed' column data
@functions.udf(returnType=types.FloatType())
def get_Beds(beds, acc):
	if beds is not None:
		beds = float(beds)
	else:
		acc = float(acc)
		beds = acc/2
	return beds

# Function to process the number of bathrooms from 'bathroom text'
@functions.udf(returnType=types.FloatType())
def bath_count(bathrooms_text):
	if bathrooms_text is not None:
		list = bathrooms_text.split(' ')
		if list[0].replace('.','',1).isdigit():
			num = float(list[0])
		else:
			num = 1.0
		return num
	else:
		return 1.0  

# Function to convert the price from string to float data type
@functions.udf(returnType=types.FloatType())
def price_Numeric(price):
    price = price.replace('$' , '')
    price = price.replace(',', '')
    return float(price) 

# Function to encode true/false values to 0/1
@functions.udf(returnType=types.IntegerType())
def tf_changer(entry):
	if entry is not None:
		if entry =='f':
			return 0
		else:
			return 1
	else:
		return 0

# Function to replace nulls with zero in 'bedroom' column
@functions.udf(returnType=types.FloatType())
def null_Converter(bedroom):
	if  bedroom is not None:
		bed = float(bedroom)
		return bed
	else:
		bed = 0.0
		return bed

# Function to process the license column
@functions.udf(returnType=types.IntegerType())
def license_Converter(License):
	if License is not None:
		binary = 1
		return binary
	else:
		binary = 0
		return binary

# Function to fill the empty values in 'review' related columns
@functions.udf(returnType=types.FloatType())
def return_Review(review):
	if review is not None:
		return float(review)
	else:
		return 0.0

# Function to generalize several property types into few distinct ones
@functions.udf(returnType=types.StringType())
def update_Property_Types(property):
    if property.lower() in ['entire condo', 'private room in condo', 'shared room in condo']:
        property = 'Condo'
        return property
    elif property.lower() in ['entire rental unit', 'entire place', \
                        'shared room in rental unit', 'entire timeshare']:
        property = 'Rental Unit'
        return property
    elif property.lower() in ['entire guest suite', 'entire guesthouse', 'private room in guest suite', \
                             'private room in guesthouse']:
        property = 'Guesthouse'
        return property
    elif property.lower() in ['entire home', 'entire serviced apartment', 'tiny home', \
                             'shared room in serviced apartment']:
        property = 'Home'
        return property
    elif property.lower() in ['entire townhouse', 'private room in townhouse', 'entire bungalow']:
        property = 'Townhouse'
        return property
    elif property.lower() in ['private room in home', 'private room in rental unit', 'private room in villa', 'room in boutique hotel', 'private room in bed and breakfast', 'room in aparthotel', 'private room in serviced apartment', 'room in bed and breakfast', 'private room in bungalow', 'private room in loft', 'private room in boat', 'private room in tiny home', 'private room in vacation home', 'room in hotel', 'private room in resort', 'private room in hostel', 'private room in camper/rv']:
        property = 'Private Room'
        return property
    else:
        property = 'Others'
        return property
