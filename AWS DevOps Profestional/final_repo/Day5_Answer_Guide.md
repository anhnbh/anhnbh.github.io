# 📚 AWS DevOps Professional Day 5 - Answer Guide

**Ngày tạo**: 31/10/2025  
**Mục đích**: Hướng dẫn đáp án đúng với giải thích chi tiết và tài liệu tham khảo

---

## Câu 73

**Loại**: Single Choice

**Câu hỏi**: A company has an application that runs on Amazon EC2 instances that are in an Auto Scaling group. When the application starts up. the application needs to process data from an Amazon S3 bucket before the application can start to serve requests. The size of the data that is stored in the S3 bucket is growing. When the Auto Scaling group adds new instances, the application now takes several minutes to download and process the data before the application can serve requests. The company must reduce the time that elapses before new EC2 instances are ready to serve requests. Which solution is the MOST cost-effective way to reduce the application startup time?

**Các lựa chọn**:

A. Configure a warm pool for the Auto Scaling group with warmed EC2 instances in the Stopped state. Configure an autoscaling:EC2_INSTANCE_LAUNCHING lifecycle hook on the Auto Scaling group. Modify the application to complete the lifecycle hook when the application is ready to serve requests. ✅

B. Increase the maximum instance count of the Auto Scaling group. Configure an autoscaling:EC2_INSTANCE_LAUNCHING lifecycle hook on the Auto Scaling group. Modify the application to complete the lifecycle hook when the application is ready to serve requests. ❌

C. Configure a warm pool for the Auto Scaling group with warmed EC2 instances in the Running state. Configure an autoscaling:EC2_INSTANCE_LAUNCHING lifecycle hook on the Auto Scaling group. Modify the application to complete the lifecycle hook when the application is ready to serve requests. ❌

D. Increase the maximum instance count of the Auto Scaling group. Configure an autoscaling:EC2_INSTANCE_LAUNCHING lifecycle hook on the Auto Scaling group. Modify the application to complete the lifecycle hook and to place the new instance in the Standby state when the application is ready to serve requests. ❌

**Đáp án đúng**: A

**Giải thích**: 
Warm pool với Stopped state là cost-effective nhất vì instances chỉ pay for storage, không pay for compute khi stopped. Pre-warmed instances đã có data processed sẵn, giảm startup time đáng kể.

**Tài liệu tham khảo**:
- [Auto Scaling Warm Pools](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html)

---

## Câu 74

**Loại**: Single Choice

**Câu hỏi**: A company is using an AWS CodeBuild project to build and package an application. The packages are copied to a shared Amazon S3 bucket before being deployed across multiple AWS accounts. The buildspec.yml file contains the following: The DevOps engineer has noticed that anybody with an AWS account is able to download the artifacts. What steps should the DevOps engineer take to stop this?

**Các lựa chọn**:

A. Modify the post_build command to use --acl public-read and configure a bucket policy that grants read access to the relevant AWS accounts only. ❌

B. Configure a default ACL for the S3 bucket that defines the set of authenticated users as the relevant AWS accounts only and grants read-only access. ❌

C. Create an S3 bucket policy that grants read access to the relevant AWS accounts and denies read access to the principal "*". ❌

D. Modify the post_build command to remove --acl authenticated-read and configure a bucket policy that allows read access to the relevant AWS accounts only. ✅

**Đáp án đúng**: D

**Giải thích**: 
Remove --acl authenticated-read để không grant access cho all authenticated AWS users. Bucket policy với specific AWS accounts provides proper access control.

**Tài liệu tham khảo**:
- [S3 Bucket Policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html)

---

## Câu 75

**Loại**: Single Choice

**Câu hỏi**: A company has developed a serverless web application that is hosted on AWS. The application consists of Amazon S3. Amazon API Gateway, several AWS Lambda functions, and an Amazon RDS for MySQL database. The company is using AWS CodeCommit to store the source code. The source code is a combination of AWS Serverless Application Model (AWS SAM) templates and Python code. A security audit and penetration test reveal that user names and passwords for authentication to the database are hardcoded within CodeCommit repositories. A DevOps engineer must implement a solution to automatically detect and prevent hardcoded secrets. What is the MOST secure solution that meets these requirements?

**Các lựa chọn**:

A. Enable Amazon CodeGuru Profiler. Decorate the handler function with @with_lambda_profiler(). Manually review the recommendation report. Write the secret to AWS Systems Manager Parameter Store as a secure string. Update the SAM templates and the Python code to pull the secret from Parameter Store. ❌

B. Associate the CodeCommit repository with Amazon CodeGuru Reviewer. Manually check the code review for any recommendations. Choose the option to protect the secret. Update the SAM templates and the Python code to pull the secret from AWS Secrets Manager. ✅

C. Enable Amazon CodeGuru Profiler. Decorate the handler function with @with_lambda_profiler(). Manually review the recommendation report. Choose the option to protect the secret. Update the SAM templates and the Python code to pull the secret from AWS Secrets Manager. ❌

D. Associate the CodeCommit repository with Amazon CodeGuru Reviewer. Manually check the code review for any recommendations. Write the secret to AWS Systems Manager Parameter Store as a string. Update the SAM templates and the Python code to pull the secret from Parameter Store. ❌

**Đáp án đúng**: B

**Giải thích**: 
CodeGuru Reviewer detects hardcoded secrets trong code. AWS Secrets Manager provides automatic rotation và better security cho database credentials hơn Parameter Store.

**Tài liệu tham khảo**:
- [CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/)
- [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/)

---

## Câu 76

**Loại**: Single Choice

**Câu hỏi**: A company is using Amazon S3 buckets to store important documents. The company discovers that some S3 buckets are not encrypted. Currently, the company's IAM users can create new S3 buckets without encryption. The company is implementing a new requirement that all S3 buckets must be encrypted. A DevOps engineer must implement a solution to ensure that server-side encryption is enabled on all existing S3 buckets and all new S3 buckets. The encryption must be enabled on new S3 buckets as soon as the S3 buckets are created. The default encryption type must be 256-bit Advanced Encryption Standard (AES-256). Which solution will meet these requirements?

**Các lựa chọn**:

A. Create an AWS Lambda function that is invoked periodically by an Amazon EventBridge scheduled rule. Program the Lambda function to scan all current S3 buckets for encryption status and to set AES-256 as the default encryption for any S3 bucket that does not have an encryption configuration. ❌

B. Set up and activate the s3-bucket-server-side-encryption-enabled AWS Config managed rule. Configure the rule to use the AWS-EnableS3BucketEncryption AWS Systems Manager Automation runbook as the remediation action. Manually run the re-evaluation process to ensure that existing S3 buckets are compliant. ✅

C. Create an AWS Lambda function that is invoked by an Amazon EventBridge event rule. Define the rule with an event pattern that matches the creation of new S3 buckets. Program the Lambda function to parse the EventBridge event, check the configuration of the S3 buckets from the event, and set AES-256 as the default encryption. ❌

D. Configure an IAM policy that denies the s3:CreateBucket action if the s3:x-amz-server-side-encryption condition key has a value that is not AES-256. Create an IAM group for all the company's IAM users. Associate the IAM policy with the IAM group. ❌

**Đáp án đúng**: B

**Giải thích**: 
AWS Config managed rule với Systems Manager Automation provides comprehensive solution cho both existing và new buckets. Automatic remediation ensures compliance.

**Tài liệu tham khảo**:
- [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html)
- [Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)

---

## Câu 77

**Loại**: Single Choice

**Câu hỏi**: A DevOps engineer is architecting a continuous development strategy for a company's software as a service (SaaS) web application running on AWS. For application and security reasons, users subscribing to this application are distributed across multiple Application Load Balancers (ALBs), each of which has a dedicated Auto Scaling group and fleet of Amazon EC2 instances. The application does not require a build stage, and when it is committed to AWS CodeCommit, the application must trigger a simultaneous deployment to all ALBs, Auto Scaling groups, and EC2 fleets. Which architecture will meet these requirements with the LEAST amount of configuration?

**Các lựa chọn**:

A. Create a single AWS CodePipeline pipeline that deploys the application in parallel using unique AWS CodeDeploy applications and deployment groups created for each ALB-Auto Scaling group pair. ❌

B. Create a single AWS CodePipeline pipeline that deploys the application using a single AWS CodeDeploy application and single deployment group. ❌

C. Create a single AWS CodePipeline pipeline that deploys the application in parallel using a single AWS CodeDeploy application and unique deployment group for each ALB-Auto Scaling group pair. ✅

D. Create an AWS CodePipeline pipeline for each ALB-Auto Scaling group pair that deploys the application using an AWS CodeDeploy application and deployment group created for the same ALB-Auto Scaling group pair. ❌

**Đáp án đúng**: C

**Giải thích**: 
Single CodeDeploy application với multiple deployment groups minimizes configuration. Parallel deployment ensures simultaneous updates across all environments.

**Tài liệu tham khảo**:
- [CodeDeploy Applications and Deployment Groups](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications.html)

---

## Câu 78

**Loại**: Single Choice

**Câu hỏi**: A company is hosting a static website from an Amazon S3 bucket. The website is available to customers at example.com. The company uses an Amazon Route 53 weighted routing policy with a TTL of 1 day. The company has decided to replace the existing static website with a dynamic web application. The dynamic web application uses an Application Load Balancer (ALB) in front of a fleet of Amazon EC2 instances. On the day of production launch to customers, the company creates an additional Route 53 weighted DNS record entry that points to the ALB with a weight of 255 and a TTL of 1 hour. Two days later, a DevOps engineer notices that the previous static website is displayed sometimes when customers navigate to example.com. How can the DevOps engineer ensure that the company serves only dynamic content for example.com?

**Các lựa chọn**:

A. Delete all objects, including previous versions, from the S3 bucket that contains the static website content. ❌

B. Update the weighted DNS record entry that points to the S3 bucket. Apply a weight of 0. Specify the domain reset option to propagate changes immediately. ❌

C. Configure webpage redirect requests on the S3 bucket with a hostname that redirects to the ALB. ❌

D. Remove the weighted DNS record entry that points to the S3 bucket from the example.com hosted zone. Wait for DNS propagation to become complete. ✅

**Đáp án đúng**: D

**Giải thích**: 
DNS caching với TTL 1 day means some clients still resolve to S3. Removing S3 DNS record completely ensures all traffic goes to ALB after DNS propagation.

**Tài liệu tham khảo**:
- [Route 53 Weighted Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted)

---

## Câu 79

**Loại**: Single Choice

**Câu hỏi**: A company is implementing AWS CodePipeline to automate its testing process. The company wants to be notified when the execution state fails and used the following custom event pattern in Amazon EventBridge: Which type of events will match this event pattern?

**Các lựa chọn**:

A. Failed deploy and build actions across all the pipelines ❌

B. All rejected or failed approval actions across all the pipelines ✅

C. All the events across all pipelines ❌

D. Approval actions across all the pipelines ❌

**Đáp án đúng**: B

**Giải thích**: 
Event pattern matches approval actions với state FAILED hoặc REJECTED. Không match deploy/build actions.

**Tài liệu tham khảo**:
- [CodePipeline Events](https://docs.aws.amazon.com/codepipeline/latest/userguide/detect-state-changes-cloudwatch-events.html)

---

## Câu 80

**Loại**: Single Choice

**Câu hỏi**: An application running on a set of Amazon EC2 instances in an Auto Scaling group requires a configuration file to operate. The instances are created and maintained with AWS CloudFormation. A DevOps engineer wants the instances to have the latest configuration file when launched, and wants changes to the configuration file to be reflected on all the instances with a minimal delay when the CloudFormation template is updated. Company policy requires that application configuration files be maintained along with AWS infrastructure configuration files in source control. Which solution will accomplish this?

**Các lựa chọn**:

A. In the CloudFormation template, add an AWS Config rule. Place the configuration file content in the rule's InputParameters property, and set the Scope property to the EC2 Auto Scaling group. Add an AWS Systems Manager Resource Data Sync resource to the template to poll for updates to the configuration. ❌

B. In the CloudFormation template, add an EC2 launch template resource. Place the configuration file content in the launch template. Configure the cfn-init script to run when the instance is launched, and configure the cfn-hup script to poll for updates to the configuration. ❌

C. In the CloudFormation template, add an EC2 launch template resource. Place the configuration file content in the launch template. Add an AWS Systems Manager Resource Data Sync resource to the template to poll for updates to the configuration. ❌

D. In the CloudFormation template, add CloudFormation init metadata. Place the configuration file content in the metadata. Configure the cfn-init script to run when the instance is launched, and configure the cfn-hup script to poll for updates to the configuration. ✅

**Đáp án đúng**: D

**Giải thích**: 
CloudFormation init metadata với cfn-init và cfn-hup provides native solution để manage configuration files trong CloudFormation templates với automatic updates.

**Tài liệu tham khảo**:
- [CloudFormation Init](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-init.html)
- [cfn-hup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-hup.html)

---
