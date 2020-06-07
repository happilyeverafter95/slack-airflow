# slack-airflow

**Accompanying Medium Article:** [Integrating Airflow with Slack for Daily Reporting](https://medium.com/@mandygu/integrating-docker-airflow-with-slack-to-get-daily-reporting-c462e7c8828a)

Simple Airflow + Slack integration for sending daily weather forecasts to my Slack workspace.


## Set up instructions

TODO: start up script to echo these secrets into an env file and run the docker commands with the env file

Specify these secrets in the `Dockerfile`:

```
# Secrets
ENV weather_api_key=
ENV slack_webhook_url=
```

Run these commands in:

```
docker build . -t airflow
docker-compose -f docker-compose.yml up -d
```

The web server will be launched at `localhost:8080`
