# Create an AWS IoT Rule

Next, we'll create an IoT Rule that listens to the MQTT topic and writes data to the DynamoDB table.

# Step-by-Step Guide

    Navigate to AWS IoT Core:
        In the AWS Console, go to Services and select IoT Core.

    Create a New Rule:
        In the left navigation pane, click on "Act".
        Click on "Rules".
        Click on "Create a rule".

    Configure the Rule:

        Rule Name: Enter store-patient-data.

        Description: Optional, e.g., Stores patient vital signs into DynamoDB.

# Rule Query Statement:

SELECT * FROM 'apolo/+/vitals'


# Set Up the DynamoDB Action:

    Under Set one or more actions, click Add action.
    Choose "Insert a message into a DynamoDB table".
    Click "Configure action".

# Configure the DynamoDB Action:

    Region: Select the AWS region where your DynamoDB table is located.

    Table name: Enter PatientVitals.

    Hash key value:
        Hash key name: patient_number
        Hash key value: ${patient_number}

    Range key value:
        Range key name: timestamp
        Range key value: ${timestamp}

# Set Up Permissions (Role Creation):

    Role name: Create a new role or use an existing one.
        Click on "Create new role".
        Name: Enter IoTRuleToDynamoDBRole.
        AWS will automatically create the necessary IAM role with permissions to write to the DynamoDB table.

    Click Add action.

Review and Create the Rule:

    Review the rule details.
    Click "Create rule".

