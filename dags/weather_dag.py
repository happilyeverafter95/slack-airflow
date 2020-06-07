import os
import requests

from airflow import DAG
from airflow.operators import PythonOperator
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator

from datetime import datetime


default_args = {
    'owner': 'Mandy',
    'depends_on_past': False,
    'start_date': datetime(2020, 6, 6),
    'retries': 0,
}

daily_weather = None


def get_daily_temperature():
    api_key = os.environ['weather_api_key']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Toronto&APPID={}'.format(api_key))
    global daily_weather
    daily_weather = r.json()['weather'][0]['description']


with DAG(
    'DailyWeatherReports',
    default_args=default_args,
    schedule_interval='12 * * * *',
    catchup=False,
) as dag:
    get_toronto_temperature = PythonOperator(
        task_id='get_toronto_temperature',
        python_callable=get_daily_temperature
    )
    post_to_slack = SlackWebhookOperator(
        task_id='post_to_slack',
        http_conn_id='slack_connection',
        webhook_token=os.environ['slack_webhook_url'],
        message='The weather today is {}'.format(daily_weather),
        channel='#daily-weather-feed'
    )

    get_toronto_temperature.set_downstream(post_to_slack)
