from kafka.producer import KafkaProducer

TOPIC_NAME = "kafka.client.tutorial" # producer는 생성한 레코드를 전송하기 위해 전송하고자 하는 토픽을 알고 있어야 한다.
BOOTSTRAP_SERVER_HOST = "kafka_tutorial:9092" # 전송하고자 하는 카프카 클러스터 서버의 host와 IP를 지정
VALUE_SERIALIZER = str.encode


producer = KafkaProducer(
    bootstrap_servers=[BOOTSTRAP_SERVER_HOST],
    value_serializer=VALUE_SERIALIZER
)
# test message without key
test_message_value = "testMessage for python with Kafka"

# send는 즉각 전송이 아닌 배치 전송이다.
producer.send(topic=TOPIC_NAME, value=test_message_value)

# flush를 통해 내부 버퍼에 가지고 있던 레코드 배치를 브로커에 전송
producer.flush()

# producer 리소스 종료
producer.close()