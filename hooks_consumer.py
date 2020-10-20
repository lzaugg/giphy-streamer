
import grpc
import hook_pb2_grpc
import hook_pb2
import time
import threading
from confluent_kafka import Consumer, KafkaError
import json
import paho.mqtt.client as mqtt
from urllib.parse import urlparse, parse_qs

endpoint = '192.168.43.148'

client = mqtt.Client()
client.username_pw_set("username_to_set", "password_to_set")
client.connect(endpoint, port=1883, keepalive=60,)
def on_connect(client, userdata, flags, rc):
  print("Connected: " + str(rc))
  #client.publish("/launchpad/led/all" ,"0", qos=0, retain=False)
  reset_leds()

def on_log(mosq, obj, mid, string):
  print("Log: " + str(string))
  pass

client.on_connect = on_connect
#client.on_message = on_message
#client.on_publish = on_publish
#client.on_subscribed = on_subscribed
#client.on_log = on_log

client.loop_start()

channel = grpc.insecure_channel(endpoint + ':6065')

stub = hook_pb2_grpc.StateChangerStub(channel)


request = hook_pb2.SubscribeChangeRequest()
metadata=[(b'authorization', b'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJMTWdPYlp0WjNZVmJQU2tuTXp1YWZBLU5IZzRTa01nZTJMRXVxejc3UXJVIn0.eyJqdGkiOiI1NTE4N2FlMi03MDMyLTRmYWItYWE5Yy1jMGVkYjJiODUxNmQiLCJleHAiOjE1NzI5ODkxNjMsIm5iZiI6MCwiaWF0IjoxNTcyOTg4MjYzLCJpc3MiOiJodHRwczovL2Rldi5zZG0uc3BvdWQuaW8vYXV0aC9yZWFsbXMvc3BvdWQiLCJhdWQiOlsicmVhbG0tbWFuYWdlbWVudCIsImFjY291bnQiXSwic3ViIjoiYmJlYzg4OWUtMzAwZC00M2VlLWIzZmItNDk5Nzg2YzI1YTM3IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoic3BvdWQtc2RtLXVpIiwibm9uY2UiOiJlYTRmZTBmMi03NWEyLTQ1MzMtODNiNC01OTRlZjJlZmUyYjciLCJhdXRoX3RpbWUiOjE1NzI5ODY1MTEsInNlc3Npb25fc3RhdGUiOiJhZmVjNjg3Ni0xYjkxLTRhMzMtYTE2MS0xZDY1OWFiZDgzZDMiLCJhY3IiOiIwIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHBzOi8vZGV2LnNkbS5zcG91ZC5pbyJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsidmlldy11c2VycyIsInF1ZXJ5LWdyb3VwcyIsInF1ZXJ5LXVzZXJzIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBlbWFpbCBwcm9maWxlIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoiTHVrYXMgWmF1Z2ciLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJsdWthcy56YXVnZ0BzcG91ZC5pbyIsImdpdmVuX25hbWUiOiJMdWthcyIsImZhbWlseV9uYW1lIjoiWmF1Z2ciLCJlbWFpbCI6Imx1a2FzLnphdWdnQHNwb3VkLmlvIn0.csEB-Z0KU1-ivPUusATC22rVZ_TORcOvv6RIrdeMjNo7Cf-tX5ACFb4mhBa31Fcw8CbpxcAccIhBgPUCQOgkf27O0_COPIfDtR7Szr8NvwmIiV5koSbWmZD3wfH6ainbjRdzAhrHe2Ovd9S-afv_fHGbJ3_g4zsbV0b0BBrri5-qySGetTKo-IfGFxaT_4r3h-aYwTuC0qgrgehv42sFp2a2MB5W6To9ZXtacTIEFMpLCou9fnMkJPfqLghuTdkZ3kiiw6lXrTiHxkch6shj9lkIGIce-h8gpOgabLhJCaArfbVU6PsCJSNkMgbaE52y2tHk6e52WfUpRZPippkwUg')]

entities = {}
boot_time = int(time.time())

#

active_consumers = {}

def consume_from_kafka(consumer_group, broker, topic):
    print('START consuming from kafka', consumer_group, broker, topic)
    c = Consumer({
        'bootstrap.servers': broker,
        'group.id': consumer_group,
        'auto.offset.reset': 'latest',
        'sasl.mechanisms': 'PLAIN',
        'security.protocol': 'SASL_SSL',
        'sasl.username': 'username_to_set',
        'sasl.password': 'password_to_set'
    })

    c.subscribe([topic])

    #print('active consumers', active_consumers)
    while consumer_group in active_consumers:
        msg = c.poll(0.1)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        # client.publish(topic ,value, qos=0, retain=False)

        
        frame = json.loads(msg.value().decode('utf-8'))
        for p in frame.keys():
            topic = "launchpad/led/" + p
            if hasattr(frame[p], "__len__") and len(frame[p]) == 3:
                value = ",".join([str(f) for f in frame[p]])
                #[str(p) for p in rgb_im.getpixel((x, y))]
                #print(topic, value)
                client.publish(topic ,value, qos=0, retain=False)
            else:
                print('ignore value! Got ', frame)
    reset_leds()
    print('STOP consuming from kafka', consumer_group, broker, topic)
    c.close()

def reset_leds():
    for x in range(8):
        for y in range(8):
            topic = "launchpad/led/" + "p" + str(x + 1) + str(y + 1)
            value = '0,0,0'
            client.publish(topic, value, qos=0, retain=False)

#reset_leds()

for update in stub.SubscribeChange(request=request, metadata=metadata):
    
    print('got event: ', update.entity_id, update.action, update.entity_type)
    #if (update.timestamp.seconds < boot_time):
    #    entities[update.entity_id] = update
    #    print('still booting up....', update.timestamp.seconds, boot_time)
    #    continue

    if (update.entity_type == hook_pb2.EntityType.Value('DATA_OFFER')):
        entities[update.entity_id] = update
        print('got data offer..')
    elif (update.entity_type == hook_pb2.EntityType.Value('DATA_SUBSCRIPTION')):
        print('got data subscription..')
        # check if ds is registered already
        
        # if (update.action == hook_pb2.StateChangeAction.Value('UPDATED')):
            
        if (update.action == hook_pb2.StateChangeAction.Value('DELETED')):
            if (update.entity_id in entities):
                # remove consumer
                print('remove consumer')
                consumer_group = update.entity_id
                del active_consumers[consumer_group]
                del entities[update.entity_id]
        else:
            
            if (update.entity_id not in entities and update.entity_id not in active_consumers):
                # create consumer
                #print(update)
                data_offer_id = update.data_subscription.data_offer.id
                data_offer_state_id = entities[data_offer_id].data_offer.data_offer_state_id
                data_offer_state_transport_url = entities[data_offer_state_id].data_offer_state.transport_url
                transport_url = urlparse(data_offer_state_transport_url)
                broker = transport_url.netloc
                topic = parse_qs(transport_url.query)['topic'][0]
                consumer_group = update.entity_id
                active_consumers[consumer_group] = True
                x = threading.Thread(target=consume_from_kafka, args=(consumer_group, broker, topic,))
                x.start()
                print('create consumer based on subscription info', data_offer_id, data_offer_state_id, data_offer_state_transport_url, broker, topic)
            entities[update.entity_id] = update
    elif (update.entity_type == hook_pb2.EntityType.Value('DATA_OFFER_STATE')):
        print('got data offer state..')
        entities[update.entity_id] = update
    elif (update.entity_type == hook_pb2.EntityType.Value('DATA_SUBSCRIPTION_STATE')):
        print('got data subscription state..')
        entities[update.entity_id] = update
    #print(update.entity_id, update.entity_type, update.timestamp.seconds)
