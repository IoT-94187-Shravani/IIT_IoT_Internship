import paho.mqtt.client as mqtt
import random
import time

def on_publish(client, userdata, mid, reason_code, properties):
  
    ldr_value = random.randint(0, 1023)       
    temp_value = round(random.uniform(20, 35), 2)  

    client.publish("sensor/ldr", ldr_value)
    client.publish("sensor/lm35", temp_value)

    print(f"Published LDR: {ldr_value}")
    print(f"Published Temperature: {temp_value} °C")

    time.sleep(5)
   
publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

publisher.on_publish = on_publish

publisher.connect("localhost")

publisher.publish("sensor/ldr", 2048)
publisher.publish("sensor/lm35", 2048)

publisher.disconnect()