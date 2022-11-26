FROM ubuntu:latest

LABEL Maintainer="2h-kim"
LABEL Description="debezium docker image"
LABEL version="0.0.1"

RUN apt-get update && apt-get -y upgrade

RUN apt-get install openjdk-11-jdk -y \
    && apt-get install wget -y \
    && apt-get install vim -y  \
    && apt-get install curl -y \
    && apt-get install mysql -y

EXPOSE 8083

RUN useradd -ms /bin/bash kafka

# FIXME: If the folder name is changed, it should be changed
COPY scripts/ /home/kafka/scripts
COPY kafka_2.12-3.3.1/ /home/kafka/kafka_2.1.2-3.3.1
COPY debezium-connector-mysql/ /home/kafka/kafka_2.1.2-3.3.1/connectors/debezium-connector-mysql
COPY source-connector-config/ /home/kafka/source-connector-config

RUN chmod -R 777 /home/kafka/scripts \
    && chmod -R 777 /home/kafka/kafka_2.1.2-3.3.1 \
    && chmod -R 777 /home/kafka/kafka_2.1.2-3.3.1/connectors/debezium-connector-mysql \
    && chmod -R 777 /home/kafka/source-connector-config \
    && chown -R kafka:kafka /home/kafka/scripts \
    && chown -R kafka:kafka /home/kafka/kafka_2.1.2-3.3.1 \
    && chown -R kafka:kafka /home/kafka/kafka_2.1.2-3.3.1/connectors/debezium-connector-mysql \
    && chown -R kafka:kafka /home/kafka/source-connector-config 
    
USER kafka
WORKDIR /home/kafka

ENTRYPOINT ["/home/kafka/scripts/entrypoint.sh"]
