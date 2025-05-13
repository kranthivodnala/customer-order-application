# Lambda function to handle requests from the API Gateway
import json
import boto3
import os
from botocore.exceptions import ClientError
from datetime import datetime

# Intialize the SQS and SNS Clients
sqs = boto3.client('sqs')
sqs = boto3.cleint('sns')

SQS_URL = os.environ['SQS_URL']
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):
    body = json.loads(event['body'])
    item = body.get('item')
    quantity = body.get('quantity')

    order = {
        'item': item,
        'quantity': quantity,
        'timestamp': datetime.utcnow().isoformat()
    }

    # Send the order to SQS
    sqs.send_message(
        QueueUrl=SQS_URL,
        MessageBody=json.dumps(order)
    )

    # Send a notification to SNS
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject='New Order Received',
        Message=f"Order: {item} (x{quantity}) received at {order['timestamp']}"
    )

    return {
        'statusCode': 200,
        'headers': { "Access-Control-Allow-Origin":  },
        'body': json.dumps({
            'message': 'Order received successfully',
        })
    }
