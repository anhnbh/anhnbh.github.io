import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    # Extract from user-agent header
    user_agent = event.get('headers', {}).get('user-agent', 'unknown')
    version = extract_version(user_agent)
    operation = event.get('path', 'unknown')
    
    # Simulate response
    response_code = 200
    
    # Log structured data for CloudWatch metric filter
    logger.info(f"API_METRIC operation={operation} version={version} response_code={response_code}")
    
    return {
        'statusCode': response_code,
        'body': json.dumps({'message': 'success'})
    }

def extract_version(user_agent):
    # Extract version from user-agent
    return user_agent.split('/')[-1] if '/' in user_agent else 'v1.0'