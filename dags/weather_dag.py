import os
import requests

from airflow import DAG
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator

from datetime import datetime


default_args = {
    'owner': 'Mandy',
    'depends_on_past': False,
    'start_date': datetime(2020, 6, 6),
    'retries': 0,
}


def get_daily_forecast() -> str:
    api_key = os.environ['weather_api_key']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Toronto&APPID={}'.format(api_key))
    forecast = r.json()['weather'][0]['description']
    return 'The forecast today is: {}'.format(forecast)


with DAG(
    'DailyWeatherReports',
    default_args=default_args,
    schedule_interval='12 * * * *',
    catchup=False,
) as dag:
    post_daily_forecast = SlackWebhookOperator(
        task_id='post_daily_forecast',
        http_conn_id='slack_connection',
        webhook_token=os.environ['slack_webhook_url'],
        message=get_daily_forecast(),
        channel='#daily-weather-feed'
    )
