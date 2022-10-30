import random
from kafka.producer import KafkaProducer
from kafka.partitioner import DefaultPartitioner, murmur2

TOPIC_NAME = "kafka.client.tutorial" # producer는 생성한 레코드를 전송하기 위해 전송하고자 하는 토픽을 알고 있어야 한다.
BOOTSTRAP_SERVER_HOST = "kafka_tutorial:9092" # 전송하고자 하는 카프카 클러스터 서버의 host와 IP를 지정
KEY_SERIALIZER = str.encode
VALUE_SERIALIZER = str.encode

class CustomPartitioner(DefaultPartitioner):
    def __init__(self, **args) -> None:
        super().__init__(**args)
    
    def __call__(cls, key, all_partitions, available):
        """
        Get the partition corresponding to key
        :param key: partitioning key
        :param all_partitions: list of all partitions sorted by partition ID
        :param available: list of available partitions in no particular order
        :return: one of the values from all_partitions or available
        """
        if key is None:
            if available:
                return random.choice(available)
            return random.choice(all_partitions)
        if key.decode('utf-8') == 'test':
            return all_partitions[0]
        
        idx = murmur2(key)
        idx &= 0x7fffffff
        idx %= len(all_partitions)
        return all_partitions[idx]


producer = KafkaProducer(
    bootstrap_servers=[BOOTSTRAP_SERVER_HOST],
    key_serializer=KEY_SERIALIZER,
    value_serializer=VALUE_SERIALIZER,
    partitioner=CustomPartitioner()
)

test_message_key = "test"
test_message_value = "testMessage for python with Kafka, with customPartition"

producer.send(topic=TOPIC_NAME, value=test_message_value, key=test_message_key)

producer.flush()
producer.close()