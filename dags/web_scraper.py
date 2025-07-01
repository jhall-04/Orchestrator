from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'you',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'arxiv_scraper',
    default_args=default_args,
    description='Scrape Arxiv weekly',
    schedule_interval='@weekly',
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    scrape_task = DockerOperator(
        task_id='run_scraper',
        image='arxiv_scraper:latest',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )