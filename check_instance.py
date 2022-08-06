#!/opt/homebrew/bin/python3
import boto3
from tabulate import tabulate

#Make sure you are in the desired region.
AWS_REGION = "us-east-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
instance_state = ""
instance_id = ""
privateipv4 = ""


#Gather all ec2 instances in the specified AWS_REGION
instances = EC2_RESOURCE.instances.all()

#Create a empty list
instance_list = []

#Loop through every instance and gather the instance state, ID, and Private Ipv4 address
for instance in instances:

    
    instance_state = instance.state["Name"]
    instance_id = instance.id
    privateipv4 = instance.private_ip_address
    print(f'EC2 instance {instance.id}" information:')
    print(f'Instance state: {instance.state["Name"]}')
    print(f'Private IPv4 address: {instance.private_ip_address}')
    print(f'Public IPv4 address: {instance.public_ip_address}')
    #print(f'Instance AMI: {instance.image.id}')
    #print(f'Instance platform: {instance.platform}')
    #print(f'Instance type: "{instance.instance_type}')
    print('-'*60)
    ec2dict = {"Instance State":instance.state["Name"], "Instance ID": instance.id, "Private IPv4":instance.private_ip_address}
    instance_list.append(ec2dict.values())

    
## Python program to understand the usage of tabulate function for printing tables in a tabular format
print (tabulate(instance_list, headers=["Instance State","Instance ID","Private ipv4"]))

   

