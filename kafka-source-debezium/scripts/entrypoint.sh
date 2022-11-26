#!/usr/bin/env bash

# kafka home
# FIXME: If the folder name is changed, it should be changed
export KAFKA_HOME=/home/kafka/kafka_2.1.2-3.3.1

# kafka configure
: "${KAFKA_ADVERTISED_HOST_NAME:=127.0.0.1}"
: "${KAFKA_ADVERTISED_PORT:=9092}"

: "${KAFKA_CONNECT_GROUP_ID:=connect-cluster}"
: "${KAFKA_CONNECT_KEY_CONVERTER:=org.apache.kafka.connect.json.JsonConverter}"
: "${KAFKA_CONNECT_VALUE_CONVERTER:=org.apache.kafka.connect.json.JsonConverter}"
: "${KAFKA_CONNECT_KEY_CONVERTER_SCHEMAS_ENABLE:=true}"
: "${KAFKA_CONNECT_VALUE_CONVERTER_SCHEMAS_ENABLE:=true}"
: "${OFFSET_STORAGE_TOPIC:=connect-offsets}"
: "${OFFSET_STORAGE_REPLICATION_FACTOR:=1}"
: "${CONFIG_STORAGE_TOPIC:=connect-configs}"
: "${CONFIG_STORAGE_REPLICATION_FACTOR:=1}"
: "${STATUS_STORAGE_TOPIC:=connect-status}"
: "${STATUS_STORAGE_REPLICATION_FACTOR:=1}"
: "${OFFSET_FLUSH_INTERVAL_MS:=10000}"
# config connector
KAFKA_PLUGIN_PATH=${KAFKA_HOME}/connectors

write_kafka_connect_config() {
    echo "bootstrap.servers=${KAFKA_ADVERTISED_HOST_NAME}:${KAFKA_ADVERTISED_PORT}"
    echo "group.id=${KAFKA_CONNECT_GROUP_ID}"
    echo "key.converter=${KAFKA_CONNECT_KEY_CONVERTER}"
    echo "value.converter=${KAFKA_CONNECT_VALUE_CONVERTER}"
    echo "key.converter.schemas.enable=${KAFKA_CONNECT_KEY_CONVERTER_SCHEMAS_ENABLE}"
    echo "value.converter.schemas.enable=${KAFKA_CONNECT_VALUE_CONVERTER_SCHEMAS_ENABLE}"
    echo "offset.storage.topic=${OFFSET_STORAGE_TOPIC}"
    echo "offset.storage.replication.factor=${OFFSET_STORAGE_REPLICATION_FACTOR}"
    echo "config.storage.topic=${CONFIG_STORAGE_TOPIC}"
    echo "config.storage.replication.factor=${CONFIG_STORAGE_REPLICATION_FACTOR}"
    echo "status.storage.topic=${STATUS_STORAGE_TOPIC}"
    echo "status.storage.replication.factor=${STATUS_STORAGE_REPLICATION_FACTOR}"
    echo "offset.flush.interval.ms=${OFFSET_FLUSH_INTERVAL_MS}"
    echo "plugin.path=${KAFKA_PLUGIN_PATH}"
} > "${KAFKA_HOME}/config/connect-distributed.properties"

# 브로커 힙 메모리 설정
# Xmx : Java 힙의 최대 크기를 지정하는 것
# Xms : Java 힙의 최초 크기를 지정하는 것
export KAFKA_HEAP_OPTS="-Xmx2G -Xms2G"
write_kafka_connect_config

# kafka connect run
${KAFKA_HOME}/bin/connect-distributed.sh ${KAFKA_HOME}/config/connect-distributed.properties
