import boto3

def list_ec2_instances():
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Retrieve information about all EC2 instances
    response = ec2.describe_instances()


    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
           print(f"Instance ID: {instance['InstanceId']}")
           print(f"Instance Type: {instance['InstanceType']}")
           print(f"State: {instance['State']['Name']}")
           print("------------------------------")
if __name__ == "__main__":
        list_ec2_instances()