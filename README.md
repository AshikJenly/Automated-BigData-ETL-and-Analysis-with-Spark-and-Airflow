# Automated Big Data ETL and Analysis with Spark and Airflow

## Tools Used

**Big Data Tools**
- Spark
- Hadoop

**Automation and Pipelining Tool**
- Airflow

**Operating System**
- Ubuntu

**Programming Languages**
- Python

## Process DAG
![DAG Screenshot](https://github.com/AshikJenly/Automated-BigData-ETL-and-Analysis-with-Spark-and-Airflow/assets/116492348/a7677477-5b7d-4f97-91aa-657bdf1fbfad)

## How to Execute the Project

### Step 1: Starting All the Required Processes (Background/Foreground)

1. Start Hadoop:
    ```bash
    $ /path/to/hadoop/sbin/start-all.sh
    ```

2. Start Spark (Optional):
    ```bash
    $ /path/to/spark/sbin/start-all.sh
    ```

3. Start Airflow:
    ```bash
    $ airflow standalone
    ```

Processes up and running:

**Hadoop:**
- ResourceManager
- NodeManager
- DataNode
- SecondaryNameNode

**Spark:**
- Worker
- Master

### Step 2: Execution

1. Required Paths (For the given path in the program):

   - In HDFS:
     - /tweet_output
     - /testingData/transformedData

   - In Local:
     - ~/TestingDatas/output/insights.json (Otherwise, change the BashOperator in dags.py)

2. Place code inside Airflow:
   ```bash
   mv /path/to/*.py /path/to/airflow
   ```

### Step 3: Open Airflow UI

In your browser, access the following path:

[http://localhost:8080/dags/](http://localhost:8080/dags/)

**Make sure to replace /path/to with the appropriate path**

