from kafka.admin import KafkaAdminClient, ConfigResource, ConfigResourceType


TOPIC_NAME = "kafka.client.tutorial"
BOOTSTRAP_SERVER_HOST = "kafka_tutorial:9092" # 카프카 클러스터 서버의 host와 port를 지정

admin_client = KafkaAdminClient(
    bootstrap_servers=BOOTSTRAP_SERVER_HOST
)

print("== Get broker information")
# return type dict
describe_cluster = admin_client.describe_cluster()
for node in describe_cluster.get('brokers'):
    print(f"node : {node}")
    cr = ConfigResource(ConfigResourceType.BROKER, name=node.get('node_id'), configs=node)
    describe_config = admin_client.describe_configs([cr])
    for config_i in describe_config:
        print(f"\tconfig:\t:{config_i}")
        
print("== End broker information")

print("== Get topic information")
describe_topic = admin_client.describe_topics([TOPIC_NAME])
for info_i in describe_topic:
    for k, v in info_i.items():
        print(f'{k}\t{v}')
    print('==================================================================')

print("== End topic information")
admin_client.close()