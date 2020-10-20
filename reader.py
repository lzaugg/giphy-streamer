from PIL import ImageSequence, Image
import json
import paho.mqtt.client as mqtt
import time

im = Image.open("video.gif")
im.seek(0)

def on_connect(client, userdata, flags, rc):
  print("Connected: " + str(rc))
  client.publish("/launchpad/led/all" ,"0", qos=0, retain=False)

def on_message(client, userdata, msg):
  #print("Received: " + msg.topic + " " + str(msg.payload))
  #if msg.topic == "temp/test":
  #  if str(msg.payload) != "":
  #    print("Message on: " + str(datetime.datetime.now()) + " - topic: " + msg.topic + ", payload: " + str(msg.payload))
  pass

def on_publish(mosq, obj, mid):
  #print("Publish mid: " + str(mid))
  pass

def on_subscribed(mosq, obj, mid, granted_qos):
  print("Subscribed: " + str(mid) + ", qos: " + str(granted_qos))

def on_log(mosq, obj, mid, string):
  print("Log: " + str(string))
  pass

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribed = on_subscribed
client.on_log = on_log

client.username_pw_set("username_to_set", "password_to_set")
client.connect("192.168.0.89", port=1883, keepalive=60,)
# published to exchange amq.topic; needs binding to PAD
#client.subscribe("launchpad/#", 0)
client.loop_start()
time.sleep(1)
for im in ImageSequence.Iterator(im):
    width, height = im.size
    rgb_im = im.convert('RGB')
    gif_json = {}
    for x in range(8):
        for y in range(8):
            r, g, b = rgb_im.getpixel((x, y))
            topic = "launchpad/led/" + "p" + str(x + 1) + str(y + 1)
            value = ",".join([str(p) for p in rgb_im.getpixel((x, y))])
            print(topic, value)
            client.publish(topic ,value, qos=0, retain=False)
            gif_json["p" + str(x + 1) + str(y + 1)] = [r,g,b]
            #time.sleep(0.1)
            #pixels = im.getdata()
    time.sleep(0.3  )
    #print(json.dumps(gif_json))
    # pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    #print(pixels[0], pixels[0+1*8], pixels[0+2*8], pixels[0+3*8], pixels[0+4*8], pixels[0+5*8], pixels[0+6*8], pixels[0+7*8])
    # client.publish("launchpad/led/row1","127", qos=0, retain=False)

#time.sleep(10)
client.disconnect()
