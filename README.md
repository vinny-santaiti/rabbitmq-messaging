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
docker pull rabbitmq:3-management
docker run -d --hostname my-rabbit --name rabbitmq-management -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```
Manage containers with gui app: [kitematic](https://github.com/docker/kitematic/releases)
