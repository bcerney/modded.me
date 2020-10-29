#!/bin/bash

set -xe

cp user-data-test.example user-data-test.txt

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

sed -i "s/BRANCH_TO_CHECKOUT/$CURRENT_BRANCH/" user-data-test.txt

INSTANCE_ID=$(aws ec2 run-instances \
  --launch-template LaunchTemplateId=lt-0adba46df63d6f34f \
  --user-data file://user-data-test.txt \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Env,Value=test-latest}]' \
  --query "Instances[*].[InstanceId]" \
  --output text)

  aws ec2 wait instance-running \
  --instance-ids $INSTANCE_ID \
  --no-paginate


EIP_ALLOC=$(aws ec2 describe-addresses --query "Addresses[*].[AllocationId]" --output text)


aws ec2 associate-address \
  --allocation-id $EIP_ALLOC \
  --instance-id $INSTANCE_ID