import json
import boto3
import logging

ec2 = boto3.resource('ec2')

def start_ec2(event, context):
    filters = [{
            'Name': 'tag:environment', 
            'Values': ['qa'] 
        }
    ]
    
    instances = ec2.instances.filter(Filters=filters)
    
    stoppedInstances = [instance.id for instance in instances]
    
    
    if len(stoppedInstances) > 0:
        startingUp = ec2.instances.filter(InstanceIds=stoppedInstances).start()
    
def stop_ec2(event, context):
    filters = [{
            'Name': 'tag:environment',
            'Values': ['qa']
        }
    ]
    
    instances = ec2.instances.filter(Filters=filters)

    runningInstances = [instance.id for instance in instances]
    
    if len(runningInstances) > 0:
        shuttingDown = ec2.instances.filter(InstanceIds=runningInstances).stop()

