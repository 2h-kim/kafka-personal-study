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

# partition number
print(consumer.partitions_for_topic(topic=TOPIC_NAME))

# assignment 할 때에는 poll을 한번 해주어야 한다.
# 안 할 시, empty set return
# https://stackoverflow.com/questions/54316951/kafka-consumer-assignment-returns-empty-set
consumer.poll(1)
print(consumer.assignment())
consumer.close()