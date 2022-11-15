import time
from kafka import ConsumerRebalanceListener
from kafka.consumer import KafkaConsumer
from kafka.structs import OffsetAndMetadata


class RebalanceListener(ConsumerRebalanceListener):
    def __init__(self) -> None:
        super().__init__()
    
    def on_partitions_assigned(self, assigned):
        print("partition are assigned")
        return super().on_partitions_assigned(assigned)

    def on_partitions_revoked(self, revoked):
        print("partition are revoked")
        return super().on_partitions_revoked(revoked)


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
consumer.subscribe([TOPIC_NAME], listener=RebalanceListener())

while True:
    # consumer.poll return dict 
    # key is TopicPartition value is List of ConsumerRecord
    records = consumer.poll(timeout_ms=1) # record output is dict
    current_offset = {}
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
            current_offset[topic_partition] = OffsetAndMetadata(consumer_record.offset + 1, None)
            # record 단위로 오프셋을 커밋
            consumer.commit(current_offset)
    
    time.sleep(1)
