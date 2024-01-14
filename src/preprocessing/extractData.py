"""
    - This script is used to download the Airbnb data from web
    
    - The downloaded data will be saved in the 'rawData' directory

    Input:
        City name

    Output:
        Data downloaded in the specified directory
    
    Usage:
        python3 extractData.py <city-name>

    Example: 
        python3 extractData.py vancouver
"""

# Importing the required libraries
import os
import sys
import shutil
import importlib
import requests
from pathlib import Path

# Append system path to include 'constants'
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import constants

# Function to process information based on the input city
def collect_information(city):

    # Convert the city to lowercase    
    city = city.lower()
    
    # For Vancouver
    if city == "vancouver":
        prepare_directory("vancouver")
        download_data("vancouver")

    # For Toronto
    elif city == "toronto":
        prepare_directory("toronto")
        download_data("toronto")

# Function to create directories based on the input city
def prepare_directory(city):

    # For Vancouver
    if city == "vancouver":

        # If the directory already exists, delete all the contents of directory
        if os.path.exists(constants.DATA_DIRECTORY_VANCOUVER):
            shutil.rmtree(constants.DATA_DIRECTORY_VANCOUVER)
        
        # Make a new directory if there is no existing directory with the given name
        os.makedirs(constants.DATA_DIRECTORY_VANCOUVER, exist_ok=True)
    
    # For Toronto
    if city == "toronto":
        
        # If the directory already exists, delete all the contents of directory
        if os.path.exists(constants.DATA_DIRECTORY_TORONTO):
            shutil.rmtree(constants.DATA_DIRECTORY_TORONTO)
        
        # Make a new directory if there is no existing directory with the given name
        os.makedirs(constants.DATA_DIRECTORY_TORONTO, exist_ok=True)

# Function to download data from the Internet
def download_data(city):
    
    # For Vancouver
    if city == 'vancouver':

        print('Downloading the data for %s' % city.upper())
        
        print('\n--------------------------------------------------------------------------------\n')
        
        print('Downloading %s File ...' % constants.LISTING_DETAILED)
        
        # Downloading 'listing.csv.gz'
        target_file1 = os.path.join(constants.DATA_DIRECTORY_VANCOUVER, constants.LISTING_DETAILED)
        with requests.get(constants.DATA_BASE_URL_VANCOUVER + 'data/' + constants.LISTING_DETAILED, stream=True) as r:
            with open(target_file1, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Download Finished!')

        print('\n--------------------------------------------------------------------------------\n')

        print('Downloading %s File ...' % constants.LISTING_SUMMARY)
        
        # Downloading 'listing.csv'
        target_file2 = os.path.join(constants.DATA_DIRECTORY_VANCOUVER, constants.LISTING_SUMMARY)
        with requests.get(constants.DATA_BASE_URL_VANCOUVER + 'visualisations/' + constants.LISTING_SUMMARY, stream=True) as r:
            with open(target_file2, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Download Finished!')

        print('\n--------------------------------------------------------------------------------\n')

        print('Downloading %s File ...' % constants.CALENDAR_DETAILED)
        
        # Downloading 'calendar.csv.gz'
        target_file3 = os.path.join(constants.DATA_DIRECTORY_VANCOUVER, constants.CALENDAR_DETAILED)
        with requests.get(constants.DATA_BASE_URL_VANCOUVER + 'data/' + constants.CALENDAR_DETAILED, stream=True) as r:
            with open(target_file3, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Download Finished!')

        print('\n--------------------------------------------------------------------------------\n')

        print('Downloading %s File ...' % constants.REVIEW_DETAILED)
        
        # Downloading 'reviews.csv.gz'
        target_file4 = os.path.join(constants.DATA_DIRECTORY_VANCOUVER, constants.REVIEW_DETAILED)
        with requests.get(constants.DATA_BASE_URL_VANCOUVER + 'data/' + constants.REVIEW_DETAILED, stream=True) as r:
            with open(target_file4, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Download Finished!')

        print('\n--------------------------------------------------------------------------------\n')

        print('Downloading %s File ...' % constants.REVIEW_SUMMARY)
        
        # Downloading 'reviews.csv'
        target_file5 = os.path.join(constants.DATA_DIRECTORY_VANCOUVER, constants.REVIEW_SUMMARY)
        with requests.get(constants.DATA_BASE_URL_VANCOUVER + 'visualisations/' + constants.REVIEW_SUMMARY, stream=True) as r:
            with open(target_file5, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Download Finished!')

        print('\n--------------------------------------------------------------------------------\n')

        print('Downloading %s File ...' % constants.NEIGHBOURHOODS)
        
        # Downloading 'neighbourhoods.csv'
        target_file6 = os.path.join(constants.DATA_DIRECTORY_VANCOUVER, constants.NEIGHBOURHOODS)
        with requests.get(constants.DATA_BASE_URL_VANCOUVER + 'visualisations/' + constants.NEIGHBOURHOODS, stream=True) as r:
            with open(target_file6, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Download Finished!')

        print('\n--------------------------------------------------------------------------------\n')

        print('Downloading %s File ...' % constants.NEIGHBOURHOODS_GEO)
        
        # Downloading 'neighbourhoods.geojson'
        target_file7 = os.path.join(constants.DATA_DIRECTORY_VANCOUVER, constants.NEIGHBOURHOODS_GEO)
        with requests.get(constants.DATA_BASE_URL_VANCOUVER + 'visualisations/' + constants.NEIGHBOURHOODS_GEO, stream=True) as r:
            with open(target_file7, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Download Finished!')

        print('\n--------------------------------------------------------------------------------\n')

        print('Data download finished for %s' % city.upper())

    # For Toronto
    if city == 'toronto':

        print('Downloading the data for %s' % city.upper())
        
        print('\n--------------------------------------------------------------------------------\n')
        
        print('Downloading %s File ...' % constants.LISTING_DETAILED)
        
        # Downloading 'listing.csv.gz'
        target_file1 = os.path.join(constants.DATA_DIRECTORY_TORONTO, constants.LISTING_DETAILED)
        with requests.get(constants.DATA_BASE_URL_TORONTO + 'data/' + constants.LISTING_DETAILED, stream=True) as r:
            with open(target_file1, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Download Finished!')

        print('\n--------------------------------------------------------------------------------\n')

        print('Downloading %s File ...' % constants.LISTING_SUMMARY)
        
        # Downloading 'listing.csv'
        target_file2 = os.path.join(constants.DATA_DIRECTORY_TORONTO, constants.LISTING_SUMMARY)
        with requests.get(constants.DATA_BASE_URL_TORONTO + 'visualisations/' + constants.LISTING_SUMMARY, stream=True) as r:
            with open(target_file2, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Download Finished!')

        print('\n--------------------------------------------------------------------------------\n')

        print('Downloading %s File ...' % constants.CALENDAR_DETAILED)
        
        # Downloading 'calendar.csv.gz'
        target_file3 = os.path.join(constants.DATA_DIRECTORY_TORONTO, constants.CALENDAR_DETAILED)
        with requests.get(constants.DATA_BASE_URL_TORONTO + 'data/' + constants.CALENDAR_DETAILED, stream=True) as r:
            with open(target_file3, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Download Finished!')

        print('\n--------------------------------------------------------------------------------\n')

        print('Downloading %s File ...' % constants.REVIEW_DETAILED)
        
        # Downloading 'reviews.csv.gz'
        target_file4 = os.path.join(constants.DATA_DIRECTORY_TORONTO, constants.REVIEW_DETAILED)
        with requests.get(constants.DATA_BASE_URL_TORONTO + 'data/' + constants.REVIEW_DETAILED, stream=True) as r:
            with open(target_file4, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Download Finished!')

        print('\n--------------------------------------------------------------------------------\n')

        print('Downloading %s File ...' % constants.REVIEW_SUMMARY)
        
        # Downloading 'reviews.csv'
        target_file5 = os.path.join(constants.DATA_DIRECTORY_TORONTO, constants.REVIEW_SUMMARY)
        with requests.get(constants.DATA_BASE_URL_TORONTO + 'visualisations/' + constants.REVIEW_SUMMARY, stream=True) as r:
            with open(target_file5, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Download Finished!')

        print('\n--------------------------------------------------------------------------------\n')

        print('Downloading %s File ...' % constants.NEIGHBOURHOODS)
        
        # Downloading 'neighbourhoods.csv'
        target_file6 = os.path.join(constants.DATA_DIRECTORY_TORONTO, constants.NEIGHBOURHOODS)
        with requests.get(constants.DATA_BASE_URL_TORONTO + 'visualisations/' + constants.NEIGHBOURHOODS, stream=True) as r:
            with open(target_file6, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Download Finished!')

        print('\n--------------------------------------------------------------------------------\n')

        print('Downloading %s ...' % constants.NEIGHBOURHOODS_GEO)
        
        # Downloading 'neighbourhoods.geojson'
        target_file7 = os.path.join(constants.DATA_DIRECTORY_TORONTO, constants.NEIGHBOURHOODS_GEO)
        with requests.get(constants.DATA_BASE_URL_TORONTO + 'visualisations/' + constants.NEIGHBOURHOODS_GEO, stream=True) as r:
            with open(target_file7, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Download Finished!')

        print('\n--------------------------------------------------------------------------------\n')

        print('Data download completed for %s' % city.upper())

# Main function
def main(city):

    # Initiating the download process with city as input argument
    collect_information(city)


if __name__ == '__main__':

    # Setting the input argument as city
    city = str(sys.argv[1])
    
    # Calling the main function
    main(city)
