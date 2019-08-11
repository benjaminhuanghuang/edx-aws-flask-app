import boto3

client = boto3.client('cognito-idp')

client.list_user_pools(MaxResults = 5)
