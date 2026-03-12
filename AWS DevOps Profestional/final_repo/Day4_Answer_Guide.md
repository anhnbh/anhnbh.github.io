# 📚 AWS DevOps Professional Day 4 - Answer Guide

**Ngày tạo**: 31/10/2025  
**Mục đích**: Hướng dẫn đáp án đúng với giải thích chi tiết và tài liệu tham khảo

---

## Câu 55

**Loại**: Single Choice

**Câu hỏi**: A company has deployed an application in a production VPC in a single AWS account. The application is popular and is experiencing heavy usage. The company's security team wants to add additional security, such as AWS WAF, to the application deployment. However, the application's product manager is concerned about cost and does not want to approve the change unless the security team can prove that additional security is necessary. The security team believes that some of the application's demand might come from users that have IP addresses that are on a deny list. The security team provides the deny list to a DevOps engineer. If any of the IP addresses on the deny list access the application, the security team wants to receive automated notification in near real time so that the security team can document that the application needs additional security. The DevOps engineer creates a VPC flow log for the production VPC. Which set of additional steps should the DevOps engineer take to meet these requirements MOST cost-effectively?

**Các lựa chọn**:

A. Create a log group in Amazon CloudWatch Logs. Configure the VPC flow log to capture accepted traffic and to send the data to the log group. Create an Amazon CloudWatch metric filter for IP addresses on the deny list. Create a CloudWatch alarm with the metric filter as input. Set the period to 5 minutes and the datapoints to alarm to 1. Use an Amazon Simple Notification Service (Amazon SNS) topic to send alarm notices to the security team. ✅

B. Create an Amazon S3 bucket for log files. Configure the VPC flow log to capture all traffic and to send the data to the S3 bucket. Configure Amazon Athena to return all log files in the S3 bucket for IP addresses on the deny list. Configure Amazon QuickSight to accept data from Athena and to publish the data as a dashboard that the security team can access. Create a threshold alert of 1 for successful access. Configure the alert to automatically notify the security team as frequently as possible when the alert threshold is met. ❌

C. Create an Amazon S3 bucket for log files. Configure the VPC flow log to capture accepted traffic and to send the data to the S3 bucket. Configure an Amazon OpenSearch Service cluster and domain for the log files. Create an AWS Lambda function to retrieve the logs from the S3 bucket, format the logs, and load the logs into the OpenSearch Service cluster. Schedule the Lambda function to run every 5 minutes. Configure an alert and condition in OpenSearch Service to send alerts to the security team through an Amazon Simple Notification Service (Amazon SNS) topic when access from the IP addresses on the deny list is detected. ❌

D. Create a log group in Amazon CloudWatch Logs. Create an Amazon S3 bucket to hold query results. Configure the VPC flow log to capture all traffic and to send the data to the log group. Deploy an Amazon Athena CloudWatch connector in AWS Lambda. Connect the connector to the log group. Configure Athena to periodically query for all accepted traffic from the IP addresses on the deny list and to store the results in the S3 bucket. Configure an S3 event notification to automatically notify the security team through an Amazon Simple Notification Service (Amazon SNS) topic when new objects are added to the S3 bucket. ❌

**Đáp án đúng**: A

**Giải thích**: 
- CloudWatch Logs với metric filter là giải pháp cost-effective nhất cho real-time monitoring
- Chỉ cần capture accepted traffic (không cần all traffic) để tiết kiệm chi phí
- CloudWatch alarm với SNS cung cấp near real-time notification
- Các option khác phức tạp hơn và tốn kém hơn (OpenSearch, QuickSight, Athena)

**Tài liệu tham khảo**:
- [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [CloudWatch Metric Filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html)
- [CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

---

## Câu 56

**Loại**: Multiple Choice

**Câu hỏi**: A DevOps engineer has automated a web service deployment by using AWS CodePipeline with the following steps: 1. An AWS CodeBuild project compiles the deployment artifact and runs unit tests. 2. An AWS CodeDeploy deployment group deploys the web service to Amazon EC2 instances in the staging environment. 3. A CodeDeploy deployment group deploys the web service to EC2 instances in the production environment. The quality assurance (QA) team requests permission to inspect the build artifact before the deployment to the production environment occurs. The QA team wants to run an internal penetration testing tool to conduct manual tests. The tool will be invoked by a REST API call. Which combination of actions should the DevOps engineer take to fulfill this request? (Choose two.)

**Các lựa chọn**:

A. Insert a manual approval action between the test actions and deployment actions of the pipeline. ✅

B. Modify the buildspec.yml file for the compilation stage to require manual approval before completion. ❌

C. Update the CodeDeploy deployment groups so that they require manual approval to proceed. ❌

D. Update the pipeline to directly call the REST API for the penetration testing tool. ❌

E. Update the pipeline to invoke an AWS Lambda function that calls the REST API for the penetration testing tool. ✅

**Đáp án đúng**: A, E

**Giải thích**:
- Manual approval action trong CodePipeline cho phép QA team inspect artifact trước khi deploy production
- Lambda function có thể call REST API của penetration testing tool một cách automated
- Buildspec.yml không phù hợp cho manual approval (chỉ cho build process)
- CodeDeploy deployment groups không có built-in manual approval feature

**Tài liệu tham khảo**:
- [CodePipeline Manual Approval Actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals.html)
- [CodePipeline Lambda Actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html)

---

## Câu 57

**Loại**: Single Choice

**Câu hỏi**: A company is hosting a web application in an AWS Region. For disaster recovery purposes, a second region is being used as a standby. Disaster recovery requirements state that session data must be replicated between regions in near-real time and 1% of requests should route to the secondary region to continuously verify system functionality. Additionally, if there is a disruption in service in the main region, traffic should be automatically routed to the secondary region, and the secondary region must be able to scale up to handle all traffic. How should a DevOps engineer meet these requirements?

**Các lựa chọn**:

A. In both regions, deploy the application on AWS Elastic Beanstalk and use Amazon DynamoDB global tables for session data. Use an Amazon Route 53 weighted routing policy with health checks to distribute the traffic across the regions. ✅

B. In both regions, launch the application in Auto Scaling groups and use DynamoDB for session data. Use a Route 53 failover routing policy with health checks to distribute the traffic across the regions. ❌

C. In both regions, deploy the application in AWS Lambda, exposed by Amazon API Gateway, and use Amazon RDS for PostgreSQL with cross-region replication for session data. Deploy the web application with client-side logic to call the API Gateway directly. ❌

D. In both regions, launch the application in Auto Scaling groups and use DynamoDB global tables for session data. Enable an Amazon CloudFront weighted distribution across regions. Point the Amazon Route 53 DNS record at the CloudFront distribution. ❌

**Đáp án đúng**: A

**Giải thích**:
- DynamoDB Global Tables cung cấp near-real time replication cho session data
- Route 53 weighted routing policy cho phép route 1% traffic đến secondary region
- Elastic Beanstalk có built-in auto scaling capabilities
- Failover policy không phù hợp vì cần 1% traffic liên tục đến secondary region

**Tài liệu tham khảo**:
- [DynamoDB Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)
- [Route 53 Weighted Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted)
- [Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)

---

## Câu 58

**Loại**: Multiple Choice

**Câu hỏi**: A company runs an application on Amazon EC2 instances. The company uses a series of AWS CloudFormation stacks to define the application resources. A developer performs updates by building and testing the application on a laptop and then uploading the build output and CloudFormation stack templates to Amazon S3. The developer's peers review the changes before the developer performs the CloudFormation stack update and installs a new version of the application onto the EC2 instances. The deployment process is prone to errors and is time-consuming when the developer updates each EC2 instance with the new application. The company wants to automate as much of the application deployment process as possible while retaining a final manual approval step before the modification of the application or resources. The company already has moved the source code for the application and the CloudFormation templates to AWS CodeCommit. The company also has created an AWS CodeBuild project to build and test the application. Which combination of steps will meet the company's requirements? (Choose two.)

**Các lựa chọn**:

A. Create an application group and a deployment group in AWS CodeDeploy. Install the CodeDeploy agent on the EC2 instances. ✅

B. Create an application revision and a deployment group in AWS CodeDeploy. Create an environment in CodeDeploy. Register the EC2 instances to the CodeDeploy environment. ❌

C. Use AWS CodePipeline to invoke the CodeBuild job, run the CloudFormation update, and pause for a manual approval step. After approval, start the AWS CodeDeploy deployment. ❌

D. Use AWS CodePipeline to invoke the CodeBuild job, create CloudFormation change sets for each of the application stacks, and pause for a manual approval step. After approval, run the CloudFormation change sets and start the AWS CodeDeploy deployment. ✅

E. Use AWS CodePipeline to invoke the CodeBuild job, create CloudFormation change sets for each of the application stacks, and pause for a manual approval step. After approval, start the AWS CodeDeploy deployment. ❌

**Đáp án đúng**: A, D

**Giải thích**:
- CodeDeploy cần application và deployment group để deploy lên EC2 instances
- CloudFormation change sets cho phép review changes trước khi apply
- Change sets cung cấp preview của modifications trước manual approval
- CodeDeploy agent cần được install trên EC2 instances để receive deployments

**Tài liệu tham khảo**:
- [CodeDeploy Applications and Deployment Groups](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications.html)
- [CloudFormation Change Sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html)
- [CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)

---

## Câu 59

**Loại**: Single Choice

**Câu hỏi**: A DevOps engineer manages a web application that runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The instances run in an EC2 Auto Scaling group across multiple Availability Zones. The engineer needs to implement a deployment strategy that: Launches a second fleet of instances with the same capacity as the original fleet. Maintains the original fleet unchanged while the second fleet is launched. Transitions traffic to the second fleet when the second fleet is fully deployed. Terminates the original fleet automatically 1 hour after transition. Which solution will satisfy these requirements?

**Các lựa chọn**:

A. Use an AWS CloudFormation template with a retention policy for the ALB set to 1 hour. Update the Amazon Route 53 record to reflect the new ALB. ❌

B. Use two AWS Elastic Beanstalk environments to perform a blue/green deployment from the original environment to the new one. Create an application version lifecycle policy to terminate the original environment in 1 hour. ❌

C. Use AWS CodeDeploy with a deployment group configured with a blue/green deployment configuration Select the option Terminate the original instances in the deployment group with a waiting period of 1 hour. ✅

D. Use AWS Elastic Beanstalk with the configuration set to Immutable. Create an .ebextension using the Resources key that sets the deletion policy of the ALB to 1 hour, and deploy the application. ❌

**Đáp án đúng**: C

**Giải thích**:
- CodeDeploy blue/green deployment tự động tạo second fleet với same capacity
- Maintains original fleet unchanged trong quá trình deployment
- Automatic traffic transition khi new fleet ready
- Built-in option để terminate original instances sau 1 hour
- Elastic Beanstalk không có precise control về termination timing

**Tài liệu tham khảo**:
- [CodeDeploy Blue/Green Deployments](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html#welcome-deployment-overview-blue-green)
- [CodeDeploy EC2/On-Premises Blue/Green](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html)

---

## Câu 60

**Loại**: Single Choice

**Câu hỏi**: A video-sharing company stores its videos in Amazon S3. The company has observed a sudden increase in video access requests, but the company does not know which videos are most popular. The company needs to identify the general access pattern for the video files. This pattern includes the number of users who access a certain file on a given day, as well as the number of pull requests for certain files. How can the company meet these requirements with the LEAST amount of effort?

**Các lựa chọn**:

A. Activate S3 server access logging. Import the access logs into an Amazon Aurora database. Use an Aurora SQL query to analyze the access patterns. ❌

B. Activate S3 server access logging. Use Amazon Athena to create an external table with the log files. Use Athena to create a SQL query to analyze the access patterns. ✅

C. Invoke an AWS Lambda function for every S3 object access event. Configure the Lambda function to write the file access information, such as user. S3 bucket, and file key, to an Amazon Aurora database. Use an Aurora SQL query to analyze the access patterns. ❌

D. Record an Amazon CloudWatch Logs log message for every S3 object access event. Configure a CloudWatch Logs log stream to write the file access information, such as user, S3 bucket, and file key, to an Amazon Kinesis Data Analytics for SQL application. Perform a sliding window analysis. ❌

**Đáp án đúng**: B

**Giải thích**:
- S3 server access logging tự động capture access patterns với minimal effort
- Athena cho phép query S3 logs directly mà không cần import vào database
- Cost-effective và serverless solution
- Lambda function cho mỗi access event sẽ rất expensive và complex
- Aurora import requires additional ETL process

**Tài liệu tham khảo**:
- [S3 Server Access Logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html)
- [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
- [Querying S3 Access Logs with Athena](https://docs.aws.amazon.com/athena/latest/ug/s3-access-logs.html)

---

## Câu 61

**Loại**: Single Choice

**Câu hỏi**: A development team wants to use AWS CloudFormation stacks to deploy an application. However, the developer IAM role does not have the required permissions to provision the resources that are specified in the AWS CloudFormation template. A DevOps engineer needs to implement a solution that allows the developers to deploy the stacks. The solution must follow the principle of least privilege. Which solution will meet these requirements?

**Các lựa chọn**:

A. Create an IAM policy that allows the developers to provision the required resources. Attach the policy to the developer IAM role. ❌

B. Create an IAM policy that allows full access to AWS CloudFormation. Attach the policy to the developer IAM role. ❌

C. Create an AWS CloudFormation service role that has the required permissions. Grant the developer IAM role a cloudformation:* action. Use the new service role during stack deployments. ❌

D. Create an AWS CloudFormation service role that has the required permissions. Grant the developer IAM role the iam:PassRole permission. Use the new service role during stack deployments. ✅

**Đáp án đúng**: D

**Giải thích**: 
CloudFormation service role cho phép developers deploy stacks mà không cần direct permissions trên resources. Developers chỉ cần iam:PassRole permission để sử dụng service role, tuân thủ principle of least privilege.

**Tài liệu tham khảo**:
- [CloudFormation Service Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-servicerole.html)

---

## Câu 62

**Loại**: Single Choice

**Câu hỏi**: A production account has a requirement that any Amazon EC2 instance that has been logged in to manually must be terminated within 24 hours. All applications in the production account are using Auto Scaling groups with the Amazon CloudWatch Logs agent configured. How can this process be automated?

**Các lựa chọn**:

A. Create a CloudWatch Logs subscription to an AWS Step Functions application. Configure an AWS Lambda function to add a tag to the EC2 instance that produced the login event and mark the instance to be decommissioned. Create an Amazon EventBridge rule to invoke a second Lambda function once a day that will terminate all instances with this tag. ❌

B. Create an Amazon CloudWatch alarm that will be invoked by the login event. Send the notification to an Amazon Simple Notification Service (Amazon SNS) topic that the operations team is subscribed to, and have them terminate the EC2 instance within 24 hours. ❌

C. Create an Amazon CloudWatch alarm that will be invoked by the login event. Configure the alarm to send to an Amazon Simple Queue Service (Amazon SQS) queue. Use a group of worker instances to process messages from the queue, which then schedules an Amazon EventBridge rule to be invoked. ❌

D. Create a CloudWatch Logs subscription to an AWS Lambda function. Configure the function to add a tag to the EC2 instance that produced the login event and mark the instance to be decommissioned. Create an Amazon EventBridge rule to invoke a daily Lambda function that terminates all instances with this tag. ✅

**Đáp án đúng**: D

**Giải thích**: 
CloudWatch Logs subscription filter tự động trigger Lambda khi có login events. Lambda tag instances và EventBridge rule chạy daily để terminate tagged instances. Fully automated solution.

**Tài liệu tham khảo**:
- [CloudWatch Logs Subscription Filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html)

---

## Câu 63

**Loại**: Single Choice

**Câu hỏi**: A company has enabled all features for its organization in AWS Organizations. The organization contains 10 AWS accounts. The company has turned on AWS CloudTrail in all the accounts. The company expects the number of AWS accounts in the organization to increase to 500 during the next year. The company plans to use multiple OUs for these accounts. The company has enabled AWS Config in each existing AWS account in the organization. A DevOps engineer must implement a solution that enables AWS Config automatically for all future AWS accounts that are created in the organization. Which solution will meet this requirement?

**Các lựa chọn**:

A. In the organization's management account, create an Amazon EventBridge rule that reacts to a CreateAccount API call. Configure the rule to invoke an AWS Lambda function that enables trusted access to AWS Config for the organization. ❌

B. In the organization's management account, create an AWS CloudFormation stack set to enable AWS Config. Configure the stack set to deploy automatically when an account is created through Organizations. ✅

C. In the organization's management account, create an SCP that allows the appropriate AWS Config API calls to enable AWS Config. Apply the SCP to the root-level OU. ❌

D. In the organization's management account, create an Amazon EventBridge rule that reacts to a CreateAccount API call. Configure the rule to invoke an AWS Systems Manager Automation runbook to enable AWS Config for the account. ❌

**Đáp án đúng**: B

**Giải thích**: 
CloudFormation StackSets có automatic deployment feature cho new accounts trong Organizations. Đây là native solution không cần custom automation.

**Tài liệu tham khảo**:
- [CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)

---

## Câu 64

**Loại**: Single Choice

**Câu hỏi**: A company has many applications. Different teams in the company developed the applications by using multiple languages and frameworks. The applications run on premises and on different servers with different operating systems. Each team has its own release protocol and process. The company wants to reduce the complexity of the release and maintenance of these applications. The company is migrating its technology stacks, including these applications, to AWS. The company wants centralized control of source code, a consistent and automatic delivery pipeline, and as few maintenance tasks as possible on the underlying infrastructure. What should a DevOps engineer do to meet these requirements?

**Các lựa chọn**:

A. Create one AWS CodeCommit repository for all applications. Put each application's code in a different branch. Merge the branches, and use AWS CodeBuild to build the applications. Use AWS CodeDeploy to deploy the applications to one centralized application server. ❌

B. Create one AWS CodeCommit repository for each of the applications. Use AWS CodeBuild to build the applications one at a time. Use AWS CodeDeploy to deploy the applications to one centralized application server. ❌

C. Create one AWS CodeCommit repository for each of the applications. Use AWS CodeBuild to build one AMI for each server. Use AWS CloudFormation StackSets to automatically provision and decommission Amazon EC2 fleets by using these AMIs. ❌

D. Create one AWS CodeCommit repository for each of the applications. Use AWS CodeBuild to build one Docker image for each application in Amazon Elastic Container Registry (Amazon ECR). Use AWS CodeDeploy to deploy the applications to Amazon Elastic Container Service (Amazon ECS) on infrastructure that AWS Fargate manages. ✅

**Đáp án đúng**: D

**Giải thích**: 
Containerization với Docker giải quyết multiple languages/frameworks. ECS Fargate eliminates infrastructure maintenance. Separate repos cho mỗi app maintains team autonomy.

**Tài liệu tham khảo**:
- [Amazon ECS](https://docs.aws.amazon.com/ecs/)
- [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)

---

## Câu 65

**Loại**: Multiple Choice

**Câu hỏi**: A company's application is currently deployed to a single AWS Region. Recently, the company opened a new office on a different continent. The users in the new office are experiencing high latency. The company's application runs on Amazon EC2 instances behind an Application Load Balancer (ALB) and uses Amazon DynamoDB as the database layer. The instances run in an EC2 Auto Scaling group across multiple Availability Zones. A DevOps engineer is tasked with minimizing application response times and improving availability for users in both Regions. Which combination of actions should be taken to address the latency issues? (Choose three.)

**Các lựa chọn**:

A. Create a new DynamoDB table in the new Region with cross-Region replication enabled. ❌

B. Create new ALB and Auto Scaling group global resources and configure the new ALB to direct traffic to the new Auto Scaling group. ❌

C. Create new ALB and Auto Scaling group resources in the new Region and configure the new ALB to direct traffic to the new Auto Scaling group. ✅

D. Create Amazon Route 53 records, health checks, and latency-based routing policies to route to the ALB. ✅

E. Create Amazon Route 53 aliases, health checks, and failover routing policies to route to the ALB. ❌

F. Convert the DynamoDB table to a global table. ✅

**Đáp án đúng**: C, D, F

**Giải thích**: 
- ALB và ASG phải tạo trong new region (không phải global resources)
- Route 53 latency-based routing tự động route users đến closest region
- DynamoDB Global Tables provide multi-region replication

**Tài liệu tham khảo**:
- [DynamoDB Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)
- [Route 53 Latency Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency)

---

## Câu 66

**Loại**: Single Choice

**Câu hỏi**: A DevOps engineer needs to apply a core set of security controls to an existing set of AWS accounts. The accounts are in an organization in AWS Organizations. Individual teams will administer individual accounts by using the AdministratorAccess AWS managed policy. For all accounts. AWS CloudTrail and AWS Config must be turned on in all available AWS Regions. Individual account administrators must not be able to edit or delete any of the baseline resources. However, individual account administrators must be able to edit or delete their own CloudTrail trails and AWS Config rules. Which solution will meet these requirements in the MOST operationally efficient way?

**Các lựa chọn**:

A. Create an AWS CloudFormation template that defines the standard account resources. Deploy the template to all accounts from the organization's management account by using CloudFormation StackSets. Set the stack policy to deny Update:Delete actions. ❌

B. Enable AWS Control Tower. Enroll the existing accounts in AWS Control Tower. Grant the individual account administrators access to CloudTrail and AWS Config. ❌

C. Designate an AWS Config management account. Create AWS Config recorders in all accounts by using AWS CloudFormation StackSets. Deploy AWS Config rules to the organization by using the AWS Config management account. Create a CloudTrail organization trail in the organization's management account. Deny modification or deletion of the AWS Config recorders by using an SCP. ✅

D. Create an AWS CloudFormation template that defines the standard account resources. Deploy the template to all accounts from the organization's management account by using Cloud Formation StackSets Create an SCP that prevents updates or deletions to CloudTrail resources or AWS Config resources unless the principal is an administrator of the organization's management account. ❌

**Đáp án đúng**: C

**Giải thích**: 
AWS Config management account với organization trail cung cấp centralized control. SCP prevents deletion của baseline resources nhưng allows individual trails/rules.

**Tài liệu tham khảo**:
- [AWS Config Multi-Account Setup](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html)
- [CloudTrail Organization Trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html)

---

## Câu 67

**Loại**: Multiple Choice

**Câu hỏi**: A company has its AWS accounts in an organization in AWS Organizations. AWS Config is manually configured in each AWS account. The company needs to implement a solution to centrally configure AWS Config for all accounts in the organization The solution also must record resource changes to a central account. Which combination of actions should a DevOps engineer perform to meet these requirements? (Choose two.)

**Các lựa chọn**:

A. Configure a delegated administrator account for AWS Config. Enable trusted access for AWS Config in the organization. ✅

B. Configure a delegated administrator account for AWS Config. Create a service-linked role for AWS Config in the organization's management account. ❌

C. Create an AWS CloudFormation template to create an AWS Config aggregator. Configure a CloudFormation stack set to deploy the template to all accounts in the organization. ❌

D. Create an AWS Config organization aggregator in the organization's management account. Configure data collection from all AWS accounts in the organization and from all AWS Regions. ❌

E. Create an AWS Config organization aggregator in the delegated administrator account. Configure data collection from all AWS accounts in the organization and from all AWS Regions. ✅

**Đáp án đúng**: A, E

**Giải thích**: 
Delegated administrator account với trusted access enables centralized Config management. Organization aggregator trong delegated account collects data từ all accounts.

**Tài liệu tham khảo**:
- [AWS Config Delegated Administrator](https://docs.aws.amazon.com/config/latest/developerguide/set-up-aggregator-cli.html)

---

## Câu 68

**Loại**: Single Choice

**Câu hỏi**: A company wants to migrate its content sharing web application hosted on Amazon EC2 to a serverless architecture. The company currently deploys changes to its application by creating a new Auto Scaling group of EC2 instances and a new Elastic Load Balancer, and then shifting the traffic away using an Amazon Route 53 weighted routing policy. For its new serverless application, the company is planning to use Amazon API Gateway and AWS Lambda. The company will need to update its deployment processes to work with the new application. It will also need to retain the ability to test new features on a small number of users before rolling the features out to the entire user base. Which deployment strategy will meet these requirements?

**Các lựa chọn**:

A. Use AWS CDK to deploy API Gateway and Lambda functions. When code needs to be changed, update the AWS CloudFormation stack and deploy the new version of the APIs and Lambda functions. Use a Route 53 failover routing policy for the canary release strategy. ❌

B. Use AWS CloudFormation to deploy API Gateway and Lambda functions using Lambda function versions. When code needs to be changed, update the CloudFormation stack with the new Lambda code and update the API versions using a canary release strategy. Promote the new version when testing is complete. ✅

C. Use AWS Elastic Beanstalk to deploy API Gateway and Lambda functions. When code needs to be changed, deploy a new version of the API and Lambda functions. Shift traffic gradually using an Elastic Beanstalk blue/green deployment. ❌

D. Use AWS OpsWorks to deploy API Gateway in the service layer and Lambda functions in a custom layer. When code needs to be changed, use OpsWorks to perform a blue/green deployment and shift traffic gradually. ❌

**Đáp án đúng**: B

**Giải thích**: 
Lambda versions với API Gateway stages support native canary deployments. CloudFormation provides infrastructure as code approach tương tự current process.

**Tài liệu tham khảo**:
- [Lambda Versions and Aliases](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html)
- [API Gateway Canary Deployments](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.html)

---

## Câu 69

**Loại**: Single Choice

**Câu hỏi**: A development team uses AWS CodeCommit, AWS CodePipeline, and AWS CodeBuild to develop and deploy an application. Changes to the code are submitted by pull requests. The development team reviews and merges the pull requests, and then the pipeline builds and tests the application. Over time, the number of pull requests has increased. The pipeline is frequently blocked because of failing tests. To prevent this blockage, the development team wants to run the unit and integration tests on each pull request before it is merged. Which solution will meet these requirements?

**Các lựa chọn**:

A. Create a CodeBuild project to run the unit and integration tests. Create a CodeCommit approval rule template. Configure the template to require the successful invocation of the CodeBuild project. Attach the approval rule to the project's CodeCommit repository. ❌

B. Create an Amazon EventBridge rule to match pullRequestCreated events from CodeCommit Create a CodeBuild project to run the unit and integration tests. Configure the CodeBuild project as a target of the EventBridge rule that includes a custom event payload with the CodeCommit repository and branch information from the event. ✅

C. Create an Amazon EventBridge rule to match pullRequestCreated events from CodeCommit. Modify the existing CodePipeline pipeline to not run the deploy steps if the build is started from a pull request. Configure the EventBridge rule to run the pipeline with a custom payload that contains the CodeCommit repository and branch information from the event. ❌

D. Create a CodeBuild project to run the unit and integration tests. Create a CodeCommit notification rule that matches when a pull request is created or updated. Configure the notification rule to invoke the CodeBuild project. ❌

**Đáp án đúng**: B

**Giải thích**: 
EventBridge rule với pullRequestCreated events tự động trigger CodeBuild để run tests trên PR branch. Custom payload provides repository và branch context.

**Tài liệu tham khảo**:
- [CodeCommit Events](https://docs.aws.amazon.com/codecommit/latest/userguide/monitoring-events.html)
- [EventBridge Rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html)

---

## Câu 70

**Loại**: Single Choice

**Câu hỏi**: A company has an application that runs on a fleet of Amazon EC2 instances. The application requires frequent restarts. The application logs contain error messages when a restart is required. The application logs are published to a log group in Amazon CloudWatch Logs. An Amazon CloudWatch alarm notifies an application engineer through an Amazon Simple Notification Service (Amazon SNS) topic when the logs contain a large number of restart-related error messages. The application engineer manually restarts the application on the instances after the application engineer receives a notification from the SNS topic. A DevOps engineer needs to implement a solution to automate the application restart on the instances without restarting the instances. Which solution will meet these requirements in the MOST operationally efficient manner?

**Các lựa chọn**:

A. Configure an AWS Systems Manager Automation runbook that runs a script to restart the application on the instances. Configure the SNS topic to invoke the runbook. ❌

B. Create an AWS Lambda function that restarts the application on the instances. Configure the Lambda function as an event destination of the SNS topic. ❌

C. Configure an AWS Systems Manager Automation runbook that runs a script to restart the application on the instances. Create an AWS Lambda function to invoke the runbook. Configure the Lambda function as an event destination of the SNS topic. ❌

D. Configure an AWS Systems Manager Automation runbook that runs a script to restart the application on the instances. Configure an Amazon EventBridge rule that reacts when the CloudWatch alarm enters ALARM state. Specify the runbook as a target of the rule. ✅

**Đáp án đúng**: D

**Giải thích**: 
EventBridge rule directly trigger Systems Manager Automation runbook khi alarm state changes. Eliminates need for SNS topic và Lambda function, most operationally efficient.

**Tài liệu tham khảo**:
- [Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [EventBridge CloudWatch Integration](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html)

---

## Câu 71

**Loại**: Multiple Choice

**Câu hỏi**: A DevOps engineer at a company is supporting an AWS environment in which all users use AWS IAM Identity Center (AWS Single Sign-On). The company wants to immediately disable credentials of any new IAM user and wants the security team to receive a notification. Which combination of steps should the DevOps engineer take to meet these requirements? (Choose three.)

**Các lựa chọn**:

A. Create an Amazon EventBridge rule that reacts to an IAM CreateUser API call in AWS CloudTrail. ✅

B. Create an Amazon EventBridge rule that reacts to an IAM GetLoginProfile API call in AWS CloudTrail. ❌

C. Create an AWS Lambda function that is a target of the EventBridge rule. Configure the Lambda function to disable any access keys and delete the login profiles that are associated with the IAM user. ✅

D. Create an AWS Lambda function that is a target of the EventBridge rule. Configure the Lambda function to delete the login profiles that are associated with the IAM user. ❌

E. Create an Amazon Simple Notification Service (Amazon SNS) topic that is a target of the EventBridge rule. Subscribe the security team's group email address to the topic. ✅

F. Create an Amazon Simple Queue Service (Amazon SQS) queue that is a target of the Lambda function. Subscribe the security team's group email address to the queue. ❌

**Đáp án đúng**: A, C, E

**Giải thích**: 
EventBridge rule monitors CreateUser events. Lambda function disables access keys và deletes login profiles. SNS topic notifies security team. Company uses SSO nên IAM users shouldn't exist.

**Tài liệu tham khảo**:
- [CloudTrail Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference.html)
- [IAM API Actions](https://docs.aws.amazon.com/IAM/latest/APIReference/)

---

## Câu 72

**Loại**: Single Choice

**Câu hỏi**: A company wants to set up a continuous delivery pipeline. The company stores application code in a private GitHub repository. The company needs to deploy the application components to Amazon Elastic Container Service (Amazon ECS). Amazon EC2, and AWS Lambda. The pipeline must support manual approval actions. Which solution will meet these requirements?

**Các lựa chọn**:

A. Use AWS CodePipeline with Amazon ECS. Amazon EC2, and Lambda as deploy providers. ❌

B. Use AWS CodePipeline with AWS CodeDeploy as the deploy provider. ✅

C. Use AWS CodePipeline with AWS Elastic Beanstalk as the deploy provider. ❌

D. Use AWS CodeDeploy with GitHub integration to deploy the application. ❌

**Đáp án đúng**: B

**Giải thích**: 
CodeDeploy supports deployment to ECS, EC2, và Lambda. CodePipeline provides manual approval actions và GitHub integration. Elastic Beanstalk không support all three targets.

**Tài liệu tham khảo**:
- [CodeDeploy Deployment Targets](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-platforms.html)
- [CodePipeline Manual Approvals](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals.html)

---

## 📚 Tài liệu học tập bổ sung

### AWS DevOps Services
- [AWS CodePipeline User Guide](https://docs.aws.amazon.com/codepipeline/latest/userguide/)
- [AWS CodeDeploy User Guide](https://docs.aws.amazon.com/codedeploy/latest/userguide/)
- [AWS CodeBuild User Guide](https://docs.aws.amazon.com/codebuild/latest/userguide/)

### Monitoring & Logging
- [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/)
- [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [AWS X-Ray Developer Guide](https://docs.aws.amazon.com/xray/latest/devguide/)

### Infrastructure as Code
- [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/)
- [CloudFormation Best Practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html)

---

**Chúc bạn học tốt! 🚀**
