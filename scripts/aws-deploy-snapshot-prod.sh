#!/bin/bash

set -xe

cp scripts/user-data-prod.example scripts/user-data-prod.txt

# Get prod EBS SnapshotId
SNAPSHOT_ID=$(aws ec2 describe-snapshots --filters Name=tag:Env,Values=prod --query "Snapshots[*].[SnapshotId]" --output text)

# https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html
INSTANCE_ID=$(aws ec2 run-instances \
  --launch-template LaunchTemplateId=lt-0adba46df63d6f34f \
  --block-device-mappings \
  "DeviceName=/dev/sdb,Ebs={DeleteOnTermination=true,SnapshotId=$SNAPSHOT_ID,VolumeSize=20,VolumeType=gp2}" \
  --user-data file://scripts/user-data-prod.txt \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Env,Value=prod}]' \
  --query "Instances[*].[InstanceId]" \
  --output text)

aws ec2 wait instance-running \
  --instance-ids $INSTANCE_ID \
  --no-paginate

EIP_ALLOC=$(aws ec2 describe-addresses --query "Addresses[*].[AllocationId]" --output text)

aws ec2 associate-address \
  --allocation-id $EIP_ALLOC \
  --instance-id $INSTANCE_ID

./scripts/wait-for-it.sh www.modded_me:80 -- echo "modded_me is UP"
