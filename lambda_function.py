import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': '************** Hello from updated Lambda!*********************'
    }

