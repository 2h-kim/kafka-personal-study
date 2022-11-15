import sys
import signal
from kafka.consumer import KafkaConsumer


TOPIC_NAME = "kafka.client.tutorial" # Consumer 생성한 레코드를 받고자 하는 토픽을 알고 있어야 한다.
BOOTSTRAP_SERVER_HOST = "kafka_tutorial:9092" # 받받고자 하는 카프카 클러스터 서버의 host와 IP를 지정
CONSUMER_GROUP_ID = "test-consumer-group"
ENABLE_AUTO_COMMIT_CONFIG = False

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=BOOTSTRAP_SERVER_HOST,
    auto_offset_reset="earliest", 
    group_id= CONSUMER_GROUP_ID,
    enable_auto_commit=ENABLE_AUTO_COMMIT_CONFIG # auto commit false
)

# TODO: 정확하지 않고 야매 방법으로 진행한 것으로 추후 정확한 방법으로 수정 필요
def signal_term_handler(signum, frame):
    global consumer
    print(f"signum got : {signum}")
    consumer.close()
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_term_handler)

try:
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
except Exception as e:
    print(e)
    raise e
finally:
    print("finally start")
    consumer.close()
