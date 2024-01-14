"""
    - This script is used to clean the raw data

    - Internally uses several User Defined Functions (UDFs) available from 'cleaningUtility.py'

    - The data is cleaned and saved as '.csv' for further analysis and processing

    Input:
        City name
    
    Output:
        Cleaned data in '.csv' format

    Usage:
        spark-submit dataCleaning.py <city-name>

    Example:
        spark-submit dataCleaning.py vancouver

"""

# Importing the required libraries
import os
import sys
import math
import cleaningUtility as udf
from pyspark.sql import SparkSession, functions, types

# Spark configurations
spark = SparkSession.builder.appName('Spark Data Cleaning').getOrCreate()
spark.sparkContext.setLogLevel('WARN')
sc = spark.sparkContext

# Making sure we have Python 3.5+
assert sys.version_info >= (3, 5) 

# Making sure we have Spark 3.0+
assert spark.version >= '3.0' 

# Main function        
def main(inputs):

    # Setting the input file name to be read by Spark
    file = 'extractedData/' + input + '/' + input + '_listing_detail.csv'
   
    # Reading the input data
    listings = spark.read.option("multiline", "true"). \
                option("quote", '"'). \
                option("header", "true"). \
                option("escape", "\\"). \
                option("escape", '"'). \
                csv(file). \
                repartition(50)

    # Dropping the unnecessary columns and caching the selected data
    listings = listings.drop('Listing_url' , 'Scrape_id' , 'last_scraped' , 'Source' , 'Neighborhood_overview' ,
                             'picture_url' , 'Host_url'  , 'Host_location' , 'Host_about' , 'Host_response_time',
                             'Host_response_rate' , 'Host_acceptance_rate' , 'Host_thumbnail_url' , 'Host_picture_url' , 'Host_neighbourhood',
                             'Host_listings_count' , 'Host_total_listings_count' , 'Host_verifications' , 'Host_has_profile_pic' , 'Host_identity_verified',
                             'Neighbourhood' , 'Neighbourhood_group_cleansed' , 'Bathrooms' , 'Calendar_updated' , 'Has_availability'
                             'Availability_30' , 'Availability_60' , 'Availability_90' , 'Calendar_last_scraped' , 'Number_of_reviews_ltm' ,
                             'Number_of_reviews_l30d' , 'First_review' , 'Last_review' , 'Calculated_host_listings_count_shared_rooms' ,
                             'Calculated_host_listings_count_private_rooms', 'Calculated_host_listings_count_entire_homes' , 'Reviews_per_month',
                             'Calculated_host_listings_count').cache()
    
    # Processing the 'bath' column
    listings = listings.withColumn('baths', udf.bath_count(listings['bathrooms_text']))

    # Dropping the column after processing and cleaning
    listings = listings.drop('bathrooms_text')

    # Cleaning the 'beds' column
    listings = listings.withColumn('beds', udf.get_Beds(listings['beds'],listings['accommodates']))

    # Cleaning the 'price' column
    listings = listings.withColumn('price',udf.price_Numeric(listings['price']))

    # Cleaning the 'availability' column
    listings = listings.withColumn('has_availability',udf.tf_changer(listings['has_availability']))

    # Cleaning the 'host_is_superhost' column
    listings = listings.withColumn('host_is_superhost',udf.tf_changer(listings['host_is_superhost']))

    # Cleaning the 'instant_bookable' column
    listings = listings.withColumn('instant_bookable',udf.tf_changer(listings['instant_bookable']))

    # Cleaning the 'bedrooms' column
    listings = listings.withColumn('bedrooms',udf.null_Converter(listings['bedrooms']))

    # Cleaning the 'license' column
    listings = listings.withColumn('license',udf.license_Converter(listings['license']))

    # Cleaning the 'review_scores_rating' column
    listings = listings.withColumn('review_scores_rating', udf.return_Review(listings['review_scores_rating']))

    # Cleaning the 'license' column
    listings = listings.withColumn('review_scores_cleanliness', udf.return_Review(listings['review_scores_cleanliness']))

    # Cleaning the 'review_scores_cleanliness' column
    listings = listings.withColumn('review_scores_checkin', udf.return_Review(listings['review_scores_checkin']))

    # Cleaning the 'review_scores_communication' column
    listings = listings.withColumn('review_scores_communication', udf.return_Review(listings['review_scores_communication']))

    # Cleaning the 'review_scores_location' column
    listings = listings.withColumn('review_scores_location', udf.return_Review(listings['review_scores_location']))

    # Cleaning the 'review_scores_value' column
    listings = listings.withColumn('review_scores_value', udf.return_Review(listings['review_scores_value']))

    # Cleaning the 'property_type' column
    listings = listings.withColumn('property_type', udf.update_Property_Types(listings['property_type']))

    # Saving the clean and processed data as a '.csv' file for further analysis
    listings.coalesce(1).write.option("quote", '"'). \
                option("header", "true"). \
                option("escape", "\\"). \
                option("escape", '"'). \
                csv('cleanData/%s/' % input,mode='overwrite')

    # Renaming the file to a specific, meaningful name for ease of use later on
    # directory = 'cleanData/%s/' % input
    # for file in os.listdir(directory):
    #     if file.endswith('.csv'):
    #         temp = file
    #         break

    # os.rename(directory + temp, directory + '%s_listing_clean.csv' % input)

if __name__ == '__main__':
    
    # Setting the input argument for city name
    input = str(sys.argv[1])

    # Calling the main function for Vancouver
    if input == 'vancouver':
        main('vancouver')
    
    # Calling the main function for Toronto
    elif input == 'toronto':
        main('toronto')
