"""
    - This script will rename some downloaded files
        and un-compress the files with '.gz' extensions 
    
    - The normal files will be renamed as per the city
    
    - The compressed files will be unzipped and placed into the specified folder

    - The compressed files will later on be deleted from the directories

    Input:
        city name

    Output:
        - Files renamed
        - Extracted files

    Usage:
        python3 restructure.py <city-name>
    
    Example:
        python3 restructure.py vancouver
"""

# Importing the required libraries
import os
import gzip
import shutil
import sys

# Setting the directory locations
vancouver_dir_name = '../../rawData/vancouver'
toronto_dir_name = '../../rawData/toronto'

# Function to rename the files
def rename_files(city):

    # For Vancouver
    if city.lower() == 'vancouver':
        os.rename(vancouver_dir_name + '/listings.csv', vancouver_dir_name + '/vancouver_listing_summary.csv')
        os.rename(vancouver_dir_name + '/reviews.csv', vancouver_dir_name + '/vancouver_review_summary.csv')
        os.rename(vancouver_dir_name + '/neighbourhoods.csv', vancouver_dir_name + '/vancouver_neighbourhoods_detail.csv')
        os.rename(vancouver_dir_name + '/neighbourhoods.geojson', vancouver_dir_name + '/vancouver_neighbourhoods_geo.geojson')

    # For Toronto
    if city.lower() == 'toronto':
        os.rename(toronto_dir_name + '/listings.csv', toronto_dir_name + '/toronto_listing_summary.csv')
        os.rename(toronto_dir_name + '/reviews.csv', toronto_dir_name + '/toronto_review_summary.csv')
        os.rename(toronto_dir_name + '/neighbourhoods.csv', toronto_dir_name + '/toronto_neighbourhoods_detail.csv')
        os.rename(toronto_dir_name + '/neighbourhoods.geojson', toronto_dir_name + '/toronto_neighbourhoods_geo.geojson')

# Function to rename the un-compressed files after extraction
def rename_extracted(city):

    # For Vancouver
    if city.lower() == 'vancouver':
        os.rename(vancouver_dir_name + '/listings.csv', vancouver_dir_name + '/vancouver_listing_detail.csv')
        os.rename(vancouver_dir_name + '/reviews.csv', vancouver_dir_name + '/vancouver_review_detail.csv')
        os.rename(vancouver_dir_name + '/calendar.csv', vancouver_dir_name + '/vancouver_calendar_detail.csv')

    # For Toronto
    if city.lower() == 'toronto':
        os.rename(toronto_dir_name + '/listings.csv', toronto_dir_name + '/toronto_listing_detail.csv')
        os.rename(toronto_dir_name + '/reviews.csv', toronto_dir_name + '/toronto_review_detail.csv')
        os.rename(toronto_dir_name + '/calendar.csv', toronto_dir_name + '/toronto_calendar_detail.csv')

# Function to extract all the compressed files with '.gz' extension in a directory
def gz_extract(directory):

    # Set the extension
    extension = ".gz"

    # Change to the specified directory
    os.chdir(directory)

    # Loop through the items in directory
    for item in os.listdir(directory): 
        
        # Check for '.gz' extension
        if item.endswith(extension): 

            # Get full path of files
            gz_name = os.path.abspath(item) 

            # Get filename for files within
            file_name = (os.path.basename(gz_name)).rsplit('.',1)[0] 
            
            # Un-compress the required files
            with gzip.open(gz_name,"rb") as f_in, open(file_name,"wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
            
            # Delete the zipped file
            os.remove(gz_name) 

# Main function
def main(city):
    
    # For Vancouver
    if city.lower() == 'vancouver':
        rename_files('vancouver')
        gz_extract(vancouver_dir_name)
        rename_extracted('vancouver')

    # For Toronto
    elif city.lower() == 'toronto':
        rename_files('toronto')
        gz_extract(toronto_dir_name)
        rename_extracted('toronto')

if __name__ == '__main__':
    
    # Setting the input argument for city
    city = str(sys.argv[1])

    # Calling the main function
    main(city)
