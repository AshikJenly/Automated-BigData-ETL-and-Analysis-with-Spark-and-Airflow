# Automated-BigData-ETL-and-Analysis-with-Spark-and-Airflow


## Tools Used 

Big Data Tools
    * Spark
    * Hadoop

Automation and Pipelining Tool
    * Airflow

Operating System
    * Ubuntu

Programming Languages
    * Python

## Process DAG
 <image url>


## How to Execute the Project

#### Step 1: Starting ALl the Required Processes(Backgroud/ForeGround)

    1) Start Hadoop
     $ /path/to/hadoop/sbin/start-all.sh

    2) Start Spark(Optional)
    $ /path/to/spark/sbin/start-all.sh

    3)Staring Airflow
        $aiflow standalone
        
Processes up and running:

Hadoop:

ResourceManager
NodeManager
DataNode
SecondaryNameNode
Spark:

Worker
Master

#### Step 2: Execution

    1) Required Path(For given path in program)
        
        * In HDFS
            /tweet_output
            /testingData/transformedData
        * In Local
            ~/TestingDatas/output/insights.json (Otherwise change the BashOperator in dags.py)
    2) Place code inside airflow

            mv /path/to/*.py /path/to/aiflow


#### Step 4:Open airflow UI

    In your browser,access following path:

    http://localhost:8080/dags/

**Make sure to replace /path/to with appropriate path**

# Output Sample:

