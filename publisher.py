from PIL import ImageSequence, Image
import json
from confluent_kafka import Producer, KafkaError
import time
import sys

if len(sys.argv) != 4:
    sys.stderr.write('Usage: %s <bootstrap-brokers> <topic> <gif-filename>\n' % sys.argv[0])
    sys.exit(1)

broker = sys.argv[1]
topic = sys.argv[2]
gif_filename = sys.argv[3]

im = Image.open(gif_filename)
im.seek(0)

#broker = 'pkc-e8mp5.eu-west-1.aws.confluent.cloud:9092'
#topic = 'launchpad1'
  
print('START producing to kafka')
p = Producer({
    'bootstrap.servers': broker,
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'acks': 0,
    'sasl.username': 'username_to_change', 
    'sasl.password': 'password_to_change'
    })

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

while True:
  counter = 0
  for im in ImageSequence.Iterator(im):
      current_time = int(time.time())
      width, height = im.size
      rgb_im = im.convert('RGB')
      gif_json = {}
      for x in range(8):
          for y in range(8):
              r, g, b = rgb_im.getpixel((x, y))
              gif_json["p" + str(x + 1) + str(y + 1)] = [r,g,b]
              #time.sleep(0.1)
              #pixels = im.getdata()
      time.sleep(0.15)
      #p.poll(0)
      p.produce(topic, json.dumps(gif_json).encode('utf-8'), callback=delivery_report, partition=0)
      #p.flush()

      #print(json.dumps(gif_json))
      print("SENT frame ", counter, current_time)
      counter = counter + 1
      # pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
      #print(pixels[0], pixels[0+1*8], pixels[0+2*8], pixels[0+3*8], pixels[0+4*8], pixels[0+5*8], pixels[0+6*8], pixels[0+7*8])
      # client.publish("launchpad/led/row1","127", qos=0, retain=False)
