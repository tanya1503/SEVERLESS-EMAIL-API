import json
import boto3

def send_email(event, context):
    body = json.loads(event['body'])
    receiver = body.get('receiver_email')
    subject = body.get('subject')
    message = body.get('body_text')

    if not receiver or not subject or not message:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing fields"})
        }

    ses = boto3.client('ses', region_name='us-east-1')

    try:
        response = ses.send_email(
            Source='tanyagoyal1503@gmail.com',
            Destination={'ToAddresses':['tanyagoyal1503@gmail.com']},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': message}}
            }
        )
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent", "MessageId": response['MessageId']})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
