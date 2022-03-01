import boto3
import json
import logging

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to INFO
logger.setLevel(logging.INFO)

region = "us-east-1"
ec2_client = boto3.client("ec2", region_name=region)


def lambda_handler(event, context):
    logger.info(f"Received event: " + json.dumps(event))
    instances = [event["detail"]["instance-id"]]
    ec2_client.start_instances(InstanceIds=instances)

    logger.info(
        f"Prod EC2 Instances Stopped - Restarting the following now: {str(instances)}"
    )
