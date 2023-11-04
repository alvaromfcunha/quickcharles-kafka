import socket
import os

from fastapi import FastAPI
from dotenv import load_dotenv
from confluent_kafka import Producer

load_dotenv()

kafka_bootstrap_servers = os.environ['KAFKA_BOOTSTRAP_SERVERS']

conf = {'bootstrap.servers': kafka_bootstrap_servers,
        'client.id': socket.gethostname()}

producer = Producer(conf)

app = FastAPI()

@app.get('/')
def test():
	producer.produce(topic='webhook',
									key='message',
									value='test')
	return {'Hello': 'World'}
