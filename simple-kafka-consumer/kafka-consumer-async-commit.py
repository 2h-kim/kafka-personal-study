import time
from kafka.consumer import KafkaConsumer
from kafka.structs import OffsetAndMetadata


def offset_commit_callback(offsets, response):
    if response is not None:
        print(f"Commit failed for offsets {offsets} : {response}")
    else:
        print("Commit succeeded")    

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

while True:
    # consumer.poll return dict 
    # key is TopicPartition value is List of ConsumerRecord
    records = consumer.poll(timeout_ms=1) # record output is dict
    for topic_partition, consumer_record_list in records.items():
        for consumer_record in consumer_record_list:
            print(
                "Topic: %s, Partition: %d, Offset: %d, Key: %s, Value: %s" %
                (
                    consumer_record.topic,
                    consumer_record.partition,
                    consumer_record.offset,
                    consumer_record.key,
                    consumer_record.value,
                )
            )
            consumer.commit_async(offsets={
                topic_partition: OffsetAndMetadata(consumer_record.offset + 1, None)
            }, callback=offset_commit_callback) 
    time.sleep(1)