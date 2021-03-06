<?php

# Weird includes for RabbitMQ
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPConnection;
use PhpAmqpLib\Message\AMQPMessage;

# Insert data into mongoDB and get new uid
$connection = new MongoClient();
$collection = $connection->wtwinterface->wtwinterface;
$data = array('ProcStatus' => 'Pending');
$data = array_merge($data, $_POST);
$collection->insert($data);
$uid = $data['_id']; 
$connection->close();

# Insert into RabbitMQ queue
$connection = new AMQPConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
$channel->queue_declare('wtwinterface', false, false, false, false);
$msg = new AMQPMessage($uid);
$channel->basic_publish($msg, '', 'wtwinterface');
$connection->close();
?>
