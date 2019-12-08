import json
import boto3

account_id = boto3.client('sts').get_caller_identity()['Account']

def tag_ec2(instanceId,username):
    ec2 =  boto3.client('ec2')
    response = ec2.create_tags(
    Resources=[
        instanceId,
    ],
    Tags=[
        {
            'Key': 'createBy',
            'Value': username
        },
    ]
    )
    print (response)
    
def tag_rds(elements,username):
    rds = boto3.client('rds')
    arn = elements["dBInstanceArn"]
    if elements["dBClusterIdentifier"] == None:
        cluster = "None"
    else:
        cluster = elements["dBClusterIdentifier"]
        clusterArn = "arn:aws:rds:us-east-1:"+account_id+":cluster:"+cluster
    response_db = rds.add_tags_to_resource(
        ResourceName=arn,
        Tags=[
            {
                'Key':'createBy',
                'Value': username
            }
            ]
    )
    response_cluster = rds.add_tags_to_resource(
        ResourceName=clusterArn,
        Tags=[
            {
                'Key': 'createBy',
                'Value': username
            }
            ]
    )
    print (response_db)
    print (response_cluster)

def lambda_handler(event, context):
    # TODO implement
    if "userName" in event["detail"]["userIdentity"].keys():
        username = event["detail"]["userIdentity"]["userName"]
    else:
        username="cloudformation"
    Source = event["source"]
    print ("Username: "+username)
    print ("Source: "+Source)
    if event["source"] == "aws.ec2":
        tag_ec2(event["detail"]["responseElements"]["instancesSet"]["items"][0]["instanceId"],username)
    if event["source"] == "aws.rds":
        tag_rds(event["detail"]["responseElements"],username)
        
    return {
        'statusCode': 200,
        'body': event
    }
