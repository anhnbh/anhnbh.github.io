# AWS DevOps Practice Test - MultipleChoice

**Số câu**: 103  
**Ngày tạo**: 20/10/2025 09:44

---

## Câu 1

**ID**: 6 | **Loại**: Multiple Choice

A company must encrypt all AMIs that the company shares across accounts. A DevOps engineer has access to a source account where an unencrypted custom AMI has been built. The DevOps engineer also has access to a target account where an Amazon EC2 Auto Scaling group will launch EC2 instances from the AMI. The DevOps engineer must share the AMI with the target account.The company has created an AWS Key Management Service (AWS KMS) key in the source account.Which additional steps should the DevOps engineer perform to meet the requirements? (Choose three.)

A. In the source account, copy the unencrypted AMI to an encrypted AMI. Specify the KMS key in the copy action.

B. In the source account, copy the unencrypted AMI to an encrypted AMI. Specify the default Amazon Elastic Block Store (Amazon EBS) encryption key in the copy action.

C. In the source account, create a KMS grant that delegates permissions to the Auto Scaling group service-linked role in the target account.

D. In the source account, modify the key policy to give the target account permissions to create a grant. In the target account, create a KMS grant that delegates permissions to the Auto Scaling group service-linked role.

E. In the source account, share the unencrypted AMI with the target account.

F. In the source account, share the encrypted AMI with the target account.

**Đáp án**: ___________

---

## Câu 2

**ID**: 7 | **Loại**: Multiple Choice

A company uses AWS CodePipeline pipelines to automate releases of its application A typical pipeline consists of three stages build, test, and deployment. The company has been using a separate AWS CodeBuild project to run scripts for each stage. However, the company now wants to use AWS CodeDeploy to handle the deployment stage of the pipelines.The company has packaged the application as an RPM package and must deploy the application to a fleet of Amazon EC2 instances. The EC2 instances are in an EC2 Auto Scaling group and are launched from a common AMI.Which combination of steps should a DevOps engineer perform to meet these requirements? (Choose two.)

A. Create a new version of the common AMI with the CodeDeploy agent installed. Update the IAM role of the EC2 instances to allow access to CodeDeploy.

B. Create a new version of the common AMI with the CodeDeploy agent installed. Create an AppSpec file that contains application deployment scripts and grants access to CodeDeploy.

C. Create an application in CodeDeploy. Configure an in-place deployment type. Specify the Auto Scaling group as the deployment target. Add a step to the CodePipeline pipeline to use EC2 Image Builder to create a new AMI. Configure CodeDeploy to deploy the newly created AMI.

D. Create an application in CodeDeploy. Configure an in-place deployment type. Specify the Auto Scaling group as the deployment target. Update the CodePipeline pipeline to use the CodeDeploy action to deploy the application.

E. Create an application in CodeDeploy. Configure an in-place deployment type. Specify the EC2 instances that are launched from the common AMI as the deployment target. Update the CodePipeline pipeline to use the CodeDeploy action to deploy the application.

**Đáp án**: ___________

---

## Câu 3

**ID**: 8 | **Loại**: Multiple Choice

A company’s security team requires that all external Application Load Balancers (ALBs) and Amazon API Gateway APIs are associated with AWS WAF web ACLs. The company has hundreds of AWS accounts, all of which are included in a single organization in AWS Organizations. The company has configured AWS Config for the organization. During an audit, the company finds some externally facing ALBs that are not associated with AWS WAF web ACLs.Which combination of steps should a DevOps engineer take to prevent future violations? (Choose two.)

A. Delegate AWS Firewall Manager to a security account.

B. Delegate Amazon GuardDuty to a security account.

C. Create an AWS Firewall Manager policy to attach AWS WAF web ACLs to any newly created ALBs and API Gateway APIs.

D. Create an Amazon GuardDuty policy to attach AWS WAF web ACLs to any newly created ALBs and API Gateway APIs.

E. Configure an AWS Config managed rule to attach AWS WAF web ACLs to any newly created ALBs and API Gateway APIs.

**Đáp án**: ___________

---

## Câu 4

**ID**: 11 | **Loại**: Multiple Choice

An ecommerce company has chosen AWS to host its new platform. The company's DevOps team has started building an AWS Control Tower landing zone. The DevOps team has set the identity store within AWS IAM Identity Center (AWS Single Sign-On) to external identity provider (IdP) and has configured SAML 2.0.The DevOps team wants a robust permission model that applies the principle of least privilege. The model must allow the team to build and manage only the team's own resources.Which combination of steps will meet these requirements? (Choose three.)

A. Create IAM policies that include the required permissions. Include the aws:PrincipalTag condition key.

B. Create permission sets. Attach an inline policy that includes the required permissions and uses the aws:PrincipalTag condition key to scope the permissions.

C. Create a group in the IdP. Place users in the group. Assign the group to accounts and the permission sets in IAM Identity Center.

D. Create a group in the IdP. Place users in the group. Assign the group to OUs and IAM policies.

E. Enable attributes for access control in IAM Identity Center. Apply tags to users. Map the tags as key-value pairs.

F. Enable attributes for access control in IAM Identity Center. Map attributes from the IdP as key-value pairs.

**Đáp án**: ___________

---

## Câu 5

**ID**: 12 | **Loại**: Multiple Choice

An ecommerce company is receiving reports that its order history page is experiencing delays in reflecting the processing status of orders. The order processing system consists of an AWS Lambda function that uses reserved concurrency. The Lambda function processes order messages from an Amazon Simple Queue Service (Amazon SQS) queue and inserts processed orders into an Amazon DynamoDB table. The DynamoDB table has auto scaling enabled for read and write capacity.Which actions should a DevOps engineer take to resolve this delay? (Choose two.)

A. Check the ApproximateAgeOfOldestMessage metric for the SQS queue. Increase the Lambda function concurrency limit.

B. Check the ApproximateAgeOfOldestMessage metnc for the SQS queue Configure a redrive policy on the SQS queue.

C. Check the NumberOfMessagesSent metric for the SQS queue. Increase the SQS queue visibility timeout.

D. Check the WriteThrottleEvents metric for the DynamoDB table. Increase the maximum write capacity units (WCUs) for the table's scaling policy.

E. Check the Throttles metric for the Lambda function. Increase the Lambda function timeout.

**Đáp án**: ___________

---

## Câu 6

**ID**: 23 | **Loại**: Multiple Choice

A company has an AWS CodePipeline pipeline that is configured with an Amazon S3 bucket in the eu-west-1 Region. The pipeline deploys an AWS Lambda application to the same Region. The pipeline consists of an AWS CodeBuild project build action and an AWS CloudFormation deploy action.The CodeBuild project uses the aws cloudformation package AWS CLI command to build an artifact that contains the Lambda function code’s .zip file and the CloudFormation template. The CloudFormation deploy action references the CloudFormation template from the output artifact of the CodeBuild project’s build action.The company wants to also deploy the Lambda application to the us-east-1 Region by using the pipeline in eu-west-1. A DevOps engineer has already updated the CodeBuild project to use the aws cloudformation package command to produce an additional output artifact for us-east-1.Which combination of additional steps should the DevOps engineer take to meet these requirements? (Choose two.)

A. Modify the CloudFormation template to include a parameter for the Lambda function code’s zip file location. Create a new CloudFormation deploy action for us-east-1 in the pipeline. Configure the new deploy action to pass in the us-east-1 artifact location as a parameter override.

B. Create a new CloudFormation deploy action for us-east-1 in the pipeline. Configure the new deploy action to use the CloudFormation template from the us-east-1 output artifact.

C. Create an S3 bucket in us-east-1. Configure the S3 bucket policy to allow CodePipeline to have read and write access.

D. Create an S3 bucket in us-east-1. Configure S3 Cross-Region Replication (CRR) from the S3 bucket in eu-west-1 to the S3 bucket in us-east-1.

E. Modify the pipeline to include the S3 bucket for us-east-1 as an artifact store. Create a new CloudFormation deploy action for us-east-1 in the pipeline. Configure the new deploy action to use the CloudFormation template from the us-east-1 output artifact.

**Đáp án**: ___________

---

## Câu 7

**ID**: 29 | **Loại**: Multiple Choice

A company has an organization in AWS Organizations. The organization includes workload accounts that contain enterprise applications. The company centrally manages users from an operations account. No users can be created in the workload accounts. The company recently added an operations team and must provide the operations team members with administrator access to each workload account.Which combination of actions will provide this access? (Choose three.)

A. Create a SysAdmin role in the operations account. Attach the AdministratorAccess policy to the role. Modify the trust relationship to allow the sts:AssumeRole action from the workload accounts.

B. Create a SysAdmin role in each workload account. Attach the AdministratorAccess policy to the role. Modify the trust relationship to allow the sts:AssumeRole action from the operations account.

C. Create an Amazon Cognito identity pool in the operations account. Attach the SysAdmin role as an authenticated role.

D. In the operations account, create an IAM user for each operations team member.

E. In the operations account, create an IAM user group that is named SysAdmins. Add an IAM policy that allows the sts:AssumeRole action for the SysAdmin role in each workload account. Add all operations team members to the group.

F. Create an Amazon Cognito user pool in the operations account. Create an Amazon Cognito user for each operations team member.

**Đáp án**: ___________

---

## Câu 8

**ID**: 32 | **Loại**: Multiple Choice

A company is implementing an Amazon Elastic Container Service (Amazon ECS) cluster to run its workload. The company architecture will run multiple ECS services on the cluster. The architecture includes an Application Load Balancer on the front end and uses multiple target groups to route traffic.A DevOps engineer must collect application and access logs. The DevOps engineer then needs to send the logs to an Amazon S3 bucket for near-real-time analysis.Which combination of steps must the DevOps engineer take to meet these requirements? (Choose three.)

A. Download the Amazon CloudWatch Logs container instance from AWS. Configure this instance as a task. Update the application service definitions to include the logging task.

B. Install the Amazon CloudWatch Logs agent on the ECS instances. Change the logging driver in the ECS task definition to awslogs.

C. Use Amazon EventBridge to schedule an AWS Lambda function that will run every 60 seconds and will run the Amazon CloudWatch Logs create-export-task command. Then point the output to the logging S3 bucket.

D. Activate access logging on the ALB. Then point the ALB directly to the logging S3 bucket.

E. Activate access logging on the target groups that the ECS services use. Then send the logs directly to the logging S3 bucket.

F. Create an Amazon Kinesis Data Firehose delivery stream that has a destination of the logging S3 bucket. Then create an Amazon CloudWatch Logs subscription filter for Kinesis Data Firehose.

**Đáp án**: ___________

---

## Câu 9

**ID**: 36 | **Loại**: Multiple Choice

A DevOps engineer needs to back up sensitive Amazon S3 objects that are stored within an S3 bucket with a private bucket policy using S3 cross-Region replication functionality. The objects need to be copied to a target bucket in a different AWS Region and account.Which combination of actions should be performed to enable this replication? (Choose three.)

A. Create a replication IAM role in the source account

B. Create a replication I AM role in the target account.

C. Add statements to the source bucket policy allowing the replication IAM role to replicate objects.

D. Add statements to the target bucket policy allowing the replication IAM role to replicate objects.

E. Create a replication rule in the source bucket to enable the replication.

F. Create a replication rule in the target bucket to enable the replication.

**Đáp án**: ___________

---

## Câu 10

**ID**: 37 | **Loại**: Multiple Choice

A company has multiple member accounts that are part of an organization in AWS Organizations. The security team needs to review every Amazon EC2 security group and their inbound and outbound rules. The security team wants to programmatically retrieve this information from the member accounts using an AWS Lambda function in the management account of the organization.Which combination of access changes will meet these requirements? (Choose three.)

A. Create a trust relationship that allows users in the member accounts to assume the management account IAM role.

B. Create a trust relationship that allows users in the management account to assume the IAM roles of the member accounts.

C. Create an IAM role in each member account that has access to the AmazonEC2ReadOnlyAccess managed policy.

D. Create an I AM role in each member account to allow the sts:AssumeRole action against the management account IAM role's ARN.

E. Create an I AM role in the management account that allows the sts:AssumeRole action against the member account IAM role's ARN.

F. Create an IAM role in the management account that has access to the AmazonEC2ReadOnlyAccess managed policy.

**Đáp án**: ___________

---

## Câu 11

**ID**: 40 | **Loại**: Multiple Choice

A company requires that its internally facing web application be highly available. The architecture is made up of one Amazon EC2 web server instance and one NAT instance that provides outbound internet access for updates and accessing public data.Which combination of architecture adjustments should the company implement to achieve high availability? (Choose two.)

A. Add the NAT instance to an EC2 Auto Scaling group that spans multiple Availability Zones. Update the route tables.

B. Create additional EC2 instances spanning multiple Availability Zones. Add an Application Load Balancer to split the load between them.

C. Configure an Application Load Balancer in front of the EC2 instance. Configure Amazon CloudWatch alarms to recover the EC2 instance upon host failure.

D. Replace the NAT instance with a NAT gateway in each Availability Zone. Update the route tables.

E. Replace the NAT instance with a NAT gateway that spans multiple Availability Zones. Update the route tables.

**Đáp án**: ___________

---

## Câu 12

**ID**: 43 | **Loại**: Multiple Choice

A DevOps team manages an API running on-premises that serves as a backend for an Amazon API Gateway endpoint. Customers have been complaining about high response latencies, which the development team has verified using the API Gateway latency metrics in Amazon CloudWatch. To identify the cause, the team needs to collect relevant data without introducing additional latency.Which actions should be taken to accomplish this? (Choose two.)

A. Install the CloudWatch agent server side and configure the agent to upload relevant logs to CloudWatch.

B. Enable AWS X-Ray tracing in API Gateway, modify the application to capture request segments, and upload those segments to X-Ray during each request.

C. Enable AWS X-Ray tracing in API Gateway, modify the application to capture request segments, and use the X-Ray daemon to upload segments to X-Ray.

D. Modify the on-premises application to send log information back to API Gateway with each request.

E. Modify the on-premises application to calculate and upload statistical data relevant to the API service requests to CloudWatch metrics.

**Đáp án**: ___________

---

## Câu 13

**ID**: 47 | **Loại**: Multiple Choice

A company runs an application with an Amazon EC2 and on-premises configuration. A DevOps engineer needs to standardize patching across both environments. Company policy dictates that patching only happens during non-business hours.Which combination of actions will meet these requirements? (Choose three.)

A. Add the physical machines into AWS Systems Manager using Systems Manager Hybrid Activations.

B. Attach an IAM role to the EC2 instances, allowing them to be managed by AWS Systems Manager.

C. Create IAM access keys for the on-premises machines to interact with AWS Systems Manager.

D. Run an AWS Systems Manager Automation document to patch the systems every hour

E. Use Amazon EventBridge scheduled events to schedule a patch window.

F. Use AWS Systems Manager Maintenance Windows to schedule a patch window.

**Đáp án**: ___________

---

## Câu 14

**ID**: 53 | **Loại**: Multiple Choice

A company is performing vulnerability scanning for all Amazon EC2 instances across many accounts. The accounts are in an organization in AWS Organizations. Each account's VPCs are attached to a shared transit gateway. The VPCs send traffic to the internet through a central egress VPC. The company has enabled Amazon Inspector in a delegated administrator account and has enabled scanning for all member accounts.A DevOps engineer discovers that some EC2 instances are listed in the "not scanning" tab in Amazon Inspector.Which combination of actions should the DevOps engineer take to resolve this issue? (Choose three.)

A. Verify that AWS Systems Manager Agent is installed and is running on the EC2 instances that Amazon Inspector is not scanning.

B. Associate the target EC2 instances with security groups that allow outbound communication on port 443 to the AWS Systems Manager service endpoint.

C. Grant inspector:StartAssessmentRun permissions to the IAM role that the DevOps engineer is using.

D. Configure EC2 Instance Connect for the EC2 instances that Amazon Inspector is not scanning.

E. Associate the target EC2 instances with instance profiles that grant permissions to communicate with AWS Systems Manager.

F. Create a managed-instance activation. Use the Activation Code and the Activation ID to register the EC2 instances.

**Đáp án**: ___________

---

## Câu 15

**ID**: 56 | **Loại**: Multiple Choice

A DevOps engineer has automated a web service deployment by using AWS CodePipeline with the following steps:1. An AWS CodeBuild project compiles the deployment artifact and runs unit tests.2. An AWS CodeDeploy deployment group deploys the web service to Amazon EC2 instances in the staging environment.3. A CodeDeploy deployment group deploys the web service to EC2 instances in the production environment.The quality assurance (QA) team requests permission to inspect the build artifact before the deployment to the production environment occurs. The QA team wants to run an internal penetration testing tool to conduct manual tests. The tool will be invoked by a REST API call.Which combination of actions should the DevOps engineer take to fulfill this request? (Choose two.)

A. Insert a manual approval action between the test actions and deployment actions of the pipeline.

B. Modify the buildspec.yml file for the compilation stage to require manual approval before completion.

C. Update the CodeDeploy deployment groups so that they require manual approval to proceed.

D. Update the pipeline to directly call the REST API for the penetration testing tool.

E. Update the pipeline to invoke an AWS Lambda function that calls the REST API for the penetration testing tool.

**Đáp án**: ___________

---

## Câu 16

**ID**: 58 | **Loại**: Multiple Choice

A company runs an application on Amazon EC2 instances. The company uses a series of AWS CloudFormation stacks to define the application resources. A developer performs updates by building and testing the application on a laptop and then uploading the build output and CloudFormation stack templates to Amazon S3. The developer's peers review the changes before the developer performs the CloudFormation stack update and installs a new version of the application onto the EC2 instances.The deployment process is prone to errors and is time-consuming when the developer updates each EC2 instance with the new application. The company wants to automate as much of the application deployment process as possible while retaining a final manual approval step before the modification of the application or resources.The company already has moved the source code for the application and the CloudFormation templates to AWS CodeCommit. The company also has created an AWS CodeBuild project to build and test the application.Which combination of steps will meet the company’s requirements? (Choose two.)

A. Create an application group and a deployment group in AWS CodeDeploy. Install the CodeDeploy agent on the EC2 instances.

B. Create an application revision and a deployment group in AWS CodeDeploy. Create an environment in CodeDeploy. Register the EC2 instances to the CodeDeploy environment.

C. Use AWS CodePipeline to invoke the CodeBuild job, run the CloudFormation update, and pause for a manual approval step. After approval, start the AWS CodeDeploy deployment.

D. Use AWS CodePipeline to invoke the CodeBuild job, create CloudFormation change sets for each of the application stacks, and pause for a manual approval step. After approval, run the CloudFormation change sets and start the AWS CodeDeploy deployment.

E. Use AWS CodePipeline to invoke the CodeBuild job, create CloudFormation change sets for each of the application stacks, and pause for a manual approval step. After approval, start the AWS CodeDeploy deployment.

**Đáp án**: ___________

---

## Câu 17

**ID**: 65 | **Loại**: Multiple Choice

A company's application is currently deployed to a single AWS Region. Recently, the company opened a new office on a different continent. The users in the new office are experiencing high latency. The company's application runs on Amazon EC2 instances behind an Application Load Balancer (ALB) and uses Amazon DynamoDB as the database layer. The instances run in an EC2 Auto Scaling group across multiple Availability Zones. A DevOps engineer is tasked with minimizing application response times and improving availability for users in both Regions.Which combination of actions should be taken to address the latency issues? (Choose three.)

A. Create a new DynamoDB table in the new Region with cross-Region replication enabled.

B. Create new ALB and Auto Scaling group global resources and configure the new ALB to direct traffic to the new Auto Scaling group.

C. Create new ALB and Auto Scaling group resources in the new Region and configure the new ALB to direct traffic to the new Auto Scaling group.

D. Create Amazon Route 53 records, health checks, and latency-based routing policies to route to the ALB.

E. Create Amazon Route 53 aliases, health checks, and failover routing policies to route to the ALB.

F. Convert the DynamoDB table to a global table.

**Đáp án**: ___________

---

## Câu 18

**ID**: 67 | **Loại**: Multiple Choice

A company has its AWS accounts in an organization in AWS Organizations. AWS Config is manually configured in each AWS account. The company needs to implement a solution to centrally configure AWS Config for all accounts in the organization The solution also must record resource changes to a central account.Which combination of actions should a DevOps engineer perform to meet these requirements? (Choose two.)

A. Configure a delegated administrator account for AWS Config. Enable trusted access for AWS Config in the organization.

B. Configure a delegated administrator account for AWS Config. Create a service-linked role for AWS Config in the organization’s management account.

C. Create an AWS CloudFormation template to create an AWS Config aggregator. Configure a CloudFormation stack set to deploy the template to all accounts in the organization.

D. Create an AWS Config organization aggregator in the organization's management account. Configure data collection from all AWS accounts in the organization and from all AWS Regions.

E. Create an AWS Config organization aggregator in the delegated administrator account. Configure data collection from all AWS accounts in the organization and from all AWS Regions.

**Đáp án**: ___________

---

## Câu 19

**ID**: 71 | **Loại**: Multiple Choice

A DevOps engineer at a company is supporting an AWS environment in which all users use AWS IAM Identity Center (AWS Single Sign-On). The company wants to immediately disable credentials of any new IAM user and wants the security team to receive a notification.Which combination of steps should the DevOps engineer take to meet these requirements? (Choose three.)

A. Create an Amazon EventBridge rule that reacts to an IAM CreateUser API call in AWS CloudTrail.

B. Create an Amazon EventBridge rule that reacts to an IAM GetLoginProfile API call in AWS CloudTrail.

C. Create an AWS Lambda function that is a target of the EventBridge rule. Configure the Lambda function to disable any access keys and delete the login profiles that are associated with the IAM user.

D. Create an AWS Lambda function that is a target of the EventBridge rule. Configure the Lambda function to delete the login profiles that are associated with the IAM user.

E. Create an Amazon Simple Notification Service (Amazon SNS) topic that is a target of the EventBridge rule. Subscribe the security team's group email address to the topic.

F. Create an Amazon Simple Queue Service (Amazon SQS) queue that is a target of the Lambda function. Subscribe the security team's group email address to the queue.

**Đáp án**: ___________

---

## Câu 20

**ID**: 81 | **Loại**: Multiple Choice

A company manages an application that stores logs in Amazon CloudWatch Logs. The company wants to archive the logs to an Amazon S3 bucket. Logs are rarely accessed after 90 days and must be retained for 10 years.Which combination of steps should a DevOps engineer take to meet these requirements? (Choose two.)

A. Configure a CloudWatch Logs subscription filter to use AWS Glue to transfer all logs to an S3 bucket.

B. Configure a CloudWatch Logs subscription filter to use Amazon Kinesis Data Firehose to stream all logs to an S3 bucket.

C. Configure a CloudWatch Logs subscription filter to stream all logs to an S3 bucket.

D. Configure the S3 bucket lifecycle policy to transition logs to S3 Glacier after 90 days and to expire logs after 3.650 days.

E. Configure the S3 bucket lifecycle policy to transition logs to Reduced Redundancy after 90 days and to expire logs after 3.650 days.

**Đáp án**: ___________

---

## Câu 21

**ID**: 82 | **Loại**: Multiple Choice

A company is developing a new application. The application uses AWS Lambda functions for its compute tier. The company must use a canary deployment for any changes to the Lambda functions. Automated rollback must occur if any failures are reported.The company’s DevOps team needs to create the infrastructure as code (IaC) and the CI/CD pipeline for this solution.Which combination of steps will meet these requirements? (Choose three.)

A. Create an AWS CloudFormation template for the application. Define each Lambda function in the template by using the AWS::Lambda::Function resource type. In the template, include a version for the Lambda function by using the AWS::Lambda::Version resource type. Declare the CodeSha256 property. Configure an AWS::Lambda::Alias resource that references the latest version of the Lambda function.

B. Create an AWS Serverless Application Model (AWS SAM) template for the application. Define each Lambda function in the template by using the AWS::Serverless::Function resource type. For each function, include configurations for the AutoPublishAlias property and the DeploymentPreference property. Configure the deployment configuration type to LambdaCanary10Percent10Minutes.

C. Create an AWS CodeCommit repository. Create an AWS CodePipeline pipeline. Use the CodeCommit repository in a new source stage that starts the pipeline. Create an AWS CodeBuild project to deploy the AWS Serverless Application Model (AWS SAM) template. Upload the template and source code to the CodeCommit repository. In the CodeCommit repository, create a buildspec.yml file that includes the commands to build and deploy the SAM application.

D. Create an AWS CodeCommit repository. Create an AWS CodePipeline pipeline. Use the CodeCommit repository in a new source stage that starts the pipeline. Create an AWS CodeDeploy deployment group that is configured for canary deployments with a DeploymentPreference type of Canary10Percent10Minutes. Upload the AWS CloudFormation template and source code to the CodeCommit repository. In the CodeCommit repository, create an appspec.yml file that includes the commands to deploy the CloudFormation template.

E. Create an Amazon CloudWatch composite alarm for all the Lambda functions. Configure an evaluation period and dimensions for Lambda. Configure the alarm to enter the ALARM state if any errors are detected or if there is insufficient data.

F. Create an Amazon CloudWatch alarm for each Lambda function. Configure the alarms to enter the ALARM state if any errors are detected. Configure an evaluation period, dimensions for each Lambda function and version, and the namespace as AWS/Lambda on the Errors metric.

**Đáp án**: ___________

---

## Câu 22

**ID**: 83 | **Loại**: Multiple Choice

A DevOps engineer is deploying a new version of a company’s application in an AWS CodeDeploy deployment group associated with its Amazon EC2 instances. After some time, the deployment fails. The engineer realizes that all the events associated with the specific deployment ID are in a Skipped status, and code was not deployed in the instances associated with the deployment group.What are valid reasons for this failure? (Choose two.)

A. The networking configuration does not allow the EC2 instances to reach the internet via a NAT gateway or internet gateway, and the CodeDeploy endpoint cannot be reached.

B. The IAM user who triggered the application deployment does not have permission to interact with the CodeDeploy endpoint.

C. The target EC2 instances were not properly registered with the CodeDeploy endpoint.

D. An instance profile with proper permissions was not attached to the target EC2 instances.

E. The appspec.yml file was not included in the application revision.

**Đáp án**: ___________

---

## Câu 23

**ID**: 87 | **Loại**: Multiple Choice

An Amazon EC2 instance is running in a VPC and needs to download an object from a restricted Amazon S3 bucket. When the DevOps engineer tries to download the object, an AccessDenied error is received.What are the possible causes for this error? (Choose two.)

A. The S3 bucket default encryption is enabled.

B. There is an error in the S3 bucket policy.

C. The object has been moved to S3 Glacier.

D. There is an error in the IAM role configuration.

E. S3 Versioning is enabled.

**Đáp án**: ___________

---

## Câu 24

**ID**: 89 | **Loại**: Multiple Choice

A DevOps engineer is working on a data archival project that requires the migration of on-premises data to an Amazon S3 bucket. The DevOps engineer develops a script that incrementally archives on-premises data that is older than 1 month to Amazon S3. Data that is transferred to Amazon S3 is deleted from the on-premises location. The script uses the S3 PutObject operation.During a code review, the DevOps engineer notices that the script does not verify whether the data was successfully copied to Amazon S3. The DevOps engineer must update the script to ensure that data is not corrupted during transmission. The script must use MD5 checksums to verify data integrity before the on-premises data is deleted.Which solutions for the script will meet these requirements? (Choose two.)

A. Check the returned response for the VersionId. Compare the returned VersionId against the MD5 checksum.

B. Include the MD5 checksum within the Content-MD5 parameter. Check the operation call’s return status to find out if an error was returned.

C. Include the checksum digest within the tagging parameter as a URL query parameter.

D. Check the returned response for the ETag. Compare the returned ETag against the MD5 checksum.

E. Include the checksum digest within the Metadata parameter as a name-value pair. After upload, use the S3 HeadObject operation to retrieve metadata from the object.

**Đáp án**: ___________

---

## Câu 25

**ID**: 93 | **Loại**: Multiple Choice

A company requires an RPO of 2 hours and an RTO of 10 minutes for its data and application at all times. An application uses a MySQL database and Amazon EC2 web servers. The development team needs a strategy for failover and disaster recovery.Which combination of deployment strategies will meet these requirements? (Choose two.)

A. Create an Amazon Aurora cluster in one Availability Zone across multiple Regions as the data store. Use Aurora’s automatic recovery capabilities in the event of a disaster.

B. Create an Amazon Aurora global database in two Regions as the data store. In the event of a failure, promote the secondary Region as the primary for the application.

C. Create an Amazon Aurora multi-master cluster across multiple Regions as the data store. Use a Network Load Balancer to balance the database traffic in different Regions.

D. Set up the application in two Regions and use Amazon Route 53 failover-based routing that points to the Application Load Balancers in both Regions. Use health checks to determine the availability in a given Region. Use Auto Scaling groups in each Region to adjust capacity based on demand.

E. Set up the application in two Regions and use a multi-Region Auto Scaling group behind Application Load Balancers to manage the capacity based on demand. In the event of a disaster, adjust the Auto Scaling group’s desired instance count to increase baseline capacity in the failover Region.

**Đáp án**: ___________

---

## Câu 26

**ID**: 101 | **Loại**: Multiple Choice

A company recently created a new AWS Control Tower landing zone in a new organization in AWS Organizations. The landing zone must be able to demonstrate compliance with the Center for Internet Security (CIS) Benchmarks for AWS Foundations.The company’s security team wants to use AWS Security Hub to view compliance across all accounts. Only the security team can be allowed to view aggregated Security Hub findings. In addition, specific users must be able to view findings from their own accounts within the organization. All accounts must be enrolled in Security Hub after the accounts are created.Which combination of steps will meet these requirements in the MOST automated way? (Choose three.)

A. Turn on trusted access for Security Hub in the organization’s management account. Create a new security account by using AWS Control Tower. Configure the new security account as the delegated administrator account for Security Hub. In the new security account, provide Security Hub with the CIS Benchmarks for AWS Foundations standards.

B. Turn on trusted access for Security Hub in the organization’s management account. From the management account, provide Security Hub with the CIS Benchmarks for AWS Foundations standards.

C. Create an AWS IAM Identity Center (AWS Single Sign-On) permission set that includes the required permissions. Use the CreateAccountAssignment API operation to associate the security team users with the permission set and with the delegated security account.

D. Create an SCP that explicitly denies any user who is not on the security team from accessing Security Hub.

E. In Security Hub, turn on automatic enablement.

F. In the organization’s management account, create an Amazon EventBridge rule that reacts to the CreateManagedAccount event. Create an AWS Lambda function that uses the Security Hub CreateMembers API operation to add new accounts to Security Hub. Configure the EventBridge rule to invoke the Lambda function.

**Đáp án**: ___________

---

## Câu 27

**ID**: 110 | **Loại**: Multiple Choice

A company uses AWS CodeArtifact to centrally store Python packages. The CodeArtifact repository is configured with the following repository policy:A development team is building a new project in an account that is in an organization in AWS Organizations. The development team wants to use a Python library that has already been stored in the CodeArtifact repository in the organization. The development team uses AWS CodePipeline and AWS CodeBuild to build the new application. The CodeBuild job that the development team uses to build the application is configured to run in a VPC. Because of compliance requirements, the VPC has no internet connectivity.The development team creates the VPC endpoints for CodeArtifact and updates the CodeBuild buildspec.yaml file. However, the development team cannot download the Python library from the repository.Which combination of steps should a DevOps engineer take so that the development team can use CodeArtifact? (Choose two.)

A. Create an Amazon S3 gateway endpoint. Update the route tables for the subnets that are running the CodeBuild job.

B. Update the repository policy’s Principal statement to include the ARN of the role that the CodeBuild project uses.

C. Share the CodeArtifact repository with the organization by using AWS Resource Access Manager (AWS RAM).

D. Update the role that the CodeBuild project uses so that the role has sufficient permissions to use the CodeArtifact repository.

E. Specify the account that hosts the repository as the delegated administrator for CodeArtifact in the organization.

**Đáp án**: ___________

---

## Câu 28

**ID**: 117 | **Loại**: Multiple Choice

A company is storing 100 GB of log data in .csv format in an Amazon S3 bucket. SQL developers want to query this data and generate graphs to visualize it. The SQL developers also need an efficient, automated way to store metadata from the .csv file.Which combination of steps will meet these requirements with the LEAST amount of effort? (Choose three.)

A. Filter the data through AWS X-Ray to visualize the data.

B. Filter the data through Amazon QuickSight to visualize the data.

C. Query the data with Amazon Athena.

D. Query the data with Amazon Redshift.

E. Use the AWS Glue Data Catalog as the persistent metadata store.

F. Use Amazon DynamoDB as the persistent metadata store.

**Đáp án**: ___________

---

## Câu 29

**ID**: 118 | **Loại**: Multiple Choice

A company deploys its corporate infrastructure on AWS across multiple AWS Regions and Availability Zones. The infrastructure is deployed on Amazon EC2 instances and connects with AWS IoT Greengrass devices. The company deploys additional resources on on-premises servers that are located in the corporate headquarters.The company wants to reduce the overhead involved in maintaining and updating its resources. The company’s DevOps team plans to use AWS Systems Manager to implement automated management and application of patches. The DevOps team confirms that Systems Manager is available in the Regions that the resources are deployed in. Systems Manager also is available in a Region near the corporate headquarters.Which combination of steps must the DevOps team take to implement automated patch and configuration management across the company’s EC2 instances, IoT devices, and on-premises infrastructure? (Choose three.)

A. Apply tags to all the EC2 instances, AWS IoT Greengrass devices, and on-premises servers. Use Systems Manager Session Manager to push patches to all the tagged devices.

B. Use Systems Manager Run Command to schedule patching for the EC2 instances, AWS IoT Greengrass devices, and on-premises servers.

C. Use Systems Manager Patch Manager to schedule patching for the EC2 instances, AWS IoT Greengrass devices, and on-premises servers as a Systems Manager maintenance window task.

D. Configure Amazon EventBridge to monitor Systems Manager Patch Manager for updates to patch baselines. Associate Systems Manager Run Command with the event to initiate a patch action for all EC2 instances, AWS IoT Greengrass devices, and on-premises servers.

E. Create an IAM instance profile for Systems Manager. Attach the instance profile to all the EC2 instances in the AWS account. For the AWS IoT Greengrass devices and on-premises servers, create an IAM service role for Systems Manager.

F. Generate a managed-instance activation. Use the Activation Code and Activation ID to install Systems Manager Agent (SSM Agent) on each server in the on-premises environment. Update the AWS IoT Greengrass IAM token exchange role. Use the role to deploy SSM Agent on all the IoT devices.

**Đáp án**: ___________

---

## Câu 30

**ID**: 121 | **Loại**: Multiple Choice

A company is building a new pipeline by using AWS CodePipeline and AWS CodeBuild in a build account. The pipeline consists of two stages. The first stage is a CodeBuild job to build and package an AWS Lambda function. The second stage consists of deployment actions that operate on two different AWS accounts: a development environment account and a production environment account. The deployment stages use the AWS CloudFormation action that CodePipeline invokes to deploy the infrastructure that the Lambda function requires.A DevOps engineer creates the CodePipeline pipeline and configures the pipeline to encrypt build artifacts by using the AWS Key Management Service (AWS KMS) AWS managed key for Amazon S3 (the aws/s3 key). The artifacts are stored in an S3 bucket. When the pipeline runs, the CloudFormation actions fail with an access denied error.Which combination of actions must the DevOps engineer perform to resolve this error? (Choose two.)

A. Create an S3 bucket in each AWS account for the artifacts. Allow the pipeline to write to the S3 buckets. Create a CodePipeline S3 action to copy the artifacts to the S3 bucket in each AWS account. Update the CloudFormation actions to reference the artifacts S3 bucket in the production account.

B. Create a customer managed KMS key. Configure the KMS key policy to allow the IAM roles used by the CloudFormation action to perform decrypt operations. Modify the pipeline to use the customer managed KMS key to encrypt artifacts.

C. Create an AWS managed KMS key. Configure the KMS key policy to allow the development account and the production account to perform decrypt operations. Modify the pipeline to use the KMS key to encrypt artifacts.

D. In the development account and in the production account, create an IAM role for CodePipeline. Configure the roles with permissions to perform CloudFormation operations and with permissions to retrieve and decrypt objects from the artifacts S3 bucket. In the CodePipeline account, configure the CodePipeline CloudFormation action to use the roles.

E. In the development account and in the production account, create an IAM role for CodePipeline. Configure the roles with permissions to perform CloudFormation operations and with permissions to retrieve and decrypt objects from the artifacts S3 bucket. In the CodePipeline account, modify the artifacts S3 bucket policy to allow the roles access. Configure the CodePipeline CloudFormation action to use the roles.

**Đáp án**: ___________

---

## Câu 31

**ID**: 122 | **Loại**: Multiple Choice

A company is using an organization in AWS Organizations to manage multiple AWS accounts. The company’s development team wants to use AWS Lambda functions to meet resiliency requirements and is rewriting all applications to work with Lambda functions that are deployed in a VPC. The development team is using Amazon Elastic File System (Amazon EFS) as shared storage in Account A in the organization.The company wants to continue to use Amazon EFS with Lambda. Company policy requires all serverless projects to be deployed in Account B.A DevOps engineer needs to reconfigure an existing EFS file system to allow Lambda functions to access the data through an existing EFS access point.Which combination of steps should the DevOps engineer take to meet these requirements? (Choose three.)

A. Update the EFS file system policy to provide Account B with access to mount and write to the EFS file system in Account A.

B. Create SCPs to set permission guardrails with fine-grained control for Amazon EFS.

C. Create a new EFS file system in Account B. Use AWS Database Migration Service (AWS DMS) to keep data from Account A and Account B synchronized.

D. Update the Lambda execution roles with permission to access the VPC and the EFS file system.

E. Create a VPC peering connection to connect Account A to Account B.

F. Configure the Lambda functions in Account B to assume an existing IAM role in Account A.

**Đáp án**: ___________

---

## Câu 32

**ID**: 127 | **Loại**: Multiple Choice

A company updated the AWS CloudFormation template for a critical business application. The stack update process failed due to an error in the updated template, and AWS CloudFormation automatically began the stack rollback process. Later, a DevOps engineer discovered that the application was still unavailable and that the stack was in the UPDATE_ROLLBACK_FAILED state.Which combination of actions should the DevOps engineer perform so that the stack rollback can complete successfully? (Choose two.)

A. Attach the AWSCloudFormationFullAccess IAM policy to the AWS CloudFormation role.

B. Automatically recover the stack resources by using AWS CloudFormation drift detection.

C. Issue a ContinueUpdateRollback command from the AWS CloudFormation console or the AWS CLI.

D. Manually adjust the resources to match the expectations of the stack.

E. Update the existing AWS CloudFormation stack by using the original template.

**Đáp án**: ___________

---

## Câu 33

**ID**: 128 | **Loại**: Multiple Choice

A development team manually builds an artifact locally and then places it in an Amazon S3 bucket. The application has a local cache that must be cleared when a deployment occurs. The team runs a command to do this, downloads the artifact from Amazon S3, and unzips the artifact to complete the deployment.A DevOps team wants to migrate to a CI/CD process and build in checks to stop and roll back the deployment when a failure occurs. This requires the team to track the progression of the deployment.Which combination of actions will accomplish this? (Choose three.)

A. Allow developers to check the code into a code repository. Using Amazon EventBridge, on every pull into the main branch, invoke an AWS Lambda function to build the artifact and store it in Amazon S3.

B. Create a custom script to clear the cache. Specify the script in the BeforeInstall lifecycle hook in the AppSpec file.

C. Create user data for each Amazon EC2 instance that contains the clear cache script. Once deployed, test the application. If it is not successful, deploy it again.

D. Set up AWS CodePipeline to deploy the application. Allow developers to check the code into a code repository as a source for the pipeline.

E. Use AWS CodeBuild to build the artifact and place it in Amazon S3. Use AWS CodeDeploy to deploy the artifact to Amazon EC2 instances.

F. Use AWS Systems Manager to fetch the artifact from Amazon S3 and deploy it to all the instances.

**Đáp án**: ___________

---

## Câu 34

**ID**: 129 | **Loại**: Multiple Choice

A DevOps engineer is working on a project that is hosted on Amazon Linux and has failed a security review. The DevOps manager has been asked to review the company buildspec.yaml file for an AWS CodeBuild project and provide recommendations. The buildspec.yaml file is configured as follows:What changes should be recommended to comply with AWS security best practices? (Choose three.)

A. Add a post-build command to remove the temporary files from the container before termination to ensure they cannot be seen by other CodeBuild users.

B. Update the CodeBuild project role with the necessary permissions and then remove the AWS credentials from the environment variable.

C. Store the DB_PASSWORD as a SecureString value in AWS Systems Manager Parameter Store and then remove the DB_PASSWORD from the environment variables.

D. Move the environment variables to the ‘db-deploy-bucket’ Amazon S3 bucket, add a prebuild stage to download, then export the variables.

E. Use AWS Systems Manager run command versus scp and ssh commands directly to the instance.

F. Scramble the environment variables using XOR followed by Base64, add a section to install, and then run XOR and Base64 to the build phase.

**Đáp án**: ___________

---

## Câu 35

**ID**: 138 | **Loại**: Multiple Choice

A company uses AWS Secrets Manager to store a set of sensitive API keys that an AWS Lambda function uses. When the Lambda function is invoked the Lambda function retrieves the API keys and makes an API call to an external service. The Secrets Manager secret is encrypted with the default AWS Key Management Service (AWS KMS) key.A DevOps engineer needs to update the infrastructure to ensure that only the Lambda function’s execution role can access the values in Secrets Manager. The solution must apply the principle of least privilege.Which combination of steps will meet these requirements? (Choose two.)

A. Update the default KMS key for Secrets Manager to allow only the Lambda function’s execution role to decrypt

B. Create a KMS customer managed key that trusts Secrets Manager and allows the Lambda function's execution role to decrypt. Update Secrets Manager to use the new customer managed key

C. Create a KMS customer managed key that trusts Secrets Manager and allows the account's root principal to decrypt. Update Secrets Manager to use the new customer managed key

D. Ensure that the Lambda function’s execution role has the KMS permissions scoped on the resource level. Configure the permissions so that the KMS key can encrypt the Secrets Manager secret

E. Remove all KMS permissions from the Lambda function’s execution role

**Đáp án**: ___________

---

## Câu 36

**ID**: 139 | **Loại**: Multiple Choice

A company's DevOps engineer is creating an AWS Lambda function to process notifications from an Amazon Simple Notification Service (Amazon SNS) topic. The Lambda function will process the notification messages and will write the contents of the notification messages to an Amazon RDS Multi-AZ DB instance.During testing, a database administrator accidentally shut down the DB instance. While the database was down the company lost several of the SNS notification messages that were delivered during that time.The DevOps engineer needs to prevent the loss of notification messages in the future.Which solutions will meet this requirement? (Choose two.)

A. Replace the RDS Multi-AZ DB instance with an Amazon DynamoDB table.

B. Configure an Amazon Simple Queue Service (Amazon SQS) queue as a destination of the Lambda function.

C. Configure an Amazon Simple Queue Service (Amazon SQS) dead-letter queue for the SNS topic.

D. Subscribe an Amazon Simple Queue Service (Amazon SQS) queue to the SNS topic. Configure the Lambda function to process messages from the SQS queue.

E. Replace the SNS topic with an Amazon EventBridge event bus. Configure an EventBridge rule on the new event bus to invoke the Lambda function for each event.

**Đáp án**: ___________

---

## Câu 37

**ID**: 157 | **Loại**: Multiple Choice

A DevOps engineer notices that all Amazon EC2 instances running behind an Application Load Balancer in an Auto Scaling group are failing to respond to user requests. The EC2 instances are also failing target group HTTP health checks.Upon inspection, the engineer notices the application process was not running in any EC2 instances. There are a significant number of out of memory messages in the system logs. The engineer needs to improve the resilience of the application to cope with a potential application memory leak. Monitoring and notifications should be enabled to alert when there is an issue.Which combination of actions will meet these requirements? (Choose two.)

A. Change the Auto Scaling configuration to replace the instances when they fail the load balancer's health checks.

B. Change the target group health check HealthCheckIntervalSeconds parameter to reduce the interval between health checks.

C. Change the target group health checks from HTTP to TCP to check if the port where the application is listening is reachable.

D. Enable the available memory consumption metric within the Amazon CloudWatch dashboard for the entire Auto Scaling group. Create an alarm when the memory utilization is high. Associate an Amazon SNS topic to the alarm to receive notifications when the alarm goes off.

E. Use the Amazon CloudWatch agent to collect the memory utilization of the EC2 instances in the Auto Scaling group. Create an alarm when the memory utilization is high and associate an Amazon SNS topic to receive a notification.

**Đáp án**: ___________

---

## Câu 38

**ID**: 160 | **Loại**: Multiple Choice

A company has an AWS Control Tower landing zone. The company's DevOps team creates a workload OU. A development OU and a production OU are nested under the workload OU. The company grants users full access to the company's AWS accounts to deploy applications.The DevOps team needs to allow only a specific management IAM role to manage the IAM roles and policies of any AWS accounts in only the production OU.Which combination of steps will meet these requirements? (Choose two.)

A. Create an SCP that denies full access with a condition to exclude the management IAM role for the organization root.

B. Ensure that the FullAWSAccess SCP is applied at the organization root.

C. Create an SCP that allows IAM related actions. Attach the SCP to the development OU.

D. Create an SCP that denies IAM related actions with a condition to exclude the management IAM role. Attach the SCP to the workload OU.

E. Create an SCP that denies IAM related actions with a condition to exclude the management IAM role. Attach the SCP to the production OU.

**Đáp án**: ___________

---

## Câu 39

**ID**: 163 | **Loại**: Multiple Choice

A company has an AWS Control Tower landing zone that manages its organization in AWS Organizations. The company created an OU structure that is based on the company's requirements. The company's DevOps team has established the core accounts for the solution and an account for all centralized AWS CloudFormation and AWS Service Catalog solutions.The company wants to offer a series of customizations that an account can request through AWS Control Tower.Which combination of steps will meet these requirements? (Choose three.)

A. Enable trusted access for CloudFormation with Organizations by using service-managed permissions.

B. Create an IAM role that is named AWSControlTowerBlueprintAccess. Configure the role with a trust policy that allows the AWSControlTowerAdmin role in the management account to assume the role. Attach the AWSServiceCatalogAdminFullAccess IAM policy to the AWSControlTowerBlueprintAccess role.

C. Create a Service Catalog product for each CloudFormation template.

D. Create a CloudFormation stack set for each CloudFormation template. Enable automatic deployment for each stack set. Create a CloudFormation stack instance that targets specific OUs.

E. Deploy the Customizations for AWS Control Tower (CfCT) CloudFormation stack.

F. Create a CloudFormation template that contains the resources for each customization.

**Đáp án**: ___________

---

## Câu 40

**ID**: 165 | **Loại**: Multiple Choice

A company builds an application that uses an Application Load Balancer in front of Amazon EC2 instances that are in an Auto Scaling group. The application is stateless. The Auto Scaling group uses a custom AMI that is fully prebuilt. The EC2 instances do not have a custom bootstrapping process.The AMI that the Auto Scaling group uses was recently deleted. The Auto Scaling group's scaling activities show failures because the AMI ID does not exist.Which combination of steps should a DevOps engineer take to meet these requirements? (Choose three.)

A. Create a new launch template that uses the new AMI.

B. Update the Auto Scaling group to use the new launch template.

C. Reduce the Auto Scaling group's desired capacity to 0.

D. Increase the Auto Scaling group's desired capacity by 1.

E. Create a new AMI from a running EC2 instance in the Auto Scaling group.

F. Create a new AMI by copying the most recent public AMI of the operating system that the EC2 instances use.

**Đáp án**: ___________

---

## Câu 41

**ID**: 166 | **Loại**: Multiple Choice

A company deploys a web application on Amazon EC2 instances that are behind an Application Load Balancer (ALB). The company stores the application code in an AWS CodeCommit repository. When code is merged to the main branch, an AWS Lambda function invokes an AWS CodeBuild project. The CodeBuild project packages the code, stores the packaged code in AWS CodeArtifact, and invokes AWS Systems Manager Run Command to deploy the packaged code to the EC2 instances.Previous deployments have resulted in defects, EC2 instances that are not running the latest version of the packaged code, and inconsistencies between instances.Which combination of actions should a DevOps engineer take to implement a more reliable deployment solution? (Choose two.)

A. Create a pipeline in AWS CodePipeline that uses the CodeCommit repository as a source provider. Configure pipeline stages that run the CodeBuild project in parallel to build and test the application. In the pipeline, pass the CodeBuild project output artifact to an AWS CodeDeploy action.

B. Create a pipeline in AWS CodePipeline that uses the CodeCommit repository as a source provider. Create separate pipeline stages that run a CodeBuild project to build and then test the application. In the pipeline, pass the CodeBuild project output artifact to an AWS CodeDeploy action.

C. Create an AWS CodeDeploy application and a deployment group to deploy the packaged code to the EC2 instances. Configure the ALB for the deployment group.

D. Create individual Lambda functions that use AWS CodeDeploy instead of Systems Manager to run build, test, and deploy actions.

E. Create an Amazon S3 bucket. Modify the CodeBuild project to store the packages in the S3 bucket instead of in CodeArtifact. Use deploy actions in CodeDeploy to deploy the artifact to the EC2 instances.

**Đáp án**: ___________

---

## Câu 42

**ID**: 169 | **Loại**: Multiple Choice

A company has a new AWS account that teams will use to deploy various applications. The teams will create many Amazon S3 buckets for application-specific purposes and to store AWS CloudTrail logs. The company has enabled Amazon Macie for the account.A DevOps engineer needs to optimize the Macie costs for the account without compromising the account's functionality.Which solutions will meet these requirements? (Choose two.)

A. Exclude S3 buckets that contain CloudTrail logs from automated discovery.

B. Exclude S3 buckets that have public read access from automated discovery.

C. Configure scheduled daily discovery jobs for all S3 buckets in the account.

D. Configure discovery jobs to include S3 objects based on the last modified criterion.

E. Configure discovery jobs to include S3 objects that are tagged as production only.

**Đáp án**: ___________

---

## Câu 43

**ID**: 170 | **Loại**: Multiple Choice

A company uses an organization in AWS Organizations to manage its AWS accounts. The company recently acquired another company that has standalone AWS accounts. The acquiring company's DevOps team needs to consolidate the administration of the AWS accounts for both companies and retain full administrative control of the accounts. The DevOps team also needs to collect and group findings across all the accounts to implement and maintain a security posture.Which combination of steps should the DevOps team take to meet these requirements? (Choose two.)

A. Invite the acquired company's AWS accounts to join the organization. Create an SCP that has full administrative privileges. Attach the SCP to the management account.

B. Invite the acquired company's AWS accounts to join the organization. Create the OrganizationAccountAccessRole IAM role in the invited accounts. Grant permission to the management account to assume the role.

C. Use AWS Security Hub to collect and group findings across all accounts. Use Security Hub to automatically detect new accounts as the accounts are added to the organization.

D. Use AWS Firewall Manager to collect and group findings across all accounts. Enable all features for the organization. Designate an account in the organization as the delegated administrator account for Firewall Manager.

E. Use Amazon Inspector to collect and group findings across all accounts. Designate an account in the organization as the delegated administrator account for Amazon Inspector.

**Đáp án**: ___________

---

## Câu 44

**ID**: 172 | **Loại**: Multiple Choice

A company uses an Amazon API Gateway regional REST API to host its application API. The REST API has a custom domain. The REST API's default endpoint is deactivated.The company's internal teams consume the API. The company wants to use mutual TLS between the API and the internal teams as an additional layer of authentication.Which combination of steps will meet these requirements? (Choose two.)

A. Use AWS Certificate Manager (ACM) to create a private certificate authority (CA). Provision a client certificate that is signed by the private CA.

B. Provision a client certificate that is signed by a public certificate authority (CA). Import the certificate into AWS Certificate Manager (ACM).

C. Upload the provisioned client certificate to an Amazon S3 bucket. Configure the API Gateway mutual TLS to use the client certificate that is stored in the S3 bucket as the trust store.

D. Upload the provisioned client certificate private key to an Amazon S3 bucket. Configure the API Gateway mutual TLS to use the private key that is stored in the S3 bucket as the trust store.

E. Upload the root private certificate authority (CA) certificate to an Amazon S3 bucket. Configure the API Gateway mutual TLS to use the private CA certificate that is stored in the S3 bucket as the trust store.

**Đáp án**: ___________

---

## Câu 45

**ID**: 179 | **Loại**: Multiple Choice

A DevOps engineer is planning to deploy a Ruby-based application to production. The application needs to interact with an Amazon RDS for MySQL database and should have automatic scaling and high availability. The stored data in the database is critical and should persist regardless of the state of the application stack.The DevOps engineer needs to set up an automated deployment strategy for the application with automatic rollbacks. The solution also must alert the application team when a deployment fails.Which combination of steps will meet these requirements? (Choose three.)

A. Deploy the application on AWS Elastic Beanstalk. Deploy an Amazon RDS for MySQL DB instance as part of the Elastic Beanstalk configuration.

B. Deploy the application on AWS Elastic Beanstalk. Deploy a separate Amazon RDS for MySQL DB instance outside of Elastic Beanstalk.

C. Configure a notification email address that alerts the application team in the AWS Elastic Beanstalk configuration.

D. Configure an Amazon EventBridge rule to monitor AWS Health events. Use an Amazon Simple Notification Service (Amazon SNS) topic as a target to alert the application team.

E. Use the immutable deployment method to deploy new application versions.

F. Use the rolling deployment method to deploy new application versions.

**Đáp án**: ___________

---

## Câu 46

**ID**: 180 | **Loại**: Multiple Choice

A company is using AWS CodePipeline to deploy an application. According to a new guideline, a member of the company's security team must sign off on any application changes before the changes are deployed into production. The approval must be recorded and retained.Which combination of actions will meet these requirements? (Choose two.)

A. Configure CodePipeline to write actions to Amazon CloudWatch Logs.

B. Configure CodePipeline to write actions to an Amazon S3 bucket at the end of each pipeline stage.

C. Create an AWS CloudTrail trail to deliver logs to Amazon S3.

D. Create a CodePipeline custom action to invoke an AWS Lambda function for approval. Create a policy that gives the security team access to manage CodePipeline custom actions.

E. Create a CodePipeline manual approval action before the deployment step. Create a policy that grants the security team access to approve manual approval stages.

**Đáp án**: ___________

---

## Câu 47

**ID**: 184 | **Loại**: Multiple Choice

A DevOps engineer is implementing governance controls for a company that requires its infrastructure to be housed within the United States. The engineer must restrict which AWS Regions can be used, and ensure an alert is sent as soon as possible if any activity outside the governance policy takes place. The controls should be automatically enabled on any new Region outside the United States (US).Which combination of actions will meet these requirements? (Choose two.)

A. Create an AWS Organizations SCP that denies access to all non-global services in non-US Regions. Attach the policy to the root of the organization.

B. Configure AWS CloudTrail to send logs to Amazon CloudWatch Logs and enable it for all Regions. Use a CloudWatch Logs metric filter to send an alert on any service activity in non-US Regions.

C. Use an AWS Lambda function that checks for AWS service activity and deploy it to all Regions. Write an Amazon EventBridge rule that runs the Lambda function every hour, sending an alert if activity is found in a non-US Region.

D. Use an AWS Lambda function to query Amazon Inspector to look for service activity in non-US Regions and send alerts if any activity is found.

E. Write an SCP using the aws:RequestedRegion condition key limiting access to US Regions. Apply the policy to all users, groups, and roles.

**Đáp án**: ___________

---

## Câu 48

**ID**: 190 | **Loại**: Multiple Choice

A company's application teams use AWS CodeCommit repositories for their applications. The application teams have repositories in multiple AWS accounts. All accounts are in an organization in AWS Organizations.Each application team uses AWS IAM Identity Center (AWS Single Sign-On) configured with an external IdP to assume a developer IAM role. The developer role allows the application teams to use Git to work with the code in the repositories.A security audit reveals that the application teams can modify the main branch in any repository. A DevOps engineer must implement a solution that allows the application teams to modify the main branch of only the repositories that they manage.Which combination of steps will meet these requirements? (Choose three.)

A. Update the SAML assertion to pass the user's team name. Update the IAM role's trust policy to add an access-team session tag that has the team name.

B. Create an approval rule template for each team in the Organizations management account. Associate the template with all the repositories. Add the developer role ARN as an approver.

C. Create an approval rule template for each account. Associate the template with all repositories. Add the "aws:ResourceTag/access-team": "$ ;{aws:PrincipalTag/access-team}" condition to the approval rule template.

D. For each CodeCommit repository, add an access-team tag that has the value set to the name of the associated team.

E. Attach an SCP to the accounts. Include the following statement:

F. Create an IAM permissions boundary in each account. Include the following statement:

**Đáp án**: ___________

---

## Câu 49

**ID**: 194 | **Loại**: Multiple Choice

A company is reviewing its IAM policies. One policy written by the DevOps engineer has been flagged as too permissive. The policy is used by an AWS Lambda function that issues a stop command to Amazon EC2 instances tagged with Environment: NonProduction over the weekend. The current policy is:What changes should the engineer make to achieve a policy of least permission? (Choose three.)

A. Add the following conditional expression:

B. Change "Resource": "*"to "Resource": "arn:aws:ec2:*:*:instance/*"

C. Add the following conditional expression:

D. Add the following conditional expression:

E. Change "Action": "ec2:*"to "Action": "ec2:StopInstances"

F. Add the following conditional expression:

**Đáp án**: ___________

---

## Câu 50

**ID**: 195 | **Loại**: Multiple Choice

A company is developing an application that will generate log events. The log events consist of five distinct metrics every one tenth of a second and produce a large amount of data.The company needs to configure the application to write the logs to Amazon Timestream. The company will configure a daily query against the Timestream table.Which combination of steps will meet these requirements with the FASTEST query performance? (Choose three.)

A. Use batch writes to write multiple log events in a single write operation.

B. Write each log event as a single write operation.

C. Treat each log as a single-measure record.

D. Treat each log as a multi-measure record.

E. Configure the memory store retention period to be longer than the magnetic store retention period.

F. Configure the memory store retention period to be shorter than the magnetic store retention period.

**Đáp án**: ___________

---

## Câu 51

**ID**: 196 | **Loại**: Multiple Choice

A DevOps engineer has created an AWS CloudFormation template that deploys an application on Amazon EC2 instances. The EC2 instances run Amazon Linux. The application is deployed to the EC2 instances by using shell scripts that contain user data. The EC2 instances have an IAM instance profile that has an IAM role with the AmazonSSMManagedinstanceCore managed policy attached.The DevOps engineer has modified the user data in the CloudFormation template to install a new version of the application. The engineer has also applied the stack update. However, the application was not updated on the running EC2 instances. The engineer needs to ensure that the changes to the application are installed on the running EC2 instances.Which combination of steps will meet these requirements? (Choose two.)

A. Configure the user data content to use the Multipurpose Internet Mail Extensions (MIME) multipart format. Set the scripts-user parameter to always in the text/cloud-config section.

B. Refactor the user data commands to use the cfn-init helper script. Update the user data to install and configure the cfn-hup and cfn-init helper scripts to monitor and apply the metadata changes.

C. Configure an EC2 launch template for the EC2 instances. Create a new EC2 Auto Scaling group. Associate the Auto Scaling group with the EC2 launch template. Use the AutoScalingScheduledAction update policy for the Auto Scaling group.

D. Refactor the user data commands to use an AWS Systems Manager document (SSM document). Add an AWS CLI command in the user data to use Systems Manager Run Command to apply the SSM document to the EC2 instances.

E. Refactor the user data command to use an AWS Systems Manager document (SSM document). Use Systems Manager State Manager to create an association between the SSM document and the EC2 instances.

**Đáp án**: ___________

---

## Câu 52

**ID**: 197 | **Loại**: Multiple Choice

A company is refactoring applications to use AWS. The company identifies an internal web application that needs to make Amazon S3 API calls in a specific AWS account.The company wants to use its existing identity provider (IdP) auth.company.com for authentication. The IdP supports only OpenID Connect (OIDC). A DevOps engineer needs to secure the web application's access to the AWS account.Which combination of steps will meet these requirements? (Choose three.)

A. Configure AWS IAM Identity Center (AWS Single Sign-On). Configure an IdP. Upload the IdP metadata from the existing IdP.

B. Create an IAM IdP by using the provider URL, audience, and signature from the existing IP.

C. Create an IAM role that has a policy that allows the necessary S3 actions. Configure the role's trust policy to allow the OIDC IP to assume the role if the sts.amazon.com:aud context key is appid_from_idp.

D. Create an IAM role that has a policy that allows the necessary S3 actions. Configure the role's trust policy to allow the OIDC IP to assume the role if the auth.company.com:aud context key is appid_from_idp.

E. Configure the web application to use the AssumeRoleWithWebIdentity API operation to retrieve temporary credentials. Use the temporary credentials to make the S3 API calls.

F. Configure the web application to use the GetFederationToken API operation to retrieve temporary credentials. Use the temporary credentials to make the S3 API calls.

**Đáp án**: ___________

---

## Câu 53

**ID**: 199 | **Loại**: Multiple Choice

A company is migrating from its on-premises data center to AWS. The company currently uses a custom on-premises Cl/CD pipeline solution to build and package software.The company wants its software packages and dependent public repositories to be available in AWS CodeArtifact to facilitate the creation of application-specific pipelines.Which combination of steps should the company take to update the CI/CD pipeline solution and to configure CodeArtifact with the LEAST operational overhead? (Choose two.)

A. Update the C1ICD pipeline to create a VM image that contains newly packaged software. Use AWS Import/Export to make the VM image available as an Amazon EC2 AMI. Launch the AMI with an attached IAM instance profile that allows CodeArtifact actions. Use AWS CLI commands to publish the packages to a CodeArtifact repository.

B. Create an AWS Identity and Access Management Roles Anywhere trust anchor. Create an IAM role that allows CodeArtifact actions and that has a trust relationship on the trust anchor. Update the on-premises CI/CD pipeline to assume the new IAM role and to publish the packages to CodeArtifact.

C. Create a new Amazon S3 bucket. Generate a presigned URL that allows the PutObject request. Update the on-premises CI/CD pipeline to use the presigned URL to publish the packages from the on-premises location to the S3 bucket. Create an AWS Lambda function that runs when packages are created in the bucket through a put command. Configure the Lambda function to publish the packages to CodeArtifact.

D. For each public repository, create a CodeArutact repository that is configured with an external connection. Configure the dependent repositories as upstream public repositories.

E. Create a Codeartitact repository that is configured with a set of external connections to the public repositories. Configure the external connections to be downstream of the repository.

**Đáp án**: ___________

---

## Câu 54

**ID**: 201 | **Loại**: Multiple Choice

A company recently deployed its web application on AWS. The company is preparing for a large-scale sales event and must ensure that the web application can scale to meet the demand.The application's frontend infrastructure includes an Amazon CloudFront distribution that has an Amazon S3 bucket as an origin. The backend infrastructure includes an Amazon API Gateway API, several AWS Lambda functions, and an Amazon Aurora DB cluster.The company's DevOps engineer conducts a load test and identifies that the Lambda functions can fulfil the peak number of requests. However, the DevOps engineer notices request latency during the initial burst of requests. Most of the requests to the Lambda functions produce queries to the database. A large portion of the invocation time is used to establish database connections.Which combination of steps will provide the application with the required scalability? (Choose three.)

A. Configure a higher reserved concurrency for the Lambda functions.

B. Configure a higher provisioned concurrency for the Lambda functions.

C. Convert the DB cluster to an Aurora global database. Add additional Aurora Replicas in AWS Regions based on the locations of the company's customers.

D. Refactor the Lambda functions. Move the code blocks that initialize database connections into the function handlers.

E. Use Amazon RDS Proxy to create a proxy for the Aurora database. Update the Lambda functions to use the proxy endpoints for database connections.

**Đáp án**: ___________

---

## Câu 55

**ID**: 208 | **Loại**: Multiple Choice

A company has deployed a complex container-based workload on AWS. The workload uses Amazon Managed Service for Prometheus for monitoring. The workload runs in an AmazonElastic Kubernetes Service (Amazon EKS) cluster in an AWS account.The company’s DevOps team wants to receive workload alerts by using the company’s Amazon Simple Notification Service (Amazon SNS) topic. The SNS topic is in the same AWS account as the EKS cluster.Which combination of steps will meet these requirements? (Choose three.)

A. Use the Amazon Managed Service for Prometheus remote write URL to send alerts to the SNS topic

B. Create an alerting rule that checks the availability of each of the workload’s containers.

C. Create an alert manager configuration for the SNS topic.

D. Modify the access policy of the SNS topic. Grant the aps.amazonaws.com service principal the sns:Publish permission and the sns:GetTopicAttributes permission for the SNS topic.

E. Modify the IAM role that Amazon Managed Service for Prometheus uses. Grant the role the sns:Publish permission and the sns:GetTopicAttributes permission for the SNS topic.

F. Create an OpenID Connect (OIDC) provider for the EKS cluster. Create a cluster service account. Grant the account the sns:Publish permission and the sns:GetTopicAttributes permission by using an IAM role.

**Đáp án**: ___________

---

## Câu 56

**ID**: 210 | **Loại**: Multiple Choice

A company has a fleet of Amazon EC2 instances that run Linux in a single AWS account. The company is using an AWS Systems Manager Automation task across the EC2 instances.During the most recent patch cycle, several EC2 instances went into an error state because of insufficient available disk space. A DevOps engineer needs to ensure that the EC2 instances have sufficient available disk space during the patching process in the future.Which combination of steps will meet these requirements? (Choose two.)

A. Ensure that the Amazon CloudWatch agent is installed on all EC2 instances.

B. Create a cron job that is installed on each EC2 instance to periodically delete temporary files.

C. Create an Amazon CloudWatch log group for the EC2 instances. Configure a cron job that is installed on each EC2 instance to write the available disk space to a CloudWatch log stream for the relevant EC2 instance.

D. Create an Amazon CloudWatch alarm to monitor available disk space on all EC2 instances. Add the alarm as a safety control to the Systems Manager Automation task.

E. Create an AWS Lambda function to periodically check for sufficient available disk space on all EC2 instances by evaluating each EC2 instance's respective Amazon CloudWatch log stream.

**Đáp án**: ___________

---

## Câu 57

**ID**: 211 | **Loại**: Multiple Choice

A DevOps engineer is building an application that uses an AWS Lambda function to query an Amazon Aurora MySQL DB cluster. The Lambda function performs only read queries. Amazon EventBridge events invoke the Lambda function.As more events invoke the Lambda function each second, the database's latency increases and the database's throughput decreases. The DevOps engineer needs to improve the performance of the application.Which combination of steps will meet these requirements? (Choose three.)

A. Use Amazon RDS Proxy to create a proxy. Connect the proxy to the Aurora cluster reader endpoint. Set a maximum connections percentage on the proxy.

B. Implement database connection pooling inside the Lambda code. Set a maximum number of connections on the database connection pool.

C. Implement the database connection opening outside the Lambda event handler code.

D. Implement the database connection opening and closing inside the Lambda event handler code.

E. Connect to the proxy endpoint from the Lambda function.

F. Connect to the Aurora cluster endpoint from the Lambda function.

**Đáp án**: ___________

---

## Câu 58

**ID**: 217 | **Loại**: Multiple Choice

A company has an application that runs on AWS Lambda and sends logs to Amazon CloudWatch Logs. An Amazon Kinesis data stream is subscribed to the log groups in CloudWatch Logs. A single consumer Lambda function processes the logs from the data stream and stores the logs in an Amazon S3 bucket.The company’s DevOps team has noticed high latency during the processing and ingestion of some logs.Which combination of steps will reduce the latency? (Choose three.)

A. Create a data stream consumer with enhanced fan-out. Set the Lambda function that processes the logs as the consumer.

B. Increase the ParallelizationFactor setting in the Lambda event source mapping.

C. Configure reserved concurrency for the Lambda function that processes the logs.

D. Increase the batch size in the Kinesis data stream.

E. Turn off the ReportBatchItemFailures setting in the Lambda event source mapping.

F. Increase the number of shards in the Kinesis data stream.

**Đáp án**: ___________

---

## Câu 59

**ID**: 219 | **Loại**: Multiple Choice

A company deploys an application in two AWS Regions. The application currently uses an Amazon S3 bucket in the primary Region to store data.A DevOps engineer needs to ensure that the application is highly available in both Regions. The DevOps engineer has created a new S3 bucket in the secondary Region. All existing and new objects must be in both S3 buckets. The application must fail over between the Regions with no data loss.Which combination of steps will meet these requirements with the MOST operational efficiency? (Choose three.)

A. Create a new IAM role that allows the Amazon S3 and S3 Batch Operations service principals to assume the role that has the necessary permissions for S3 replication.

B. Create a new IAM role that allows the AWS Batch service principal to assume the role that has the necessary permissions for S3 replication.

C. Create an S3 Cross-Region Replication (CRR) rule on the source S3 bucket. Configure the rule to use the IAM role for Amazon S3 to replicate to the target S3 bucket.

D. Create a two-way replication rule on the source S3 bucket. Configure the rule to use the IAM role for Amazon S3 to replicate to the target S3 bucket.

E. Create an AWS Batch job that has an AWS Fargate orchestration type. Configure the job to use the IAM role for AWS Batch. Specify a Bash command to use the AWS CLI to synchronize the contents of the source S3 bucket and the target S3 bucket

F. Create an operation in S3 Batch Operations to replicate the contents of the source S3 bucket to the target S3 bucket. Configure the operation to use the IAM role for Amazon S3.

**Đáp án**: ___________

---

## Câu 60

**ID**: 220 | **Loại**: Multiple Choice

A company uses an organization in AWS Organizations to manage multiple AWS accounts. The company needs an automated process across all AWS accounts to isolate any compromised Amazon EC2 instances when the instances receive a specific tag.Which combination of steps will meet these requirements? (Choose two.)

A. Use AWS CloudFormation StackSets to deploy the CloudFormation stacks in all AWS accounts.

B. Create an SCP that has a Deny statement for the ec2:* action with a condition of "aws:RequestTag/isolation": false.

C. Attach the SCP to the root of the organization.

D. Create an AWS CloudFormation template that creates an EC2 instance role that has no IAM policies attached. Configure the template to have a security group that has an explicit Deny rule on all traffic. Use the CloudFormation template to create an AWS Lambda function that attaches the IAM role to instances. Configure the Lambda function to add a network ACL. Set up an Amazon EventBridge rule to invoke the Lambda function when a specific tag is applied to a compromised EC2 instance.

E. Create an AWS CloudFormation template that creates an EC2 instance role that has no IAM policies attached. Configure the template to have a security group that has no inbound rules or outbound rules. Use the CloudFormation template to create an AWS Lambda function that attaches the IAM role to instances. Configure the Lambda function to replace any existing security groups with the new security group. Set up an Amazon EventBridge rule to invoke the Lambda function when a specific tag is applied to a compromised EC2 instance.

**Đáp án**: ___________

---

## Câu 61

**ID**: 225 | **Loại**: Multiple Choice

A company wants to deploy a workload on several hundred Amazon EC2 instances. The company will provision the EC2 instances in an Auto Scaling group by using a launch template.The workload will pull files from an Amazon S3 bucket, process the data, and put the results into a different S3 bucket. The EC2 instances must have least-privilege permissions and must use temporary security credentials.Which combination of steps will meet these requirements? (Choose two.)

A. Create an IAM role that has the appropriate permissions for S3 buckets Add the IAM role to an instance profile.

B. Update the launch template to include the IAM instance profile.

C. Create an IAM user that has the appropriate permissions for Amazon S3 Generate a secret key and token.

D. Create a trust anchor and profile Attach the IAM role to the profile.

E. Update the launch template Modify the user data to use the new secret key and token.

**Đáp án**: ___________

---

## Câu 62

**ID**: 230 | **Loại**: Multiple Choice

A company uses AWS Organizations to manage its AWS accounts. The company wants its monitoring system to receive an alert when a root user logs in. The company also needs a dashboard to display any log activity that the root user generates.Which combination of steps will meet these requirements? (Choose three.)

A. Enable AWS Config with a multi-account aggregator. Configure log forwarding to Amazon CloudWatch Logs.

B. Create an Amazon QuickSight dashboard that uses an Amazon CloudWatch Logs query.

C. Create an Amazon CloudWatch Logs metric filter to match root user login events. Configure a CloudWatch alarm and an Amazon Simple Notification Service (Amazon SNS) topic to send alerts to the company's monitoring system.

D. Create an Amazon CloudWatch Logs subscription filter to match root user login events. Configure the filter to forward events to an Amazon Simple Notification Service (Amazon SNS) topic. Configure the SNS topic to send alerts to the company's monitoring system.

E. Create an AWS CloudTrail organization trail. Configure the organization trail to send events to Amazon CloudWatch Logs.

F. Create an Amazon CloudWatch dashboard that uses a CloudWatch Logs Insights query.

**Đáp án**: ___________

---

## Câu 63

**ID**: 231 | **Loại**: Multiple Choice

A company uses AWS Organizations to manage its AWS accounts. A DevOps engineer must ensure that all users who access the AWS Management Console are authenticated through the company’s corporate identity provider (IdP).Which combination of steps will meet these requirements? (Choose two.)

A. Use Amazon GuardDuty with a delegated administrator account Use GuardDuty to enforce denial of IAM user logins.

B. Use AWS IAM Identity Center to configure identity federation with SAML 2.0.

C. Create a permissions boundary in AWS IAM Identity Center to deny password logins for IAM users.

D. Create IAM groups in the Organizations management account to apply consistent permissions for all IAM users.

E. Create an SCP in Organizations to deny password creation for IAM users.

**Đáp án**: ___________

---

## Câu 64

**ID**: 232 | **Loại**: Multiple Choice

A company has deployed a new platform that runs on Amazon Elastic Kubernetes Service (Amazon EKS). The new platform hosts web applications that users frequently update. The application developers build the Docker images for the applications and deploy the Docker images manually to the platform.The platform usage has increased to more than 500 users every day. Frequent updates, building the updated Docker images for the applications, and deploying the Docker images on the platform manually have all become difficult to manage.The company needs to receive an Amazon Simple Notification Service (Amazon SNS) notification if Docker image scanning returns any HIGH or CRITICAL findings for operating system or programming language package vulnerabilities.Which combination of steps will meet these requirements? (Choose two.)

A. Create an AWS CodeCommit repository to store the Dockerfile and Kubernetes deployment files. Create a pipeline in AWS CodePipeline. Use an Amazon S3 event to invoke the pipeline when a newer version of the Dockerfile is committed. Add a step to the pipeline to initiate the AWS CodeBuild project.

B. Create an AWS CodeCommit repository to store the Dockerfile and Kubernetes deployment files. Create a pipeline in AWS CodePipeline. Use an Amazon EventBridge event to invoke the pipeline when a newer version of the Dockerfile is committed. Add a step to the pipeline to initiate the AWS CodeBuild project.

C. Create an AWS CodeBuild project that builds the Docker images and stores the Docker images in an Amazon Elastic Container Registry (Amazon ECR) repository. Turn on basic scanning for the ECR repository. Create an Amazon EventBridge rule that monitors Amazon GuardDuty events. Configure the EventBridge rule to send an event to an SNS topic when the finding-severity-counts parameter is more than 0 at a CRITICAL or HIGH level.

D. Create an AWS CodeBuild project that builds the Docker images and stores the Docker images in an Amazon Elastic Container Registry (Amazon ECR) repository. Turn on enhanced scanning for the ECR repository. Create an Amazon EventBridge rule that monitors ECR image scan events. Configure the EventBridge rule to send an event to an SNS topic when the finding-severity-counts parameter is more than 0 at a CRITICAL or HIGH level.

E. Create an AWS CodeBuild project that scans the Dockerfile. Configure the project to build the Docker images and store the Docker images in an Amazon Elastic Container Registry (Amazon ECR) repository if the scan is successful. Configure an SNS topic to provide notification if the scan returns any vulnerabilities.

**Đáp án**: ___________

---

## Câu 65

**ID**: 233 | **Loại**: Multiple Choice

A company groups its AWS accounts in OUs in an organization in AWS Organizations. The company has deployed a set of Amazon API Gateway APIs in one of the Organizations accounts. The APIs are bound to the account's VPC and have no existing authentication mechanism. Only principals in a specific OU can have permissions to invoke the APIs.The company applies the following policy to the API Gateway interface VPC endpoint:The company also updates the API Gateway resource policies to deny invocations that do not come through the interface VPC endpoint. After the updates, the following error message appears during attempts to use the interface VPC endpoint URL to invoke an API: "User: anonymous is not authorized."Which combination of steps will solve this problem? (Choose two.)

A. Enable IAM authentication on all API methods by setting AWS JAM as the authorization method.

B. Create a token-based AWS Lambda authorizer that passes the caller's identity in a bearer token.

C. Create a request parameter-based AWS Lambda authorizer that passes the caller's identity in a combination of headers, query string parameters, stage variables, and $cortext variables.

D. Use Amazon Cognito user pools as the authorizer to control access to the API.

E. Verify the identity of the requester by using Signature Version 4 to sign client requests by using AWS credentials.

**Đáp án**: ___________

---

## Câu 66

**ID**: 237 | **Loại**: Multiple Choice

A company has an event-driven JavaScript application. The application uses decoupled AWS managed services that publish, consume, and route events. During application testing, events are not delivered to the target that is specified by an Amazon EventBridge rule.A DevOps team must provide application testers with additional functionality to view, troubleshoot, and prevent the loss of events without redeployment of the application.Which combination of steps should the DevOps team take to meet these requirements? (Choose three.)

A. Launch AWS Device Farm with a standard test environment and project to run a specific build of the application.

B. Create an Amazon S3 bucket. Enable AWS CloudTrail. Create a CloudTrail trail that specifies the S3 bucket as the storage location.

C. Configure the EventBridge rule to use an Amazon Simple Queue Service (Amazon SQS) standard queue as a dead-letter queue.

D. Configure the EventBridge rule to use an Amazon Simple Queue Service (Amazon SQS) FIFO queue as a dead-letter queue.

E. Create a log group in Amazon CloudWatch Logs Specify the log group as an additional target of the EventBridge rule.

F. Update the application code base to use the AWS X-Ray SDK tracing feature to instrument the code with support for the X-Amzn-Trace-Id header.

**Đáp án**: ___________

---

## Câu 67

**ID**: 238 | **Loại**: Multiple Choice

A company is migrating its container-based workloads to an AWS Organizations multi-account environment. The environment consists of application workload accounts that the company uses to deploy and run the containerized workloads. The company has also provisioned a shared services account for shared workloads in the organization.The company must follow strict compliance regulations. All container images must receive security scanning before they are deployed to any environment. Images can be consumed by downstream deployment mechanisms after the images pass a scan with no critical vulnerabilities. Pre-scan and post-scan images must be isolated from one another so that a deployment can never use pre-scan images.A DevOps engineer needs to create a strategy to centralize this process.Which combination of steps will meet these requirements with the LEAST administrative overhead? (Choose two.)

A. Create Amazon Elastic Container Registry (Amazon ECR) repositories in the shared services account: one repository for each pre-scan image and one repository for each post-scan image. Configure Amazon ECR image scanning to run on new image pushes to the pre-scan repositories. Use resource-based policies to grant the organization write access to the pre-scan repositories and read access to the post-scan repositories.

B. Create pre-scan Amazon Elastic Container Registry (Amazon ECR) repositories in each account that publishes container images. Create repositories for post-scan images in the shared services account. Configure Amazon ECR image scanning to run on new image pushes to the pre-scan repositories. Use resource-based policies to grant the organization read access to the post-scan repositories.

C. Configure image replication for each image from the image's pre-scan repository to the image's post-scan repository.

D. Create a pipeline in AWS CodePipeline for each pre-scan repository. Create a source stage that runs when new images are pushed to the pre-scan repositories. Create a stage that uses AWS CodeBuild as the action provider. Write a buildspec.yaml definition that determines the image scanning status and pushes images without critical vulnerabilities to the post-scan repositories.

E. Create an AWS Lambda function. Create an Amazon EventBridge rule that reacts to image scanning completed events and invokes the Lambda function. Write function code that determines the image scanning status and pushes images without critical vulnerabilities to the post-scan repositories.

**Đáp án**: ___________

---

## Câu 68

**ID**: 241 | **Loại**: Multiple Choice

A company has an application that stores data that includes personally identifiable information (PII) in an Amazon S3 bucket. All data is encrypted with AWS Key Management Service (AWS KMS) customer managed keys. All AWS resources are deployed from an AWS CloudFormation template.A DevOps engineer needs to set up a development environment for the application in a different AWS account. The data in the development environment's S3 bucket needs to be updated once a week from the production environment's S3 bucket.The company must not move PII from the production environment without anonymizing the PII first. The data in each environment must be encrypted with different KMS customer managed keys.Which combination of steps should the DevOps engineer take to meet these requirements? (Choose two.)

A. Activate Amazon Macie on the S3 bucket in the production account. Create an AWS Step Functions state machine to initiate a discovery job and redact all PII before copying files to the S3 bucket in the development account. Give the state machine tasks decrypt permissions on the KMS key in the production account. Give the state machine tasks encrypt permissions on the KMS key in the development account.

B. Set up S3 replication between the production S3 bucket and the development S3 bucket. Activate Amazon Macie on the development S3 bucket. Create an AWS Step Functions state machine to initiate a discovery job and redact all PII as the files are copied to the development S3 bucket. Give the state machine tasks encrypt and decrypt permissions on the KMS key in the development account.

C. Set up an S3 Batch Operations job to copy files from the production S3 bucket to the development S3 bucket. In the development account, configure an AWS Lambda function to redact ail PII. Configure S3 Object Lambda to use the Lambda function for S3 GET requests. Give the Lambda function's IAM role encrypt and decrypt permissions on the KMS key in the development account.

D. Create a development environment from the CloudFormation template in the development account. Schedule an Amazon EventBridge rule to start the AWS Step Functions state machine once a week.

E. Create a development environment from the CloudFormation template in the development account. Schedule a cron job on an Amazon EC2 instance to run once a week to start the S3 Batch Operations job.

**Đáp án**: ___________

---

## Câu 69

**ID**: 243 | **Loại**: Multiple Choice

A company's application has an API that retrieves workload metrics. The company needs to audit, analyze, and visualize these metrics from the application to detect issues at scale.Which combination of steps will meet these requirements? (Choose three.)

A. Configure an Amazon EventBridge schedule to invoke an AWS Lambda function that calls the API to retrieve workload metrics. Store the workload metric data in an Amazon S3 bucket.

B. Configure an Amazon EventBridge schedule to invoke an AWS Lambda function that calls the API to retrieve workload metrics. Store the workload metric data in an Amazon DynamoDB table that has a DynamoDB stream enabled.

C. Create an AWS Glue crawler to catalog the workload metric data in the Amazon S3 bucket. Create views in Amazon Athena for the cataloged data.

D. Connect an AWS Glue crawler to the Amazon DynamoDB stream to catalog the workload metric data. Create views in Amazon Athena for the cataloged data.

E. Create Amazon QuickSight datasets from the Amazon Athena views. Create a QuickSight analysis to visualize the workload metric data as a dashboard.

F. Create an Amazon CloudWatch dashboard that has custom widgets that invoke AWS Lambda functions. Configure the Lambda functions to query the workload metrics data from the Amazon Athena views.

**Đáp án**: ___________

---

## Câu 70

**ID**: 244 | **Loại**: Multiple Choice

A DevOps engineer is building the infrastructure for an application. The application needs to run on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster that includes Amazon EC2 instances. The EC2 instances need to use an Amazon Elastic File System (Amazon EFS) file system as a storage backend. The Amazon EFS Container Storage Interface (CSI) driver is installed on the EKS cluster.When the DevOps engineer starts the application, the EC2 instances do not mount the EFS file system.Which solutions will fix the problem? (Choose three.)

A. Switch the EKS nodes from Amazon EC2 to AWS Fargate.

B. Add an inbound rule to the EFS file system’s security group to allow NFS traffic from the EKS cluster.

C. Create an IAM role that allows the Amazon EFS CSI driver to interact with the file system

D. Set up AWS DataSync to configure file transfer between the EFS file system and the EKS nodes.

E. Create a mount target for the EFS file system in the subnet of the EKS nodes.

F. Disable encryption or the EFS file system.

**Đáp án**: ___________

---

## Câu 71

**ID**: 245 | **Loại**: Multiple Choice

A company deploys an application on on-premises devices in the company’s on-premises data center. The company uses an AWS Direct Connect connection between the data center and the company's AWS account. During initial setup of the on-premises devices and during application updates, the application needs to retrieve configuration files from an Amazon Elastic File System (Amazon EFS) file system.All traffic from the on-premises devices to Amazon EFS must remain private and encrypted. The on-premises devices must follow the principle of least privilege for AWS access. The company's DevOps team needs the ability to revoke access from a single device without affecting the access of the other devices.Which combination of steps will meet these requirements? (Choose two.)

A. Create an IAM user that has an access key and a secret key for each device. Attach the AmazonElasticFileSystemFullAccess policy to all IAM users. Configure the AWS CLI on the on-premises devices to use the IAM user's access key and secret key.

B. Generate certificates for each on-premises device in AWS Private Certificate Authority. Create a trust anchor in IAM Roles Anywhere that references an AWS Private CA. Create an IAM role that trust IAM Roles Anywhere. Attach the AmazonElasticFileSystemClientReadWriteAccess to the role. Create an IAM Roles Anywhere profile for the IAM role. Configure the AWS CLI on the on-premises devices to use the aws_signing_helper command to obtain credentials.

C. Create an IAM user that has an access key and a secret key for all devices. Attach the AmazonElasticFileSystemClientReadWriteAccess policy to the IAM user. Configure the AWS CLI on the on-premises devices to use the IAM user's access key and secret key.

D. Use the amazon-efs-utils package to mount the EFS file system.

E. Use the native Linux NFS client to mount the EFS file system.

**Đáp án**: ___________

---

## Câu 72

**ID**: 252 | **Loại**: Multiple Choice

A company needs to increase the security of the container images that run in its production environment. The company wants to integrate operating system scanning and programming language package vulnerability scanning for the containers in its CI/CD pipeline. The CI/CD pipeline is an AWS CodePipeline pipeline that includes an AWS CodeBuild build project, AWS CodeDeploy actions, and an Amazon Elastic Container Registry (Amazon ECR) repository.A DevOps engineer needs to add an image scan to the CI/CD pipeline. The CI/CD pipeline must deploy only images without CRITICAL and HIGH findings into production.Which combination of steps will meet these requirements? (Choose two.)

A. Use Amazon ECR basic scanning.

B. Use Amazon ECR enhanced scanning.

C. Configure Amazon ECR to submit a Rejected status to the CI/CD pipeline when the image scan returns CRITICAL or HIGH findings.

D. Configure an Amazon EventBridge rule to invoke an AWS Lambda function when the image scan is completed. Configure the Lambda function to consume the Amazon Inspector scan status and to submit an Approved or Rejected status to the CI/CD pipeline.

E. Configure an Amazon EventBridge rule to invoke an AWS Lambda function when the image scan is completed. Configure the Lambda function to consume the Clair scan status and to submit an Approved or Rejected status to the CI/CD pipeline.

**Đáp án**: ___________

---

## Câu 73

**ID**: 255 | **Loại**: Multiple Choice

A company needs a strategy for failover and disaster recovery of its data and application. The application uses a MySQL database and Amazon EC2 instances. The company requires a maximum RPO of 2 hours and a maximum RTO of 10 minutes for its data and application at all times.Which combination of deployment strategies will meet these requirements? (Choose two.)

A. Create an Amazon Aurora Single-AZ cluster in multiple AWS Regions as the data store. Use Aurora's automatic recovery capabilities in the event of a disaster.

B. Create an Amazon Aurora global database in two AWS Regions as the data store. In the event of a failure, promote the secondary Region to the primary for the application. Update the application to use the Aurora cluster endpoint in the secondary Region.

C. Create an Amazon Aurora cluster in multiple AWS Regions as the data store. Use a Network Load Balancer to balance the database traffic in different Regions.

D. Set up the application in two AWS Regions. Use Amazon Route 53 failover routing that points to Application Load Balancers in both Regions. Use health checks and Auto Scaling groups in each Region.

E. Set up the application in two AWS Regions. Configure AWS Global Accelerator to point to Application Load Balancers (ALBs) in both Regions. Add both ALBs to a single endpoint group. Use health checks and Auto Scaling groups in each Region.

**Đáp án**: ___________

---

## Câu 74

**ID**: 256 | **Loại**: Multiple Choice

A developer is using the AWS Serverless Application Model (AWS SAM) to create a prototype for an AWS Lambda function. The AWS SAM template contains an AWS::Serverless::Function resource that has the CodeUri property that points to an Amazon S3 location. The developer wants to identify the correct commands for deployment before creating a CI/CD pipeline.The developer creates an archive of the Lambda function code named package.zip. The developer uploads the .zip file archive to the S3 location specified in the CodeUri property. The developer runs the sam deploy command and deploys the Lambda function. The developer updates the Lambda function code and uses the same steps to deploy the new version of the Lambda function. The sam deploy command fails and returns an error of no changes to deploy.Which solutions will deploy the new version? (Choose two.)

A. Use the aws cloudformation update-stack command instead of the sam deploy command.

B. Use the aws cloudformation update-stack-instances command instead of the sam deploy command.

C. Update the CodeUri property to reference the local application code folder. Use the sam deploy command.

D. Update the CodeUri property to reference the local application code folder. Use the aws cloudformation create-change-set command and the aws cloudformation execute-change-set command.

E. Update the CodeUri property to reference the local application code folder. Use the aws cloudformation package command and the aws cloudformation deploy command.

**Đáp án**: ___________

---

## Câu 75

**ID**: 259 | **Loại**: Multiple Choice

A company's development team uses AWS CloudFormation to deploy its application resources. The team must use CloudFormation for all changes to the environment. The team cannot use the AWS Management Console or the AWS CLI to make manual changes directly.The team uses a developer IAM role to access the environment. The role is configured with the AdministratorAccess managed IAM policy. The company has created a new CloudFormationDeployment IAM role that has the following policy attached:The company wants to ensure that only CloudFormation can use the new role. The development team cannot make any manual changes to the deployed resources.Which combination of steps will meet these requirements? (Choose three.)

A. Remove the AdministratorAccess policy. Assign the ReadOnlyAccess managed IAM policy to the developer role. Instruct the developers to use the CloudFormationDeployment role as a CloudFormation service role when the developers deploy new stacks.

B. Update the trust policy of the CloudFormationDeployment role to allow the developer IAM role to assume the CloudFormationDeployment role.

C. Configure the developer IAM role to be able to get and pass the CloudFormationDeployment role if iam:PassedToService equals . Configure the CloudFormationDeployment role to allow all cloudformation actions for all resources.

D. Update the trust policy of the CloudFormationDeployment role to allow the cloudformation.amazonaws.com AWS principal to perform the iam:AssumeRole action.

E. Remove the AdministratorAccess policy. Assign the ReadOnlyAccess managed IAM policy to the developer role. Instruct the developers to assume the CloudFormationDeployment role when the developers deploy new stacks.

F. Add an IAM policy to the CloudFormationDeployment role to allow cloudformation:* on all resources. Add a policy that allows the iam:PassRole action for the ARN of the CloudFormationDeployment role if iam:PassedToService equals cloudformation.amazonaws.com.

**Đáp án**: ___________

---

## Câu 76

**ID**: 262 | **Loại**: Multiple Choice

A company has an organization in AWS Organizations for its multi-account environment. A DevOps engineer is developing an AWS CodeArtifact based strategy for application package management across the organization. Each application team at the company has its own account in the organization. Each application team also has limited access to a centralized shared services account.Each application team needs full access to download, publish, and grant access to its own packages. Some common library packages that the application teams use must also be shared with the entire organization.Which combination of steps will meet these requirements with the LEAST administrative overhead? (Choose three.)

A. Create a domain in each application team's account. Grant each application team's account full read access and write access to the application team's domain.

B. Create a domain in the shared services account. Grant the organization read access and CreateRepository access.

C. Create a repository in each application team’s account. Grant each application team’s account full read access and write access to its own repository.

D. Create a repository in the shared services account. Grant the organization read access to the repository in the shared services account Set the repository as the upstream repository in each application team's repository.

E. For teams that require shared packages, create resource-based policies that allow read access to the repository from other application teams' accounts.

F. Set the other application teams' repositories as upstream repositories.

**Đáp án**: ___________

---

## Câu 77

**ID**: 264 | **Loại**: Multiple Choice

A company has set up AWS CodeArtifact repositories with public upstream repositories. The company's development team consumes open source dependencies from the repositories in the company's internal network.The company's security team recently discovered a critical vulnerability in the most recent version of a package that the development team consumes. The security team has produced a patched version to fix the vulnerability. The company needs to prevent the vulnerable version from being downloaded. The company also needs to allow the security team to publish the patched version.Which combination of steps will meet these requirements? (Choose two.)

A. Update the status of the affected CodeArtifact package version to unlisted.

B. Update the status of the affected CodeArtifact package version to deleted.

C. Update the status of the affected CodeArtifact package version to archived.

D. Update the CodeArtifact package origin control settings to allow direct publishing and to block upstream operations.

E. Update the CodeArtifact package origin control settings to block direct publishing and to allow upstream operations.

**Đáp án**: ___________

---

## Câu 78

**ID**: 267 | **Loại**: Multiple Choice

A company's application uses a fleet of Amazon EC2 On-Demand Instances to analyze and process data. The EC2 instances are in an Auto Scaling group. The Auto Scaling group is a target group for an Application Load Balancer (ALB). The application analyzes critical data that cannot tolerate interruption. The application also analyzes noncritical data that can withstand interruption.The critical data analysis requires quick scalability in response to real-time application demand. The noncritical data analysis involves memory consumption. A DevOps engineer must implement a solution that reduces scale-out latency for the critical data. The solution also must process the noncritical data.Which combination of steps will meet these requirements? (Choose two.)

A. For the critical data, modify the existing Auto Scaling group. Create a warm pool instance in the stopped state. Define the warm pool size. Create a new version of the launch template that has detailed monitoring enabled. Use Spot Instances.

B. For the critical data, modify the existing Auto Scaling group. Create a warm pool instance in the stopped state. Define the warm pool size. Create a new version of the launch template that has detailed monitoring enabled. Use On-Demand Instances.

C. For the critical data, modify the existing Auto Scaling group. Create a lifecycle hook to ensure that bootstrap scripts are completed successfully. Ensure that the application on the instances is ready to accept traffic before the instances are registered. Create a new version of the launch template that has detailed monitoring enabled.

D. For the noncritical data, create a second Auto Scaling group that uses a launch template. Configure the launch template to install the unified Amazon CloudWatch agent and to configure the CloudWatch agent with a custom memory utilization metric. Use Spot Instances. Add the new Auto Scaling group as the target group for the ALB. Modify the application to use two target groups for critical data and noncritical data.

E. For the noncritical data, create a second Auto Scaling group. Choose the predefined memory utilization metric type for the target tracking scaling policy. Use Spot Instances. Add the new Auto Scaling group as the target group for the ALB. Modify the application to use two target groups for critical data and noncritical data.

**Đáp án**: ___________

---

## Câu 79

**ID**: 268 | **Loại**: Multiple Choice

A company recently migrated its application to an Amazon Elastic Kubernetes Service (Amazon EKS) cluster that uses Amazon EC2 instances. The company configured the application to automatically scale based on CPU utilization.The application produces memory errors when it experiences heavy loads. The application also does not scale out enough to handle the increased load. The company needs to collect and analyze memory metrics for the application over time.Which combination of steps will meet these requirements? (Choose three.)

A. Attach the CloudWatchAgentServerPolicy managed IAM policy to the IAM instance profile that the cluster uses.

B. Attach the CloudWatchAgentServerPolicy managed IAM policy to a service account role for the cluster.

C. Collect performance metrics by deploying the unified Amazon CloudWatch agent to the existing EC2 instances in the cluster. Add the agent to the AMI for any new EC2 instances that are added to the cluster.

D. Collect performance logs by deploying the AWS Distro for OpenTelemetry collector as a DaemonSet.

E. Analyze the pod_memory_utilization Amazon CloudWatch metric in the ContainerInsights namespace by using the Service dimension.

F. Analyze the node_memory_utilization Amazon CloudWatch metric in the ContainerInsights namespace by using the ClusterName dimension.

**Đáp án**: ___________

---

## Câu 80

**ID**: 270 | **Loại**: Multiple Choice

A company uses AWS Organizations to manage hundreds of AWS accounts. The company has a team that is responsible for AWS Identity and Access Management (IAM).The IAM team wants to implement AWS IAM Identity Center (AWS Single Sign-On). The IAM team must have only the minimum needed permissions to manage IAM Identity Center. The IAM team must not be able to gain unneeded access to the Organizations management account. The IAM team must be able to provision new IAM Identity Center permission sets and assignments for existing and new member accounts.Which combination of steps will meet these requirements? (Choose three.)

A. Create a new AWS account for the IAM team. In the new account, enable IAM Identity Center. In the Organizations management account, register the new account as a delegated administrator for IAM Identity Center.

B. Create a new AWS account for the IAM team. In the Organizations management account, enable IAM Identity Center. In the Organizations management account, register the new account as a delegated administrator for IAM Identity Center.

C. In IAM Identity Center, create users and a group for the IAM team. Add the users to the group. Create a new permission set. Attach the AWSSSODirectoryAdministrator managed IAM policy to the group.

D. In IAM Identity Center, create users and a group for the IAM team. Add the users to the group. Create a new permission set. Attach the AWSSSOMemberAccountAdministrator managed IAM policy to the group.

E. Assign the permission set to the Organizations management account. Allow the IAM team group to use the permission set.

F. Assign the permission set to the new AWS account. Allow the IAM team group to use the permission set.

**Đáp án**: ___________

---

## Câu 81

**ID**: 271 | **Loại**: Multiple Choice

A company uses an organization in AWS Organizations that has all features enabled. The company uses AWS Backup in a primary account and uses an AWS Key Management Service (AWS KMS) key to encrypt the backups.The company needs to automate a cross-account backup of the resources that AWS Backup backs up in the primary account. The company configures cross-account backup in the Organizations management account. The company creates a new AWS account in the organization and configures an AWS Backup backup vault in the new account. The company creates a KMS key in the new account to encrypt the backups. Finally, the company configures a new backup plan in the primary account. The destination for the new backup plan is the backup vault in the new account.When the AWS Backup job in the primary account is invoked, the job creates backups in the primary account. However, the backups are not copied to the new account's backup vault.Which combination of steps must the company take so that backups can be copied to the new account's backup vault? (Choose two.)

A. Edit the backup vault access policy in the new account to allow access to the primary account.

B. Edit the backup vault access policy in the primary account to allow access to the new account.

C. Edit the backup vault access policy in the primary account to allow access to the KMS key in the new account.

D. Edit the key policy of the KMS key in the primary account to share the key with the new account.

E. Edit the key policy of the KMS key in the new account to share the key with the primary account.

**Đáp án**: ___________

---

## Câu 82

**ID**: 272 | **Loại**: Multiple Choice

A company runs an application that uses an Amazon S3 bucket to store images. A DevOps engineer needs to implement a multi-Region strategy for the objects that are stored in the S3 bucket. The company needs to be able to fail over to an S3 bucket in another AWS Region. When an image is added to either S3 bucket, the image must be replicated to the other S3 bucket within 15 minutes.The DevOps engineer enables two-way replication between the S3 buckets.Which combination of steps should the DevOps engineer take next to meet the requirements? (Choose three.)

A. Enable S3 Replication Time Control (S3 RTC) on each replication rule.

B. Create an S3 Multi-Region Access Point in an active-passive configuration.

C. Call the SubmitMultiRegionAccessPointRoutes operation in the AWS API when the company needs to fail over to the S3 bucket in the other Region.

D. Enable S3 Transfer Acceleration on both S3 buckets.

E. Configure a routing control in Amazon Route 53 Recovery Controller. Add the S3 buckets in an active-passive configuration.

F. Call the UpdateRoutingControlStates operation in the AWS API when the company needs to fail over to the S3 bucket in the other Region.

**Đáp án**: ___________

---

## Câu 83

**ID**: 273 | **Loại**: Multiple Choice

A company uses the AWS Cloud Development Kit (AWS CDK) to define its application. The company uses a pipeline that consists of AWS CodePipeline and AWS CodeBuild to deploy the CDK application.The company wants to introduce unit tests to the pipeline to test various infrastructure components. The company wants to ensure that a deployment proceeds if no unit tests result in a failure.Which combination of steps will enforce the testing requirement in the pipeline? (Choose two.)

A. Update the CodeBuild build phase commands to run the tests then to deploy the application. Set the OnFailure phase property to ABORT.

B. Update the CodeBuild build phase commands to run the tests then to deploy the application. Add the --rollback true flag to the cdk deploy command.

C. Update the CodeBuild build phase commands to run the tests then to deploy the application. Add the --require-approval any-change flag to the cdk deploy command.

D. Create a test that uses the AWS CDK assertions module. Use the template.hasResourceProperties assertion to test that resources have the expected properties.

E. Create a test that uses the cdk diff command. Configure the test to fail if any resources have changed.

**Đáp án**: ___________

---

## Câu 84

**ID**: 276 | **Loại**: Multiple Choice

A DevOps engineer needs to implement integration tests into an existing AWS CodePipeline CI/CD workflow for an Amazon Elastic Container Service (Amazon ECS) service. The CI/CD workflow retrieves new application code from an AWS CodeCommit repository and builds a container image. The Cl/CD workflow then uploads the container image to Amazon Elastic Container Registry (Amazon ECR) with a new image tag version.The integration tests must ensure that new versions of the service endpoint are reachable and that various API methods return successful response data. The DevOps engineer has already created an ECS cluster to test the service.Which combination of steps will meet these requirements with the LEAST management overhead? (Choose three.)

A. Add a deploy stage to the pipeline. Configure Amazon ECS as the action provider.

B. Add a deploy stage to the pipeline. Configure AWS CodeDeploy as the action provider.

C. Add an appspec.yml file to the CodeCommit repository.

D. Update the image build pipeline stage to output an imagedefinitions.json file that references the new image tag.

E. Create an AWS Lambda function that runs connectivity checks and API calls against the service. Integrate the Lambda function with CodePipeline by using a Lambda action stage.

F. Write a script that runs integration tests against the service. Upload the script to an Amazon S3 bucket. Integrate the script in the S3 bucket with CodePipeline by using an S3 action stage.

**Đáp án**: ___________

---

## Câu 85

**ID**: 277 | **Loại**: Multiple Choice

A company runs applications on Windows and Linux Amazon EC2 instances. The instances run across multiple Availability Zones in an AWS Region. The company uses Auto Scaling groups for each application.The company needs a durable storage solution for the instances. The solution must use SMB for Windows and must use NFS for Linux. The solution must also have sub-millisecond latencies. All instances will read and write the data.Which combination of steps will meet these requirements? (Choose three.)

A. Create an Amazon Elastic File System (Amazon EFS) file system that has targets in multiple Availability Zones.

B. Create an Amazon FSx for NetApp ONTAP Multi-AZ file system.

C. Create a General Purpose SSD (gp3) Amazon Elastic Block Store (Amazon EBS) volume to use for shared storage.

D. Update the user data for each application’s launch template to mount the file system.

E. Perform an instance refresh on each Auto Scaling group.

F. Update the EC2 instances for each application to mount the file system when new instances are launched.

**Đáp án**: ___________

---

## Câu 86

**ID**: 282 | **Loại**: Multiple Choice

A DevOps engineer manages a Java-based application that runs in an Amazon Elastic Container Service (Amazon ECS) cluster on AWS Fargate. Auto scaling has not been configured for the application.The DevOps engineer has determined that the Java Virtual Machine (JVM) thread count is a good indicator of when to scale the application. The application serves customer traffic on port 8080 and makes JVM metrics available on port 9404.Application use has recently increased. The DevOps engineer needs to configure auto scaling for the application.Which solution will meet these requirements with the LEAST operational overhead? (Choose two.)

A. Deploy the Amazon CloudWatch agent as a container sidecar. Configure the CloudWatch agent to retrieve JVM metrics from port 9404. Create CloudWatch alarms on the JVM thread count metric to scale the application. Add a step scaling policy in Fargate to scale up and scale down based on the CloudWatch alarms.

B. Deploy the Amazon CloudWatch agent as a container sidecar. Configure a metric filter for the JVM thread count metric on the CloudWatch log group for the CloudWatch agent. Add a target tracking policy in Fargate. Select the metric from the metric filter as a scale target.

C. Create an Amazon Managed Service for Prometheus workspace. Deploy AWS Distro for OpenTelemetry as a container sidecar to publish the JVM metrics from port 9404 to the Prometheus workspace. Configure rules for the workspace to use the JVM thread count metric to scale the application. Add a step scaling policy in Fargate. Select the Prometheus rules to scale up and scaling down.

D. Create an Amazon Managed Service for Prometheus workspace. Deploy AWS Distro for OpenTelemetry as a container sidecar to retrieve JVM metrics from port 9404 to publish the JVM metrics from port 9404 to the Prometheus workspace. Add a target tracking policy in Fargate. Select the Prometheus metric as a scale target.

**Đáp án**: ___________

---

## Câu 87

**ID**: 296 | **Loại**: Multiple Choice

A company uses AWS Organizations to manage hundreds of AWS accounts. The company has a team that is responsible for AWS Identity and Access Management (IAM).The IAM team wants to implement AWS IAM Identity Center. The IAM team must have only the minimum required permissions to manage IAM Identity Center. The IAM team must not be able to gain unnecessary access to the Organizations management account. The IAM team must be able to provision new IAM Identity Center permission sets and assignments for new and existing member accounts.Which combination of steps will meet these requirements? (Choose three.)

A. Create a new AWS account for the IAM team. Enable IAM Identity Center in the new account. In the Organizations management account, register the new account as a delegated administrator for IAM Identity Center.

B. Create a new AWS account for the IAM team. Enable IAM Identity Center in the Organizations management account. In the Organizations management account, register the new account as a delegated administrator for IAM Identity Center.

C. Create an SCP in Organizations. Create a new OU for the Organizations management account, and link the new SCP to the OU. Configure the SCP to deny all access to IAM Identity Center.

D. Create IAM users and an IAM group for the IAM team in IAM Identity Center. Add the users to the group. Create a new permission set. Attach the AWSSSOMemberAccountAdministrator managed IAM policy to the group.

E. Assign the new permission set to the Organizations management account. Allow the IAM team's group to use the permission set.

F. Assign the new permission set to the new AWS account. Allow the IAM team's group to use the permission set.

**Đáp án**: ___________

---

## Câu 88

**ID**: 298 | **Loại**: Multiple Choice

A company has a web application that is hosted on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. The EKS cluster runs on AWS Fargate that is available through an internet-facing Application Load Balancer.The application is experiencing stability issues that lead to longer response times. A DevOps engineer needs to configure observability in Amazon CloudWatch to troubleshoot the issue. The solution must provide only the minimum necessary permissions.Which combination of steps will meet these requirements? (Choose three.)

A. Deploy the CloudWatch agent as a Kubernetes StatefulSet to the EKS cluster.

B. Deploy the AWS Distro for OpenTelemetry Collector as a Kubernetes DaemonSet to the EKS cluster.

C. Associate a Kubernetes service account with an IAM role by using IAM roles for service accounts in Amazon EKS. Use the CloudWatchAgentServerPolicy AWS managed policy.

D. Associate a Kubernetes service account with an IAM role by using IAM roles for service accounts in Amazon EKS. Use the CloudWatchAgentAdminPolicy AWS managed policy.

E. Configure an IAM OpenID Connect (OIDC) provider for the EKS cluster.

F. Enable EKS control plane logging for the EKS cluster.

**Đáp án**: ___________

---

## Câu 89

**ID**: 303 | **Loại**: Multiple Choice

A company recently configured AWS Control Tower in its organization in AWS Organizations. The company enrolled all existing AWS accounts in AWS Control Tower. The company wants to ensure that all new AWS accounts are automatically enrolled in AWS Control Tower.The company has an existing AWS Step Functions workflow that creates new AWS accounts and performs any actions required as part of account creation. The Step Functions workflow is defined in the same AWS account as AWS Control Tower.Which combination of steps should the company add to the Step Functions workflow to meet these requirements? (Choose two.)

A. Create an Amazon EventBridge event that has an aws.controltower source and a CreateManagedAccount detail-type. Add the details of the new AWS account to the detail field of the event.

B. Create an Amazon EventBridge event that has an aws.controltower source and a SetupLandingZone detail-type. Add the details of the new AWS account to the detail field of the event.

C. Create an AWSControlTowerExecution role in the new AWS account. Configure the role to allow the AWS Control Tower administrator account to assume the role.

D. Call the AWS Service Catalog ProvisionProduct API operation with the details of the new AWS account.

E. Call the Organizations EnableAWSServiceAccess API operation with the controltower.amazonaws.com service name and the details of the new AWS account.

**Đáp án**: ___________

---

## Câu 90

**ID**: 306 | **Loại**: Multiple Choice

A company has deployed an Amazon Elastic Kubernetes Service (Amazon EKS) cluster with Amazon EC2 node groups. The company's DevOps team uses the Kubernetes Horizontal Pod Autoscaler and recently installed a supported EKS cluster Autoscaler.The DevOps team needs to implement a solution to collect metrics and logs of the EKS cluster to establish a baseline for performance. The DevOps team will create an initial set of thresholds for specific metrics and will update the thresholds over time as the cluster is used. The DevOps team must receive an Amazon Simple Notification Service (Amazon SNS) email notification if the initial set of thresholds is exceeded or if the EKS cluster Autoscaler is not functioning properly.The solution must collect cluster, node, and pod metrics. The solution also must capture logs in Amazon CloudWatch.Which combination of steps should the DevOps team take to meet these requirements? (Choose three.)

A. Deploy the CloudWatch agent and Fluent Bit to the cluster. Ensure that the EKS cluster has appropriate permissions to send metrics and logs to CloudWatch.

B. Deploy AWS Distro for OpenTelemetry to the cluster. Ensure that the EKS cluster has appropriate permissions to send metrics and logs to CloudWatch.

C. Create CloudWatch alarms to monitor the CPU, memory, and node failure metrics of the cluster. Configure the alarms to send an SNS email notification to the DevOps team if thresholds are exceeded.

D. Create a CloudWatch composite alarm to monitor a metric log filter of the CPU, memory, and node metrics of the cluster. Configure the alarm to send an SNS email notification to the DevOps team when anomalies are detected.

E. Create a CloudWatch alarm to monitor the logs of the Autoscaler deployments for errors. Configure the alarm to send an SNS email notification to the DevOps team if thresholds are exceeded.

F. Create a CloudWatch alarm to monitor a metric log filter of the Autoscaler deployments for errors. Configure the alarm to send an SNS email notification to the DevOps team if thresholds are exceeded.

**Đáp án**: ___________

---

## Câu 91

**ID**: 310 | **Loại**: Multiple Choice

A company has an AWS CodePipeline pipeline in the eu-west-1 Region. The pipeline stores the build artifacts in an Amazon S3 bucket. The pipeline builds and deploys an AWS Lambda function by using an AWS CloudFormation deploy action.A DevOps engineer needs to update the existing pipeline to also deploy the Lambda function to the us-east-1 Region. The pipeline has already been updated to create an additional artifact to deploy to us-east-1.Which combination of steps should the DevOps engineer take to meet these requirements? (Choose two.)

A. Modify the CloudFormation template to include a parameter for the Lambda function code's .zip file location. Create a new CloudFormation deploy action for us-east-1 in the pipeline. Configure the new deploy action to pass in the us-east-1 artifact location as a parameter override.

B. Create a new CloudFormation deploy action for us-east-1 in the pipeline. Configure the new deploy action to use the CloudFormation template from the additional artifact that was created for us-east-1.

C. Create an S3 bucket in us-east-1. Configure the S3 bucket policy to allow CodePipeline to have read and write access.

D. Create an S3 bucket in us-east-1. Configure S3 Cross-Region Replication (CRR) from the S3 bucket in eu-west-1 to the S3 bucket in us-east-1.

E. Modify the pipeline to include the S3 bucket for us-east-1 as an artifact store. Create a new CloudFormation deploy action for us-east-1 in the pipeline. Configure the new deploy action to use the CloudFormation template from the us-east-1 artifact.

**Đáp án**: ___________

---

## Câu 92

**ID**: 313 | **Loại**: Multiple Choice

A security team sets up a workflow that invokes an AWS Step Functions workflow when Amazon EventBridge matches specific events. The events can be generated by several AWS services. AWS CloudTrail records user activities.The security team notices that some important events do not invoke the workflow as expected. The CloudTrail logs do not indicate any direct errors related to the missing events.Which combination of steps will identify the root cause of the missing event invocations? (Choose three.)

A. Enable EventBridge schema discovery on the event bus to determine whether the event patterns match the expected schema.

B. Configure Amazon CloudWatch to monitor EventBridge metrics and Step Functions metrics. Set up alerts for anomalies in event patterns and workflow invocations.

C. Configure an AWS Lambda logging function to monitor and log events from EventBridge to provide more details about the processed events.

D. Review the Step Functions execution history for patterns of failures or timeouts that could correlate to the missing event invocations.

E. Review metrics for the EventBridge failed invocations to ensure that the IAM execution role that is attached to the rule has sufficient permissions.

F. Verify that the Step Functions workflow has the correct permissions to be invoked by EventBridge.

**Đáp án**: ___________

---

## Câu 93

**ID**: 318 | **Loại**: Multiple Choice

A company runs a fleet of Amazon EC2 instances in a VPC. The company's employees remotely access the EC2 instances by using the Remote Desktop Protocol (RDP).The company wants to collect metrics about how many RDP sessions the employees initiate every day.Which combination of steps will meet this requirement? (Choose three.)

A. Create an Amazon EventBridge rule that reacts to EC2 Instance State-change Notification events.

B. Create an Amazon CloudWatch Logs log group. Specify the log group as a target for the EventBridge rule.

C. Create a flow log in VPC Flow Logs.

D. Create an Amazon CloudWatch Logs log group. Specify the log group as a destination for the flow log.

E. Create a log group metric filter.

F. Create a log group subscription filter. Use EventBridge as the destination.

**Đáp án**: ___________

---

## Câu 94

**ID**: 322 | **Loại**: Multiple Choice

A company is running an internal application in an Amazon Elastic Container Service (Amazon ECS) cluster on Amazon EC2. The ECS cluster instances can connect to the public internet. The ECS tasks that run on the cluster instances are configured to use images from both private Amazon Elastic Container Registry (Amazon ECR) repositories and a public ECR registry repository.A new security policy requires the company to remove the ECS cluster's direct access to the internet. The company must remove any NAT gateways and internet gateways from the VPC that hosts the cluster. A DevOps engineer needs to ensure the ECS cluster can still download images from both the public ECR registry and the private ECR repositories. Images from the public ECR registry must remain up-to-date. New versions of the images must be available to the ECS cluster within 24 hours of publication.Which combination of steps will meet these requirements with the LEAST operational overhead? (Choose three.)

A. Create an AWS CodeBuild project and a new private ECR repository for each image that is downloaded from the public ECR registry. Configure each project to pull the image from the public ECR repository and push the image to the new private ECR repository. Create an Amazon EventBridge rule that invokes the CodeBuild project once every 24 hours. Update each task definition in the ECS cluster to refer to the new private ECR repository.

B. Create a new Amazon ECR pull through cache rule for each image that is downloaded from the public ECR registry. Create an AWS Lambda function that invokes each pull through cache rule. Create an Amazon EventBridge rule that invokes the Lambda function once every 24 hours. Update each task definition in the ECS cluster to refer to the image from the pull through cache.

C. Create a new Amazon ECR pull through cache rule for the public ECR registry. Update each task definition in the ECS cluster to refer to the image from the pull through cache. Ensure each public image has been downloaded through the pull through cache at least once before removing internet access from the VPC.

D. Create an Amazon ECR interface VPC endpoint for the public ECR repositories that are in the VPC.

E. Create an Amazon ECR interface VPC endpoint for the private ECR repositories that are in the VPC.

F. Create an Amazon S3 gateway endpoint in the VPC.

**Đáp án**: ___________

---

## Câu 95

**ID**: 323 | **Loại**: Multiple Choice

A company has a continuous integration pipeline where the company creates container images by using AWS CodeBuild. The created images are stored in Amazon Elastic Container Registry (Amazon ECR).Checking for and fixing the vulnerabilities in the images takes the company too much time. The company wants to identify the image vulnerabilities quickly and notify the security team of the vulnerabilities.Which combination of steps will meet these requirements with the LEAST operational overhead? (Choose two.)

A. Activate Amazon Inspector enhanced scanning for Amazon ECR. Configure the enhanced scanning to use continuous scanning. Set up a topic in Amazon Simple Notification Service (Amazon SNS).

B. Create an Amazon EventBridge rule for Amazon Inspector findings. Set an Amazon Simple Notification Service (Amazon SNS) topic as the rule target.

C. Activate AWS Lambda enhanced scanning for Amazon ECR. Configure the enhanced scanning to use continuous scanning. Set up a topic in Amazon Simple Email Service (Amazon SES).

D. Create a new AWS Lambda function. Invoke the new Lambda function when scan findings are detected.

E. Activate default basic scanning for Amazon ECR for all container images. Configure the default basic scanning to use continuous scanning. Set up a topic in Amazon Simple Notification Service (Amazon SNS).

**Đáp án**: ___________

---

## Câu 96

**ID**: 325 | **Loại**: Multiple Choice

A company uses Amazon Redshift as its data warehouse solution. The company wants to create a dashboard to view changes to the Redshift users and the queries the users perform.Which combination of steps will meet this requirement? (Choose two.)

A. Create an Amazon CloudWatch log group. Create an AWS CloudTrail trail that writes to the CloudWatch log group.

B. Create a new Amazon S3 bucket. Configure default audit logging on the Redshift cluster. Configure the S3 bucket as the target.

C. Configure the Redshift cluster database audit logging to include user activity logs. Configure Amazon CloudWatch as the target.

D. Create an Amazon CloudWatch dashboard that has a log widget. Configure the widget to display user details from the Redshift logs.

E. Create an AWS Lambda function that uses Amazon Athena to query the Redshift logs. Create an Amazon CloudWatch dashboard that has a custom widget type that uses the Lambda function.

**Đáp án**: ___________

---

## Câu 97

**ID**: 327 | **Loại**: Multiple Choice

A DevOps engineer uses a pipeline in AWS CodePipeline. The pipeline has a build action and a deploy action for a single-page web application that is delivered to an Amazon S3 bucket. Amazon CloudFront serves the web application. The build action creates an artifact for the web application.The DevOps engineer has created an AWS CloudFormation template that defines the S3 bucket and configures the S3 bucket to host the application. The DevOps engineer has configured a CloudFormation deploy action before the S3 action. The CloudFormation deploy action creates the S3 bucket. The DevOps engineer needs to configure the S3 deploy action to use the S3 bucket from the CloudFormation template.Which combination of steps will meet these requirements? (Choose two.)

A. Add an output named BucketName to the CloudFormation template. Set the output's value to refer to the S3 bucket from the CloudFormation template. Configure the output value to export to an AWS::SSM::Parameter resource named Stackvariables.

B. Add an output named BucketName to the CloudFormation template. Set the output's value to refer to the S3 bucket from the CloudFormation template. Set the CloudFormation action's namespace to StackVariables in the pipeline.

C. Configure the output artifacts of the CloudFormation action in the pipeline to be an AWS Systems Manager Parameter Store parameter named StackVariables. Name the artifact BucketName.

D. Configure the build artifact from the build action as the input to the CodePipeline S3 deploy action. Configure the deploy action to deploy to the S3 bucket by using the StackVariables.BucketName variable.

E. Configure the build artifact from the build action and the AWS Systems Manager parameter as the inputs to the deploy action. Configure the deploy action to deploy to the S3 bucket by using the StackVariables.BucketName variable.

**Đáp án**: ___________

---

## Câu 98

**ID**: 334 | **Loại**: Multiple Choice

A company use an organization in AWS Organizations to manage multiple AWS accounts. The company has enabled all features enabled for the organization. The company configured the organization as a hierarchy of OUs under the root OU. The company recently registered all its OUs and enrolled all its AWS accounts in AWS Control Tower.The company needs to customize the AWS Control Tower managed AWS Config configuration recorder in each of the company's AWS accounts. The company needs to apply the customizations to both the existing AWS accounts and to any new AWS accounts that the company enrolls in AWS Control Tower in the future.Which combination of steps will meet these requirements? (Choose three.)

A. Create a new AWS account. Create an AWS Lambda function in the new account to apply the customizations to the AWS Config configuration recorder in each AWS account in the organization.

B. Create a new AWS account as an AWS Config delegated administrator. Create an AWS Lambda function in the delegated administrator account to apply the customizations to the AWS Config configuration recorder in the delegated administrator account.

C. Configure an Amazon EventBridge rule in the AWS Control Tower management account to invoke an AWS Lambda function when the Organizations OU is registered or reregistered. Re-register the root Organizations OU.

D. Configure the AWSControlTowerExecution IAM role in each AWS account in the organization to be assumable by an AWS Lambda function. Configure the Lambda function to assume the AWSControlTowerExecution IAM role.

E. Create an IAM role in the AWS Control Tower management account that an AWS Lambda function can assume. Grant the IAM role permission to assume the AWSControlTowerExecution IAM role in any account in the organization. Configure the Lambda function to use the new IAM role.

F. Configure an Amazon EventBridge rule in the AWS Control Tower management account to invoke an AWS Lambda function when an AWS account is updated or enrolled in AWS Control Tower or when the landing zone is updated. Re-register each Organizations OU in the organization.

**Đáp án**: ___________

---

## Câu 99

**ID**: 337 | **Loại**: Multiple Choice

A company runs an application that stores artifacts in an Amazon S3 bucket. The application has a large user base. The application writes a high volume of objects to the S3 bucket. The company has enabled event notifications for the S3 bucket.When the application writes an object to the S3 bucket, several processing tasks need to be performed simultaneously. The company's DevOps team needs to create an AWS Step Functions workflow to orchestrate the processing tasks.Which combination of steps should the DevOps team take to meet these requirements with the LEAST operational overhead? (Choose two.)

A. Create a Standard workflow that contains a parallel state that defines the processing tasks. Create an Asynchronous Express workflow that contains a parallel state that defines the processing tasks.

B. Create a Synchronous Express workflow that contains a map state that defines the processing tasks.

C. Create an Amazon EventBridge rule to match when a new S3 object is created. Configure the EventBridge rule to invoke an AWS Lambda function. Configure the Lambda function to start the processing workflow.

D. Create an Amazon EventBridge rule to match when a new S3 object is created. Configure the EventBridge rule to start the processing workflow.

**Đáp án**: ___________

---

## Câu 100

**ID**: 338 | **Loại**: Multiple Choice

A DevOps team supports an application that runs in an Amazon Elastic Container Service (Amazon ECS) cluster behind an Application Load Balancer (ALB). Currently, the DevOps team uses AWS CodeDeploy to deploy the application by using a blue/green all-at-once strategy. Recently, the DevOps team had to roll back a deployment when a new version of the application dramatically increased response times for requests.The DevOps team needs use to a deployment strategy that will allow the team to monitor a new version of the application before the team shifts all traffic to the new version. If a new version of the application increases response times, the deployment should be rolled back as quickly as possible.Which combination of steps will meet these requirements? (Choose two.)

A. Modify the CodeDeploy deployment to use the CodeDeployDefault.ECSCanary10Percent5Minutes configuration.

B. Modify the CodeDeploy deployment to use the CodeDeployDefault.ECSLinear10PercentEvery3Minutes configuration.

C. Create an Amazon CloudWatch alarm to monitor the UnHealthyHostCount metric for the ALB. Set the alarm to activate if the metric is higher than the desired value. Associate the alarm with the CodeDeploy deployment group. Modify the deployment group to roll back when a deployment fails.

D. Create an Amazon CloudWatch alarm to monitor the TargetResponseTime metric for the ALB. Set the alarm to activate if the metric is higher than the desired value. Associate the alarm with the CodeDeploy deployment group. Modify the deployment group to roll back when alarm thresholds are met.

E. Create an Amazon CloudWatch alarm to monitor the TargetConnectionErrorCount metric for the ALB. Set the alarm to activate if the metric is higher than the desired value. Associate the alarm with the CodeDeploy deployment group. Modify the deployment group to roll back when alarm thresholds are met.

**Đáp án**: ___________

---

## Câu 101

**ID**: 346 | **Loại**: Multiple Choice

A DevOps team supports an application that runs on a large number of Amazon EC2 instances in an Auto Scaling group. The DevOps team uses AWS CloudFormation to deploy the EC2 instances. The application recently experienced an issue. A single instance returned errors to a large percentage of requests. The EC2 instance responded as healthy to both Amazon EC2 and Elastic Load Balancing health checks.The DevOps team collects application logs in Amazon CloudWatch by using the embedded metric format. The DevOps team needs to receive an alert if any EC2 instance is responsible for more than half of all errors.Which combination of steps will meet these requirements with the LEAST operational overhead? (Choose two.)

A. Create a CloudWatch Contributor Insights rule that groups logs from the CloudWatch application logs based on instance ID and errors.

B. Create a resource group in AWS Resource Groups. Use the CloudFormation stack to group the resources for the application. Add the application to CloudWatch Application Insights. Use the resource group to identify the application.

C. Create a metric filter for the application logs to count the occurrence of the term "Error.'' Create a CloudWatch alarm that uses the METRIC_COUNT function to determine whether errors have occurred. Configure the CloudWatch alarm to send a notification to an Amazon Simple Notification Service (Amazon SNS) topic to notify the DevOps team.

D. Create a CloudWatch alarm that uses the INSIGHT_RULE_METRIC function to determine whether a specific instance is responsible for more than half of all errors reported by EC2 instances. Configure the CloudWatch alarm to send a notification to an Amazon Simple Notification Service (Amazon SNS) topic to notify the DevOps team.

E. Create a CloudWatch subscription filter for the application logs that filters for errors and invokes an AWS Lambda function. Configure the Lambda function to send the instance ID and error and in a notification to an Amazon Simple Notification Service (Amazon SNS) topic to notify the DevOps team.

**Đáp án**: ___________

---

## Câu 102

**ID**: 351 | **Loại**: Multiple Choice

A company uses an organization in AWS Organizations to manage multiple AWS accounts in a hierarchical structure. An SCP that is associated with the organization root allows IAM users to be created.A DevOps team must be able to create IAM users with any level of permissions. Developers must also be able to create IAM users. However, developers must not be able to grant new IAM users excessive permissions. The developers have the CreateAndManageUsers role in each account. The DevOps team must be able to prevent other users from creating IAM users.Which combination of steps will meet these requirements? (Choose two.)

A. Create an SCP in the organization to deny users the ability to create and modify IAM users. Attach the SCP to the root of the organization. Attach the CreateAndManageUsers role to developers.

B. Create an SCP in the organization to grant users that have the DeveloperBoundary policy attached the ability to create new IAM users and to modify IAM users. Configure the SCP to require users to attach the PermissionBoundaries policy to any new IAM user. Attach the SCP to the root of the organization.

C. Create an IAM permissions policy named PermissionBoundaries within each account. Configure the PermissionBoundaries policy to specify the maximum permissions that a developer can grant to a new IAM user.

D. Create an IAM permissions policy named PermissionBoundaries within each account. Configure PermissionsBoundaries to allow users who have the PermissionBoundaries policy to create new IAM users.

E. Create an IAM permissions policy named DeveloperBoundary within each account. Configure the DeveloperBoundary policy to allow developers to create IAM users and to assign policies to IAM users of only if the developer includes the PermissionBoundaries policy as the permissions boundary. Attach the DeveloperBoundary policy to the CreateAndManageUsers role within each account.

**Đáp án**: ___________

---

## Câu 103

**ID**: 358 | **Loại**: Multiple Choice

A DevOps engineer is implementing governance controls for a company that requires its infrastructure to be housed within the United States. The company has many AWS accounts in an organization in AWS Organizations that has all features enabled.The engineer must restrict which AWS Regions the company can use. The engineer must also ensure that an alert is sent as soon as possible if any activity outside the governance policy occurs. The controls must be automatically enabled on any new Region outside the United States.Which combination of steps will meet these requirements? (Choose two.)

A. Create an Organizations SCP deny policy that has a condition that the aws:RequestedRegion property does not match a list of all US Regions. Include an exception in the policy for global services. Attach the policy to the root of the organization.

B. Configure AWS CloudTrail to send logs to Amazon CloudWatch Logs. Enable CloudTrail for all Regions. Use a CloudWatch Logs metric filter to create a metric in non-US Regions. Configure a CloudWatch alarm to send an alert if the metric is greater than 0.

C. Use an AWS Lambda function that checks for AWS service activity. Deploy the Lambda function to all Regions. Write an Amazon EventBridge rule that runs the Lambda function every hour. Configure the rule to send an alert if the Lambda function finds any activity in a non-US Region.

D. Use an AWS Lambda function to query Amazon Inspector to look for service activity in non-US Regions. Configure the Lambda function to send alerts if Amazon Inspector finds any activity.

E. Create an Organizations SCP allow policy that has a condition that the aws:RequestedRegion property matches a list of all US Regions. Include an exception in the policy for global services. Attach the policy to the root of the organization.

**Đáp án**: ___________

---


# Đáp Án

**Câu 1** (ID 6): A, D, F

**Câu 2** (ID 7): A, D

**Câu 3** (ID 8): A, C

**Câu 4** (ID 11): B, C, F

**Câu 5** (ID 12): A, D

**Câu 6** (ID 23): C, E

**Câu 7** (ID 29): B, D, E

**Câu 8** (ID 32): B, D, F

**Câu 9** (ID 36): A, D, E

**Câu 10** (ID 37): B, C, E

**Câu 11** (ID 40): B, D

**Câu 12** (ID 43): A, C

**Câu 13** (ID 47): A, B, F

**Câu 14** (ID 53): A, B, E

**Câu 15** (ID 56): A, E

**Câu 16** (ID 58): A, D

**Câu 17** (ID 65): C, D, F

**Câu 18** (ID 67): A, E

**Câu 19** (ID 71): A, C, E

**Câu 20** (ID 81): B, D

**Câu 21** (ID 82): B, C, F

**Câu 22** (ID 83): A, D

**Câu 23** (ID 87): B, D

**Câu 24** (ID 89): B, D

**Câu 25** (ID 93): B, D

**Câu 26** (ID 101): A, C, E

**Câu 27** (ID 110): A, D

**Câu 28** (ID 117): B, C, E

**Câu 29** (ID 118): C, E, F

**Câu 30** (ID 121): B, E

**Câu 31** (ID 122): A, D, E

**Câu 32** (ID 127): C, D

**Câu 33** (ID 128): B, D, E

**Câu 34** (ID 129): B, C, E

**Câu 35** (ID 138): B, D

**Câu 36** (ID 139): C, D

**Câu 37** (ID 157): A, E

**Câu 38** (ID 160): B, E

**Câu 39** (ID 163): B, C, F

**Câu 40** (ID 165): A, B, E

**Câu 41** (ID 166): B, C

**Câu 42** (ID 169): A, D

**Câu 43** (ID 170): B, C

**Câu 44** (ID 172): A, E

**Câu 45** (ID 179): B, C, E

**Câu 46** (ID 180): C, E

**Câu 47** (ID 184): A, B

**Câu 48** (ID 190): A, D, E

**Câu 49** (ID 194): B

**Câu 50** (ID 195): A, D, F

**Câu 51** (ID 196): B, E

**Câu 52** (ID 197): B, D, E

**Câu 53** (ID 199): B, D

**Câu 54** (ID 201): B, C, F

**Câu 55** (ID 208): B, C, D

**Câu 56** (ID 210): A, D

**Câu 57** (ID 211): A, C, E

**Câu 58** (ID 217): A, B, F

**Câu 59** (ID 219): A, D, F

**Câu 60** (ID 220): A, E

**Câu 61** (ID 225): A, B

**Câu 62** (ID 230): C, E, F

**Câu 63** (ID 231): B, E

**Câu 64** (ID 232): B, D

**Câu 65** (ID 233): A, E

**Câu 66** (ID 237): B, C, E

**Câu 67** (ID 238): A, E

**Câu 68** (ID 241): A, D

**Câu 69** (ID 243): A, C, E

**Câu 70** (ID 244): B, C, E

**Câu 71** (ID 245): B, D

**Câu 72** (ID 252): B, D

**Câu 73** (ID 255): B, D

**Câu 74** (ID 256): C, E

**Câu 75** (ID 259): A, D, F

**Câu 76** (ID 262): B, C, D

**Câu 77** (ID 264): C, D

**Câu 78** (ID 267): B, D

**Câu 79** (ID 268): A, C, E

**Câu 80** (ID 270): A, D, F

**Câu 81** (ID 271): A, D

**Câu 82** (ID 272): A, B, C

**Câu 83** (ID 273): A, D

**Câu 84** (ID 276): A, D, E

**Câu 85** (ID 277): B, D, E

**Câu 86** (ID 282): A, D

**Câu 87** (ID 296): B, D, F

**Câu 88** (ID 298): A, C, F

**Câu 89** (ID 303): C, D

**Câu 90** (ID 306): A, C, F

**Câu 91** (ID 310): C, E

**Câu 92** (ID 313): A, B, E

**Câu 93** (ID 318): C, D, E

**Câu 94** (ID 322): C, E, F

**Câu 95** (ID 323): A, B

**Câu 96** (ID 325): C, D

**Câu 97** (ID 327): B, D

**Câu 98** (ID 334): A, E, F

**Câu 99** (ID 337): A, D

**Câu 100** (ID 338): A, D

**Câu 101** (ID 346): A, D

**Câu 102** (ID 351): C, E

**Câu 103** (ID 358): A, B

