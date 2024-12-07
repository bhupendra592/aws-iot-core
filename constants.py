# constants.py

# AWS_IOT_ENDPOINT = "your-aws-iot-endpoint.amazonaws.com"
# CA_CERT = "path/to/AmazonRootCA1.pem"
# CLIENT_CERT = "path/to/your-certificate.pem.crt"
# PRIVATE_KEY = "path/to/your-private.pem.key"
# constants.py

AWS_IOT_ENDPOINT = "a2yl03138096o1-ats.iot.ap-south-1.amazonaws.com"
CA_CERT = "./AmazonRootCA1.pem"
CLIENT_CERT = "./3737782a99d57a2d7e6fc3f3263f327a8a5b992d6f61454e3b9fd465485a083b-certificate.pem.crt"
PRIVATE_KEY = "./3737782a99d57a2d7e6fc3f3263f327a8a5b992d6f61454e3b9fd465485a083b-private.pem.key"

MQTT_PORT = 8883

# List of patient numbers for simulation
PATIENT_NUMBERS = ["12345", "67890", "11223"]  # Replace with actual patient numbers

# MQTT topic base with placeholder for patient number
MQTT_TOPIC_BASE = "apolo/{patient_number}/vitals"

PUBLISH_INTERVAL = 60  # Interval in seconds

