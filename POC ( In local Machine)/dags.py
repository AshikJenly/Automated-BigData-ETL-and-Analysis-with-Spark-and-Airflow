from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import datetime
from airflow.utils.dates import days_ago
from datetime import datetime
from etl import tranform_data
from analyze import Analyze_and_save

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M")


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 7),
    'email': ['jenlyashik@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag_1',
    default_args=default_args,
    description='DAG with ETL process!',
    schedule=timedelta(days=1),
)
# clean path for tranform data
cleaning_path = BashOperator(
    task_id="cleaning_path_1_task",
    bash_command="hdfs dfs -rm -r /testingData/transformedData",
    dag = dag
)

#tranforming
transform_data_task = PythonOperator(
    task_id='transform_data_task',
    python_callable=tranform_data,
    dag=dag,
)

logging_path_in_hdfs = BashOperator(
    task_id="logging_hdfs_path",
    bash_command="hdfs dfs -ls /tweet_output >> ~/TestingDatas/output/logs",
    dag = dag
)

#clean current path
cleaning_path_final_local = BashOperator(
    task_id="cleaning_final_output_path_task",
    bash_command="rm ~/TestingDatas/output/insights.json",
    dag = dag
)
analyse_task = PythonOperator(
    task_id='analyse_task',
    python_callable=Analyze_and_save,
    dag=dag,
)
#load output into hdfs
command = f"hdfs dfs -mkdir /tweet_output/{formatted_datetime};hdfs dfs -put ~/TestingDatas/output/insights.json /tweet_output/{formatted_datetime}/;"
moving_output_to_hdfs = BashOperator(
    task_id="loading_data_to_hdfs",
    bash_command=command,
    dag = dag
)

cleaning_path >> transform_data_task >> [logging_path_in_hdfs,cleaning_path_final_local]\
    >> analyse_task >> moving_output_to_hdfs
