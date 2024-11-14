# Weather Data Pipeline with Apache Airflow

## Project Overview

This project demonstrates a weather data pipeline using Apache Airflow. The pipeline fetches weather data from the OpenWeatherMap API for a specified location (in this case, Dallas, TX) and saves the data to a JSON file on the local system. Apache Airflow orchestrates the process, ensuring the weather data is fetched on a schedule and stored in a structured format. This project serves as a foundational example of building data pipelines using Airflow, which can be extended for various data engineering and ETL tasks.

## Use Case

The primary use case of this project is to automate the retrieval of weather data at regular intervals for analysis and storage purposes. This could be beneficial for:

- **Data Analysis**: Collecting weather data over time allows for historical analysis, trend detection, and forecasting.
- **Machine Learning**: The stored weather data can be used for machine learning models that predict weather patterns or assess correlations with other data points.
- **Data Warehousing**: As a foundational step to build more complex pipelines, this project can be adapted to load data into a data warehouse or data lake for broader analytics.

## What the Pipeline Does

1. **Fetch Weather Data**: Using the OpenWeatherMap API, the pipeline fetches weather data for Dallas, TX. It can be modified to fetch data for any location by changing the API parameters.
2. **Save Data to JSON**: The data is saved to a JSON file on the local system, creating a time-stamped log of each data pull.
3. **Orchestrate with Airflow**: Apache Airflow is used to schedule and monitor the pipeline, ensuring that data is fetched at regular intervals without manual intervention.

## Project Structure

- `weather_data_pipeline.py`: The main DAG file that defines the Airflow tasks for fetching and storing weather data.
- `README.md`: This documentation file explaining the project, its purpose, and how to set it up and run.

## How It Works

The pipeline is structured with the following Airflow tasks:

1. **Start DAG**: A dummy task to mark the beginning of the DAG.
2. **Fetch Weather Data**: A PythonOperator task that calls the OpenWeatherMap API to retrieve the weather data.
3. **Save Data**: Another PythonOperator task that saves the fetched data to a JSON file in a designated directory.
4. **End DAG**: A dummy task to mark the completion of the DAG run.

## Getting Started

### Prerequisites

To run this project, you'll need:

- **Python 3.x**: Make sure Python 3 is installed on your system.
- **Apache Airflow**: Airflow should be installed and configured in your environment. [Airflow Installation Guide](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html)
- **OpenWeatherMap API Key**: Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get an API key.
