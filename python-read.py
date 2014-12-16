#!/usr/bin/python
import pika
import pymongo
from bson.objectid import ObjectId
import time
def callback(ch, method, properties, body):
  # Ackowledge RabbitMQ
  ch.basic_ack(delivery_tag = method.delivery_tag)
  # Get the entry from mongoDB via an http request
  print body
#uid_object = ObjectId(body)
#pip_entry = db.pipinterface.find( { "_id": uid_object } )[0]
  # Brief pause set processing state via http
#db.pipinterface.update({"_id": uid_object}, {"$set":{"ProcStatus": "Processing"}})
  random_pause = pip_entry["WaitTime"]
  print " [x] Received %r" % (pip_entry,) + " -- Sleeping " + str(random_pause) + " seconds"
  time.sleep(random_pause)
  # Set final processing status via http
#db.pipinterface.update({"_id": uid_object}, {"$set":{"ProcStatus": "Processed"}})
# MAIN : Get uids from RabbitMQ queue
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue='pipinterface')
channel.basic_consume(callback, queue="pipinterface")
channel.start_consuming()
