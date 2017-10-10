#!/bin/bash
echo Script name: $0
echo $# arguments
if [$# -ne 1];
    then echo "Usage $0: UserName Password"
    exit 1
fi



aws cloudformation  create-stack --stack-name userforclass \
--template-body file:./adduser.yml \
ParameterKey=Password,ParameterValue=$2 ParameterKey=Name,ParameterValue=$1
