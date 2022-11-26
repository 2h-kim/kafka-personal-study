# Before build docker image

```bash
wget https://downloads.apache.org/kafka/3.3.1/kafka_2.12-3.3.1.tgz
tar xvf kafka_2.12-3.3.1.tgz
wget https://repo1.maven.org/maven2/io/debezium/debezium-connector-mysql/2.0.0.Final/debezium-connector-mysql-2.0.0.Final-plugin.tar.gz
tar xvf debezium-connector-mysql-2.0.0.Final-plugin.tar.gz
```

# Build
```bash
docker build --tag debezium-kafka-source-connector:0.0.1 .
```

# Run
```bash
docker run -d \
    -e KAFKA_ADVERTISED_HOST_NAME=kafka_tutorial \
    -e KAFKA_ADVERTISED_PORT=9092 \
    -e KAFKA_CONNECT_GROUP_ID=kafka-debezium-source-connector \
    -v $(pwd)/source-connector-config:/home/kafka/source-connector-config \
    -p 8083:8083 \
    --net=test-network \
    --name=kafka-source-connector \
    debezium-kafka-source-connector:0.0.1
```

## docker network 연결
```bash
docker network connect test-network  kafka-source-connector
docker network connect test-network  mysql-container
```

## connector 연결
```bash
curl --location --request POST 'http://localhost:8083/connectors' --header 'Content-Type: application/json' -d @test-connector.json
```

## connector list
```bash
curl --location --request GET 'http://localhost:8083/connectors'
```

