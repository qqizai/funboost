from auto_run_on_remote import run_current_script_on_remote
# run_current_script_on_remote()
from funboost import boost
from funboost.consumers.pulsar_consumer import PulsarConsumer

from funboost.publishers.pulsar_publisher import PulsarPublisher


from funboost.assist.user_custom_broker_register import register_custom_broker


BROKER_PULSAR_KIND = 202

register_custom_broker(BROKER_PULSAR_KIND,PulsarPublisher,PulsarConsumer)

@boost('test_pulsar_topic2',broker_kind=BROKER_PULSAR_KIND,qps=2,broker_exclusive_config={'subscription_name':'funboost_g2'})
def add(x,y):
    print(x+y)

if __name__ == '__main__':
    add.consume()