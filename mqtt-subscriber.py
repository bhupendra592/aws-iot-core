# subscriber.py

import ssl
import paho.mqtt.client as mqtt
from constants import *
import json

# MQTT message callback
def on_message(client, userdata, msg):
    # Extract the patient number from the topic
    topic_parts = msg.topic.split('/')
    if len(topic_parts) >= 3:
        patient_number = topic_parts[1]
    else:
        patient_number = "Unknown"

    # Decode and parse the payload
    payload_str = msg.payload.decode()
    try:
        payload = json.loads(payload_str)
    except json.JSONDecodeError:
        print(f"Invalid JSON payload from patient {patient_number}: {payload_str}")
        return

    print(f"Received data from patient {patient_number}: {payload}")

    # Additional processing can be added here
    # For example, storing data in a database or triggering alerts

# Create MQTT client and configure TLS
client = mqtt.Client()
client.tls_set(
    ca_certs=CA_CERT,
    certfile=CLIENT_CERT,
    keyfile=PRIVATE_KEY,
    tls_version=ssl.PROTOCOL_TLSv1_2
)
client.on_message = on_message

# Connect and subscribe to the topic with wildcard '+'
client.connect(AWS_IOT_ENDPOINT, MQTT_PORT)
client.subscribe("apolo/+/vitals")  # Subscribe to all patient vitals topics
print("Subscriber is listening to apolo/+/vitals topics...")
client.loop_forever()
