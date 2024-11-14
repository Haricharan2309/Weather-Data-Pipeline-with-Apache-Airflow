from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import requests
import json
from airflow.models import Variable
from datetime import datetime
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['your_email@example.com'],  # Update with your email
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'weather_data_pipeline',
    default_args=default_args,
    description='A simple weather data pipeline',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
)

def fetch_weather_data(**kwargs):
    api_key = "3a4c272dc9098b779636d4123c41e9c4"
    city = "Dallas"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    kwargs['ti'].xcom_push(key='weather_data', value=data)

def save_weather_data(**kwargs):
    data = kwargs['ti'].xcom_pull(key='weather_data', task_ids='fetch_weather_data_task')
    date_str = datetime.now().strftime('%Y%m%d')
    
    # Define the file path for saving the weather data
    file_path = os.path.join("/mnt/d/Projects/Weather_data", f"weather_data_{date_str}.json")  # Using WSL path format
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Save the data to the specified file
    with open(file_path, 'w') as f:
        json.dump(data, f)

fetch_weather_data_task = PythonOperator(
    task_id='fetch_weather_data_task',
    python_callable=fetch_weather_data,
    provide_context=True,
    dag=dag,
)

save_weather_data_task = PythonOperator(
    task_id='save_weather_data_task',
    python_callable=save_weather_data,
    provide_context=True,
    dag=dag,
)

fetch_weather_data_task >> save_weather_data_task
