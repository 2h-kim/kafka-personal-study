from kafka.producer import KafkaProducer

TOPIC_NAME = "kafka.client.tutorial" # producer는 생성한 레코드를 전송하기 위해 전송하고자 하는 토픽을 알고 있어야 한다.
BOOTSTRAP_SERVER_HOST = "kafka_tutorial:9092" # 전송하고자 하는 카프카 클러스터 서버의 host와 IP를 지정
KEY_SERIALIZER = str.encode
VALUE_SERIALIZER = str.encode


producer = KafkaProducer(
    bootstrap_servers=[BOOTSTRAP_SERVER_HOST],
    key_serializer=KEY_SERIALIZER,
    value_serializer=VALUE_SERIALIZER
)
# test message with key
test_message_key = "test"
test_message_value = "testMessage for python with Kafka"

# key_serializer 함수의 경우 None처리가 필요해보임(Spark udf와 같이)
producer.send(topic=TOPIC_NAME, value=test_message_value, key=test_message_key)
producer.flush()
producer.close()