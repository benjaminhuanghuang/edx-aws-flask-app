# AWS Developer: Building on AWS
https://courses.edx.org/courses/course-v1:AWS+OTP-AWSD1+2T2019/course/



## Create account


## Exercise 1: Billing Alert
My account -> Preferences -> check Receive Free Tier Usage Alerts and fill Email Address
-> Receive Billing Alerts


## Exercise 2: Create EC2 instance
Go to EC2 dashboard -> Launch instance 
1. Choose **AMI** (Amazon Machine Image) (Amazon Linux AMI) 
2. Choose an **Instance Type**  -> Next
3. Configure Instance Details ->
4. Add Storage
5. Add Tag
6. Configure **Security Group**
7. Review Instance Launch , Create and Download **Key Pair**


## Connect to EC2
Go to EC2 dashboard -> connect -> copy the command to connect to EC2

To view the instance metadata:
```
curl http://169.254.169.254/latest/meta-data/
```

Get the instance identity document:
```
$ curl http://169.254.169.254/latest/dynamic/instance-identity/document
```

## Create VPC (Virtual Private Cloud correct) and run EC2 instance in it
Go CloudFormation to create and config the network
A stack is an instance of template


## Create user and setup credential
1. Setup credential (AWS_ACCESS_KEY and AWS_SECUET_KEY)
Go to IAM dashboard -> users
Create user -> Create group and select policy 
Download access key and secrect key

2. Install access key to EC2
Go to EC2 dashboard -> select instance -> click connect
```
  ssh -i "BenAWSLab.pem" ec2-user@ec2-54-184-96-39.us-west-2.compute.amazonaws.com
```
Install keys to EC2
```
  $ aws configure
```
Test
```
  $ aws ec2 describe-instances
```

3. Install python and boto3
```
sudo yum -y install python36
sudo pip-3.6 install boto3
```

## S3
```
https://<bucket name>/key
```
S3 Access Control
- Policies
- IAM users / Groups
- Access Control list

## Download app source code
```
wget https://us-west-2-tcdev.s3.amazonaws.com/courses/AWS-100-ADG/v1.1.0/exercises/ex-s3-upload.zip
```

## Amazon Recognition
