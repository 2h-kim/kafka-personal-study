from kafka.producer import KafkaProducer

TOPIC_NAME = "kafka.client.tutorial" # producer는 생성한 레코드를 전송하기 위해 전송하고자 하는 토픽을 알고 있어야 한다.
BOOTSTRAP_SERVER_HOST = "kafka_tutorial:9092" # 전송하고자 하는 카프카 클러스터 서버의 host와 IP를 지정
KEY_SERIALIZER = str.encode
VALUE_SERIALIZER = str.encode

def on_send_success(record_metadata):
    # 원칙적인 로깅 방식
    # logging.info(record_metadata.topic, record_metadata.partition, record_metadata.offset)
    # 여기서는 print
    print(record_metadata.topic, record_metadata.partition, record_metadata.offset)

def on_send_error(exception):
    # logging.error(f'Error Occured : ', exc_info=exception)
    print(f'Error Occured : ', exc_info=exception)


producer = KafkaProducer(
    bootstrap_servers=[BOOTSTRAP_SERVER_HOST],
    key_serializer=KEY_SERIALIZER,
    value_serializer=VALUE_SERIALIZER,
)

test_message_key = "test"
test_message_value = "testMessage for python with Kafka, with customPartition"

producer.send(topic=TOPIC_NAME, value=test_message_value, key=test_message_key) \
    .add_callback(on_send_success) \
    .add_errback(on_send_error)

producer.flush()
producer.close()