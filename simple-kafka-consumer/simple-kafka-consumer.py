from kafka.consumer import KafkaConsumer

TOPIC_NAME = "kafka.client.tutorial" # Consumer 생성한 레코드를 받고자 하는 토픽을 알고 있어야 한다.
BOOTSTRAP_SERVER_HOST = "kafka_tutorial:9092" # 받받고자 하는 카프카 클러스터 서버의 host와 IP를 지정
CONSUMER_GROUP_ID = "test-consumer-group"

# auto_offset_reset
# - latest : 가장 마지막 offset부터
# - earliest : 가장 처음 offset부터
# - none : 해당 consumer group이 가져가고자 하는 topic의 consuer offset정보가 없으면 exception을 발생시킴.
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=BOOTSTRAP_SERVER_HOST,
    auto_offset_reset="earliest", 
    group_id= CONSUMER_GROUP_ID,
)

print("Consumer message start")

for message in consumer:
    print(
        "Topic: %s, Partition: %d, Offset: %d, Key: %s, Value: %s"
        % (
            message.topic,
            message.partition,
            message.offset,
            message.key,
            message.value,
        )
    )