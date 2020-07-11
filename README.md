# rabbitmq-messaging
Send and consume messages using python pika

RabbitMQ

/usr/local/sbin/rabbitmq-server

amqp://guest:guest@localhost:5672/

Sample dockerfile
```
FROM rabbitmq

RUN rabbitmq-plugins enable --offline rabbitmq_management

EXPOSE 15671 15672
```
Alternate method to install:
```
docker run -d -p 5672:5672 -p 15672:15672 macintoshplus/rabbitmq-management
```
Manage containers with gui app: [kitematic](https://github.com/docker/kitematic/releases)
