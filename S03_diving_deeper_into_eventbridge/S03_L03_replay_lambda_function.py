# importing module
import logging

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to INFO
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    # Parsing incoming event data.
    instance_id = event["detail"]["instance-id"]
    instance_state = event["detail"]["state"]
    time = str(event["time"])

    # logging the state and instance id with a custom message.
    logger.info(
        f"We have just received notice that EC2 instance {instance_id} has just reached a state of {instance_state} at {time}."
    )
    logger.info(f"Please verify this is not in production.")
