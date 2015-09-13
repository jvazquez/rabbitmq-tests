# -*- coding: utf-8 -*-

"""
Author: Jorge Omar Vazquez <jorgeomar.vazquez@gmail.com>
"""
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# Declare a queue or the messages will be trashed
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
connection.close()
