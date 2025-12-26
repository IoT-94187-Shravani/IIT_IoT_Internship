import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
   status = message.payload.decode()

   if message.topic == "Light/Fan/AC":
      print("Light turned", status)

   elif message.topic == "Light/Fan/AC":
       print("Fan turned", status)

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

subscriber.on_message = on_message

subscriber.connect("localhost")

subscriber.subscribe("Light/Fan/AC")

subscriber.loop_forever()