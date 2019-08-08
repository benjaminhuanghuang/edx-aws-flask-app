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
Go to EC2 dashboard -> connect -> copy the command
Get EC2 information:
$ curl http://169.254.169.254/latest/dynamic/instance-identity/document

## Create VPC () and run EC2 instance in it
Go CloudFormation to create and config the network