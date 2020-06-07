# slack-airflow

**Accompanying Medium Article:** [Integrating Docker Airflow with Slack to get Daily Reporting](https://medium.com/@mandygu/integrating-docker-airflow-with-slack-to-get-daily-reporting-c462e7c8828a)

Simple Airflow <> Slack integration for sending daily weather forecasts to my Slack workspace.


## Set up instructions

Run these commands in:

```
docker build . -t airflow
docker-compose -f docker-compose.yml up -d
```

The web server will be launched at `localhost:8080`
