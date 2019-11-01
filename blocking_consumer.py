# https://github.com/pika/pika/releases/tag/0.10.0
import pika
import random

def on_message(channel, method_frame, header_frame, body):
    print(method_frame.delivery_tag)
    print(body)
    print()
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

credentials = pika.PlainCredentials("username", "password")
parameters = pika.ConnectionParameters(
    host="host",
    credentials=credentials,
    virtual_host="virtual_host"
    connection_attempts=1
    retry_delay=60)

while(True):
    try:
        print("Connecting...")
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.basic_qos(prefetch_count=1)
        channel.queue_declare('recovery-example', durable = False, auto_delete = True)
        channel.basic_consume('recovery-example', on_message)
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
            connection.close()
            break
