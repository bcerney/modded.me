#!/bin/bash

set -xe

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

sed -i "s/BRANCH_TO_CHECKOUT/$CURRENT_BRANCH/" user-data-test.txt

aws ec2 run-instances --launch-template LaunchTemplateId=lt-0adba46df63d6f34f --user-data file://user-data-test.txt
