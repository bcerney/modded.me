#!/bin/bash

set -xe

# INSTANCE_ID=$(curl http://169.254.169.254/latest/meta-data/instance-id)

# Current EBS volumes ID
VOLUME_ID=$(aws ec2 describe-volumes --filters Name=attachment.device,Values=/dev/sdb Name=tag:Env,Values=test-latest --query "Volumes[*].VolumeId" --output text)

# Latest 
SNAPSHOT_ID=$(aws ec2 describe-snapshots --filters Name=tag:Env,Values=test-latest --query "Snapshots[*].[SnapshotId]" --output text)

aws ec2 create-snapshot --volume-id $VOLUME_ID --tag-specifications 'ResourceType=snapshot,Tags=[{Key=Env,Value=test-latest}]'

aws ec2 delete-snapshot --snapshot-id $SNAPSHOT_ID
