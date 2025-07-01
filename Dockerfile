FROM apache/airflow:2.6.1

USER root

# Install Docker CLI inside the container
RUN apt-get update && apt-get install -y docker.io

USER airflow