from kafka import KafkaConsumer
consumer = KafkaConsumer('techbleat')
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s message=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
