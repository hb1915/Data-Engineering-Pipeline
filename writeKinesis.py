import json
import boto3

def lambda_handler(event, context):
    
    print("MyEvent:")
    print(event)
    
    method = event['context']['http-method']
    
    if method == "GET":
        .
        dynamo_client = boto3.client('dynamodb')
        
        im_customerID = event['params']['querystring']['CustomerID']
        print(im_customerID)
        response = dynamo_client.get_item(TableName = 'Customers', Key = {'CustomerID':{'N': im_customerID}})
        print(response['Item'])
        
        
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item']) 
           }
    
    elif method == "POST":
    
        p_record = event['body-json']
        recordstring = json.dumps(p_record)
        
        client = boto3.client('kinesis')
        response = client.put_record(
            StreamName='kinesis_stream_1',
            Data= recordstring,
            PartitionKey='string'
        )
            
        return {
            'statusCode': 200,
            'body': json.dumps(p_record)
        }
    else:
        return {
            'statusCode': 501,
            'body': json.dumps("Server Error")
        }