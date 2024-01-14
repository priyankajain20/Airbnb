"""
    - This script is used to analyze the amenities available for every Airbnb listing

    - Internally calls 'amenitiesUtility' script to process data using User Defined Functions (UDFs)

    - The analysis will then be used to find out the availability of essential amenities

    - This data will be supplied to dashboards for visualization

    Input:
        City name
    
    Output:
        '.csv' file with analysis of amenities in the specified directory

    Usage:
        spark-submit analyzeAmenities.py <city-name>
    
    Example:
        spark-submit analyzeAmenities.py vancouver
"""

# Importing the required libraries
import os
import sys
import amenitiesUtility as udf
from collections import Counter
from pyspark.sql import SparkSession, functions , types

# Spark configurations
spark = SparkSession.builder.appName('Spark Amenities Analysis').getOrCreate()
spark.sparkContext.setLogLevel('WARN')
sc = spark.sparkContext

# Making sure we have Python 3.5+
assert sys.version_info >= (3, 5)

# Making sure we have Spark 3.0+
assert spark.version >= '3.0'

# Main function
def main(input):

    # Setting the input file name to be read by spark
    file = 'cleanData/' + input + '/' + input + '_listing_clean.csv'

    # Reading the input data
    city_Cleaned = spark.read.option("multiline", "true")\
            .option("quote", '"') \
            .option("header", "true") \
            .option("escape", "\\") \
            .option("escape", '"'). \
            csv(file).cache()
    
    # Calculating the total number of amenities available
    amenities = city_Cleaned.withColumn('amenities_value', udf.no_Of_Amenities(city_Cleaned['amenities']))

    # Calculating the number of essential amenities out of the total amenities available
    amenities = amenities.withColumn('essential_count', udf.essential_Amenities(amenities['amenities']))

    # Saving the final processed file with a '.csv' extension for further analysis
    amenities.coalesce(1).write. \
                option("quote", '"'). \
                option("header", "true"). \
                option("escape", "\\"). \
                option("escape", '"'). \
                csv('amenitiesData/%s/' % input, mode='overwrite')

    # Renaming the file to a specific, meaningful name for ease of use later on
    # directory = '../../amenitiesData/%s/' % input
    # for file in os.listdir(directory):
    #     if file.endswith('.csv'):
    #         temp = file
    #         break

    # os.rename(directory + temp, directory + '%s_amenities.csv' % input)

if __name__ == '__main__':

    # Setting the input argument as city name
    input = str(sys.argv[1])

    # For Vancouver
    if input.lower() == 'vancouver':
        main('vancouver')

    # For Toronto
    elif input.lower() == 'toronto':
        main('toronto')
