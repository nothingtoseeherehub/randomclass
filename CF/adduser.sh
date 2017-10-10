#!/bin/bash
echo Script name: $0
echo $# arguments
if [ "$#" -ne 2 ]; then
    echo "Usage $0: UserName Password"
    exit 1
fi



aws cloudformation  create-stack --stack-name userforclass --capabilities CAPABILITY_IAM \
--template-body file://./adduser.yml \
--parameters ParameterKey=Password,ParameterValue=$2 ParameterKey=EnteredUserName,ParameterValue=$1
