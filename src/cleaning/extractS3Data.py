"""
    - This script is used to extract the data from S3 to local machine

    - The data is then utilized for cleaning and analytical purposes

    Input:
        City name
    
    Output:
        File downloaded to local machine

    Usage:
        python3 extractS3Data.py <city-name>

    Example:
        python3 extractS3Data.py vancouver

"""

# Importing the required libraries
import os
import sys
import boto3
import botocore
from configparser import ConfigParser

# Creating a 'config' object to access the config file
config_object = ConfigParser()
config_object.read('../utils/config.ini')

# Searching for the required user in the config file
user = config_object['AWSCONSOLE']

# Fetching all the required details
ACCESS = user['ACCESS_KEY']
SECRET = user['SECRET_KEY']
BUCKET = user['BUCKET_NAME']
REGION = user['BUCKET_REGION']

# Main function
def main(input):

    # Creating a 'boto' session connection
    session = boto3.Session(
        aws_access_key_id=ACCESS,
        aws_secret_access_key=SECRET,
        region_name=REGION
    )

    # Setting the resource and bucket name
    s3 = session.resource('s3')
    bucket = s3.Bucket(BUCKET)

    # Downloading the required file
    file_to_downloaded = ["%s/%s_listing_detail.csv" % (input, input)]
    for fileObject in bucket.objects.all():
        file_name = str(fileObject.key)
        if file_name in file_to_downloaded:
            bucket.download_file(file_name, '../../extractedData/%s/%s_listing_detail.csv' % (input, input))
    
if __name__ == '__main__':

    # Setting the input argument as city name
    city = str(sys.argv[1])

    # For Vancouver
    if city.lower() == 'vancouver':
        main('vancouver')
    
    # For Toronto
    elif city.lower() == 'toronto':
        main('toronto')
