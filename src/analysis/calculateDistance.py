"""
    - This script is used to calculate distances between an Airbnb listing
        and an educational institute
    
    - Purpose of this analysis is to help students find nearest Airbnb 
        listings from the institute

    Input:
        City name
    
    Output:
        Processed data in '.csv' format
    
    Usage:
        spark-submit calculateDistance.py <city-name>
    
    Example:
        spark-submit calculateDistance.py vancouver

"""

# Importing the required libraries
import os
import sys
import distanceUtility as udf
from pathlib import Path
from math import sin, cos, sqrt, atan2, radians
from pyspark.sql import SparkSession, functions, types
from pyspark.sql.functions import lit

# Spark configurations
spark = SparkSession.builder.appName('Spark Distance Analysis').getOrCreate()
spark.sparkContext.setLogLevel('WARN')
sc = spark.sparkContext

# Importing 'constants' file
sc.addFile('../utils/constants.py')
import constants as constants

# Making sure we have Python 3.5+
assert sys.version_info >= (3, 5)

# Making sure we have Spark 3.0+
assert spark.version >= '3.0' 

# Main function
def main(input):

    # Setting the input file name to be read by spark
    file = 'cleanData/' + input + '/' + input + '_listing_clean.csv'

    # Reading the input data
    listings = spark.read.option("multiline", "true"). \
                option("quote", '"'). \
                option("header", "true"). \
                option("escape", "\\"). \
                option("escape", '"'). \
                csv(file). \
                repartition(50).cache()

    # Calculating distances for educational institutes in Vancouver
    if input == 'vancouver':
        listings = listings.withColumn('distance_SFU', udf.calculate_Distance(listings['latitude'] , listings['longitude'], lit(constants.VAN_SFU_LAT), lit(constants.VAN_SFU_LON)))
        listings = listings.withColumn('distance_BCIT', udf.calculate_Distance(listings['latitude'] , listings['longitude'], lit(constants.VAN_BCIT_LAT), lit(constants.VAN_BCIT_LON)))
        listings = listings.withColumn('distance_UBC', udf.calculate_Distance(listings['latitude'] , listings['longitude'], lit(constants.VAN_UBC_LAT), lit(constants.VAN_UBC_LON)))
        listings = listings.withColumn('distance_Langara', udf.calculate_Distance(listings['latitude'] , listings['longitude'], lit(constants.VAN_LAN_LAT), lit(constants.VAN_LAN_LON)))
        listings = listings.withColumn('distance_VCC', udf.calculate_Distance(listings['latitude'] , listings['longitude'], lit(constants.VAN_VCC_LAT), lit(constants.VAN_VCC_LON)))
        listings = listings.withColumn('distance_Columbia_College', udf.calculate_Distance(listings['latitude'] , listings['longitude'], lit(constants.VAN_COL_LAT), lit(constants.VAN_COL_LON)))
        listings = listings.withColumn('distance_UCW', udf.calculate_Distance(listings['latitude'] , listings['longitude'], lit(constants.VAN_UCW_LAT), lit(constants.VAN_UCW_LON)))

    # Calculating distances for educational institutes in Toronto
    elif input == 'toronto':
        listings = listings.withColumn('distance_UOT', udf.calculate_Distance(listings['latitude'] , listings['longitude'], lit(constants.TOR_UOT_LAT), lit(constants.TOR_UOT_LON)))
        listings = listings.withColumn('distance_YORK', udf.calculate_Distance(listings['latitude'] , listings['longitude'], lit(constants.TOR_YU_LAT), lit(constants.TOR_YU_LON)))
        listings = listings.withColumn('distance_HUMBER', udf.calculate_Distance(listings['latitude'] , listings['longitude'], lit(constants.TOR_HUM_LAT), lit(constants.TOR_HUM_LON)))
        listings = listings.withColumn('distance_GBC', udf.calculate_Distance(listings['latitude'] , listings['longitude'], lit(constants.TOR_GBC_LAT), lit(constants.TOR_GBC_LON)))
        listings = listings.withColumn('distance_VICTORIA', udf.calculate_Distance(listings['latitude'] , listings['longitude'], lit(constants.TOR_VU_LAT), lit(constants.TOR_VU_LON)))

    # Saving the processed data as a '.csv' file for further analysis
    listings.coalesce(1).write. \
            option("quote", '"'). \
            option("header", "true"). \
            option("escape", "\\"). \
            option("escape", '"'). \
            csv('processedData/%s/' % input, mode='overwrite')

    # Renaming the file to a specific, meaningful name for ease of use later on
    # directory = '../../processedData/%s/' % input
    # for file in os.listdir(directory):
    #     if file.endswith('.csv'):
    #         temp = file
    #         break

    # os.rename(directory + temp, directory + '%s_distances_calculated.csv' % input)

if __name__ == '__main__':

    # Setting the input argument as city name
    input = str(sys.argv[1])

    # For Vancouver
    if input.lower() == 'vancouver':
        main('vancouver')

    # For Toronto
    elif input.lower() == 'toronto':
        main('toronto')
