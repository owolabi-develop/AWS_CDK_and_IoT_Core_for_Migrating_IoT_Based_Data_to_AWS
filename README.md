## Project Under developement



## End to end iot data migration from mysql to aws  

Aim
is to use AWS IoT device Simulator to replicate an On-Premise Data Center infrastructure by ingesting real-time IoT-based ecommarce data to kinesisFirehose and then use lambda funtion to write the data to mysql database on ec2 instance on a private vpc. The second process is migrating and analyzing the data to “AWS Cloud Premise” using DMS, RDS, Glue, AWS Timestream, and QuickSight.
 Infrastructure-as-a-Code (IaC) using AWS CDK (Cloud Development Kit).

Data Description
Using the Device Simulator, to simulate and deal with the ecommarce data parallelly   

Tech Stack:
Framework: AWS CDK

Language: Python
Services: AWS IoT core, Kinesis Firehose, AWS Lambda, MariaDB, AWS S3, AWS Secrets Manager, AWS CloudFormation

## Project Architechure
![alt text](digramphoto/aws_arch7.png)
