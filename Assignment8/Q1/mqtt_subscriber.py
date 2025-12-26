import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    topic = message.topic
    value = float(message.payload.decode())

    if topic == "sensor/ldr":
       
        print(f"LDR Data Saved: {value}")

    elif topic == "sensor/lm35":
       
        print(f"Temperature Data Saved: {value} °C") 

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

subscriber.on_message = on_message

subscriber.connect("localhost")

subscriber.subscribe("sensor/ldr")
subscriber.subscribe("sensor/lm35")

subscriber.loop_forever()