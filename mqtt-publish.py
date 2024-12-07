# publisher.py

import json
import time
import random
import ssl
import paho.mqtt.client as mqtt
from constants import *

# Simulate vital signs within valid ranges
def simulate_vitals(patient_number):
    vitals = {
        "patient_number": patient_number,
        "heart_rate": random.randint(60, 100),                # beats per minute
        "blood_pressure_systolic": random.randint(110, 130),  # mm Hg
        "blood_pressure_diastolic": random.randint(70, 85),   # mm Hg
        "body_temperature": round(random.uniform(36.5, 37.5), 1),  # Celsius
        "oxygen_saturation": random.randint(95, 100),         # Percentage
        "respiration_rate": random.randint(12, 18),           # breaths per minute
        "blood_sugar_level": random.randint(70, 140),         # mg/dL
    }
    return vitals

# MQTT publish callback
def on_publish(client, userdata, mid):
    print("Message Published...")

# Create MQTT client and configure TLS
client = mqtt.Client()
client.tls_set(
    ca_certs=CA_CERT,
    certfile=CLIENT_CERT,
    keyfile=PRIVATE_KEY,
    tls_version=ssl.PROTOCOL_TLSv1_2
)
client.on_publish = on_publish

# Connect to AWS IoT Core
client.connect(AWS_IOT_ENDPOINT, MQTT_PORT)
client.loop_start()

try:
    while True:
        for patient_number in PATIENT_NUMBERS:
            vitals = simulate_vitals(patient_number)
            payload = json.dumps(vitals)
            topic = MQTT_TOPIC_BASE.format(patient_number=patient_number)
            client.publish(topic, payload)
            print(f"Published to {topic}: {payload}")
        time.sleep(PUBLISH_INTERVAL)
except KeyboardInterrupt:
    print("Publisher stopped.")
finally:
    client.loop_stop()
    client.disconnect()
