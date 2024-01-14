# Instructions to Execute the Project

## Environment

The project is designed to run on the SFU Cluster, which can be connected at ```cluster.cs.sfu.ca``` by SSH.

More details on connecting to SFU Cluster can be found [here](https://coursys.sfu.ca/2022fa-cmpt-732-g1/pages/Cluster).

## Instructions Overview & Explanation

There are two approaches to execute the project:

- Execute the entire project via one bash script [(See Direct Execution Steps)](#direct-execution-steps)

- Execute the project by individually running all the scripts [(See Individual Runs for All Scripts)](#individual-runs-for-all-scripts)

Below is the overview of project execution with a little bit of explanation:

1. Login to the SFU Cluster.

2. The bash terminal would now show ```<computing-id>@pmp-gateway:~$```

3. This would be your current working directory at ```/home/<computing-id>```

4. Now, execute the command ```git clone git@github.sfu.ca:hmk9/cmpt732-marshmallow-project.git```

5. This should clone the git repository into your current directory.

    * **Possible Errors:**
        1. The `git clone` command would not succeed.
    <br><br>
    * **Possible Resolutions:**
        1. You'll probably want to access the repository by SSH. If you don't already have an SSH key, you will need to generate one. Once you have an SSH key, [add the key in GitHub](https://github.sfu.ca/settings/keys).
    <br><br>
    * **Alternative Workaround:**
        1. Navigate to this [link](https://github.sfu.ca/hmk9/cmpt732-marshmallow-project).
        
        2. Make sure you have selected the `main` branch from the available branch dropdown menu.
        
        3. Click on `Code` button in `green` colour on the right and select the option `Download ZIP`.
        
        4. Unzip the downloaded data and then upload the project directory to the cluster.

6. If everything is successful, you must be able to see a directory named `cmpt732-marshmallow-project` in your working directory.

7. Execute the command ```cd cmpt732-marshmallow-project``` to navigate inside the project directory.

8. Now, execute the command ```chmod +x executeProject.sh```

9. Once the above steps are successful, we are now ready to run the project.

10. Execute the command ```./executeProject.sh```

11. This bash file will execute all the project required commands by itself. No interaction is required.

12. First it will run all the steps for `Vancouver` data followed by execution of same steps for `Toronto` data.

13. In case you would want to see individual commands, you can refer to the instructions below.

14. Once the file execution is completed, the project execution will terminate.

15. This will automatically clean all the HDFS storage and bring the necessary output files to the local directory.

## Direct Execution Steps

Please follow the given steps to execute the entire project using a bash file:

1.     git clone git@github.sfu.ca:hmk9/cmpt732-marshmallow-project.git

2.     cd cmpt732-marshmallow-project

3.     chmod +x executeProject.sh

4.     ./executeProject.sh

## Individual Runs for All Scripts

If you want to take a look at all the processing and outputs happening during the execution of the project, kindly follow the instructions given below to run each script individually:

1.     git clone git@github.sfu.ca:hmk9/cmpt732-marshmallow-project.git

2.     cd cmpt732-marshmallow-project

3.     python3 -m pip install -r requirements.txt

4.      rm -rf rawData 
        rm -rf processedData
        rm -rf extractedData
        rm -rf cleanData
        rm -rf amenitiesData

5.     mkdir -p rawData/{vancouver,toronto}
       mkdir -p extractedData/{vancouver,toronto}

6.     cd src/preprocessing && python3 extractData.py vancouver

7.      cd .. && cd utils && python3 restructure.py vancouver

8.      cd .. && cd preprocessing && python3 loadData.py vancouver

9.      cd .. && cd cleaning && python3 extractS3Data.py vancouver

10.      cd .. && cd ..
         hdfs dfs -mkdir extractedData
         hdfs dfs -copyFromLocal extractedData/vancouver/ extractedData/
         cd src/cleaning

11.      spark-submit dataCleaning.py vancouver
         hdfs dfs -mv cleanData/vancouver/part-* cleanData/vancouver/vancouver_listing_clean.csv

12.     cd .. && cd analysis 
        spark-submit calculateDistance.py vancouver 
        hdfs dfs -mv processedData/vancouver/part-* processedData/vancouver/vancouver_distances_calculated.csv

13.     spark-submit analyzeAmenities.py vancouver 
        hdfs dfs -mv amenitiesData/vancouver/part-* amenitiesData/vancouver/vancouver_amenities.csv

14.     cd .. && cd preprocessing && python3 extractData.py toronto

15.     cd .. && cd utils && python3 restructure.py toronto 

16.     cd .. && cd preprocessing && python3 loadData.py toronto 

17.     cd .. && cd cleaning && python3 extractS3Data.py toronto

18.     cd .. && cd ..
        hdfs dfs -copyFromLocal extractedData/toronto/ extractedData/
        cd src/cleaning

19.     spark-submit dataCleaning.py toronto
        hdfs dfs -mv cleanData/toronto/part-* cleanData/toronto/toronto_listing_clean.csv

20.     cd .. && cd analysis 
        spark-submit calculateDistance.py toronto
        hdfs dfs -mv processedData/toronto/part-* processedData/toronto/toronto_distances_calculated.csv

21.     spark-submit analyzeAmenities.py toronto 
        hdfs dfs -mv amenitiesData/toronto/part-* amenitiesData/toronto/toronto_amenities.csv

22.     cd .. && cd ..
        hdfs dfs -copyToLocal amenitiesData/
        hdfs dfs -copyToLocal processedData/
        hdfs dfs -copyToLocal cleanData/

23.     hdfs dfs -rm -r amenitiesData/
        hdfs dfs -rm -r processedData/
        hdfs dfs -rm -r cleanData/
        hdfs dfs -rm -r extractedData/

---

Thank You!

---
