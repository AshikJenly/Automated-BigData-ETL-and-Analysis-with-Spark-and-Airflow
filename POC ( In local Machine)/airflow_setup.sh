
sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow

#Run the airflow in standalone
airflow standalone

#To add dag in aiflow
mkdir ~/airflow/tweet_dag
sudo nano ~/airflow/airflow.cfg

# In airflow.cfg 
    #add below line 
    dags_folder = /home/jenly/airflow/tweet_dag

#restart aiflow
