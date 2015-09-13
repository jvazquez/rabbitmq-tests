# -*- coding: utf-8 -*-

"""
Author: Jorge Omar Vazquez <jorgeomar.vazquez@gmail.com>
"""
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# Declare a queue or the messages will be trashed
channel.queue_declare(queue='hello')
print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print " [x] Received {body}".format(body=body)

channel.basic_consume(callback, queue='hello', no_ack=True)

channel.start_consuming()
