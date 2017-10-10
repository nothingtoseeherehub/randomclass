#!/bin/bash
echo Script name: $0
echo $# arguments
if [ "$#" -ne 2 ]; then
    echo "Usage $0: UserName Password"
    exit 1
fi

STACKNAME=userforclass




aws cloudformation delete-stack --stack-name $STACKNAME
aws cloudformation wait stack-delete-complete --stack-name $STACKNAME

aws cloudformation  create-stack --stack-name $STACKNAME --capabilities CAPABILITY_NAMED_IAM \
--template-body file://./adduser.yml \
--parameters ParameterKey=Password,ParameterValue=$2 ParameterKey=EnteredUserName,ParameterValue=$1

aws cloudformation wait stack-create-complete --stack-name $STACKNAME
