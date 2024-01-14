spinner() 
{
    local pid=$!
    local spin='-\|/'
    local i=0
  
    while kill -0 $pid 2>/dev/null; do
        printf '▓'
        sleep .2
    done
  
    echo ' '
}

echo 'Welcome to CMPT 732 Project' 
echo 'Airbnb Data Engineering and Visualization'
echo '---------------------------------------------------------------'
echo ' '
echo 'Prepared by: Group :: Marshmallow'
echo '---------------------------------------------------------------'
echo ' '

echo 'Starting Setup ...'
echo ' '
sleep 2 & spinner
echo ' '

echo 'Installing the Required Libraries'
echo ' '
python3 -m pip install -r requirements.txt
echo ' '
echo 'Library Setup Complete!'
echo '---------------------------------------------------------------'
echo ' '
echo 'Configuring Data Directories'
echo ' '

rm -rf rawData 
rm -rf processedData
rm -rf extractedData
rm -rf cleanData
rm -rf amenitiesData

mkdir -p rawData/{vancouver,toronto}
mkdir -p extractedData/{vancouver,toronto}

sleep 2 & spinner

echo ' '
echo 'Data Directories Configured!'
echo '---------------------------------------------------------------'
echo ' '

echo 'Executing Project Now ...'
echo ' '
sleep 2 & spinner
echo ' '

echo 'DATA ENGINEERING FOR AIRBNB VANCOUVER LISTINGS'
echo '==============================================================='
echo ' '

echo 'Extracting Data From the Internet'
echo '---------------------------------------------------------------'
echo ' '
sleep 2 & spinner
echo ' '

cd src/preprocessing && python3 extractData.py vancouver
echo '---------------------------------------------------------------'
echo ' '
echo ' '

echo 'Restructuring, Extracting and Renaming Files | Pre-Upload Preparation'
echo '---------------------------------------------------------------'
echo ' '
cd .. && cd utils && python3 restructure.py vancouver & spinner
echo ' '
echo 'Process Complete!'
echo '---------------------------------------------------------------'
echo ' '
echo ' '

echo 'Uploading Vancouver Raw Data to AWS S3'
echo '---------------------------------------------------------------'
echo ' '
cd .. && cd preprocessing && python3 loadData.py vancouver & spinner
echo '---------------------------------------------------------------'
echo ' '
echo ' '

echo 'Data Cleaning'
echo '---------------------------------------------------------------'
echo ' '
echo 'Working on Listings Raw Data'
echo '---------------------------------------------------------------'
echo ' '
cd .. && cd cleaning && python3 extractS3Data.py vancouver & spinner
echo ' '
echo 'Data Cleaning in Progress ...'
echo '---------------------------------------------------------------'
echo ' '
cd .. && cd ..
hdfs dfs -mkdir extractedData
hdfs dfs -copyFromLocal extractedData/vancouver/ extractedData/
cd src/cleaning
spark-submit dataCleaning.py vancouver
hdfs dfs -mv cleanData/vancouver/part-* cleanData/vancouver/vancouver_listing_clean.csv
echo '---------------------------------------------------------------'
echo ' '
echo ' '

sleep 5
echo 'Moving to Data Analysis for Vancouver'
echo '---------------------------------------------------------------'
echo ' '
echo 'Running Distance Calculation Program ...'
echo '---------------------------------------------------------------'
echo ' '
cd .. && cd analysis 
spark-submit calculateDistance.py vancouver 
hdfs dfs -mv processedData/vancouver/part-* processedData/vancouver/vancouver_distances_calculated.csv
echo '---------------------------------------------------------------'
echo ' '
echo ' '

echo 'Running Amenity Analysis Program ...'
echo '---------------------------------------------------------------'
echo ' '
spark-submit analyzeAmenities.py vancouver 
hdfs dfs -mv amenitiesData/vancouver/part-* amenitiesData/vancouver/vancouver_amenities.csv
echo '---------------------------------------------------------------'
echo ' '

echo 'VANCOUVER LISTING ANALYSIS COMPLETE!'
echo 'THE VISUALIZATIONS SHOULD NOW BE AVAILABLE FOR VANCOUVER'
echo '==============================================================='
echo ' '
echo ' '

echo 'DATA ENGINEERING FOR AIRBNB TORONTO LISTINGS'
echo '==============================================================='
echo ' '

echo 'Extracting Data From the Internet'
echo '---------------------------------------------------------------'
echo ' '
sleep 2 & spinner
echo ' '

cd .. && cd preprocessing && python3 extractData.py toronto
echo '---------------------------------------------------------------'
echo ' '
echo ' '

echo 'Restructuring, Extracting and Renaming Files | Pre-Upload Preparation'
echo '---------------------------------------------------------------'
echo ' '
cd .. && cd utils && python3 restructure.py toronto & spinner
echo ' '
echo 'Process Complete!'
echo '---------------------------------------------------------------'
echo ' '
echo ' '

echo 'Uploading Toronto Raw Data to AWS S3'
echo '---------------------------------------------------------------'
echo ' '
cd .. && cd preprocessing && python3 loadData.py toronto & spinner
echo '---------------------------------------------------------------'
echo ' '
echo ' '

echo 'Data Cleaning'
echo '---------------------------------------------------------------'
echo ' '
echo 'Working on Listings Raw Data'
echo '---------------------------------------------------------------'
echo ' '
cd .. && cd cleaning && python3 extractS3Data.py toronto & spinner
echo ' '
echo 'Data Cleaning in Progress ...'
echo '---------------------------------------------------------------'
echo ' '
cd .. && cd ..
hdfs dfs -copyFromLocal extractedData/toronto/ extractedData/
cd src/cleaning
spark-submit dataCleaning.py toronto
hdfs dfs -mv cleanData/toronto/part-* cleanData/toronto/toronto_listing_clean.csv
echo '---------------------------------------------------------------'
echo ' '
echo ' '

sleep 5
echo 'Moving to Data Analysis for Toronto'
echo '---------------------------------------------------------------'
echo ' '
echo 'Running Distance Calculation Program ...'
echo '---------------------------------------------------------------'
echo ' '
cd .. && cd analysis 
spark-submit calculateDistance.py toronto
hdfs dfs -mv processedData/toronto/part-* processedData/toronto/toronto_distances_calculated.csv
echo '---------------------------------------------------------------'
echo ' '
echo ' '

echo 'Running Amenity Analysis Program ...'
echo '---------------------------------------------------------------'
echo ' '
spark-submit analyzeAmenities.py toronto 
hdfs dfs -mv amenitiesData/toronto/part-* amenitiesData/toronto/toronto_amenities.csv
echo '---------------------------------------------------------------'
echo ' '

echo 'TORONTO LISTING ANALYSIS COMPLETE!'
echo 'THE VISUALIZATIONS SHOULD NOW BE AVAILABLE FOR TORONTO'
echo '==============================================================='
echo ' '

echo 'Execution Complete, Data Cleanup in Progress ...'
echo '---------------------------------------------------------------'
echo ' '
cd .. && cd ..
hdfs dfs -copyToLocal amenitiesData/
hdfs dfs -copyToLocal processedData/
hdfs dfs -copyToLocal cleanData/
hdfs dfs -rm -r amenitiesData/
hdfs dfs -rm -r processedData/
hdfs dfs -rm -r cleanData/
hdfs dfs -rm -r extractedData/

echo ' '
echo '---------------------------------------------------------------'
echo ' '
echo 'HDFS Storage Clean and Normal'
echo ' '
echo '---------------------------------------------------------------'
echo ' '
echo 'Project Shutdown'
echo ' '
echo '---------------------------------------------------------------'
echo ' '
echo '==============================================================='
echo 'Thank You!'
echo '==============================================================='
echo ' '
