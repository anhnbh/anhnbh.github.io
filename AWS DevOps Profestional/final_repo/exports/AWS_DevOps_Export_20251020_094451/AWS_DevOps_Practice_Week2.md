# AWS DevOps Practice Test - Week2

**Số câu**: 126  
**Ngày tạo**: 20/10/2025 09:44

---

## Câu 1

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

## Câu 2

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

## Câu 3

**ID**: 130 | **Loại**: Single Choice

A company has a legacy application. A DevOps engineer needs to automate the process of building the deployable artifact for the legacy application. The solution must store the deployable artifact in an existing Amazon S3 bucket for future deployments to reference.Which solution will meet these requirements in the MOST operationally efficient way?

A. Create a custom Docker image that contains all the dependencies for the legacy application. Store the custom Docker image in a new Amazon Elastic Container Registry (Amazon ECR) repository. Configure a new AWS CodeBuild project to use the custom Docker image to build the deployable artifact and to save the artifact to the S3 bucket.

B. Launch a new Amazon EC2 instance. Install all the dependencies for the legacy application on the EC2 instance. Use the EC2 instance to build the deployable artifact and to save the artifact to the S3 bucket.

C. Create a custom EC2 Image Builder image. Install all the dependencies for the legacy application on the image. Launch a new Amazon EC2 instance from the image. Use the new EC2 instance to build the deployable artifact and to save the artifact to the S3 bucket.

D. Create an Amazon Elastic Kubernetes Service (Amazon EKS) cluster with an AWS Fargate profile that runs in multiple Availability Zones. Create a custom Docker image that contains all the dependencies for the legacy application. Store the custom Docker image in a new Amazon Elastic Container Registry (Amazon ECR) repository. Use the custom Docker image inside the EKS cluster to build the deployable artifact and to save the artifact to the S3 bucket.

**Đáp án**: ___________

---

## Câu 4

**ID**: 131 | **Loại**: Single Choice

A company builds a container image in an AWS CodeBuild project by running Docker commands. After the container image is built, the CodeBuild project uploads the container image to an Amazon S3 bucket. The CodeBuild project has an IAM service role that has permissions to access the S3 bucket.A DevOps engineer needs to replace the S3 bucket with an Amazon Elastic Container Registry (Amazon ECR) repository to store the container images. The DevOps engineer creates an ECR private image repository in the same AWS Region of the CodeBuild project. The DevOps engineer adjusts the IAM service role with the permissions that are necessary to work with the new ECR repository. The DevOps engineer also places new repository information into the docker build command and the docker push command that are used in the buildspec.yml file.When the CodeBuild project runs a build job, the job fails when the job tries to access the ECR repository.Which solution will resolve the issue of failed access to the ECR repository?

A. Update the buildspec.yml file to log in to the ECR repository by using the aws ecr get-login-password AWS CLI command to obtain an authentication token. Update the docker login command to use the authentication token to access the ECR repository.

B. Add an environment variable of type SECRETS_MANAGER to the CodeBuild project. In the environment variable, include the ARN of the CodeBuild project's IAM service role. Update the buildspec.yml file to use the new environment variable to log in with the docker login command to access the ECR repository.

C. Update the ECR repository to be a public image repository. Add an ECR repository policy that allows the IAM service role to have access.

D. Update the buildspec.yml file to use the AWS CLI to assume the IAM service role for ECR operations. Add an ECR repository policy that allows the IAM service role to have access.

**Đáp án**: ___________

---

## Câu 5

**ID**: 132 | **Loại**: Single Choice

A company manually provisions IAM access for its employees. The company wants to replace the manual process with an automated process. The company has an existing Active Directory system configured with an external SAML 2.0 identity provider (IdP).The company wants employees to use their existing corporate credentials to access AWS. The groups from the existing Active Directory system must be available for permission management in AWS Identity and Access Management (IAM). A DevOps engineer has completed the initial configuration of AWS IAM Identity Center (AWS Single Sign-On) in the company’s AWS account.What should the DevOps engineer do next to meet the requirements?

A. Configure an external IdP as an identity source. Configure automatic provisioning of users and groups by using the SCIM protocol.

B. Configure AWS Directory Service as an identity source. Configure automatic provisioning of users and groups by using the SAML protocol.

C. Configure an AD Connector as an identity source. Configure automatic provisioning of users and groups by using the SCIM protocol.

D. Configure an external IdP as an identity source Configure automatic provisioning of users and groups by using the SAML protocol.

**Đáp án**: ___________

---

## Câu 6

**ID**: 133 | **Loại**: Single Choice

A company is using AWS to run digital workloads. Each application team in the company has its own AWS account for application hosting. The accounts are consolidated in an organization in AWS Organizations.The company wants to enforce security standards across the entire organization. To avoid noncompliance because of security misconfiguration, the company has enforced the use of AWS CloudFormation. A production support team can modify resources in the production environment by using the AWS Management Console to troubleshoot and resolve application-related issues.A DevOps engineer must implement a solution to identify in near real time any AWS service misconfiguration that results in noncompliance. The solution must automatically remediate the issue within 15 minutes of identification. The solution also must track noncompliant resources and events in a centralized dashboard with accurate timestamps.Which solution will meet these requirements with the LEAST development overhead?

A. Use CloudFormation drift detection to identify noncompliant resources. Use drift detection events from CloudFormation to invoke an AWS Lambda function for remediation. Configure the Lambda function to publish logs to an Amazon CloudWatch Logs log group. Configure an Amazon CloudWatch dashboard to use the log group for tracking.

B. Turn on AWS CloudTrail in the AWS accounts. Analyze CloudTrail logs by using Amazon Athena to identify noncompliant resources. Use AWS Step Functions to track query results on Athena for drift detection and to invoke an AWS Lambda function for remediation. For tracking, set up an Amazon QuickSight dashboard that uses Athena as the data source.

C. Turn on the configuration recorder in AWS Config in all the AWS accounts to identify noncompliant resources. Enable AWS Security Hub with the --no-enable-default-standards option in all the AWS accounts. Set up AWS Config managed rules and custom rules. Set up automatic remediation by using AWS Config conformance packs. For tracking, set up a dashboard on Security Hub in a designated Security Hub administrator account.

D. Turn on AWS CloudTrail in the AWS accounts. Analyze CloudTrail logs by using Amazon CloudWatch Logs to identify noncompliant resources. Use CloudWatch Logs filters for drift detection. Use Amazon EventBridge to invoke the Lambda function for remediation. Stream filtered CloudWatch logs to Amazon OpenSearch Service. Set up a dashboard on OpenSearch Service for tracking.

**Đáp án**: ___________

---

## Câu 7

**ID**: 134 | **Loại**: Single Choice

A company uses AWS Organizations to manage its AWS accounts. The organization root has an OU that is named Environments. The Environments OU has two child OUs that are named Development and Production, respectively.The Environments OU and the child OUs have the default FullAWSAccess policy in place. A DevOps engineer plans to remove the FullAWSAccess policy from the Development OU and replace the policy with a policy that allows all actions on Amazon EC2 resources.What will be the outcome of this policy replacement?

A. All users in the Development OU will be allowed all API actions on all resources.

B. All users in the Development OU will be allowed all API actions on EC2 resources. All other API actions will be denied.

C. All users in the Development OU will be denied all API actions on all resources.

D. All users in the Development OU will be denied all API actions on EC2 resources. All other API actions will be allowed.

**Đáp án**: ___________

---

## Câu 8

**ID**: 135 | **Loại**: Single Choice

A company is examining its disaster recovery capability and wants the ability to switch over its daily operations to a secondary AWS Region. The company uses AWS CodeCommit as a source control tool in the primary Region.A DevOps engineer must provide the capability for the company to develop code in the secondary Region. If the company needs to use the secondary Region, developers can add an additional remote URL to their local Git configuration.Which solution will meet these requirements?

A. Create a CodeCommit repository in the secondary Region. Create an AWS CodeBuild project to perform a Git mirror operation of the primary Region's CodeCommit repository to the secondary Region's CodeCommit repository. Create an AWS Lambda function that invokes the CodeBuild project. Create an Amazon EventBridge rule that reacts to merge events in the primary Region's CodeCommit repository. Configure the EventBridge rule to invoke the Lambda function.

B. Create an Amazon S3 bucket in the secondary Region. Create an AWS Fargate task to perform a Git mirror operation of the primary Region's CodeCommit repository and copy the result to the S3 bucket. Create an AWS Lambda function that initiates the Fargate task. Create an Amazon EventBridge rule that reacts to merge events in the CodeCommit repository. Configure the EventBridge rule to invoke the Lambda function.

C. Create an AWS CodeArtifact repository in the secondary Region. Create an AWS CodePipeline pipeline that uses the primary Region’s CodeCommit repository for the source action. Create a cross-Region stage in the pipeline that packages the CodeCommit repository contents and stores the contents in the CodeArtifact repository when a pull request is merged into the CodeCommit repository.

D. Create an AWS Cloud9 environment and a CodeCommit repository in the secondary Region. Configure the primary Region's CodeCommit repository as a remote repository in the AWS Cloud9 environment. Connect the secondary Region's CodeCommit repository to the AWS Cloud9 environment.

**Đáp án**: ___________

---

## Câu 9

**ID**: 136 | **Loại**: Single Choice

A DevOps team is merging code revisions for an application that uses an Amazon RDS Multi-AZ DB cluster for its production database. The DevOps team uses continuous integration to periodically verify that the application works. The DevOps team needs to test the changes before the changes are deployed to the production database.Which solution will meet these requirements?

A. Use a buildspec file in AWS CodeBuild to restore the DB cluster from a snapshot of the production database, run integration tests, and drop the restored database after verification.

B. Deploy the application to production. Configure an audit log of data control language (DCL) operations to capture database activities to perform if verification fails.

C. Create a snapshot of the DB cluster before deploying the application. Use the Update requires:Replacement property on the DB instance in AWS CloudFormation to deploy the application and apply the changes.

D. Ensure that the DB cluster is a Multi-AZ deployment. Deploy the application with the updates. Fail over to the standby instance if verification fails.

**Đáp án**: ___________

---

## Câu 10

**ID**: 137 | **Loại**: Single Choice

A company manages a multi-tenant environment in its VPC and has configured Amazon GuardDuty for the corresponding AWS account. The company sends all GuardDuty findings to AWS Security Hub.Traffic from suspicious sources is generating a large number of findings. A DevOps engineer needs to implement a solution to automatically deny traffic across the entire VPC when GuardDuty discovers a new suspicious source.Which solution will meet these requirements?

A. Create a GuardDuty threat list. Configure GuardDuty to reference the list. Create an AWS Lambda function that will update the threat list. Configure the Lambda function to run in response to new Security Hub findings that come from GuardDuty.

B. Configure an AWS WAF web ACL that includes a custom rule group. Create an AWS Lambda function that will create a block rule in the custom rule group. Configure the Lambda function to run in response to new Security Hub findings that come from GuardDuty.

C. Configure a firewall in AWS Network Firewall. Create an AWS Lambda function that will create a Drop action rule in the firewall policy. Configure the Lambda function to run in response to new Security Hub findings that come from GuardDuty.

D. Create an AWS Lambda function that will create a GuardDuty suppression rule. Configure the Lambda function to run in response to new Security Hub findings that come from GuardDuty.

**Đáp án**: ___________

---

## Câu 11

**ID**: 138 | **Loại**: Multiple Choice

A company uses AWS Secrets Manager to store a set of sensitive API keys that an AWS Lambda function uses. When the Lambda function is invoked the Lambda function retrieves the API keys and makes an API call to an external service. The Secrets Manager secret is encrypted with the default AWS Key Management Service (AWS KMS) key.A DevOps engineer needs to update the infrastructure to ensure that only the Lambda function’s execution role can access the values in Secrets Manager. The solution must apply the principle of least privilege.Which combination of steps will meet these requirements? (Choose two.)

A. Update the default KMS key for Secrets Manager to allow only the Lambda function’s execution role to decrypt

B. Create a KMS customer managed key that trusts Secrets Manager and allows the Lambda function's execution role to decrypt. Update Secrets Manager to use the new customer managed key

C. Create a KMS customer managed key that trusts Secrets Manager and allows the account's root principal to decrypt. Update Secrets Manager to use the new customer managed key

D. Ensure that the Lambda function’s execution role has the KMS permissions scoped on the resource level. Configure the permissions so that the KMS key can encrypt the Secrets Manager secret

E. Remove all KMS permissions from the Lambda function’s execution role

**Đáp án**: ___________

---

## Câu 12

**ID**: 139 | **Loại**: Multiple Choice

A company's DevOps engineer is creating an AWS Lambda function to process notifications from an Amazon Simple Notification Service (Amazon SNS) topic. The Lambda function will process the notification messages and will write the contents of the notification messages to an Amazon RDS Multi-AZ DB instance.During testing, a database administrator accidentally shut down the DB instance. While the database was down the company lost several of the SNS notification messages that were delivered during that time.The DevOps engineer needs to prevent the loss of notification messages in the future.Which solutions will meet this requirement? (Choose two.)

A. Replace the RDS Multi-AZ DB instance with an Amazon DynamoDB table.

B. Configure an Amazon Simple Queue Service (Amazon SQS) queue as a destination of the Lambda function.

C. Configure an Amazon Simple Queue Service (Amazon SQS) dead-letter queue for the SNS topic.

D. Subscribe an Amazon Simple Queue Service (Amazon SQS) queue to the SNS topic. Configure the Lambda function to process messages from the SQS queue.

E. Replace the SNS topic with an Amazon EventBridge event bus. Configure an EventBridge rule on the new event bus to invoke the Lambda function for each event.

**Đáp án**: ___________

---

## Câu 13

**ID**: 140 | **Loại**: Single Choice

A company has an application that runs on Amazon EC2 instances. The company uses an AWS CodePipeline pipeline to deploy the application into multiple AWS Regions. The pipeline is configured with a stage for each Region. Each stage contains an AWS CloudFormation action for each Region.When the pipeline deploys the application to a Region, the company wants to confirm that the application is in a healthy state before the pipeline moves on to the next Region. Amazon Route 53 record sets are configured for the application in each Region. A DevOps engineer creates a Route 53 health check that is based on an Amazon CloudWatch alarm for each Region where the application is deployed.What should the DevOps engineer do next to meet the requirements?

A. Create an AWS Step Functions workflow to check the state of the CloudWatch alarm. Configure the Step Functions workflow to exit with an error if the alarm is in the ALARM state. Create a new stage in the pipeline between each Region deployment stage. In each new stage, include an action to invoke the Step Functions workflow.

B. Configure an AWS CodeDeploy application to deploy a CloudFormation template with automatic rollback. Configure the CloudWatch alarm as the instance health check for the CodeDeploy application. Remove the CloudFormation actions from the pipeline. Create a CodeDeploy action in the pipeline stage for each Region.

C. Create a new pipeline stage for each Region where the application is deployed. Configure a CloudWatch alarm action for the new stage to check the state of the CloudWatch alarm and to exit with an error if the alarm is in the ALARM state

D. Configure the CloudWatch agent on the EC2 instances to report the application status to the Route 53 health check. Create a new pipeline stage for each Region where the application is deployed. Configure a CloudWatch alarm action to exit with an error if the CloudWatch alarm is in the ALARM state.

**Đáp án**: ___________

---

## Câu 14

**ID**: 141 | **Loại**: Single Choice

A company plans to use Amazon CloudWatch to monitor its Amazon EC2 instances. The company needs to stop EC2 instances when the average of the NetworkPacketsIn metric is less than 5 for at least 3 hours in a 12-hour time window. The company must evaluate the metric every hour. The EC2 instances must continue to run if there is missing data for the NetworkPacketsIn metric during the evaluation period.A DevOps engineer creates a CloudWatch alarm for the NetworkPacketsIn metric. The DevOps engineer configures a threshold value of 5 and an evaluation period of 1 hour.Which set of additional actions should the DevOps engineer take to meet these requirements?

A. Configure the Datapoints to Alarm value to be 3 out of 12. Configure the alarm to treat missing data as breaching the threshold. Add an AWS Systems Manager action to stop the instance when the alarm enters the ALARM state.

B. Configure the Datapoints to Alarm value to be 3 out of 12. Configure the alarm to treat missing data as not breaching the threshold. Add an EC2 action to stop the instance when the alarm enters the ALARM state.

C. Configure the Datapoints to Alarm value to be 9 out of 12. Configure the alarm to treat missing data as breaching the threshold. Add an EC2 action to stop the instance when the alarm enters the ALARM state.

D. Configure the Datapoints to Alarm value to be 9 out of 12. Configure the alarm to treat missing data as not breaching the threshold. Add an AWS Systems Manager action to stop the instance when the alarm enters the ALARM state.

**Đáp án**: ___________

---

## Câu 15

**ID**: 142 | **Loại**: Single Choice

A company manages 500 AWS accounts that are in an organization in AWS Organizations. The company discovers many unattached Amazon Elastic Block Store (Amazon EBS) volumes in all the accounts. The company wants to automatically tag the unattached EBS volumes for investigation.A DevOps engineer needs to deploy an AWS Lambda function to all the AWS accounts. The Lambda function must run every 30 minutes to tag all the EBS volumes that have been unattached for a period of 7 days or more.Which solution will meet these requirements in the MOST operationally efficient manner?

A. Configure a delegated administrator account for the organization. Create an AWS CloudFormation template that contains the Lambda function. Use CloudFormation StackSets to deploy the CloudFormation template from the delegated administrator account to all the member accounts in the organization. Create an Amazon EventBridge event bus in the delegated administrator account to invoke the Lambda function in each member account every 30 minutes.

B. Create a cross-account IAM role in the organization's member accounts. Attach the AWSLambda_FullAccess policy and the AWSCloudFormationFullAccess policy to the role. Create an AWS CloudFormation template that contains the Lambda function and an Amazon EventBridge scheduled rule to invoke the Lambda function every 30 minutes. Create a custom script in the organization’s management account that assumes the role and deploys the CloudFormation template to the member accounts.

C. Configure a delegated administrator account for the organization. Create an AWS CloudFormation template that contains the Lambda function and an Amazon EventBridge scheduled rule to invoke the Lambda function every 30 minutes. Use CloudFormation StackSets to deploy the CloudFormation template from the delegated administrator account to all the member accounts in the organization

D. Create a cross-account IAM role in the organization's member accounts. Attach the AmazonS3FullAccess policy and the AWSCodeDeployDeployerAccess policy to the role. Use AWS CodeDeploy to assume the role to deploy the Lambda function from the organization's management account. Configure an Amazon EventBridge scheduled rule in the member accounts to invoke the Lambda function every 30 minutes.

**Đáp án**: ___________

---

## Câu 16

**ID**: 143 | **Loại**: Single Choice

A company's production environment uses an AWS CodeDeploy blue/green deployment to deploy an application. The deployment incudes Amazon EC2 Auto Scaling groups that launch instances that run Amazon Linux 2.A working appspec.yml file exists in the code repository and contains the following text:A DevOps engineer needs to ensure that a script downloads and installs a license file onto the instances before the replacement instances start to handle request traffic. The DevOps engineer adds a hooks section to the appspec.yml file.Which hook should the DevOps engineer use to run the script that downloads and installs the license file?

A. AfterBlockTraffic

B. BeforeBlockTraffic

C. BeforeInstall

D. DownloadBundle

**Đáp án**: ___________

---

## Câu 17

**ID**: 144 | **Loại**: Single Choice

A company has an application that includes AWS Lambda functions. The Lambda functions run Python code that is stored in an AWS CodeCommit repository. The company has recently experienced failures in the production environment because of an error in the Python code. An engineer has written unit tests for the Lambda functions to help avoid releasing any future defects into the production environment.The company's DevOps team needs to implement a solution to integrate the unit tests into an existing AWS CodePipeline pipeline. The solution must produce reports about the unit tests for the company to view.Which solution will meet these requirements?

A. Associate the CodeCommit repository with Amazon CodeGuru Reviewer. Create a new AWS CodeBuild project. In the CodePipeline pipeline, configure a test stage that uses the new CodeBuild project. Create a buildspec.yml file in the CodeCommit repository. In the buildspec yml file, define the actions to run a CodeGuru review.

B. Create a new AWS CodeBuild project. In the CodePipeline pipeline, configure a test stage that uses the new CodeBuild project. Create a CodeBuild report group. Create a buildspec.yml file in the CodeCommit repository. In the buildspec.yml file, define the actions to run the unit tests with an output of JUNITXML in the build phase section. Configure the test reports to be uploaded to the new CodeBuild report group.

C. Create a new AWS CodeArtifact repository. Create a new AWS CodeBuild project. In the CodePipeline pipeline, configure a test stage that uses the new CodeBuild project. Create an appspec.yml file in the original CodeCommit repository. In the appspec.yml file, define the actions to run the unit tests with an output of CUCUMBERJSON in the build phase section. Configure the tests reports to be sent to the new CodeArtifact repository.

D. Create a new AWS CodeBuild project. In the CodePipeline pipeline, configure a test stage that uses the new CodeBuild project. Create a new Amazon S3 bucket. Create a buildspec.yml file in the CodeCommit repository. In the buildspec yml file, define the actions to run the unit tests with an output of HTML in the phases section. In the reports section, upload the test reports to the S3 bucket.

**Đáp án**: ___________

---

## Câu 18

**ID**: 146 | **Loại**: Single Choice

A company uses AWS and has a VPC that contains critical compute infrastructure with predictable traffic patterns. The company has configured VPC flow logs that are published to a log group in Amazon CloudWatch Logs.The company's DevOps team needs to configure a monitoring solution for the VPC flow logs to identify anomalies in network traffic to the VPC over time. If the monitoring solution detects an anomaly, the company needs the ability to initiate a response to the anomaly.How should the DevOps team configure the monitoring solution to meet these requirements?

A. Create an Amazon Kinesis data stream. Subscribe the log group to the data stream. Configure Amazon Kinesis Data Analytics to detect log anomalies in the data stream. Create an AWS Lambda function to use as the output of the data stream. Configure the Lambda function to write to the default Amazon EventBridge event bus in the event of an anomaly finding.

B. Create an Amazon Kinesis Data Firehose delivery stream that delivers events to an Amazon S3 bucket. Subscribe the log group to the delivery stream. Configure Amazon Lookout for Metrics to monitor the data in the S3 bucket for anomalies. Create an AWS Lambda function to run in response to Lookout for Metrics anomaly findings. Configure the Lambda function to publish to the default Amazon EventBridge event bus.

C. Create an AWS Lambda function to detect anomalies. Configure the Lambda function to publish an event to the default Amazon EventBridge event bus if the Lambda function detects an anomaly. Subscribe the Lambda function to the log group.

D. Create an Amazon Kinesis data stream. Subscribe the log group to the data stream. Create an AWS Lambda function to detect log anomalies. Configure the Lambda function to write to the default Amazon EventBridge event bus if the Lambda function detects an anomaly. Set the Lambda function as the processor for the data stream.

**Đáp án**: ___________

---

## Câu 19

**ID**: 147 | **Loại**: Single Choice

AnyCompany is using AWS Organizations to create and manage multiple AWS accounts. AnyCompany recently acquired a smaller company, Example Corp. During the acquisition process, Example Corp's single AWS account joined AnyCompany's management account through an Organizations invitation. AnyCompany moved the new member account under an OU that is dedicated to Example Corp.AnyCompany's DevOps engineer has an IAM user that assumes a role that is named OrganizationAccountAccessRole to access member accounts. This role is configured with a full access policy. When the DevOps engineer tries to use the AWS Management Console to assume the role in Example Corp's new member account, the DevOps engineer receives the following error message: "Invalid information in one or more fields. Check your information or contact your administrator."Which solution will give the DevOps engineer access to the new member account?

A. In the management account, grant the DevOps engineer's IAM user permission to assume the OrganizationAccountAccessRole IAM role in the new member account.

B. In the management account, create a new SCP. In the SCP, grant the DevOps engineer's IAM user full access to all resources in the new member account. Attach the SCP to the OU that contains the new member account.

C. In the new member account, create a new IAM role that is named OrganizationAccountAccessRole. Attach the AdministratorAccess AWS managed policy to the role. In the role's trust policy, grant the management account permission to assume the role.

D. In the new member account, edit the trust policy for the OrganizationAccountAccessRole IAM role. Grant the management account permission to assume the role.

**Đáp án**: ___________

---

## Câu 20

**ID**: 148 | **Loại**: Single Choice

A DevOps engineer is designing an application that integrates with a legacy REST API. The application has an AWS Lambda function that reads records from an Amazon Kinesis data stream. The Lambda function sends the records to the legacy REST API.Approximately 10% of the records that the Lambda function sends from the Kinesis data stream have data errors and must be processed manually. The Lambda function event source configuration has an Amazon Simple Queue Service (Amazon SQS) dead-letter queue as an on-failure destination. The DevOps engineer has configured the Lambda function to process records in batches and has implemented retries in case of failure.During testing, the DevOps engineer notices that the dead-letter queue contains many records that have no data errors and that already have been processed by the legacy REST API. The DevOps engineer needs to configure the Lambda function's event source options to reduce the number of errorless records that are sent to the dead-letter queue.Which solution will meet these requirements?

A. Increase the retry attempts.

B. Configure the setting to split the batch when an error occurs.

C. Increase the concurrent batches per shard.

D. Decrease the maximum age of record.

**Đáp án**: ___________

---

## Câu 21

**ID**: 149 | **Loại**: Single Choice

A company has microservices running in AWS Lambda that read data from Amazon DynamoDB. The Lambda code is manually deployed by developers after successful testing. The company now needs the tests and deployments be automated and run in the cloud. Additionally, traffic to the new versions of each microservice should be incrementally shifted over time after deployment.What solution meets all the requirements, ensuring the MOST developer velocity?

A. Create an AWS CodePipeline configuration and set up a post-commit hook to trigger the pipeline after tests have passed. Use AWS CodeDeploy and create a Canary deployment configuration that specifies the percentage of traffic and interval.

B. Create an AWS CodeBuild configuration that triggers when the test code is pushed. Use AWS CloudFormation to trigger an AWS CodePipeline configuration that deploys the new Lambda versions and specifies the traffic shift percentage and interval.

C. Create an AWS CodePipeline configuration and set up the source code step to trigger when code is pushed. Set up the build step to use AWS CodeBuild to run the tests. Set up an AWS CodeDeploy configuration to deploy, then select the CodeDeployDefault.LambdaLinear10PercentEvery3Minutes option.

D. Use the AWS CLI to set up a post-commit hook that uploads the code to an Amazon S3 bucket after tests have passed Set up an S3 event trigger that runs a Lambda function that deploys the new version. Use an interval in the Lambda function to deploy the code over time at the required percentage.

**Đáp án**: ___________

---

## Câu 22

**ID**: 150 | **Loại**: Single Choice

A company is building a web and mobile application that uses a serverless architecture powered by AWS Lambda and Amazon API Gateway. The company wants to fully automate the backend Lambda deployment based on code that is pushed to the appropriate environment branch in an AWS CodeCommit repository.The deployment must have the following:• Separate environment pipelines for testing and production• Automatic deployment that occurs for test environments onlyWhich steps should be taken to meet these requirements?

A. Configure a new AWS CodePipeline service. Create a CodeCommit repository for each environment. Set up CodePipeline to retrieve the source code from the appropriate repository. Set up the deployment step to deploy the Lambda functions with AWS CloudFormation.

B. Create two AWS CodePipeline configurations for test and production environments. Configure the production pipeline to have a manual approval step. Create a CodeCommit repository for each environment. Set up each CodePipeline to retrieve the source code from the appropriate repository. Set up the deployment step to deploy the Lambda functions with AWS CloudFormation.

C. Create two AWS CodePipeline configurations for test and production environments. Configure the production pipeline to have a manual approval step. Create one CodeCommit repository with a branch for each environment. Set up each CodePipeline to retrieve the source code from the appropriate branch in the repository. Set up the deployment step to deploy the Lambda functions with AWS CloudFormation.

D. Create an AWS CodeBuild configuration for test and production environments. Configure the production pipeline to have a manual approval step. Create one CodeCommit repository with a branch for each environment. Push the Lambda function code to an Amazon S3 bucket. Set up the deployment step to deploy the Lambda functions from the S3 bucket.

**Đáp án**: ___________

---

## Câu 23

**ID**: 151 | **Loại**: Single Choice

A DevOps engineer wants to find a solution to migrate an application from on premises to AWS. The application is running on Linux and needs to run on specific versions of Apache Tomcat, HAProxy, and Varnish Cache to function properly. The application's operating system-level parameters require tuning. The solution must include a way to automate the deployment of new application versions. The infrastructure should be scalable and faulty servers should be replaced automatically.Which solution should the DevOps engineer use?

A. Upload the application as a Docker image that contains all the necessary software to Amazon ECR. Create an Amazon ECS cluster using an AWS Fargate launch type and an Auto Scaling group. Create an AWS CodePipeline pipeline that uses Amazon ECR as a source and Amazon ECS as a deployment provider.

B. Upload the application code to an AWS CodeCommit repository with a saved configuration file to configure and install the software. Create an AWS Elastic Beanstalk web server tier and a load balanced-type environment that uses the Tomcat solution stack. Create an AWS CodePipeline pipeline that uses CodeCommit as a source and Elastic Beanstalk as a deployment provider.

C. Upload the application code to an AWS CodeCommit repository with a set of .ebextensions files to configure and install the software. Create an AWS Elastic Beanstalk worker tier environment that uses the Tomcat solution stack. Create an AWS CodePipeline pipeline that uses CodeCommit as a source and Elastic Beanstalk as a deployment provider.

D. Upload the application code to an AWS CodeCommit repository with an appspec.yml file to configure and install the necessary software. Create an AWS CodeDeploy deployment group associated with an Amazon EC2 Auto Scaling group. Create an AWS CodePipeline pipeline that uses CodeCommit as a source and CodeDeploy as a deployment provider.

**Đáp án**: ___________

---

## Câu 24

**ID**: 152 | **Loại**: Single Choice

A DevOps engineer is using AWS CodeDeploy across a fleet of Amazon EC2 instances in an EC2 Auto Scaling group. The associated CodeDeploy deployment group, which is integrated with EC2 Auto Scaling, is configured to perform in-place deployments with CodeDeployDefault.OneAtATime. During an ongoing new deployment, the engineer discovers that, although the overall deployment finished successfully, two out of five instances have the previous application revision deployed. The other three instances have the newest application revision.What is likely causing this issue?

A. The two affected instances failed to fetch the new deployment.

B. A failed AfterInstall lifecycle event hook caused the CodeDeploy agent to roll back to the previous version on the affected instances.

C. The CodeDeploy agent was not installed in two affected instances.

D. EC2 Auto Scaling launched two new instances while the new deployment had not yet finished, causing the previous version to be deployed on the affected instances.

**Đáp án**: ___________

---

## Câu 25

**ID**: 153 | **Loại**: Single Choice

A security team is concerned that a developer can unintentionally attach an Elastic IP address to an Amazon EC2 instance in production. No developer should be allowed to attach an Elastic IP address to an instance. The security team must be notified if any production server has an Elastic IP address at any time.How can this task be automated?

A. Use Amazon Athena to query AWS CloudTrail logs to check for any associate-address attempts. Create an AWS Lambda function to disassociate the Elastic IP address from the instance, and alert the security team.

B. Attach an IAM policy to the developers' IAM group to deny associate-address permissions. Create a custom AWS Config rule to check whether an Elastic IP address is associated with any instance tagged as production, and alert the security team.

C. Ensure that all IAM groups associated with developers do not have associate-address permissions. Create a scheduled AWS Lambda function to check whether an Elastic IP address is associated with any instance tagged as production, and alert the security team if an instance has an Elastic IP address associated with it.

D. Create an AWS Config rule to check that all production instances have EC2 IAM roles that include deny associate-address permissions. Verify whether there is an Elastic IP address associated with any instance, and alert the security team if an instance has an Elastic IP address associated with it.

**Đáp án**: ___________

---

## Câu 26

**ID**: 154 | **Loại**: Single Choice

A company is using AWS Organizations to create separate AWS accounts for each of its departments. The company needs to automate the following tasks:• Update the Linux AMIs with new patches periodically and generate a golden image• Install a new version of Chef agents in the golden image, if available• Provide the newly generated AMIs to the department's accountsWhich solution meets these requirements with the LEAST management overhead?

A. Write a script to launch an Amazon EC2 instance from the previous golden image. Apply the patch updates. Install the new version of the Chef agent, generate a new golden image, and then modify the AMI permissions to share only the new image with the department's accounts.

B. Use Amazon EC2 Image Builder to create an image pipeline that consists of the base Linux AMI and components to install the Chef agent. Use AWS Resource Access Manager to share EC2 Image Builder images with the department's accounts.

C. Use an AWS Systems Manager Automation runbook to update the Linux AMI by using the previous image. Provide the URL for the script that will update the Chef agent. Use AWS Organizations to replace the previous golden image in the department's accounts.

D. Use Amazon EC2 Image Builder to create an image pipeline that consists of the base Linux AMI and components to install the Chef agent. Create a parameter in AWS Systems Manager Parameter Store to store the new AMI ID that can be referenced by the department's accounts.

**Đáp án**: ___________

---

## Câu 27

**ID**: 155 | **Loại**: Single Choice

A company has a mission-critical application on AWS that uses automatic scaling. The company wants the deployment lifecycle to meet the following parameters:• The application must be deployed one instance at a time to ensure the remaining fleet continues to serve traffic.• The application is CPU intensive and must be closely monitored.• The deployment must automatically roll back if the CPU utilization of the deployment instance exceeds 85%.Which solution will meet these requirements?

A. Use AWS CloudFormation to create an AWS Step Functions state machine and Auto Scaling lifecycle hooks to move to one instance at a time into a wait state. Use AWS Systems Manager automation to deploy the update to each instance and move it back into the Auto Scaling group using the heartbeat timeout.

B. Use AWS CodeDeploy with Amazon EC2 Auto Scaling Configure an alarm tied to the CPU utilization metric. Use the CodeDeployDefault OneAtAtime configuration as a deployment strategy. Configure automatic rollbacks within the deployment group to roll back the deployment if the alarm thresholds are breached.

C. Use AWS Elastic Beanstalk for load balancing and AWS Auto Scaling. Configure an alarm tied to the CPU utilization metric. Configure rolling deployments with a fixed batch size of one instance. Enable enhanced health to monitor the status of the deployment and roll back based on the alarm previously created.

D. Use AWS Systems Manager to perform a blue/green deployment with Amazon EC2 Auto Scaling. Configure an alarm tied to the CPU utilization metric. Deploy updates one at a time. Configure automatic rollbacks within the Auto Scaling group to roll back the deployment if the alarm thresholds are breached.

**Đáp án**: ___________

---

## Câu 28

**ID**: 156 | **Loại**: Single Choice

A company has a single developer writing code for an automated deployment pipeline. The developer is storing source code in an Amazon S3 bucket for each project. The company wants to add more developers to the team but is concerned about code conflicts and lost work. The company also wants to build a test environment to deploy newer versions of code for testing and allow developers to automatically deploy to both environments when code is changed in the repository.What is the MOST efficient way to meet these requirements?

A. Create an AWS CodeCommit repository for each project, use the main branch for production code, and create a testing branch for code deployed to testing. Use feature branches to develop new features and pull requests to merge code to testing and main branches.

B. Create another S3 bucket for each project for testing code, and use an AWS Lambda function to promote code changes between testing and production buckets. Enable versioning on all buckets to prevent code conflicts.

C. Create an AWS CodeCommit repository for each project, and use the main branch for production and test code with different deployment pipelines for each environment. Use feature branches to develop new features.

D. Enable versioning and branching on each S3 bucket, use the main branch for production code, and create a testing branch for code deployed to testing. Have developers use each branch for developing in each environment.

**Đáp án**: ___________

---

## Câu 29

**ID**: 157 | **Loại**: Multiple Choice

A DevOps engineer notices that all Amazon EC2 instances running behind an Application Load Balancer in an Auto Scaling group are failing to respond to user requests. The EC2 instances are also failing target group HTTP health checks.Upon inspection, the engineer notices the application process was not running in any EC2 instances. There are a significant number of out of memory messages in the system logs. The engineer needs to improve the resilience of the application to cope with a potential application memory leak. Monitoring and notifications should be enabled to alert when there is an issue.Which combination of actions will meet these requirements? (Choose two.)

A. Change the Auto Scaling configuration to replace the instances when they fail the load balancer's health checks.

B. Change the target group health check HealthCheckIntervalSeconds parameter to reduce the interval between health checks.

C. Change the target group health checks from HTTP to TCP to check if the port where the application is listening is reachable.

D. Enable the available memory consumption metric within the Amazon CloudWatch dashboard for the entire Auto Scaling group. Create an alarm when the memory utilization is high. Associate an Amazon SNS topic to the alarm to receive notifications when the alarm goes off.

E. Use the Amazon CloudWatch agent to collect the memory utilization of the EC2 instances in the Auto Scaling group. Create an alarm when the memory utilization is high and associate an Amazon SNS topic to receive a notification.

**Đáp án**: ___________

---

## Câu 30

**ID**: 158 | **Loại**: Single Choice

An ecommerce company uses a large number of Amazon Elastic Block Store (Amazon EBS) backed Amazon EC2 instances. To decrease manual work across all the instances, a DevOps engineer is tasked with automating restart actions when EC2 instance retirement events are scheduled.How can this be accomplished?

A. Create a scheduled Amazon EventBridge rule to run an AWS Systems Manager Automation runbook that checks if any EC2 instances are scheduled for retirement once a week. If the instance is scheduled for retirement, the runbook will hibernate the instance.

B. Enable EC2 Auto Recovery on all of the instances. Create an AWS Config rule to limit the recovery to occur during a maintenance window only.

C. Reboot all EC2 instances during an approved maintenance window that is outside of standard business hours. Set up Amazon CloudWatch alarms to send a notification in case any instance is failing EC2 instance status checks.

D. Set up an AWS Health Amazon EventBridge rule to run AWS Systems Manager Automation runbooks that stop and start the EC2 instance when a retirement scheduled event occurs.

**Đáp án**: ___________

---

## Câu 31

**ID**: 159 | **Loại**: Single Choice

A company manages AWS accounts for application teams in AWS Control Tower. Individual application teams are responsible for securing their respective AWS accounts.A DevOps engineer needs to enable Amazon GuardDuty for all AWS accounts in which the application teams have not already enabled GuardDuty. The DevOps engineer is using AWS CloudFormation StackSets from the AWS Control Tower management account.How should the DevOps engineer configure the CloudFormation template to prevent failure during the StackSets deployment?

A. Create a CloudFormation custom resource that invokes an AWS Lambda function. Configure the Lambda function to conditionally enable GuardDuty if GuardDuty is not already enabled in the accounts.

B. Use the Conditions section of the CloudFormation template to enable GuardDuty in accounts where GuardDuty is not already enabled.

C. Use the CloudFormation Fn::GetAtt intrinsic function to check whether GuardDuty is already enabled. If GuardDuty is not already enabled, use the Resources section of the CloudFormation template to enable GuardDuty.

D. Manually discover the list of AWS account IDs where GuardDuty is not enabled. Use the CloudFormation Fn::ImportValue intrinsic function to import the list of account IDs into the CloudFormation template to skip deployment for the listed AWS accounts.

**Đáp án**: ___________

---

## Câu 32

**ID**: 160 | **Loại**: Multiple Choice

A company has an AWS Control Tower landing zone. The company's DevOps team creates a workload OU. A development OU and a production OU are nested under the workload OU. The company grants users full access to the company's AWS accounts to deploy applications.The DevOps team needs to allow only a specific management IAM role to manage the IAM roles and policies of any AWS accounts in only the production OU.Which combination of steps will meet these requirements? (Choose two.)

A. Create an SCP that denies full access with a condition to exclude the management IAM role for the organization root.

B. Ensure that the FullAWSAccess SCP is applied at the organization root.

C. Create an SCP that allows IAM related actions. Attach the SCP to the development OU.

D. Create an SCP that denies IAM related actions with a condition to exclude the management IAM role. Attach the SCP to the workload OU.

E. Create an SCP that denies IAM related actions with a condition to exclude the management IAM role. Attach the SCP to the production OU.

**Đáp án**: ___________

---

## Câu 33

**ID**: 161 | **Loại**: Single Choice

A company hired a penetration tester to simulate an internal security breach. The tester performed port scans on the company's Amazon EC2 instances. The company's security measures did not detect the port scans.The company needs a solution that automatically provides notification when port scans are performed on EC2 instances. The company creates and subscribes to an Amazon Simple Notification Service (Amazon SNS) topic.What should the company do next to meet the requirement?

A. Ensure that Amazon GuardDuty is enabled. Create an Amazon CloudWatch alarm for detected EC2 and port scan findings. Connect the alarm to the SNS topic.

B. Ensure that Amazon Inspector is enabled. Create an Amazon EventBridge event for detected network reachability findings that indicate port scans. Connect the event to the SNS topic.

C. Ensure that Amazon Inspector is enabled. Create an Amazon EventBridge event for detected CVEs that cause open port vulnerabilities. Connect the event to the SNS topic.

D. Ensure that AWS CloudTrail is enabled. Create an AWS Lambda function to analyze the CloudTrail logs for unusual amounts of traffic from an IP address range. Connect the Lambda function to the SNS topic.

**Đáp án**: ___________

---

## Câu 34

**ID**: 162 | **Loại**: Single Choice

A company runs applications in an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. The EKS cluster uses an Application Load Balancer to route traffic to the applications that run in the cluster.A new application that was migrated to the EKS cluster is performing poorly. All the other applications in the EKS cluster maintain appropriate operation. The new application scales out horizontally to the preconfigured maximum number of pods immediately upon deployment, before any user traffic routes to the web application.Which solution will resolve the scaling behavior of the web application in the EKS cluster?

A. Implement the Horizontal Pod Autoscaler in the EKS cluster.

B. Implement the Vertical Pod Autoscaler in the EKS cluster.

C. Implement the Cluster Autoscaler.

D. Implement the AWS Load Balancer Controller in the EKS cluster.

**Đáp án**: ___________

---

## Câu 35

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

## Câu 36

**ID**: 164 | **Loại**: Single Choice

A company runs a workload on Amazon EC2 instances. The company needs a control that requires the use of Instance Metadata Service Version 2 (IMDSv2) on all EC2 instances in the AWS account. If an EC2 instance does not prevent the use of Instance Metadata Service Version 1 (IMDSv1), the EC2 instance must be terminated.Which solution will meet these requirements?

A. Set up AWS Config in the account. Use a managed rule to check EC2 instances. Configure the rule to remediate the findings by using AWS Systems Manager Automation to terminate the instance.

B. Create a permissions boundary that prevents the ec2:RunInstance action if the ec2:MetadataHttpTokens condition key is not set to a value of required. Attach the permissions boundary to the IAM role that was used to launch the instance.

C. Set up Amazon Inspector in the account. Configure Amazon Inspector to activate deep inspection for EC2 instances. Create an Amazon EventBridge rule for an Inspector2 finding. Set an AWS Lambda function as the target to terminate the instance.

D. Create an Amazon EventBridge rule for the EC2 instance launch successful event. Send the event to an AWS Lambda function to inspect the EC2 metadata and to terminate the instance.

**Đáp án**: ___________

---

## Câu 37

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

## Câu 38

**ID**: 166 | **Loại**: Multiple Choice

A company deploys a web application on Amazon EC2 instances that are behind an Application Load Balancer (ALB). The company stores the application code in an AWS CodeCommit repository. When code is merged to the main branch, an AWS Lambda function invokes an AWS CodeBuild project. The CodeBuild project packages the code, stores the packaged code in AWS CodeArtifact, and invokes AWS Systems Manager Run Command to deploy the packaged code to the EC2 instances.Previous deployments have resulted in defects, EC2 instances that are not running the latest version of the packaged code, and inconsistencies between instances.Which combination of actions should a DevOps engineer take to implement a more reliable deployment solution? (Choose two.)

A. Create a pipeline in AWS CodePipeline that uses the CodeCommit repository as a source provider. Configure pipeline stages that run the CodeBuild project in parallel to build and test the application. In the pipeline, pass the CodeBuild project output artifact to an AWS CodeDeploy action.

B. Create a pipeline in AWS CodePipeline that uses the CodeCommit repository as a source provider. Create separate pipeline stages that run a CodeBuild project to build and then test the application. In the pipeline, pass the CodeBuild project output artifact to an AWS CodeDeploy action.

C. Create an AWS CodeDeploy application and a deployment group to deploy the packaged code to the EC2 instances. Configure the ALB for the deployment group.

D. Create individual Lambda functions that use AWS CodeDeploy instead of Systems Manager to run build, test, and deploy actions.

E. Create an Amazon S3 bucket. Modify the CodeBuild project to store the packages in the S3 bucket instead of in CodeArtifact. Use deploy actions in CodeDeploy to deploy the artifact to the EC2 instances.

**Đáp án**: ___________

---

## Câu 39

**ID**: 167 | **Loại**: Single Choice

A company uses an organization in AWS Organizations to manage its AWS accounts. The company's automation account contains a CI/CD pipeline that creates and configures new AWS accounts.The company has a group of internal service teams that provide services to accounts in the organization. The service teams operate out of a set of services accounts. The service teams want to receive an AWS CloudTrail event in their services accounts when the CreateAccount API call creates a new account.How should the company share this CloudTrail event with the service accounts?

A. Create an Amazon EventBridge rule in the automation account to send account creation events to the default event bus in the services accounts. Update the default event bus in the services accounts to allow events from the automation account.

B. Create a custom Amazon EventBridge event bus in the services accounts. Update the custom event bus to allow events from the automation account. Create an EventBridge rule in the services account that directly listens to CloudTrail events from the automation account.

C. Create a custom Amazon EventBridge event bus in the automation account and the services accounts. Create an EventBridge rule and policy that connects the custom event buses that are in the automation account and the services accounts.

D. Create a custom Amazon EventBridge event bus in the automation account. Create an EventBridge rule and policy that connects the custom event bus to the default event buses in the services accounts.

**Đáp án**: ___________

---

## Câu 40

**ID**: 168 | **Loại**: Single Choice

A DevOps engineer is building a solution that uses Amazon Simple Queue Service (Amazon SQS) standard queues. The solution also includes an AWS Lambda function and an Amazon DynamoDB table. The Lambda function pulls content from an SQS queue event source and writes the content to the DynamoDB table.The solution must maximize the scalability of Lambda and must prevent successfully processed SQS messages from being processed multiple times.Which solution will meet these requirements?

A. Decrease the batch window to 1 second when configuring the Lambda function's event source mapping.

B. Decrease the batch size to 1 when configuring the Lambda function's event source mapping.

C. Include the ReportBatchItemFailures value in the FunctionResponseTypes list in the Lambda function's event source mapping.

D. Set the queue visibility timeout on the Lambda function's event source mapping to account for invocation throttling of the Lambda function.

**Đáp án**: ___________

---

## Câu 41

**ID**: 169 | **Loại**: Multiple Choice

A company has a new AWS account that teams will use to deploy various applications. The teams will create many Amazon S3 buckets for application-specific purposes and to store AWS CloudTrail logs. The company has enabled Amazon Macie for the account.A DevOps engineer needs to optimize the Macie costs for the account without compromising the account's functionality.Which solutions will meet these requirements? (Choose two.)

A. Exclude S3 buckets that contain CloudTrail logs from automated discovery.

B. Exclude S3 buckets that have public read access from automated discovery.

C. Configure scheduled daily discovery jobs for all S3 buckets in the account.

D. Configure discovery jobs to include S3 objects based on the last modified criterion.

E. Configure discovery jobs to include S3 objects that are tagged as production only.

**Đáp án**: ___________

---

## Câu 42

**ID**: 170 | **Loại**: Multiple Choice

A company uses an organization in AWS Organizations to manage its AWS accounts. The company recently acquired another company that has standalone AWS accounts. The acquiring company's DevOps team needs to consolidate the administration of the AWS accounts for both companies and retain full administrative control of the accounts. The DevOps team also needs to collect and group findings across all the accounts to implement and maintain a security posture.Which combination of steps should the DevOps team take to meet these requirements? (Choose two.)

A. Invite the acquired company's AWS accounts to join the organization. Create an SCP that has full administrative privileges. Attach the SCP to the management account.

B. Invite the acquired company's AWS accounts to join the organization. Create the OrganizationAccountAccessRole IAM role in the invited accounts. Grant permission to the management account to assume the role.

C. Use AWS Security Hub to collect and group findings across all accounts. Use Security Hub to automatically detect new accounts as the accounts are added to the organization.

D. Use AWS Firewall Manager to collect and group findings across all accounts. Enable all features for the organization. Designate an account in the organization as the delegated administrator account for Firewall Manager.

E. Use Amazon Inspector to collect and group findings across all accounts. Designate an account in the organization as the delegated administrator account for Amazon Inspector.

**Đáp án**: ___________

---

## Câu 43

**ID**: 171 | **Loại**: Single Choice

A company has an application and a CI/CD pipeline. The CI/CD pipeline consists of an AWS CodePipeline pipeline and an AWS CodeBuild project. The CodeBuild project runs tests against the application as part of the build process and outputs a test report. The company must keep the test reports for 90 days.Which solution will meet these requirements?

A. Add a new stage in the CodePipeline pipeline after the stage that contains the CodeBuild project. Create an Amazon S3 bucket to store the reports. Configure an S3 deploy action type in the new CodePipeline stage with the appropriate path and format for the reports.

B. Add a report group in the CodeBuild project buildspec file with the appropriate path and format for the reports. Create an Amazon S3 bucket to store the reports. Configure an Amazon EventBridge rule that invokes an AWS Lambda function to copy the reports to the S3 bucket when a build is completed. Create an S3 Lifecycle rule to expire the objects after 90 days.

C. Add a new stage in the CodePipeline pipeline. Configure a test action type with the appropriate path and format for the reports. Configure the report expiration time to be 90 days in the CodeBuild project buildspec file.

D. Add a report group in the CodeBuild project buildspec file with the appropriate path and format for the reports. Create an Amazon S3 bucket to store the reports. Configure the report group as an artifact in the CodeBuild project buildspec file. Configure the S3 bucket as the artifact destination. Set the object expiration to 90 days.

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

**ID**: 173 | **Loại**: Single Choice

A company uses AWS Directory Service for Microsoft Active Directory as its identity provider (IdP). The company requires all infrastructure to be defined and deployed by AWS CloudFormation.A DevOps engineer needs to create a fleet of Windows-based Amazon EC2 instances to host an application. The DevOps engineer has created a CloudFormation template that contains an EC2 launch template, IAM role, EC2 security group, and EC2 Auto Scaling group. The DevOps engineer must implement a solution that joins all EC2 instances to the domain of the AWS Managed Microsoft AD directory.Which solution will meet these requirements with the MOST operational efficiency?

A. In the CloudFormation template, create an AWS::SSM::Document resource that joins the EC2 instance to the AWS Managed Microsoft AD domain by using the parameters for the existing directory. Update the launch template to include the SSMAssociation property to use the new SSM document. Attach the AmazonSSMManagedInstanceCore and AmazonSSMDirectoryServiceAccess AWS managed policies to the IAM role that the EC2 instances use.

B. In the CloudFormation template, update the launch template to include specific tags that propagate on launch. Create an AWS::SSM::Association resource to associate the AWS-JoinDirectoryServiceDomain Automation runbook with the EC2 instances that have the specified tags. Define the required parameters to join the AWS Managed Microsoft AD directory. Attach the AmazonSSMManagedInstanceCore and AmazonSSMDirectoryServiceAccess AWS managed policies to the IAM role that the EC2 instances use.

C. Store the existing AWS Managed Microsoft AD domain connection details in AWS Secrets Manager. In the CloudFormation template, create an AWS::SSM::Association resource to associate the AWS-CreateManagedWindowsInstanceWithApproval Automation runbook with the EC2 Auto Scaling group. Pass the ARNs for the parameters from Secrets Manager to join the domain. Attach the AmazonSSMDirectoryServiceAccess and SecretsManagerReadWrite AWS managed policies to the IAM role that the EC2 instances use.

D. Store the existing AWS Managed Microsoft AD domain administrator credentials in AWS Secrets Manager. In the CloudFormation template, update the EC2 launch template to include user data. Configure the user data to pull the administrator credentials from Secrets Manager and to join the AWS Managed Microsoft AD domain. Attach the AmazonSSMManagedInstanceCore and SecretsManagerReadWrite AWS managed policies to the IAM role that the EC2 instances use.

**Đáp án**: ___________

---

## Câu 46

**ID**: 174 | **Loại**: Single Choice

A company uses AWS Organizations to manage its AWS accounts. The company has a root OU that has a child OU. The root OU has an SCP that allows all actions on all resources. The child OU has an SCP that allows all actions for Amazon DynamoDB and AWS Lambda, and denies all other actions.The company has an AWS account that is named vendor-data in the child OU. A DevOps engineer has an IAM user that is attached to the Administrator Access IAM policy in the vendor-data account. The DevOps engineer attempts to launch an Amazon EC2 instance in the vendor-data account but receives an access denied error.Which change should the DevOps engineer make to launch the EC2 instance in the vendor-data account?

A. Attach the AmazonEC2FullAccess IAM policy to the IAM user.

B. Create a new SCP that allows all actions for Amazon EC2. Attach the SCP to the vendor-data account.

C. Update the SCP in the child OU to allow all actions for Amazon EC2.

D. Create a new SCP that allows all actions for Amazon EC2. Attach the SCP to the root OU.

**Đáp án**: ___________

---

## Câu 47

**ID**: 175 | **Loại**: Single Choice

A company's security policies require the use of security hardened AMIs in production environments. A DevOps engineer has used EC2 Image Builder to create a pipeline that builds the AMIs on a recurring schedule.The DevOps engineer needs to update the launch templates of the company's Auto Scaling groups. The Auto Scaling groups must use the newest AMIs during the launch of Amazon EC2 instances.Which solution will meet these requirements with the MOST operational efficiency?

A. Configure an Amazon EventBridge rule to receive new AMI events from Image Builder. Target an AWS Systems Manager Run Command document that updates the launch templates of the Auto Scaling groups with the newest AMI ID.

B. Configure an Amazon EventBridge rule to receive new AMI events from Image Builder. Target an AWS Lambda function that updates the launch templates of the Auto Scaling groups with the newest AMI ID.

C. Configure the launch template to use a value from AWS Systems Manager Parameter Store for the AMI ID. Configure the Image Builder pipeline to update the Parameter Store value with the newest AMI ID.

D. Configure the Image Builder distribution settings to update the launch templates with the newest AMI IConfigure the Auto Scaling groups to use the newest version of the launch template.

**Đáp án**: ___________

---

## Câu 48

**ID**: 176 | **Loại**: Single Choice

A company has configured an Amazon S3 event source on an AWS Lambda function. The company needs the Lambda function to run when a new object is created or an existing object is modified in a particular S3 bucket. The Lambda function will use the S3 bucket name and the S3 object key of the incoming event to read the contents of the created or modified S3 object. The Lambda function will parse the contents and save the parsed contents to an Amazon DynamoDB table.The Lambda function's execution role has permissions to read from the S3 bucket and to write to the DynamoDB table. During testing, a DevOps engineer discovers that the Lambda function does not run when objects are added to the S3 bucket or when existing objects are modified.Which solution will resolve this problem?

A. Increase the memory of the Lambda function to give the function the ability to process large files from the S3 bucket.

B. Create a resource policy on the Lambda function to grant Amazon S3 the permission to invoke the Lambda function for the S3 bucket.

C. Configure an Amazon Simple Queue Service (Amazon SQS) queue as an OnFailure destination for the Lambda function.

D. Provision space in the /tmp folder of the Lambda function to give the function the ability to process large files from the S3 bucket.

**Đáp án**: ___________

---

## Câu 49

**ID**: 177 | **Loại**: Single Choice

A company has deployed a critical application in two AWS Regions. The application uses an Application Load Balancer (ALB) in both Regions. The company has Amazon Route 53 alias DNS records for both ALBs.The company uses Amazon Route 53 Application Recovery Controller to ensure that the application can fail over between the two Regions. The Route 53 ARC configuration includes a routing control for both Regions. The company uses Route 53 ARC to perform quarterly disaster recovery (DR) tests.During the most recent DR test, a DevOps engineer accidentally turned off both routing controls. The company needs to ensure that at least one routing control is turned on at all times.Which solution will meet these requirements?

A. In Route 53 ARC, create a new assertion safety rule. Apply the assertion safety rule to the two routing controls. Configure the rule with the ATLEAST type with a threshold of 1.

B. In Route 53 ARC, create a new gating safety rule. Apply the assertion safety rule to the two routing controls. Configure the rule with the OR type with a threshold of 1.

C. In Route 53 ARC, create a new resource set. Configure the resource set with an AWS::Route53::HealthCheck resource type. Specify the ARNs of the two routing controls as the target resource. Create a new readiness check for the resource set.

D. In Route 53 ARC, create a new resource set. Configure the resource set with an AWS::Route53RecoveryReadiness::DNSTargetResource resource type. Add the domain names of the two Route 53 alias DNS records as the target resource. Create a new readiness check for the resource set.

**Đáp án**: ___________

---

## Câu 50

**ID**: 178 | **Loại**: Single Choice

A healthcare services company is concerned about the growing costs of software licensing for an application for monitoring patient wellness. The company wants to create an audit process to ensure that the application is running exclusively on Amazon EC2 Dedicated Hosts. A DevOps engineer must create a workflow to audit the application to ensure compliance.What steps should the engineer take to meet this requirement with the LEAST administrative overhead?

A. Use AWS Systems Manager Configuration Compliance. Use calls to the put-compliance-items API action to scan and build a database of noncompliant EC2 instances based on their host placement configuration. Use an Amazon DynamoDB table to store these instance IDs for fast access. Generate a report through Systems Manager by calling the list-compliance-summaries API action.

B. Use custom Java code running on an EC2 instance. Set up EC2 Auto Scaling for the instance depending on the number of instances to be checked. Send the list of noncompliant EC2 instance IDs to an Amazon SQS queue. Set up another worker instance to process instance IDs from the SQS queue and write them to Amazon DynamoDUse an AWS Lambda function to terminate noncompliant instance IDs obtained from the queue, and send them to an Amazon SNS email topic for distribution.

C. Use AWS Config. Identify all EC2 instances to be audited by enabling Config Recording on all Amazon EC2 resources for the region. Create a custom AWS Config rule that triggers an AWS Lambda function by using the "config-rule-change -triggered" blueprint. Modify the Lambda evaluateCompliance() function to verify host placement to return a NON_COMPLIANT result if the instance is not running on an EC2 Dedicated Host. Use the AWS Config report to address noncompliant instances.

D. Use AWS CloudTrail. Identify all EC2 instances to be audited by analyzing all calls to the EC2 RunCommand API action. Invoke an AWS Lambda function that analyzes the host placement of the instance. Store the EC2 instance ID of noncompliant resources in an Amazon RDS for MySQL DB instance. Generate a report by querying the RDS instance and exporting the query results to a CSV text file.

**Đáp án**: ___________

---

## Câu 51

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

## Câu 52

**ID**: 180 | **Loại**: Multiple Choice

A company is using AWS CodePipeline to deploy an application. According to a new guideline, a member of the company's security team must sign off on any application changes before the changes are deployed into production. The approval must be recorded and retained.Which combination of actions will meet these requirements? (Choose two.)

A. Configure CodePipeline to write actions to Amazon CloudWatch Logs.

B. Configure CodePipeline to write actions to an Amazon S3 bucket at the end of each pipeline stage.

C. Create an AWS CloudTrail trail to deliver logs to Amazon S3.

D. Create a CodePipeline custom action to invoke an AWS Lambda function for approval. Create a policy that gives the security team access to manage CodePipeline custom actions.

E. Create a CodePipeline manual approval action before the deployment step. Create a policy that grants the security team access to approve manual approval stages.

**Đáp án**: ___________

---

## Câu 53

**ID**: 181 | **Loại**: Single Choice

A company requires its internal business teams to launch resources through pre-approved AWS CloudFormation templates only. The security team requires automated monitoring when resources drift from their expected state.Which strategy should be used to meet these requirements?

A. Allow users to deploy CloudFormation stacks using a CloudFormation service role only. Use CloudFormation drift detection to detect when resources have drifted from their expected state.

B. Allow users to deploy CloudFormation stacks using a CloudFormation service role only. Use AWS Config rules to detect when resources have drifted from their expected state.

C. Allow users to deploy CloudFormation stacks using AWS Service Catalog only. Enforce the use of a launch constraint. Use AWS Config rules to detect when resources have drifted from their expected state.

D. Allow users to deploy CloudFormation stacks using AWS Service Catalog only. Enforce the use of a template constraint. Use Amazon EventBridge notifications to detect when resources have drifted from their expected state.

**Đáp án**: ___________

---

## Câu 54

**ID**: 182 | **Loại**: Single Choice

A company has multiple development groups working in a single shared AWS account. The senior manager of the groups wants to be alerted via a third-party API call when the creation of resources approaches the service limits for the account.Which solution will accomplish this with the LEAST amount of development effort?

A. Create an Amazon EventBridge rule that runs periodically and targets an AWS Lambda function. Within the Lambda function, evaluate the current state of the AWS environment and compare deployed resource values to resource limits on the account. Notify the senior manager if the account is approaching a service limit.

B. Deploy an AWS Lambda function that refreshes AWS Trusted Advisor checks, and configure an Amazon EventBridge rule to run the Lambda function periodically. Create another EventBridge rule with an event pattern matching Trusted Advisor events and a target Lambda function. In the target Lambda function, notify the senior manager.

C. Deploy an AWS Lambda function that refreshes AWS Health Dashboard checks, and configure an Amazon EventBridge rule to run the Lambda function periodically. Create another EventBridge rule with an event pattern matching Health Dashboard events and a target Lambda function. In the target Lambda function, notify the senior manager.

D. Add an AWS Config custom rule that runs periodically, checks the AWS service limit status, and streams notifications to an Amazon Simple Notification Service (Amazon SNS) topic. Deploy an AWS Lambda function that notifies the senior manager, and subscribe the Lambda function to the SNS topic.

**Đáp án**: ___________

---

## Câu 55

**ID**: 183 | **Loại**: Single Choice

A DevOps engineer is setting up a container-based architecture. The engineer has decided to use AWS CloudFormation to automatically provision an Amazon ECS cluster and an Amazon EC2 Auto Scaling group to launch the EC2 container instances. After successfully creating the CloudFormation stack, the engineer noticed that, even though the ECS cluster and the EC2 instances were created successfully and the stack finished the creation, the EC2 instances were associating with a different cluster.How should the DevOps engineer update the CloudFormation template to resolve this issue?

A. Reference the EC2 instances in the AWS::ECS::Cluster resource and reference the ECS cluster in the AWS::ECS::Service resource.

B. Reference the ECS cluster in the AWS::AutoScaling::LaunchConfiguration resource of the UserData property.

C. Reference the ECS cluster in the AWS::EC2::Instance resource of the UserData property.

D. Reference the ECS cluster in the AWS::CloudFormation::CustomResource resource to trigger an AWS Lambda function that registers the EC2 instances with the appropriate ECS cluster.

**Đáp án**: ___________

---

## Câu 56

**ID**: 184 | **Loại**: Multiple Choice

A DevOps engineer is implementing governance controls for a company that requires its infrastructure to be housed within the United States. The engineer must restrict which AWS Regions can be used, and ensure an alert is sent as soon as possible if any activity outside the governance policy takes place. The controls should be automatically enabled on any new Region outside the United States (US).Which combination of actions will meet these requirements? (Choose two.)

A. Create an AWS Organizations SCP that denies access to all non-global services in non-US Regions. Attach the policy to the root of the organization.

B. Configure AWS CloudTrail to send logs to Amazon CloudWatch Logs and enable it for all Regions. Use a CloudWatch Logs metric filter to send an alert on any service activity in non-US Regions.

C. Use an AWS Lambda function that checks for AWS service activity and deploy it to all Regions. Write an Amazon EventBridge rule that runs the Lambda function every hour, sending an alert if activity is found in a non-US Region.

D. Use an AWS Lambda function to query Amazon Inspector to look for service activity in non-US Regions and send alerts if any activity is found.

E. Write an SCP using the aws:RequestedRegion condition key limiting access to US Regions. Apply the policy to all users, groups, and roles.

**Đáp án**: ___________

---

## Câu 57

**ID**: 185 | **Loại**: Single Choice

A company sells products through an ecommerce web application. The company wants a dashboard that shows a pie chart of product transaction details. The company wants to integrate the dashboard with the company's existing Amazon CloudWatch dashboards.Which solution will meet these requirements with the MOST operational efficiency?

A. Update the ecommerce application to emit a JSON object to a CloudWatch log group for each processed transaction. Use CloudWatch Logs Insights to query the log group and to visualize the results in a pie chart format. Attach the results to the desired CloudWatch dashboard.

B. Update the ecommerce application to emit a JSON object to an Amazon S3 bucket for each processed transaction. Use Amazon Athena to query the S3 bucket and to visualize the results in a pie chart format. Export the results from Athena. Attach the results to the desired CloudWatch dashboard.

C. Update the ecommerce application to use AWS X-Ray for instrumentation. Create a new X-Ray subsegment. Add an annotation for each processed transaction. Use X-Ray traces to query the data and to visualize the results in a pie chart format. Attach the results to the desired CloudWatch dashboard.

D. Update the ecommerce application to emit a JSON object to a CloudWatch log group for each processed transaction. Create an AWS Lambda function to aggregate and write the results to Amazon DynamoDB. Create a Lambda subscription filter for the log file. Attach the results to the desired CloudWatch dashboard.

**Đáp án**: ___________

---

## Câu 58

**ID**: 186 | **Loại**: Single Choice

A company is launching an application. The application must use only approved AWS services. The account that runs the application was created less than 1 year ago and is assigned to an AWS Organizations OU.The company needs to create a new Organizations account structure. The account structure must have an appropriate SCP that supports the use of only services that are currently active in the AWS account. The company will use AWS Identity and Access Management (IAM) Access Analyzer in the solution.Which solution will meet these requirements?

A. Create an SCP that allows the services that IAM Access Analyzer identifies. Create an OU for the account. Move the account into the new OU. Attach the new SCP to the new OU. Detach the default FullAWSAccess SCP from the new OU.

B. Create an SCP that denies the services that IAM Access Analyzer identifies. Create an OU for the account. Move the account into the new OU. Attach the new SCP to the new OU.

C. Create an SCP that allows the services that IAM Access Analyzer identifies. Attach the new SCP to the organization's root.

D. Create an SCP that allows the services that IAM Access Analyzer identifies. Create an OU for the account. Move the account into the new OU. Attach the new SCP to the management account. Detach the default FullAWSAccess SCP from the new OU.

**Đáp án**: ___________

---

## Câu 59

**ID**: 187 | **Loại**: Single Choice

A company has multiple development teams in different business units that work in a shared single AWS account. All Amazon EC2 resources that are created in the account must include tags that specify who created the resources. The tagging must occur within the first hour of resource creation.A DevOps engineer needs to add tags to the created resources that include the user ID that created the resource and the cost center ID. The DevOps engineer configures an AWS Lambda function with the cost center mappings to tag the resources. The DevOps engineer also sets up AWS CloudTrail in the AWS account. An Amazon S3 bucket stores the CloudTrail event logs.Which solution will meet the tagging requirements?

A. Create an S3 event notification on the S3 bucket to invoke the Lambda function for s3:ObjectTagging:Put events. Enable bucket versioning on the S3 bucket.

B. Enable server access logging on the S3 bucket. Create an S3 event notification on the S3 bucket for s3:ObjectTagging:* events.

C. Create a recurring hourly Amazon EventBridge scheduled rule that invokes the Lambda function. Modify the Lambda function to read the logs from the S3 bucket.

D. Create an Amazon EventBridge rule that uses Amazon EC2 as the event source. Configure the rule to match events delivered by CloudTrail. Configure the rule to target the Lambda function.

**Đáp án**: ___________

---

## Câu 60

**ID**: 188 | **Loại**: Single Choice

A company runs an application for multiple environments in a single AWS account. An AWS CodePipeline pipeline uses a development Amazon Elastic Container Service (Amazon ECS) cluster to test an image for the application from an Amazon Elastic Container Registry (Amazon ECR) repository. The pipeline promotes the image to a production ECS cluster.The company needs to move the production cluster into a separate AWS account in the same AWS Region. The production cluster must be able to download the images over a private connection.Which solution will meet these requirements?

A. Use Amazon ECR VPC endpoints and an Amazon S3 gateway endpoint. In the separate AWS account, create an ECR repository. Set the repository policy to allow the production ECS tasks to pull images from the main AWS account. Configure the production ECS task execution role to have permission to download the image from the ECR repository.

B. Set a repository policy on the production ECR repository in the main AWS account. Configure the repository policy to allow the production ECS tasks in the separate AWS account to pull images from the main account. Configure the production ECS task execution role to have permission to download the image from the ECR repository.

C. Configure ECR private image replication in the main AWS account. Activate cross-account replication. Define the destination account ID of the separate AWS account.

D. Use Amazon ECR VPC endpoints and an Amazon S3 gateway endpoint. Set a repository policy on the production ECR repository in the main AWS account. Configure the repository policy to allow the production ECS tasks in the separate AWS account to pull images from the main account. Configure the production ECS task execution role to have permission to download the image from the ECR repository.

**Đáp án**: ___________

---

## Câu 61

**ID**: 189 | **Loại**: Single Choice

A company needs to ensure that flow logs remain configured for all existing and new VPCs in its AWS account. The company uses an AWS CloudFormation stack to manage its VPCs. The company needs a solution that will work for any VPCs that any IAM user creates.Which solution will meet these requirements?

A. Add the AWS::EC2::FlowLog resource to the CloudFormation stack that creates the VPCs.

B. Create an organization in AWS Organizations. Add the company's AWS account to the organization. Create an SCP to prevent users from modifying VPC flow logs.

C. Turn on AWS Config. Create an AWS Config rule to check whether VPC flow logs are turned on. Configure automatic remediation to turn on VPC flow logs.

D. Create an IAM policy to deny the use of API calls for VPC flow logs. Attach the IAM policy to all IAM users.

**Đáp án**: ___________

---

## Câu 62

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

## Câu 63

**ID**: 191 | **Loại**: Single Choice

A company uses AWS WAF to protect its cloud infrastructure. A DevOps engineer needs to give an operations team the ability to analyze log messages from AWS WAF. The operations team needs to be able to create alarms for specific patterns in the log output.Which solution will meet these requirements with the LEAST operational overhead?

A. Create an Amazon CloudWatch Logs log group. Configure the appropriate AWS WAF web ACL to send log messages to the log group. Instruct the operations team to create CloudWatch metric filters.

B. Create an Amazon OpenSearch Service cluster and appropriate indexes. Configure an Amazon Kinesis Data Firehose delivery stream to stream log data to the indexes. Use OpenSearch Dashboards to create filters and widgets.

C. Create an Amazon S3 bucket for the log output. Configure AWS WAF to send log outputs to the S3 bucket. Instruct the operations team to create AWS Lambda functions that detect each desired log message pattern. Configure the Lambda functions to publish to an Amazon Simple Notification Service (Amazon SNS) topic.

D. Create an Amazon S3 bucket for the log output. Configure AWS WAF to send log outputs to the S3 bucket. Use Amazon Athena to create an external table definition that fits the log message pattern. Instruct the operations team to write SQL queries and to create Amazon CloudWatch metric filters for the Athena queries.

**Đáp án**: ___________

---

## Câu 64

**ID**: 192 | **Loại**: Single Choice

A software team is using AWS CodePipeline to automate its Java application release pipeline. The pipeline consists of a source stage, then a build stage, and then a deploy stage. Each stage contains a single action that has a runOrder value of 1.The team wants to integrate unit tests into the existing release pipeline. The team needs a solution that deploys only the code changes that pass all unit tests.Which solution will meet these requirements?

A. Modify the build stage. Add a test action that has a runOrder value of 1. Use AWS CodeDeploy as the action provider to run unit tests.

B. Modify the build stage. Add a test action that has a runOrder value of 2. Use AWS CodeBuild as the action provider to run unit tests.

C. Modify the deploy stage. Add a test action that has a runOrder value of 1. Use AWS CodeDeploy as the action provider to run unit tests.

D. Modify the deploy stage. Add a test action that has a runOrder value of 2. Use AWS CodeBuild as the action provider to run unit tests.

**Đáp án**: ___________

---

## Câu 65

**ID**: 193 | **Loại**: Single Choice

A company uses an organization in AWS Organizations to manage several AWS accounts that the company's developers use. The company requires all data to be encrypted in transit.Multiple Amazon S3 buckets that were created in developer accounts allow unencrypted connections. A DevOps engineer must enforce encryption of data in transit for all existing S3 buckets that are created in accounts in the organization.Which solution will meet these requirements?

A. Use AWS CloudFormation StackSets to deploy an AWS Network Firewall firewall to each account. Route all outbound requests from the AWS environment through the firewall. Deploy a policy to block access to all outbound requests on port 80.

B. Use AWS CloudFormation StackSets to deploy an AWS Network Firewall firewall to each account. Route all inbound requests to the AWS environment through the firewall. Deploy a policy to block access to all inbound requests on port 80.

C. Turn on AWS Config for the organization. Deploy a conformance pack that uses the s3-bucket-ssl-requests-only managed rule and an AWS Systems Manager Automation runbook. Use a runbook that adds a bucket policy statement to deny access to an S3 bucket when the value of the aws:SecureTransport condition key is false.

D. Turn on AWS Config for the organization. Deploy a conformance pack that uses the s3-bucket-ssl-requests-only managed rule and an AWS Systems Manager Automation runbook. Use a runbook that adds a bucket policy statement to deny access to an S3 bucket when the value of the s3:x-amz-server-side-encryption-aws-kms-key-id condition key is null.

**Đáp án**: ___________

---

## Câu 66

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

## Câu 67

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

## Câu 68

**ID**: 196 | **Loại**: Multiple Choice

A DevOps engineer has created an AWS CloudFormation template that deploys an application on Amazon EC2 instances. The EC2 instances run Amazon Linux. The application is deployed to the EC2 instances by using shell scripts that contain user data. The EC2 instances have an IAM instance profile that has an IAM role with the AmazonSSMManagedinstanceCore managed policy attached.The DevOps engineer has modified the user data in the CloudFormation template to install a new version of the application. The engineer has also applied the stack update. However, the application was not updated on the running EC2 instances. The engineer needs to ensure that the changes to the application are installed on the running EC2 instances.Which combination of steps will meet these requirements? (Choose two.)

A. Configure the user data content to use the Multipurpose Internet Mail Extensions (MIME) multipart format. Set the scripts-user parameter to always in the text/cloud-config section.

B. Refactor the user data commands to use the cfn-init helper script. Update the user data to install and configure the cfn-hup and cfn-init helper scripts to monitor and apply the metadata changes.

C. Configure an EC2 launch template for the EC2 instances. Create a new EC2 Auto Scaling group. Associate the Auto Scaling group with the EC2 launch template. Use the AutoScalingScheduledAction update policy for the Auto Scaling group.

D. Refactor the user data commands to use an AWS Systems Manager document (SSM document). Add an AWS CLI command in the user data to use Systems Manager Run Command to apply the SSM document to the EC2 instances.

E. Refactor the user data command to use an AWS Systems Manager document (SSM document). Use Systems Manager State Manager to create an association between the SSM document and the EC2 instances.

**Đáp án**: ___________

---

## Câu 69

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

## Câu 70

**ID**: 198 | **Loại**: Single Choice

A company uses Amazon RDS for all databases in its AWS accounts. The company uses AWS Control Tower to build a landing zone that has an audit and logging account. All databases must be encrypted at rest for compliance reasons. The company's security engineer needs to receive notification about any noncompliant databases that are in the company’s accounts.Which solution will meet these requirements with the MOST operational efficiency?

A. Use AWS Control Tower to activate the optional detective control (guardrail) to determine whether the RDS storage is encrypted. Create an Amazon Simple Notification Service (Amazon SNS) topic in the company's audit account. Create an Amazon EventBridge rule to filter noncompliant events from the AWS Control Tower control (guardrail) to notify the SNS topic. Subscribe the security engineer's email address to the SNS topic.

B. Use AWS CloudFormation StackSets to deploy AWS Lambda functions to every account. Write the Lambda function code to determine whether the RDS storage is encrypted in the account the function is deployed to. Send the findings as an Amazon CloudWatch metric to the management account. Create an Amazon Simple Notification Service (Amazon SNS) topic. Create a CloudWatch alarm that notifies the SNS topic when metric thresholds are met. Subscribe the security engineer's email address to the SNS topic.

C. Create a custom AWS Config rule in every account to determine whether the RDS storage is encrypted. Create an Amazon Simple Notification Service (Amazon SNS) topic in the audit account. Create an Amazon EventBidge rule to filter noncompliant events from the AWS Control Tower control (guardrail) to notify the SNS topic. Subscribe the security engineer's email address to the SNS topic.

D. Launch an Amazon C2 instance. Run an hourly cron job by using the AWS CLI to determine whether the RDS storage is encrypted in each AWS account. Store the results in an RDS database. Notify the security engineer by sending email messages from the EC2 instance when noncompliance is detected

**Đáp án**: ___________

---

## Câu 71

**ID**: 199 | **Loại**: Multiple Choice

A company is migrating from its on-premises data center to AWS. The company currently uses a custom on-premises Cl/CD pipeline solution to build and package software.The company wants its software packages and dependent public repositories to be available in AWS CodeArtifact to facilitate the creation of application-specific pipelines.Which combination of steps should the company take to update the CI/CD pipeline solution and to configure CodeArtifact with the LEAST operational overhead? (Choose two.)

A. Update the C1ICD pipeline to create a VM image that contains newly packaged software. Use AWS Import/Export to make the VM image available as an Amazon EC2 AMI. Launch the AMI with an attached IAM instance profile that allows CodeArtifact actions. Use AWS CLI commands to publish the packages to a CodeArtifact repository.

B. Create an AWS Identity and Access Management Roles Anywhere trust anchor. Create an IAM role that allows CodeArtifact actions and that has a trust relationship on the trust anchor. Update the on-premises CI/CD pipeline to assume the new IAM role and to publish the packages to CodeArtifact.

C. Create a new Amazon S3 bucket. Generate a presigned URL that allows the PutObject request. Update the on-premises CI/CD pipeline to use the presigned URL to publish the packages from the on-premises location to the S3 bucket. Create an AWS Lambda function that runs when packages are created in the bucket through a put command. Configure the Lambda function to publish the packages to CodeArtifact.

D. For each public repository, create a CodeArutact repository that is configured with an external connection. Configure the dependent repositories as upstream public repositories.

E. Create a Codeartitact repository that is configured with a set of external connections to the public repositories. Configure the external connections to be downstream of the repository.

**Đáp án**: ___________

---

## Câu 72

**ID**: 200 | **Loại**: Single Choice

A DevOps team uses AWS CodePipeline, AWS CodeBuild, and AWS CodeDeploy to deploy an application. The application is a REST API that uses AWS Lambda functions and Amazon API Gateway. Recent deployments have introduced errors that have affected many customers.The DevOps team needs a solution that reverts to the most recent stable version of the application when an error is detected. The solution must affect the fewest customers possible.Which solution will meet these requirements with the MOST operational efficiency?

A. Set the deployment configuration in CodeDeploy to LambdaAllAtOnce. Configure automatic rollbacks on the deployment group. Create an Amazon CloudWatch alarm that detects HTTP Bad Gateway errors on API Gateway. Configure the deployment group to roll back when the number of alarms meets the alarm threshold.

B. Set the deployment configuration in CodeDeploy to LambdaCanary10Percent10Minutes. Configure automatic rollbacks on the deployment group. Create an Amazon CloudWatch alarm that detects HTTP Bad Gateway errors on API Gateway. Configure the deployment group to roll back when the number of alarms meets the alarm threshold.

C. Set the deployment configuration in CodeDeploy to LambdaAllAtOnce. Configure manual rollbacks on the deployment group. Create an Amazon Simple Notification Service (Amazon SNS) topic to send notifications every time a deployment fails. Configure the SNS topic to invoke a new Lambda function that stops the current deployment and starts the most recent successful deployment.

D. Set the deployment configuration in CodeDeploy to LambdaCanary10Percent10Minutes. Configure manual rollbacks on the deployment group. Create a metric filter on an Amazon CloudWatch log group for API Gateway to monitor HTTP Bad Gateway errors. Configure the metric filter to invoke a new Lambda function that stops the current deployment and starts the most recent successful deployment.

**Đáp án**: ___________

---

## Câu 73

**ID**: 201 | **Loại**: Multiple Choice

A company recently deployed its web application on AWS. The company is preparing for a large-scale sales event and must ensure that the web application can scale to meet the demand.The application's frontend infrastructure includes an Amazon CloudFront distribution that has an Amazon S3 bucket as an origin. The backend infrastructure includes an Amazon API Gateway API, several AWS Lambda functions, and an Amazon Aurora DB cluster.The company's DevOps engineer conducts a load test and identifies that the Lambda functions can fulfil the peak number of requests. However, the DevOps engineer notices request latency during the initial burst of requests. Most of the requests to the Lambda functions produce queries to the database. A large portion of the invocation time is used to establish database connections.Which combination of steps will provide the application with the required scalability? (Choose three.)

A. Configure a higher reserved concurrency for the Lambda functions.

B. Configure a higher provisioned concurrency for the Lambda functions.

C. Convert the DB cluster to an Aurora global database. Add additional Aurora Replicas in AWS Regions based on the locations of the company's customers.

D. Refactor the Lambda functions. Move the code blocks that initialize database connections into the function handlers.

E. Use Amazon RDS Proxy to create a proxy for the Aurora database. Update the Lambda functions to use the proxy endpoints for database connections.

**Đáp án**: ___________

---

## Câu 74

**ID**: 202 | **Loại**: Single Choice

A company runs a web application that extends across multiple Availability Zones. The company uses an Application Load Balancer (ALB) for routing, AWS Fargate for the application, and Amazon Aurora for the application data. The company uses AWS CloudFormation templates to deploy the application. The company stores all Docker images in an Amazon Elastic Container Registry (Amazon ECR) repository in the same AWS account and AWS Region.A DevOps engineer needs to establish a disaster recovery (DR) process in another Region. The solution must meet an RPO of 8 hours and an RTO of 2 hours. The company sometimes needs more than 2 hours to build the Docker images from the Dockerfile.Which solution will meet the RTO and RPO requirements MOST cost-effectively?

A. Copy the CloudFormation templates and the Dockerfile to an Amazon S3 bucket in the DR Region. Use AWS Backup to configure automated Aurora cross-Region hourly snapshots. In case of DR, build the most recent Docker image and upload the Docker image to an ECR repository in the DR Region. Use the CloudFormation template that has the most recent Aurora snapshot and the Docker image from the ECR repository to launch a new CloudFormation stack in the DR Region. Update the application DNS records to point to the new ALB.

B. Copy the CloudFormation templates to an Amazon S3 bucket in the DR Region. Configure Aurora automated backup Cross-Region Replication. Configure ECR Cross-Region Replication. In case of DR, use the CloudFormation template with the most recent Aurora snapshot and the Docker image from the local ECR repository to launch a new CloudFormation stack in the DR Region. Update the application DNS records to point to the new ALB.

C. Copy the CloudFormation templates to an Amazon S3 bucket in the DR Region. Use Amazon EventBridge to schedule an AWS Lambda function to take an hourly snapshot of the Aurora database and of the most recent Docker image in the ECR repository. Copy the snapshot and the Docker image to the DR Region. In case of DR, use the CloudFormation template with the most recent Aurora snapshot and the Docker image from the local ECR repository to launch a new CloudFormation stack in the DR Region.

D. Copy the CloudFormation templates to an Amazon S3 bucket in the DR Region. Deploy a second application CloudFormation stack in the DR Region. Reconfigure Aurora to be a global database. Update both CloudFormation stacks when a new application release in the current Region is needed. In case of DR, update the application DNS records to point to the new ALB.

**Đáp án**: ___________

---

## Câu 75

**ID**: 203 | **Loại**: Single Choice

A company's application runs on Amazon EC2 instances. The application writes to a log file that records the username, date, time, and source IP address of the login. The log is published to a log group in Amazon CloudWatch Logs.The company is performing a root cause analysis for an event that occurred on the previous day. The company needs to know the number of logins for a specific user from the past 7 days.Which solution will provide this information?

A. Create a CloudWatch Logs metric filter on the log group. Use a filter pattern that matches the username. Publish a CloudWatch metric that sums the number of logins over the past 7 days.

B. Create a CloudWatch Logs subscription on the log group. Use a filter pattern that matches the username. Publish a CloudWatch metric that sums the number of logins over the past 7 days.

C. Create a CloudWatch Logs Insights query that uses an aggregation function to count the number of logins for the username over the past 7 days. Run the query against the log group.

D. Create a CloudWatch dashboard. Add a number widget that has a filter pattern that counts the number of logins for the username over the past 7 days directly from the log group.

**Đáp án**: ___________

---

## Câu 76

**ID**: 204 | **Loại**: Single Choice

A company has an AWS CodeDeploy application. The application has a deployment group that uses a single tag group to identify instances for the deployment of Application. The single tag group configuration identifies instances that have Environment=Production and Name=ApplicationA tags for the deployment of ApplicationA.The company launches an additional Amazon EC2 instance with Department=Marketing, Environment=Production, and Name=ApplicationB tags. On the next CodeDeploy deployment of Application, the additional instance has ApplicationA installed on it. A DevOps engineer needs to configure the existing deployment group to prevent ApplicationA from being installed on the additional instance.Which solution will meet these requirements?

A. Change the current single tag group to include only the Environment=Production tag. Add another single tag group that includes only the Name=ApplicationA tag.

B. Change the current single tag group to include the Department=Marketing, Environment=production, and Name=ApplicationA tags.

C. Add another single tag group that includes only the Department=Marketing tag. Keep the Environment=Production and Name=ApplicationA tags with the current single tag group.

D. Change the current single tag group to include only the Environment=Production tag. Add another single tag group that includes only the Department=Marketing tag.

**Đáp án**: ___________

---

## Câu 77

**ID**: 205 | **Loại**: Single Choice

A company is launching an application that stores raw data in an Amazon S3 bucket. Three applications need to access the data to generate reports. The data must be redacted differently for each application before the applications can access the data.Which solution will meet these requirements?

A. Create an S3 bucket for each application. Configure S3 Same-Region Replication (SRR) from the raw data's S3 bucket to each application's S3 bucket. Configure each application to consume data from its own S3 bucket.

B. Create an Amazon Kinesis data stream. Create an AWS Lambda function that is invoked by object creation events in the raw data’s S3 bucket. Program the Lambda function to redact data for each application. Publish the data on the Kinesis data stream. Configure each application to consume data from the Kinesis data stream.

C. For each application, create an S3 access point that uses the raw data's S3 bucket as the destination. Create an AWS Lambda function that is invoked by object creation events in the raw data's S3 bucket. Program the Lambda function to redact data for each application. Store the data in each application's S3 access point. Configure each application to consume data from its own S3 access point.

D. Create an S3 access point that uses the raw data’s S3 bucket as the destination. For each application, create an S3 Object Lambda access point that uses the S3 access point. Configure the AWS Lambda function for each S3 Object Lambda access point to redact data when objects are retrieved. Configure each application to consume data from its own S3 Object Lambda access point

**Đáp án**: ___________

---

## Câu 78

**ID**: 206 | **Loại**: Single Choice

A company uses AWS Control Tower and AWS CloudFormation to manage its AWS accounts and to create AWS resources. The company requires all Amazon S3 buckets to be encrypted with AWS Key Management Service (AWS KMS) when the S3 buckets are created in a CloudFormation stack.Which solution will meet this requirement?

A. Use AWS Organizations. Attach an SCP that denies the s3:PutObject permission if the request does not include an x-amz-server-side-encryption header that requests server-side encryption with AWS KMS keys (SSE-KMS).

B. Use AWS Control Tower with a multi-account environment. Configure and enable proactive AWS Control Tower controls on all OUs with CloudFormation hooks.

C. Use AWS Control Tower with a multi-account environment. Configure and enable detective AWS Control Tower controls on all OUs with CloudFormation hooks.

D. Use AWS Organizations. Create an AWS Config organizational rule to check whether a KMS encryption key is enabled for all S3 buckets. Deploy the rule. Create and apply an SCP to prevent users from stopping and deleting AWS Config across all AWS accounts,

**Đáp án**: ___________

---

## Câu 79

**ID**: 207 | **Loại**: Single Choice

A DevOps engineer has developed an AWS Lambda function. The Lambda function starts an AWS CloudFormation drift detection operation on all supported resources for a specific CloudFormation stack. The Lambda function then exits its invocation.The DevOps engineer has created an Amazon EventBridge scheduled rule that invokes the Lambda function every hour. An Amazon Simple Notification Service (Amazon SNS) topic already exists in the AWS account. The DevOps engineer has subscribed to the SNS topic to receive notifications.The DevOps engineer needs to receive a notification as soon as possible when drift is detected in this specific stack configuration.Which solution will meet these requirements?

A. Configure the existing EventBridge rule to also target the SNS topic. Configure an SNS subscription filter policy to match the CloudFormation stack. Attach the subscription filter policy to the SNS topic.

B. Create a second Lambda function to query the CloudFormation API for the drift detection results for the stack. Configure the second Lambda function to publish a message to the SNS topic if drift is detected. Adjust the existing EventBridge rule to also target the second Lambda function.

C. Configure Amazon GuardDuty in the account with drift detection for all CloudFormation stacks. Create a second EventBridge rule that reacts to the GuardDuty drift detection event finding for the specific CloudFormation stack. Configure the SNS topic as a target of the second EventBridge rule.

D. Configure AWS Config in the account. Use the cloudformation-stack-drift-detection-check managed rule. Create a second EventBridge rule that reacts to a compliance change event for the CloudFormation stack. Configure the SNS topic as a target of the second EventBridge rule.

**Đáp án**: ___________

---

## Câu 80

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

## Câu 81

**ID**: 209 | **Loại**: Single Choice

A company's organization in AWS Organizations has a single OU. The company runs Amazon EC2 instances in the OU accounts. The company needs to limit the use of each EC2 instance’s credentials to the specific EC2 instance that the credential is assigned to. A DevOps engineer must configure security for the EC2 instances.Which solution will meet these requirements?

A. Create an SCP that specifies the VPC CIDR block. Configure the SCP to check whether the value of the aws:VpcSourcelp condition key is in the specified block. In the same SCP check, check whether the values of the aws:EC2InstanceSourcePrivatelPv4 and aws:SourceVpc condition keys are the same. Deny access if either condition is false. Apply the SCP to the OU.

B. Create an SCP that checks whether the values of the aws:EC2InstanceSourceVPC and aws:SourceVpc condition keys are the same. Deny access if the values are not the same. In the same SCP check, check whether the values of the aws:EC2InstanceSourcePrivateIPv4 and aws:VpcSourceIp condition keys are the same. Deny access if the values are not the same. Apply the SCP to the OU.

C. Create an SCP that includes a list of acceptable VPC values and checks whether the value of the aws:SourceVpc condition key is in the list. In the same SCP check, define a list of acceptable IP address values and check whether the value of the aws:VpcSourceIp condition key is in the list. Deny access if either condition is false. Apply the SCP to each account in the organization.

D. Create an SCP that checks whether the values of the aws:EC2InstanceSourceVPC and aws:VpcSourceIp condition keys are the same. Deny access if the values are not the same. In the same SCP check, check whether the values of the aws:EC2InstanceSourcePrivateIPv4 and aws:SourceVpc condition keys are the same. Deny access if the values are not the same. Apply the SCP to each account in the organization.

**Đáp án**: ___________

---

## Câu 82

**ID**: 210 | **Loại**: Multiple Choice

A company has a fleet of Amazon EC2 instances that run Linux in a single AWS account. The company is using an AWS Systems Manager Automation task across the EC2 instances.During the most recent patch cycle, several EC2 instances went into an error state because of insufficient available disk space. A DevOps engineer needs to ensure that the EC2 instances have sufficient available disk space during the patching process in the future.Which combination of steps will meet these requirements? (Choose two.)

A. Ensure that the Amazon CloudWatch agent is installed on all EC2 instances.

B. Create a cron job that is installed on each EC2 instance to periodically delete temporary files.

C. Create an Amazon CloudWatch log group for the EC2 instances. Configure a cron job that is installed on each EC2 instance to write the available disk space to a CloudWatch log stream for the relevant EC2 instance.

D. Create an Amazon CloudWatch alarm to monitor available disk space on all EC2 instances. Add the alarm as a safety control to the Systems Manager Automation task.

E. Create an AWS Lambda function to periodically check for sufficient available disk space on all EC2 instances by evaluating each EC2 instance's respective Amazon CloudWatch log stream.

**Đáp án**: ___________

---

## Câu 83

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

## Câu 84

**ID**: 212 | **Loại**: Single Choice

A company has an AWS CloudFormation stack that is deployed in a single AWS account. The company has configured the stack to send event notifications to an Amazon Simple Notification Service (Amazon SNS) topic.A DevOps engineer must implement an automated solution that applies a tag to the specific CloudFormation stack instance only after a successful stack update occurs. The DevOps engineer has created an AWS Lambda function that applies and updates this tag for the specific stack instance.Which solution will meet these requirements?

A. Run the AWS-UpdateCloudFormationStack AWS Systems ManagerAutomation runbook when Systems Manager detects an UPDATE_COMPLETE event for the instance status of the CloudFormation stack. Configure the runbook to invoke the Lambda function.

B. Create a custom AWS Config rule that produces a compliance change event if the CloudFormation stack has an UPDATE_COMPLETE instance status. Configure AWS Config to directly invoke the Lambda function to automatically remediate the change event.

C. Create an Amazon EventBridge rule that matches the UPDATE_COMPLETE event pattern for the instance status of the CloudFormation stack. Configure the rule to invoke the Lambda function.

D. Adjust the configuration of the CloudFormation stack to send notifications for only an UPDATE_COMPLETE instance status event to the SNS topic. Subscribe the Lambda function to the SNS topic.

**Đáp án**: ___________

---

## Câu 85

**ID**: 213 | **Loại**: Single Choice

A company deploys an application to two AWS Regions. The application creates and stores objects in an Amazon S3 bucket that is in the same Region as the application. Both deployments of the application need to have access to all the objects and their metadata from both Regions. The company has configured two-way replication between the S3 buckets and has enabled S3 Replication metrics on each S3 bucket.A DevOps engineer needs to implement a solution that retries the replication process if an object fails to replicate.Which solution will meet these requirements?

A. Create an Amazon EventBridge rule that listens to S3 event notifications for failed replication events. Create an AWS Lambda function that downloads the failed replication object and then runs a PutObject command for the object to the destination bucket. Configure the EventBridge rule to invoke the Lambda function to handle the object that failed to replicate.

B. Create an Amazon Simple Queue Service (Amazon SQS) queue. Configure S3 event notifications to send failed replication notifications to the SQS queue. Create an AWS Lambda function that downloads the failed replication object and then runs a PutObject command for the object to the destination bucket. Configure the Lambda function to poll the queue for notifications to process.

C. Create an Amazon EventBridge rule that listens to S3 event notifications for failed replications. Create an AWS Lambda function that downloads the failed replication object and then runs a PutObject command for the object to the destination bucket.

D. Create an AWS Lambda function that will use S3 batch operations to retry the replication on the existing object for a failed replication. Configure S3 event notifications to send failed replication notifications to the Lambda function.

**Đáp án**: ___________

---

## Câu 86

**ID**: 214 | **Loại**: Single Choice

A company needs to implement failover for its application. The application includes an Amazon CloudFront distribution and a public Application Load Balancer (ALB) in an AWS Region. The company has configured the ALB as the default origin for the distribution.After some recent application outages, the company wants a zero-second RTO. The company deploys the application to a secondary Region in a warm standby configuration. A DevOps engineer needs to automate the failover of the application to the secondary Region so that HTTP GET requests meet the desired RTO.Which solution will meet these requirements?

A. Create a second CloudFront distribution that has the secondary ALB as the default origin. Create Amazon Route 53 alias records that have a failover policy and Evaluate Target Health set to Yes for both CloudFront distributions. Update the application to use the new record set.

B. Create a new origin on the distribution for the secondary ALCreate a new origin group. Set the original ALB as the primary origin. Configure the origin group to fail over for HTTP 5xx status codes. Update the default behavior to use the origin group.

C. Create Amazon Route 53 alias records that have a failover policy and Evaluate Target Health set to Yes for both ALBs. Set the TTL of both records to 0. Update the distribution's origin to use the new record set.

D. Create a CloudFront function that detects HTTP 5xx status codes. Configure the function to return a 307 Temporary Redirect error response to the secondary ALB if the function detects 5xx status codes. Update the distribution's default behavior to send origin responses to the function.

**Đáp án**: ___________

---

## Câu 87

**ID**: 215 | **Loại**: Single Choice

A cloud team uses AWS Organizations and AWS IAM Identity Center (AWS Single Sign-On) to manage a company's AWS accounts. The company recently established a research team. The research team requires the ability to fully manage the resources in its account. The research team must not be able to create IAM users.The cloud team creates a Research Administrator permission set in IAM Identity Center for the research team. The permission set has the AdministratorAccess AWS managed policy attached. The cloud team must ensure that no one on the research team can create IAM users.Which solution will meet these requirements?

A. Create an IAM policy that denies the iam:CreateUser action. Attach the IAM policy to the Research Administrator permission set.

B. Create an IAM policy that allows all actions except the iam:CreateUser action. Use the IAM policy to set the permissions boundary for the Research Administrator permission set.

C. Create an SCP that denies the iam:CreateUser action. Attach the SCP to the research team's AWS account.

D. Create an AWS Lambda function that deletes IAM users. Create an Amazon EventBridge rule that detects the IAM CreateUser event. Configure the rule to invoke the Lambda function.

**Đáp án**: ___________

---

## Câu 88

**ID**: 216 | **Loại**: Single Choice

A company releases a new application in a new AWS account. The application includes an AWS Lambda function that processes messages from an Amazon Simple Queue Service (Amazon SQS) standard queue. The Lambda function stores the results in an Amazon S3 bucket for further downstream processing. The Lambda function needs to process the messages within a specific period of time after the messages are published. The Lambda function has a batch size of 10 messages and takes a few seconds to process a batch of messages.As load increases on the application's first day of service, messages in the queue accumulate at a greater rate than the Lambda function can process the messages. Some messages miss the required processing timelines. The logs show that many messages in the queue have data that is not valid. The company needs to meet the timeline requirements for messages that have valid data.Which solution will meet these requirements?

A. Increase the Lambda function's batch size. Change the SQS standard queue to an SQS FIFO queue. Request a Lambda concurrency increase in the AWS Region.

B. Reduce the Lambda function's batch size. Increase the SQS message throughput quota. Request a Lambda concurrency increase in the AWS Region.

C. Increase the Lambda function's batch size. Configure S3 Transfer Acceleration on the S3 bucket. Configure an SQS dead-letter queue.

D. Keep the Lambda function's batch size the same. Configure the Lambda function to report failed batch items. Configure an SQS dead-letter queue.

**Đáp án**: ___________

---

## Câu 89

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

## Câu 90

**ID**: 218 | **Loại**: Single Choice

A company operates sensitive workloads across the AWS accounts that are in the company's organization in AWS Organizations. The company uses an IP address range to delegate IP addresses for Amazon VPC CIDR blocks and all non-cloud hardware.The company needs a solution that prevents principals that are outside the company’s IP address range from performing AWS actions in the organization's accounts.Which solution will meet these requirements?

A. Configure AWS Firewall Manager for the organization. Create an AWS Network Firewall policy that allows only source traffic from the company's IP address range. Set the policy scope to all accounts in the organization.

B. In Organizations, create an SCP that denies source IP addresses that are outside of the company’s IP address range. Attach the SCP to the organization's root.

C. Configure Amazon GuardDuty for the organization. Create a GuardDuty trusted IP address list for the company's IP range. Activate the trusted IP list for the organization.

D. In Organizations, create an SCP that allows source IP addresses that are inside of the company’s IP address range. Attach the SCP to the organization's root.

**Đáp án**: ___________

---

## Câu 91

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

## Câu 92

**ID**: 220 | **Loại**: Multiple Choice

A company uses an organization in AWS Organizations to manage multiple AWS accounts. The company needs an automated process across all AWS accounts to isolate any compromised Amazon EC2 instances when the instances receive a specific tag.Which combination of steps will meet these requirements? (Choose two.)

A. Use AWS CloudFormation StackSets to deploy the CloudFormation stacks in all AWS accounts.

B. Create an SCP that has a Deny statement for the ec2:* action with a condition of "aws:RequestTag/isolation": false.

C. Attach the SCP to the root of the organization.

D. Create an AWS CloudFormation template that creates an EC2 instance role that has no IAM policies attached. Configure the template to have a security group that has an explicit Deny rule on all traffic. Use the CloudFormation template to create an AWS Lambda function that attaches the IAM role to instances. Configure the Lambda function to add a network ACL. Set up an Amazon EventBridge rule to invoke the Lambda function when a specific tag is applied to a compromised EC2 instance.

E. Create an AWS CloudFormation template that creates an EC2 instance role that has no IAM policies attached. Configure the template to have a security group that has no inbound rules or outbound rules. Use the CloudFormation template to create an AWS Lambda function that attaches the IAM role to instances. Configure the Lambda function to replace any existing security groups with the new security group. Set up an Amazon EventBridge rule to invoke the Lambda function when a specific tag is applied to a compromised EC2 instance.

**Đáp án**: ___________

---

## Câu 93

**ID**: 221 | **Loại**: Single Choice

A company manages multiple AWS accounts by using AWS Organizations with OUs for the different business divisions. The company is updating their corporate network to use new IP address ranges. The company has 10 Amazon S3 buckets in different AWS accounts. The S3 buckets store reports for the different divisions. The S3 bucket configurations allow only private corporate network IP addresses to access the S3 buckets.A DevOps engineer needs to change the range of IP addresses that have permission to access the contents of the S3 buckets. The DevOps engineer also needs to revoke the permissions of two OUs in the company.Which solution will meet these requirements?

A. Create a new SCP that has two statements, one that allows access to the new range of IP addresses for all the S3 buckets and one that denies access to the old range of IP addresses for all the S3 buckets. Set a permissions boundary for the OrganizationAccountAccessRole role in the two OUs to deny access to the S3 buckets.

B. Create a new SCP that has a statement that allows only the new range of IP addresses to access the S3 buckets. Create another SCP that denies access to the S3 buckets. Attach the second SCP to the two OUs.

C. On all the S3 buckets, configure resource-based policies that allow only the new range of IP addresses to access the S3 buckets. Create a new SCP that denies access to the S3 buckets. Attach the SCP to the two OUs.

D. On all the S3 buckets, configure resource-based policies that allow only the new range of IP addresses to access the S3 buckets. Set a permissions boundary for the OrganizationAccountAccessRole role in the two OUs to deny access to the S3 buckets.

**Đáp án**: ___________

---

## Câu 94

**ID**: 222 | **Loại**: Single Choice

A company has started using AWS across several teams. Each team has multiple accounts and unique security profiles. The company manages the accounts in an organization in AWS Organizations. Each account has its own configuration and security controls.The company's DevOps team wants to use preventive and detective controls to govern all accounts. The DevOps team needs to ensure the security of accounts now and in the future as the company creates new accounts in the organization.Which solution will meet these requirements?

A. Use Organizations to create OUs that have appropriate SCPs attached for each team. Place team accounts in the appropriate OUs to apply security controls. Create any new team accounts in the appropriate OUs.

B. Create an AWS Control Tower landing zone. Configure OUs and appropriate controls in AWS Control Tower for the existing teams. Configure trusted access for AWS Control Tower. Enroll the existing accounts in the appropriate OUs that match the appropriate security policies for each team. Use AWS Control Tower to provision any new accounts.

C. Create AWS CloudFormation stack sets in the organization's management account. Configure a stack set that deploys AWS Config with configuration rules and remediation actions for all controls to each account in the organization. Update the stack sets to deploy to new accounts as the accounts are created.

D. Configure AWS Config to manage the AWS Config rules across all AWS accounts in the organization. Deploy conformance packs that provide AWS Config rules and remediation actions across the organization.

**Đáp án**: ___________

---

## Câu 95

**ID**: 223 | **Loại**: Single Choice

A company uses an AWS CodeCommit repository to store its source code and corresponding unit tests. The company has configured an AWS CodePipeline pipeline that includes an AWS CodeBuild project that runs when code is merged to the main branch of the repository.The company wants the CodeBuild project to run the unit tests. If the unit tests pass, the CodeBuild project must tag the most recent commit.How should the company configure the CodeBuild project to meet these requirements?

A. Configure the CodeBuild project to use native Git to done the CodeCommit repository. Configure the project to run the unit tests. Configure the project to use native Git to create a tag and to push the Git tag to the repository if the code passes the unit tests.

B. Configure the CodeBuild projed to use native Git to done the CodeCommit repository. Configure the project to run the unit tests. Configure the project to use AWS CLI commands to create a new repository tag in the repository if the code passes the unit tests.

C. Configure the CodeBuild project to use AWS CLI commands to copy the code from the CodeCommit repository. Configure the project to run the unit tests. Configure the project to use AWS CLI commands to create a new Git tag in the repository if the code passes the unit tests.

D. Configure the CodeBuild project to use AWS CLI commands to copy the code from the CodeCommit repository. Configure the project to run the unit tests. Configure the project to use AWS CLI commands to create a new repository tag in the repository if the code passes the unit tests.

**Đáp án**: ___________

---

## Câu 96

**ID**: 224 | **Loại**: Single Choice

A DevOps engineer manages a company's Amazon Elastic Container Service (Amazon ECS) cluster. The cluster runs on several Amazon EC2 instances that are in an Auto Scaling group. The DevOps engineer must implement a solution that logs and reviews all stopped tasks for errors.Which solution will meet these requirements?

A. Create an Amazon EventBridge rule to capture task state changes. Send the event to Amazon CloudWatch Logs. Use CloudWatch Logs Insights to investigate stopped tasks.

B. Configure tasks to write log data in the embedded metric format. Store the logs in Amazon CloudWatch Logs. Monitor the ContainerInstanceCount metric for changes.

C. Configure the EC2 instances to store logs in Amazon CloudWatch Logs. Create a CloudWatch Contributor Insights rule that uses the EC2 instance log data. Use the Contributor Insights rule to investigate stopped tasks.

D. Configure an EC2 Auto Scaling lifecycle hook for the EC2_INSTANCE_TERMINATING scale-in event. Write the SystemEventLog file to Amazon S3. Use Amazon Athena to query the log file for errors.

**Đáp án**: ___________

---

## Câu 97

**ID**: 225 | **Loại**: Multiple Choice

A company wants to deploy a workload on several hundred Amazon EC2 instances. The company will provision the EC2 instances in an Auto Scaling group by using a launch template.The workload will pull files from an Amazon S3 bucket, process the data, and put the results into a different S3 bucket. The EC2 instances must have least-privilege permissions and must use temporary security credentials.Which combination of steps will meet these requirements? (Choose two.)

A. Create an IAM role that has the appropriate permissions for S3 buckets Add the IAM role to an instance profile.

B. Update the launch template to include the IAM instance profile.

C. Create an IAM user that has the appropriate permissions for Amazon S3 Generate a secret key and token.

D. Create a trust anchor and profile Attach the IAM role to the profile.

E. Update the launch template Modify the user data to use the new secret key and token.

**Đáp án**: ___________

---

## Câu 98

**ID**: 226 | **Loại**: Single Choice

A company is using AWS CodeDeploy to automate software deployment. The deployment must meet these requirements:• A number of instances must be available to serve traffic during the deployment. Traffic must be balanced across those instances, and the instances must automatically heal in the event of failure. • A new fleet of instances must be launched for deploying a new revision automatically, with no manual provisioning.• Traffic must be rerouted to the new environment to half of the new instances at a time. The deployment should succeed if traffic is rerouted to at least half of the instances: otherwise, it should fail.• Before routing traffic to the new fleet of instances, the temporary files generated during the deployment process must be deleted.• At the end of a successful deployment, the original instances in the deployment group must be deleted immediately to reduce costs.How can a DevOps engineer meet these requirements?

A. Use an Application Load Balancer and an in-place deployment. Associate the Auto Scaling group with the deployment group. Use the Automatically copy Auto Scaling group option, and use CodeDeployDefault.OneAtAtime as the deployment configuration. Instruct AWS CodeDeploy to terminate the original instances in the deployment group, and use the AllowTraffic hook within appspec.yml to delete the temporary files.

B. Use an Application Load Balancer and a blue/green deployment. Associate the Auto Scaling group and Application Load Balancer target group with the deployment group. Use the Automatically copy Auto Scaling group option, create a custom deployment configuration with minimum healthy hosts defined as 50%, and assign the configuration to the deployment group. Instruct AWS CodeDeploy to terminate the original instances in the deployment group, and use the BeforeBlockTraffic hook within appspec.yml to delete the temporary files.

C. Use an Application Load Balancer and a blue/green deployment. Associate the Auto Scaling group and the Application Load Balancer target group with the deployment group. Use the Automatically copy Auto Scaling group option, and use CodeDeployDefault.HalfAtAtime as the deployment configuration. Instruct AWS CodeDeploy to terminate the original instances in the deployment group, and use the BeforeAllowTraffic hook within appspec.yml to delete the temporary files.

D. Use an Application Load Balancer and an in-place deployment. Associate the Auto Scaling group and Application Load Balancer target group with the deployment group. Use the Automatically copy Auto Scaling group option, and use CodeDeployDefault.AllatOnce as a deployment configuration. Instruct AWS CodeDeploy to terminate the original instances in the deployment group, and use the BlockTraffic hook within appspec.yml to delete the temporary files.

**Đáp án**: ___________

---

## Câu 99

**ID**: 227 | **Loại**: Single Choice

A company needs to adopt a multi-account strategy to deploy its applications and the associated CI/CD infrastructure. The company has created an organization in AWS Organizations that has all features enabled. The company has configured AWS Control Tower and has set up a landing zone.The company needs to use AWS Control Tower controls (guardrails) in all AWS accounts in the organization. The company must create the accounts for a multi-environment application and must ensure that all accounts are configured to an initial baseline.Which solution will meet these requirements with the LEAST operational overhead?

A. Create an AWS Control Tower Account Factory Customization (AFC) blueprint that uses the baseline configuration. Use AWS Control Tower Account Factory to provision a dedicated AWS account for each environment and a CI/CD account by using the blueprint.

B. Use AWS Control Tower Account Factory to provision a dedicated AWS account for each environment and a CI/CD account. Use AWS CloudFormation StackSets to apply the baseline configuration to the new accounts.

C. Use Organizations to provision a multi-environment AWS account and a CI/CD account. In the Organizations management account, create an AWS Lambda function that assumes the Organizations access role to apply the baseline configuration to the new accounts.

D. Use Organizations to provision a dedicated AWS account for each environment, an audit account, and a CI/CD account. Use AWS CloudFormation StackSets to apply the baseline configuration to the new accounts.

**Đáp án**: ___________

---

## Câu 100

**ID**: 228 | **Loại**: Single Choice

A DevOps team has created a Custom Lambda rule in AWS Config. The rule monitors Amazon Elastic Container Repository (Amazon ECR) policy statements for ecr:* actions. When a noncompliant repository is detected, Amazon EventBridge uses Amazon Simple Notification Service (Amazon SNS) to route the notification to a security team.When the custom AWS Config rule is evaluated, the AWS Lambda function fails to run.Which solution will resolve the issue?

A. Modify the Lambda function's resource policy to grant AWS Config permission to invoke the function.

B. Modify the SNS topic policy to include configuration changes for EventBridge to publish to the SNS topic.

C. Modify the Lambda function's execution role to include configuration changes for custom AWS Config rules.

D. Modify all the ECR repository policies to grant AWS Config access to the necessary ECR API actions.

**Đáp án**: ___________

---

## Câu 101

**ID**: 229 | **Loại**: Single Choice

A developer is creating a proof of concept for a new software as a service (SaaS) application. The application is in a shared development AWS account that is part of an organization in AWS Organizations.The developer needs to create service-linked IAM roles for the AWS services that are being considered for the proof of concept. The solution needs to give the developer the ability to create and configure the service-linked roles only.Which solution will meet these requirements?

A. Create an IAM user for the developer in the organization's management account. Configure a cross-account role in the development account for the developer to use. Limit the scope of the cross-account role to common services.

B. Add the developer to an IAM group. Attach the PowerUserAccess managed policy to the IAM group. Enforce multi-factor authentication (MFA) on the user account.

C. Add an SCP to the development account in Organizations. Configure the SCP with a Deny rule for iam:* to limit the developer's access.

D. Create an IAM role that has the necessary IAM access to allow the developer to create policies and roles. Create and attach a permissions boundary to the role. Grant the developer access to assume the role.

**Đáp án**: ___________

---

## Câu 102

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

## Câu 103

**ID**: 231 | **Loại**: Multiple Choice

A company uses AWS Organizations to manage its AWS accounts. A DevOps engineer must ensure that all users who access the AWS Management Console are authenticated through the company’s corporate identity provider (IdP).Which combination of steps will meet these requirements? (Choose two.)

A. Use Amazon GuardDuty with a delegated administrator account Use GuardDuty to enforce denial of IAM user logins.

B. Use AWS IAM Identity Center to configure identity federation with SAML 2.0.

C. Create a permissions boundary in AWS IAM Identity Center to deny password logins for IAM users.

D. Create IAM groups in the Organizations management account to apply consistent permissions for all IAM users.

E. Create an SCP in Organizations to deny password creation for IAM users.

**Đáp án**: ___________

---

## Câu 104

**ID**: 232 | **Loại**: Multiple Choice

A company has deployed a new platform that runs on Amazon Elastic Kubernetes Service (Amazon EKS). The new platform hosts web applications that users frequently update. The application developers build the Docker images for the applications and deploy the Docker images manually to the platform.The platform usage has increased to more than 500 users every day. Frequent updates, building the updated Docker images for the applications, and deploying the Docker images on the platform manually have all become difficult to manage.The company needs to receive an Amazon Simple Notification Service (Amazon SNS) notification if Docker image scanning returns any HIGH or CRITICAL findings for operating system or programming language package vulnerabilities.Which combination of steps will meet these requirements? (Choose two.)

A. Create an AWS CodeCommit repository to store the Dockerfile and Kubernetes deployment files. Create a pipeline in AWS CodePipeline. Use an Amazon S3 event to invoke the pipeline when a newer version of the Dockerfile is committed. Add a step to the pipeline to initiate the AWS CodeBuild project.

B. Create an AWS CodeCommit repository to store the Dockerfile and Kubernetes deployment files. Create a pipeline in AWS CodePipeline. Use an Amazon EventBridge event to invoke the pipeline when a newer version of the Dockerfile is committed. Add a step to the pipeline to initiate the AWS CodeBuild project.

C. Create an AWS CodeBuild project that builds the Docker images and stores the Docker images in an Amazon Elastic Container Registry (Amazon ECR) repository. Turn on basic scanning for the ECR repository. Create an Amazon EventBridge rule that monitors Amazon GuardDuty events. Configure the EventBridge rule to send an event to an SNS topic when the finding-severity-counts parameter is more than 0 at a CRITICAL or HIGH level.

D. Create an AWS CodeBuild project that builds the Docker images and stores the Docker images in an Amazon Elastic Container Registry (Amazon ECR) repository. Turn on enhanced scanning for the ECR repository. Create an Amazon EventBridge rule that monitors ECR image scan events. Configure the EventBridge rule to send an event to an SNS topic when the finding-severity-counts parameter is more than 0 at a CRITICAL or HIGH level.

E. Create an AWS CodeBuild project that scans the Dockerfile. Configure the project to build the Docker images and store the Docker images in an Amazon Elastic Container Registry (Amazon ECR) repository if the scan is successful. Configure an SNS topic to provide notification if the scan returns any vulnerabilities.

**Đáp án**: ___________

---

## Câu 105

**ID**: 233 | **Loại**: Multiple Choice

A company groups its AWS accounts in OUs in an organization in AWS Organizations. The company has deployed a set of Amazon API Gateway APIs in one of the Organizations accounts. The APIs are bound to the account's VPC and have no existing authentication mechanism. Only principals in a specific OU can have permissions to invoke the APIs.The company applies the following policy to the API Gateway interface VPC endpoint:The company also updates the API Gateway resource policies to deny invocations that do not come through the interface VPC endpoint. After the updates, the following error message appears during attempts to use the interface VPC endpoint URL to invoke an API: "User: anonymous is not authorized."Which combination of steps will solve this problem? (Choose two.)

A. Enable IAM authentication on all API methods by setting AWS JAM as the authorization method.

B. Create a token-based AWS Lambda authorizer that passes the caller's identity in a bearer token.

C. Create a request parameter-based AWS Lambda authorizer that passes the caller's identity in a combination of headers, query string parameters, stage variables, and $cortext variables.

D. Use Amazon Cognito user pools as the authorizer to control access to the API.

E. Verify the identity of the requester by using Signature Version 4 to sign client requests by using AWS credentials.

**Đáp án**: ___________

---

## Câu 106

**ID**: 234 | **Loại**: Single Choice

A company wants to decrease the time it takes to develop new features. The company uses AWS CodeBuild and AWS CodeDeploy to build and deploy its applications. The company uses AWS CodePipeline to deploy each microservice with its own CI/CD pipeline.The company needs more visibility into the average time between the release of new features and the average time to recover after a failed deployment.Which solution will provide this visibility with the LEAST configuration effort?

A. Program an AWS Lambda function that creates Amazon CloudWatch custom metrics with information about successful runs and failed runs for each pipeline. Create an Amazon EventBridge rule to invoke the Lambda function every 5 minutes. Use the metrics to build a CloudWatch dashboard.

B. Program an AWS Lambda function that creates Amazon CloudWatch custom metrics with information about successful runs and failed runs for each pipeline. Create an Amazon EventBridge rule to invoke the Lambda function after every successful run and after every failed run. Use the metrics to build a CloudWatch dashboard.

C. Program an AWS Lambda function that writes information about successful runs and failed runs to Amazon DynamoDB. Create an Amazon EventBridge rule to invoke the Lambda function after every successful run and after every failed run. Build an Amazon QuickSight dashboard to show the information from DynamoDB.

D. Program an AWS Lambda function that writes information about successful runs and failed runs to Amazon DynamoDB. Create an Amazon EventBridge rule to invoke the Lambda function every 5 minutes. Build an Amazon QuickSight dashboard to show the information from DynamoDB.

**Đáp án**: ___________

---

## Câu 107

**ID**: 235 | **Loại**: Single Choice

A company has developed a static website hosted on an Amazon S3 bucket. The website is deployed using AWS CloudFormation. The CloudFormation template defines an S3 bucket and a custom resource that copies content into the bucket from a source location.The company has decided that it needs to move the website to a new location, so the existing CloudFormation stack must be deleted and re-created. However, CloudFormation reports that the stack could not be deleted cleanly.What is the MOST likely cause and how can the DevOps engineer mitigate this problem for this and future versions of the website?

A. Deletion has failed because the S3 bucket has an active website configuration. Modify the CloudFormation template to remove the WebsiteConfiguration property from the S3 bucket resource.

B. Deletion has failed because the S3 bucket is not empty. Modify the custom resource's AWS Lambda function code to recursively empty the bucket when RequestType is Delete.

C. Deletion has failed because the custom resource does not define a deletion policy. Add a DeletionPolicy property to the custom resource definition with a value of RemoveOnDeletion.

D. Deletion has failed because the S3 bucket is not empty. Modify the S3 bucket resource in the CloudFormation template to add a DeletionPolicy property with a value of Empty.

**Đáp án**: ___________

---

## Câu 108

**ID**: 236 | **Loại**: Single Choice

A company uses Amazon EC2 as its primary compute platform. A DevOps team wants to audit the company's EC2 instances to check whether any prohibited applications have been installed on the EC2 instances.Which solution will meet these requirements with the MOST operational efficiency?

A. Configure AWS Systems Manager on each instance. Use AWS Systems Manager Inventory. Use Systems Manager resource data sync to synchronize and store findings in an Amazon S3 bucket. Create an AWS Lambda function that runs when new objects are added to the S3 bucket. Configure the Lambda function to identify prohibited applications.

B. Configure AWS Systems Manager on each instance. Use Systems Manager Inventory Create AWS Config rules that monitor changes from Systems Manager Inventory to identify prohibited applications.

C. Configure AWS Systems Manager on each instance. Use Systems Manager Inventory. Filter a trail in AWS CloudTrail for Systems Manager Inventory events to identify prohibited applications.

D. Designate Amazon CloudWatch Logs as the log destination for all application instances. Run an automated script across all instances to create an inventory of installed applications. Configure the script to forward the results to CloudWatch Logs. Create a CloudWatch alarm that uses filter patterns to search log data to identify prohibited applications.

**Đáp án**: ___________

---

## Câu 109

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

## Câu 110

**ID**: 238 | **Loại**: Multiple Choice

A company is migrating its container-based workloads to an AWS Organizations multi-account environment. The environment consists of application workload accounts that the company uses to deploy and run the containerized workloads. The company has also provisioned a shared services account for shared workloads in the organization.The company must follow strict compliance regulations. All container images must receive security scanning before they are deployed to any environment. Images can be consumed by downstream deployment mechanisms after the images pass a scan with no critical vulnerabilities. Pre-scan and post-scan images must be isolated from one another so that a deployment can never use pre-scan images.A DevOps engineer needs to create a strategy to centralize this process.Which combination of steps will meet these requirements with the LEAST administrative overhead? (Choose two.)

A. Create Amazon Elastic Container Registry (Amazon ECR) repositories in the shared services account: one repository for each pre-scan image and one repository for each post-scan image. Configure Amazon ECR image scanning to run on new image pushes to the pre-scan repositories. Use resource-based policies to grant the organization write access to the pre-scan repositories and read access to the post-scan repositories.

B. Create pre-scan Amazon Elastic Container Registry (Amazon ECR) repositories in each account that publishes container images. Create repositories for post-scan images in the shared services account. Configure Amazon ECR image scanning to run on new image pushes to the pre-scan repositories. Use resource-based policies to grant the organization read access to the post-scan repositories.

C. Configure image replication for each image from the image's pre-scan repository to the image's post-scan repository.

D. Create a pipeline in AWS CodePipeline for each pre-scan repository. Create a source stage that runs when new images are pushed to the pre-scan repositories. Create a stage that uses AWS CodeBuild as the action provider. Write a buildspec.yaml definition that determines the image scanning status and pushes images without critical vulnerabilities to the post-scan repositories.

E. Create an AWS Lambda function. Create an Amazon EventBridge rule that reacts to image scanning completed events and invokes the Lambda function. Write function code that determines the image scanning status and pushes images without critical vulnerabilities to the post-scan repositories.

**Đáp án**: ___________

---

## Câu 111

**ID**: 239 | **Loại**: Single Choice

A company uses an Amazon Elastic Kubernetes Service (Amazon EKS) cluster to deploy its web applications on containers. The web applications contain confidential data that cannot be decrypted without specific credentials.A DevOps engineer has stored the credentials in AWS Secrets Manager. The secrets are encrypted by an AWS Key Management Service (AWS KMS) customer managed key. A Kubernetes service account for a third-party tool makes the secrets available to the applications. The service account assumes an IAM role that the company created to access the secrets.The service account receives an Access Denied (403 Forbidden) error while trying to retrieve the secrets from Secrets Manager.What is the root cause of this issue?

A. The IAM role that is attached to the EKS cluster does not have access to retrieve the secrets from Secrets Manager.

B. The key policy for the customer managed key does not allow the Kubernetes service account IAM role to use the key.

C. The key policy for the customer managed key does not allow the EKS cluster IAM role to use the key.

D. The IAM role that is assumed by the Kubernetes service account does not have permission to access the EKS cluster.

**Đáp án**: ___________

---

## Câu 112

**ID**: 240 | **Loại**: Single Choice

A company is migrating its product development teams from an on-premises data center to a hybrid environment. The new environment will add four AWS Regions and will give the developers the ability to use the Region that is geographically closest to them.All the development teams use a shared set of Linux applications. The on-premises data center stores the applications on a NetApp ONTAP storage device. The storage volume is mounted read-only on the development on-premises VMs. The company updates the applications on the shared volume once a week.A DevOps engineer needs to replicate the data to all the new Regions. The DevOps engineer must ensure that the data is always up to date with deduplication. The data also must not be dependent on the availability of the on-premises storage device.Which solution will meet these requirements?

A. Create an Amazon S3 File Gateway in the on-premises data center. Create S3 buckets in each Region. Set up a cron job to copy the data from the storage device to the S3 File Gateway. Set up S3 Cross-Region Replication (CRR) to the S3 buckets in each Region.

B. Create an Amazon FSx File Gateway in one Region. Create file servers in Amazon FSx for Windows File Server in each Region. Set up a cron job to copy the data from the storage device to the FSx File Gateway.

C. Create Multi-AZ Amazon FSx for NetApp ONTAP instances and volumes in each Region. Configure a scheduled SnapMirror relationship between the on-premises storage device and the FSx for ONTAP instances.

D. Create an Amazon Elastic File System (Amazon EFS) file system in each Region. Deploy an AWS DataSync agent in the on-premises data center. Configure a schedule for DataSync to copy the data to Amazon EFS daily.

**Đáp án**: ___________

---

## Câu 113

**ID**: 241 | **Loại**: Multiple Choice

A company has an application that stores data that includes personally identifiable information (PII) in an Amazon S3 bucket. All data is encrypted with AWS Key Management Service (AWS KMS) customer managed keys. All AWS resources are deployed from an AWS CloudFormation template.A DevOps engineer needs to set up a development environment for the application in a different AWS account. The data in the development environment's S3 bucket needs to be updated once a week from the production environment's S3 bucket.The company must not move PII from the production environment without anonymizing the PII first. The data in each environment must be encrypted with different KMS customer managed keys.Which combination of steps should the DevOps engineer take to meet these requirements? (Choose two.)

A. Activate Amazon Macie on the S3 bucket in the production account. Create an AWS Step Functions state machine to initiate a discovery job and redact all PII before copying files to the S3 bucket in the development account. Give the state machine tasks decrypt permissions on the KMS key in the production account. Give the state machine tasks encrypt permissions on the KMS key in the development account.

B. Set up S3 replication between the production S3 bucket and the development S3 bucket. Activate Amazon Macie on the development S3 bucket. Create an AWS Step Functions state machine to initiate a discovery job and redact all PII as the files are copied to the development S3 bucket. Give the state machine tasks encrypt and decrypt permissions on the KMS key in the development account.

C. Set up an S3 Batch Operations job to copy files from the production S3 bucket to the development S3 bucket. In the development account, configure an AWS Lambda function to redact ail PII. Configure S3 Object Lambda to use the Lambda function for S3 GET requests. Give the Lambda function's IAM role encrypt and decrypt permissions on the KMS key in the development account.

D. Create a development environment from the CloudFormation template in the development account. Schedule an Amazon EventBridge rule to start the AWS Step Functions state machine once a week.

E. Create a development environment from the CloudFormation template in the development account. Schedule a cron job on an Amazon EC2 instance to run once a week to start the S3 Batch Operations job.

**Đáp án**: ___________

---

## Câu 114

**ID**: 242 | **Loại**: Single Choice

A company uses an Amazon Elastic Kubernetes Service (Amazon EKS) cluster to host its machine learning (ML) application. As the ML model and the container image size grow, the time that new pods take to start up has increased to several minutes.A DevOps engineer needs to reduce the startup time to seconds. The solution must also reduce the startup time to seconds when the pod runs on nodes that were recently added to the cluster.The DevOps engineer creates an Amazon EventBridge rule that invokes an automation in AWS Systems Manager. The automation prefetches the container images from an Amazon Elastic Container Registry (Amazon ECR) repository when new images are pushed to the repository. The DevOps engineer also configures tags to be applied to the cluster and the node groups.What should the DevOps engineer do next to meet the requirements?

A. Create an IAM role that has a policy that allows EventBridge to use Systems Manager to run commands in the EKS cluster's control plane nodes. Create a Systems Manager State Manager association that uses the control plane nodes' tags to prefetch corresponding container images.

B. Create an IAM role that has a policy that allows EventBridge to use Systems Manager to run commands in the EKS cluster's nodes. Create a Systems Manager State Manager association that uses the nodes' machine size to prefetch corresponding container images.

C. Create an IAM role that has a policy that allows EventBridge to use Systems Manager to run commands in the EKS cluster's nodes. Create a Systems Manager State Manager association that uses the nodes' tags to prefetch corresponding container images.

D. Create an IAM role that has a policy that allows EventBridge to use Systems Manager to run commands in the EKS cluster's control plane nodes. Create a Systems Manager State Manager association that uses the nodes' tags to prefetch corresponding container images.

**Đáp án**: ___________

---

## Câu 115

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

## Câu 116

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

## Câu 117

**ID**: 245 | **Loại**: Multiple Choice

A company deploys an application on on-premises devices in the company’s on-premises data center. The company uses an AWS Direct Connect connection between the data center and the company's AWS account. During initial setup of the on-premises devices and during application updates, the application needs to retrieve configuration files from an Amazon Elastic File System (Amazon EFS) file system.All traffic from the on-premises devices to Amazon EFS must remain private and encrypted. The on-premises devices must follow the principle of least privilege for AWS access. The company's DevOps team needs the ability to revoke access from a single device without affecting the access of the other devices.Which combination of steps will meet these requirements? (Choose two.)

A. Create an IAM user that has an access key and a secret key for each device. Attach the AmazonElasticFileSystemFullAccess policy to all IAM users. Configure the AWS CLI on the on-premises devices to use the IAM user's access key and secret key.

B. Generate certificates for each on-premises device in AWS Private Certificate Authority. Create a trust anchor in IAM Roles Anywhere that references an AWS Private CA. Create an IAM role that trust IAM Roles Anywhere. Attach the AmazonElasticFileSystemClientReadWriteAccess to the role. Create an IAM Roles Anywhere profile for the IAM role. Configure the AWS CLI on the on-premises devices to use the aws_signing_helper command to obtain credentials.

C. Create an IAM user that has an access key and a secret key for all devices. Attach the AmazonElasticFileSystemClientReadWriteAccess policy to the IAM user. Configure the AWS CLI on the on-premises devices to use the IAM user's access key and secret key.

D. Use the amazon-efs-utils package to mount the EFS file system.

E. Use the native Linux NFS client to mount the EFS file system.

**Đáp án**: ___________

---

## Câu 118

**ID**: 246 | **Loại**: Single Choice

A DevOps engineer is setting up an Amazon Elastic Container Service (Amazon ECS) blue/green deployment for an application by using AWS CodeDeploy and AWS CloudFormation. During the deployment window, the application must be highly available and CodeDeploy must shift 10% of traffic to a new version of the application every minute until all traffic is shifted.Which configuration should the DevOps engineer add in the CloudFormation template to meet these requirements?

A. Add an AppSpec file with the CodeDeployDefault.ECSLinearl OPercentEveryl Minutes deployment configuration.

B. Add the AWS::CodeDeployBlueGreen transform and the AWS::CodeDeploy::BlueGreen hook parameter with the CodeDeployDefault.ECSLinear10PercentEvery1Minutes deployment configuration.

C. Add an AppSpec file with the ECSCanary10Percent5Minutes deployment configuration.

D. Add the AWS::CodeDeployBlueGreen transform and the AWS::CodeDepioy::BlueGreen hook parameter with the ECSCanary10Percent5Minutes deployment configuration.

**Đáp án**: ___________

---

## Câu 119

**ID**: 247 | **Loại**: Single Choice

A company uses an organization in AWS Organizations to manage its AWS accounts. The company's DevOps team has developed an AWS Lambda function that calls the Organizations API to create new AWS accounts.The Lambda function runs in the organization's management account. The DevOps team needs to move the Lambda function from the management account to a dedicated AWS account. The DevOps team must ensure that the Lambda function has the ability to create new AWS accounts only in Organizations before the team deploys the Lambda function to the new account.Which solution will meet these requirements?

A. In the management account, create a new IAM role that has the necessary permission to create new accounts in Organizations. Allow the role to be assumed by the Lambda execution role in the new AWS account. Update the Lambda function code to assume the role when the Lambda function creates new AWS accounts. Update the Lambda execution role to ensure that it has permission to assume the new role.

B. In the management account, turn on delegated administration for Organizations. Create a new delegation policy that grants the new AWS account permission to create new AWS accounts in Organizations. Ensure that the Lambda execution role has the organizations:CreateAccount permission.

C. In the management account, create a new IAM role that has the necessary permission to create new accounts in Organizations. Allow the role to be assumed by the Lambda service principal. Update the Lambda function code to assume the role when the Lambda function creates new AWS accounts. Update the Lambda execution role to ensure that it has permission to assume the new role.

D. In the management account, enable AWS Control Tower. Turn on delegated administration for AWS Control Tower. Create a resource policy that allows the new AWS account to create new AWS accounts in AWS Control Tower. Update the Lambda function code to use the AWS Control Tower API in the new AWS account. Ensure that the Lambda execution role has the controltower:CreateManagedAccount permission.

**Đáp án**: ___________

---

## Câu 120

**ID**: 248 | **Loại**: Single Choice

A company has deployed an application in a single AWS Region. The application backend uses Amazon DynamoDB tables and Amazon S3 buckets.The company wants to deploy the application in a secondary Region. The company must ensure that the data in the DynamoDB tables and the S3 buckets persists across both Regions. The data must also immediately propagate across Regions.Which solution will meet these requirements with the MOST operational efficiency?

A. Implement two-way S3 bucket replication between the primary Region's S3 buckets and the secondary Region’s S3 buckets. Convert the DynamoDB tables into global tables. Set the secondary Region as the additional Region.

B. Implement S3 Batch Operations copy jobs between the primary Region and the secondary Region for all S3 buckets. Convert the DynamoDB tables into global tables. Set the secondary Region as the additional Region.

C. Implement two-way S3 bucket replication between the primary Region's S3 buckets and the secondary Region's S3 buckets. Enable DynamoDB streams on the DynamoDB tables in both Regions. In each Region, create an AWS Lambda function that subscribes to the DynamoDB streams. Configure the Lambda function to copy new records to the DynamoDB tables in the other Region.

D. Implement S3 Batch Operations copy jobs between the primary Region and the secondary Region for all S3 buckets. Enable DynamoDB streams on the DynamoDB tables in both Regions. In each Region, create an AWS Lambda function that subscribes to the DynamoDB streams. Configure the Lambda function to copy new records to the DynamoDB tables in the other Region.

**Đáp án**: ___________

---

## Câu 121

**ID**: 249 | **Loại**: Single Choice

A company has configured Amazon RDS storage autoscaling for its RDS DB instances. A DevOps team needs to visualize the autoscaling events on an Amazon CloudWatch dashboard.Which solution will meet this requirement?

A. Create an Amazon EventBridge rule that reacts to RDS storage autoscaling events from RDS events. Create an AWS Lambda function that publishes a CloudWatch custom metric. Configure the EventBridge rule to invoke the Lambda function. Visualize the custom metric by using the CloudWatch dashboard.

B. Create a trail by using AWS CloudTrail with management events configured. Configure the trail to send the management events to Amazon CloudWatch Logs. Create a metric filter in CloudWatch Logs to match the RDS storage autoscaling events. Visualize the metric filter by using the CloudWatch dashboard.

C. Create an Amazon EventBridge rule that reacts to RDS storage autoscaling events from the RDS events. Create a CloudWatch alarm. Configure the EventBridge rule to change the status of the CloudWatch alarm. Visualize the alarm status by using the CloudWatch dashboard.

D. Create a trail by using AWS CloudTrail with data events configured. Configure the trail to send the data events to Amazon CloudWatch Logs. Create a metric filter in CloudWatch Logs to match the RDS storage autoscaling events. Visualize the metric filter by using the CloudWatch dashboard.

**Đáp án**: ___________

---

## Câu 122

**ID**: 250 | **Loại**: Single Choice

A company uses containers for its applications. The company learns that some container images are missing required security configurations.A DevOps engineer needs to implement a solution to create a standard base image. The solution must publish the base image weekly to the us-west-2 Region, us-east-2 Region, and eu-central-1 Region.Which solution will meet these requirements?

A. Create an EC2 Image Builder pipeline that uses a container recipe to build the image. Configure the pipeline to distribute the image to an Amazon Elastic Container Registry (Amazon ECR) repository in us-west-2. Configure ECR replication from us-west-2 to us-east-2 and from us-east-2 to eu-central-1. Configure the pipeline to run weekly.

B. Create an AWS CodePipeline pipeline that uses an AWS CodeBuild project to build the image. Use AWS CodeDeploy to publish the image to an Amazon Elastic Container Registry (Amazon ECR) repository in us-west-2. Configure ECR replication from us-west-2 to us-east-2 and from us-east-2 to eu-central-1. Configure the pipeline to run weekly.

C. Create an EC2 Image Builder pipeline that uses a container recipe to build the image. Configure the pipeline to distribute the image to Amazon Elastic Container Registry (Amazon ECR) repositories in all three Regions. Configure the pipeline to run weekly.

D. Create an AWS CodePipeline pipeline that uses an AWS CodeBuild project to build the image. Use AWS CodeDeploy to publish the image to Amazon Elastic Container Registry (Amazon ECR) repositories in all three Regions. Configure the pipeline to run weekly.

**Đáp án**: ___________

---

## Câu 123

**ID**: 251 | **Loại**: Single Choice

A DevOps engineer needs to implement a solution to install antivirus software on all the Amazon EC2 instances in an AWS account. The EC2 instances run the most recent version of Amazon Linux.The solution must detect all instances and must use an AWS Systems Manager document to install the software if the software is not present.Which solution will meet these requirements?

A. Create an association in Systems Manager State Manager. Target all the managed nodes. Include the software in the association. Configure the association to use the Systems Manager document.

B. Set up AWS Config to record all the resources in the account. Create an AWS Config custom rule to determine if the software is installed on all the EC2 instances. Configure an automatic remediation action that uses the Systems Manager document for noncompliant EC2 instances.

C. Activate Amazon EC2 scanning on Amazon Inspector to determine if the software is installed on all the EC2 instances. Associate the findings with the Systems Manager document.

D. Create an Amazon EventBridge rule that uses AWS CloudTrail to detect the Runinstances API call. Configure inventory collection in Systems Manager Inventory to determine if the software is installed on the EC2 instances. Associate the Systems Manager inventory with the Systems Manager document.

**Đáp án**: ___________

---

## Câu 124

**ID**: 252 | **Loại**: Multiple Choice

A company needs to increase the security of the container images that run in its production environment. The company wants to integrate operating system scanning and programming language package vulnerability scanning for the containers in its CI/CD pipeline. The CI/CD pipeline is an AWS CodePipeline pipeline that includes an AWS CodeBuild build project, AWS CodeDeploy actions, and an Amazon Elastic Container Registry (Amazon ECR) repository.A DevOps engineer needs to add an image scan to the CI/CD pipeline. The CI/CD pipeline must deploy only images without CRITICAL and HIGH findings into production.Which combination of steps will meet these requirements? (Choose two.)

A. Use Amazon ECR basic scanning.

B. Use Amazon ECR enhanced scanning.

C. Configure Amazon ECR to submit a Rejected status to the CI/CD pipeline when the image scan returns CRITICAL or HIGH findings.

D. Configure an Amazon EventBridge rule to invoke an AWS Lambda function when the image scan is completed. Configure the Lambda function to consume the Amazon Inspector scan status and to submit an Approved or Rejected status to the CI/CD pipeline.

E. Configure an Amazon EventBridge rule to invoke an AWS Lambda function when the image scan is completed. Configure the Lambda function to consume the Clair scan status and to submit an Approved or Rejected status to the CI/CD pipeline.

**Đáp án**: ___________

---

## Câu 125

**ID**: 253 | **Loại**: Single Choice

A company's DevOps team manages a set of AWS accounts that are in an organization in AWS Organizations.The company needs a solution that ensures that all Amazon EC2 instances use approved AM Is that the DevOps team manages. The solution also must remediate the usage of AMIs that are not approved. The individual account administrators must not be able to remove the restriction to use approved AMIs.Which solution will meet these requirements?

A. Use AWS CloudFormation StackSets to deploy an Amazon EventBridge rule to each account. Configure the rule to react to AWS CloudTrail events for Amazon EC2 and to send a notification to an Amazon Simple Notification Service (Amazon SNS) topic. Subscribe the DevOps team to the SNS topic.

B. Use AWS CloudFormation StackSets to deploy the approved-amis-by-id AWS Config managed rule to each account. Configure the rule with the list of approved AMIs. Configure the rule to run the AWS-StopEC2Instance AWS Systems Manager Automation runbook for the noncompliant EC2 instances.

C. Create an AWS Lambda function that processes AWS CloudTrail events for Amazon EC2. Configure the Lambda function to send a notification to an Amazon Simple Notification Service (Amazon SNS) topic. Subscribe the DevOps team to the SNS topic. Deploy the Lambda function in each account in the organization. Create an Amazon EventBridge rule in each account. Configure the EventBridge rules to react to AWS CloudTrail events for Amazon EC2 and to invoke the Lambda function.

D. Enable AWS Config across the organization. Create a conformance pack that uses the approved-amis-by-id AWS Config managed rule with the list of approved AMIs. Deploy the conformance pack across the organization. Configure the rule to run the AWS-StopEC2lnstance AWS Systems Manager Automation runbook for the noncompliant EC2 instances.

**Đáp án**: ___________

---

## Câu 126

**ID**: 254 | **Loại**: Single Choice

A company gives its employees limited rights to AWS. DevOps engineers have the ability to assume an administrator role. For tracking purposes, the security team wants to receive a near-real-time notification when the administrator role is assumed.How should this be accomplished?

A. Configure AWS Config to publish logs to an Amazon S3 bucket. Use Amazon Athena to query the logs and send a notification to the security team when the administrator role is assumed.

B. Configure Amazon GuardDuty to monitor when the administrator role is assumed and send a notification to the security team.

C. Create an Amazon EventBridge event rule using an AWS Management Console sign-in events event pattern that publishes a message to an Amazon SNS topic if the administrator role is assumed.

D. Create an Amazon EventBridge events rule using an AWS API call that uses an AWS CloudTrail event pattern to invoke an AWS Lambda function that publishes a message to an Amazon SNS topic if the administrator role is assumed.

**Đáp án**: ___________

---


# Đáp Án

**Câu 1** (ID 128): B, D, E

**Câu 2** (ID 129): B, C, E

**Câu 3** (ID 130): A

**Câu 4** (ID 131): A

**Câu 5** (ID 132): A

**Câu 6** (ID 133): C

**Câu 7** (ID 134): B

**Câu 8** (ID 135): A

**Câu 9** (ID 136): A

**Câu 10** (ID 137): C

**Câu 11** (ID 138): B, D

**Câu 12** (ID 139): C, D

**Câu 13** (ID 140): A

**Câu 14** (ID 141): B

**Câu 15** (ID 142): C

**Câu 16** (ID 143): C

**Câu 17** (ID 144): B

**Câu 18** (ID 146): B

**Câu 19** (ID 147): C

**Câu 20** (ID 148): B

**Câu 21** (ID 149): C

**Câu 22** (ID 150): C

**Câu 23** (ID 151): D

**Câu 24** (ID 152): D

**Câu 25** (ID 153): B

**Câu 26** (ID 154): B

**Câu 27** (ID 155): B

**Câu 28** (ID 156): A

**Câu 29** (ID 157): A, E

**Câu 30** (ID 158): D

**Câu 31** (ID 159): A

**Câu 32** (ID 160): B, E

**Câu 33** (ID 161): A

**Câu 34** (ID 162): B

**Câu 35** (ID 163): B, C, F

**Câu 36** (ID 164): A

**Câu 37** (ID 165): A, B, E

**Câu 38** (ID 166): B, C

**Câu 39** (ID 167): A

**Câu 40** (ID 168): C

**Câu 41** (ID 169): A, D

**Câu 42** (ID 170): B, C

**Câu 43** (ID 171): B

**Câu 44** (ID 172): A, E

**Câu 45** (ID 173): B

**Câu 46** (ID 174): C

**Câu 47** (ID 175): D

**Câu 48** (ID 176): B

**Câu 49** (ID 177): A

**Câu 50** (ID 178): C

**Câu 51** (ID 179): B, C, E

**Câu 52** (ID 180): C, E

**Câu 53** (ID 181): C

**Câu 54** (ID 182): B

**Câu 55** (ID 183): B

**Câu 56** (ID 184): A, B

**Câu 57** (ID 185): A

**Câu 58** (ID 186): A

**Câu 59** (ID 187): D

**Câu 60** (ID 188): D

**Câu 61** (ID 189): C

**Câu 62** (ID 190): A, D, E

**Câu 63** (ID 191): A

**Câu 64** (ID 192): B

**Câu 65** (ID 193): C

**Câu 66** (ID 194): B

**Câu 67** (ID 195): A, D, F

**Câu 68** (ID 196): B, E

**Câu 69** (ID 197): B, D, E

**Câu 70** (ID 198): A

**Câu 71** (ID 199): B, D

**Câu 72** (ID 200): B

**Câu 73** (ID 201): B, C, F

**Câu 74** (ID 202): B

**Câu 75** (ID 203): C

**Câu 76** (ID 204): A

**Câu 77** (ID 205): D

**Câu 78** (ID 206): B

**Câu 79** (ID 207): D

**Câu 80** (ID 208): B, C, D

**Câu 81** (ID 209): B

**Câu 82** (ID 210): A, D

**Câu 83** (ID 211): A, C, E

**Câu 84** (ID 212): C

**Câu 85** (ID 213): D

**Câu 86** (ID 214): B

**Câu 87** (ID 215): C

**Câu 88** (ID 216): D

**Câu 89** (ID 217): A, B, F

**Câu 90** (ID 218): B

**Câu 91** (ID 219): A, D, F

**Câu 92** (ID 220): A, E

**Câu 93** (ID 221): C

**Câu 94** (ID 222): B

**Câu 95** (ID 223): A

**Câu 96** (ID 224): A

**Câu 97** (ID 225): A, B

**Câu 98** (ID 226): C

**Câu 99** (ID 227): A

**Câu 100** (ID 228): A

**Câu 101** (ID 229): D

**Câu 102** (ID 230): C, E, F

**Câu 103** (ID 231): B, E

**Câu 104** (ID 232): B, D

**Câu 105** (ID 233): A, E

**Câu 106** (ID 234): B

**Câu 107** (ID 235): B

**Câu 108** (ID 236): B

**Câu 109** (ID 237): B, C, E

**Câu 110** (ID 238): A, E

**Câu 111** (ID 239): B

**Câu 112** (ID 240): C

**Câu 113** (ID 241): A, D

**Câu 114** (ID 242): C

**Câu 115** (ID 243): A, C, E

**Câu 116** (ID 244): B, C, E

**Câu 117** (ID 245): B, D

**Câu 118** (ID 246): B

**Câu 119** (ID 247): A

**Câu 120** (ID 248): A

**Câu 121** (ID 249): A

**Câu 122** (ID 250): C

**Câu 123** (ID 251): A

**Câu 124** (ID 252): B, D

**Câu 125** (ID 253): D

**Câu 126** (ID 254): D

