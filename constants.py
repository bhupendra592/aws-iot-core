# constants.py

# AWS_IOT_ENDPOINT = "your-aws-iot-endpoint.amazonaws.com"
# CA_CERT = "path/to/AmazonRootCA1.pem"
# CLIENT_CERT = "path/to/your-certificate.pem.crt"
# PRIVATE_KEY = "path/to/your-private.pem.key"
# constants.py

AWS_IOT_ENDPOINT = "xxxxxx-ats.iot.ap-south-1.amazonaws.com" # get from security section
CA_CERT = "./AmazonRootCA1.pem"
CLIENT_CERT = "./example-certificate.pem.crt"
PRIVATE_KEY = "./example-private.pem.key"

MQTT_PORT = 8883

# List of patient numbers for simulation
PATIENT_NUMBERS = ["12345", "67890", "11223"]  # Replace with actual patient numbers

# MQTT topic base with placeholder for patient number
MQTT_TOPIC_BASE = "apolo/{patient_number}/vitals"

PUBLISH_INTERVAL = 60  # Interval in seconds

