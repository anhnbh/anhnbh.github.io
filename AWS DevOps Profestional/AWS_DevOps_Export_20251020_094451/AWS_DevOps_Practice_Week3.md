# AWS DevOps Practice Test - Week3

**Số câu**: 108  
**Ngày tạo**: 20/10/2025 09:44

---

## Câu 1

**ID**: 255 | **Loại**: Multiple Choice

A company needs a strategy for failover and disaster recovery of its data and application. The application uses a MySQL database and Amazon EC2 instances. The company requires a maximum RPO of 2 hours and a maximum RTO of 10 minutes for its data and application at all times.Which combination of deployment strategies will meet these requirements? (Choose two.)

A. Create an Amazon Aurora Single-AZ cluster in multiple AWS Regions as the data store. Use Aurora's automatic recovery capabilities in the event of a disaster.

B. Create an Amazon Aurora global database in two AWS Regions as the data store. In the event of a failure, promote the secondary Region to the primary for the application. Update the application to use the Aurora cluster endpoint in the secondary Region.

C. Create an Amazon Aurora cluster in multiple AWS Regions as the data store. Use a Network Load Balancer to balance the database traffic in different Regions.

D. Set up the application in two AWS Regions. Use Amazon Route 53 failover routing that points to Application Load Balancers in both Regions. Use health checks and Auto Scaling groups in each Region.

E. Set up the application in two AWS Regions. Configure AWS Global Accelerator to point to Application Load Balancers (ALBs) in both Regions. Add both ALBs to a single endpoint group. Use health checks and Auto Scaling groups in each Region.

**Đáp án**: ___________

---

## Câu 2

**ID**: 256 | **Loại**: Multiple Choice

A developer is using the AWS Serverless Application Model (AWS SAM) to create a prototype for an AWS Lambda function. The AWS SAM template contains an AWS::Serverless::Function resource that has the CodeUri property that points to an Amazon S3 location. The developer wants to identify the correct commands for deployment before creating a CI/CD pipeline.The developer creates an archive of the Lambda function code named package.zip. The developer uploads the .zip file archive to the S3 location specified in the CodeUri property. The developer runs the sam deploy command and deploys the Lambda function. The developer updates the Lambda function code and uses the same steps to deploy the new version of the Lambda function. The sam deploy command fails and returns an error of no changes to deploy.Which solutions will deploy the new version? (Choose two.)

A. Use the aws cloudformation update-stack command instead of the sam deploy command.

B. Use the aws cloudformation update-stack-instances command instead of the sam deploy command.

C. Update the CodeUri property to reference the local application code folder. Use the sam deploy command.

D. Update the CodeUri property to reference the local application code folder. Use the aws cloudformation create-change-set command and the aws cloudformation execute-change-set command.

E. Update the CodeUri property to reference the local application code folder. Use the aws cloudformation package command and the aws cloudformation deploy command.

**Đáp án**: ___________

---

## Câu 3

**ID**: 257 | **Loại**: Single Choice

A company runs its container workloads in AWS App Runner. A DevOps engineer manages the company's container repository in Amazon Elastic Container Registry (Amazon ECR).The DevOps engineer must implement a solution that continuously monitors the container repository. The solution must create a new container image when the solution detects an operating system vulnerability or language package vulnerability.Which solution will meet these requirements?

A. Use EC2 Image Builder to create a container image pipeline. Use Amazon ECR as the target repository. Turn on enhanced scanning on the ECR repository. Create an Amazon EventBridge rule to capture an Inspector? finding event. Use the event to invoke the image pipeline. Re-upload the container to the repository.

B. Use EC2 Image Builder to create a container image pipeline. Use Amazon ECR as the target repository. Enable Amazon GuardDuty Malware Protection on the container workload. Create an Amazon EventBridge rule to capture a GuardDuty finding event. Use the event to invoke the image pipeline.

C. Create an AWS CodeBuild project to create a container image. Use Amazon ECR as the target repository. Turn on basic scanning on the repository. Create an Amazon EventBridge rule to capture an ECR image action event. Use the event to invoke the CodeBuild project. Re-upload the container to the repository.

D. Create an AWS CodeBuild project to create a container image. Use Amazon ECR as the target repository. Configure AWS Systems Manager Compliance to scan all managed nodes. Create an Amazon EventBridge rule to capture a configuration compliance state change event. Use the event to invoke the CodeBuild project.

**Đáp án**: ___________

---

## Câu 4

**ID**: 258 | **Loại**: Single Choice

A company wants to use AWS Systems Manager documents to bootstrap physical laptops for developers. The bootstrap code is stored in GitHub. A DevOps engineer has already created a Systems Manager activation, installed the Systems Manager agent with the registration code, and installed an activation ID on all the laptops.Which set of steps should be taken next?

A. Configure the Systems Manager document to use the AWS-RunShellScript command to copy the files from GitHub to Amazon S3, then use the aws-downloadContent plugin with a sourceType of S3.

B. Configure the Systems Manager document to use the aws-configurePackage plugin with an install action and point to the Git repository.

C. Configure the Systems Manager document to use the aws-downloadContent plugin with a sourceType of GitHub and sourceInfo with the repository details.

D. Configure the Systems Manager document to use the aws:softwareInventory plugin and run the script from the Git repository.

**Đáp án**: ___________

---

## Câu 5

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

## Câu 6

**ID**: 260 | **Loại**: Single Choice

A company is developing a web application's infrastructure using AWS CloudFormation. The database engineering team maintains the database resources in a CloudFormation template, and the software development team maintains the web application resources in a separate CloudFormation template. As the scope of the application grows, the software development team needs to use resources maintained by the database engineering team. However, both teams have their own review and lifecycle management processes that they want to keep. Both teams also require resource-level change-set reviews. The software development team would like to deploy changes to this template using their CI/CD pipeline.Which solution will meet these requirements?

A. Create a stack export from the database CloudFormation template and import those references into the web application CloudFormation template.

B. Create a CloudFormation nested stack to make cross-stack resource references and parameters available in both stacks.

C. Create a CloudFormation stack set to make cross-stack resource references and parameters available in both stacks.

D. Create input parameters in the web application CloudFormation template and pass resource names and IDs from the database stack.

**Đáp án**: ___________

---

## Câu 7

**ID**: 261 | **Loại**: Single Choice

A company has an organization in AWS Organizations. A DevOps engineer needs to maintain multiple AWS accounts that belong to different OUs in the organization. All resources, including IAM policies and Amazon S3 policies within an account, are deployed through AWS CloudFormation. All templates and code are maintained in an AWS CodeCommit repository. Recently, some developers have not been able to access an S3 bucket from some accounts in the organization.The following policy is attached to the S3 bucket:What should the DevOps engineer do to resolve this access issue?

A. Modify the S3 bucket policy. Turn off the S3 Block Public Access setting on the S3 bucket. In the S3 policy, add the aws:SourceAccount condition. Add the AWS account IDs of all developers who are experiencing the issue.

B. Verify that no IAM permissions boundaries are denying developers access to the S3 bucket. Make the necessary changes to IAM permissions boundaries. Use an AWS Config recorder in the individual developer accounts that are experiencing the issue to revert any changes that are blocking access. Commit the fix back into the CodeCommit repository. Invoke deployment through CloudFormation to apply the changes.

C. Configure an SCP that stops anyone from modifying IAM resources in developer OUs. In the S3 policy, add the aws:SourceAccount condition. Add the AWS account IDs of all developers who are experiencing the issue. Commit the fix back into the CodeCommit repository. Invoke deployment through CloudFormation to apply the changes.

D. Ensure that no SCP is blocking access for developers to the S3 bucket. Ensure that no IAM policy permissions boundaries are denying access to developer IAM users. Make the necessary changes to the SCP and IAM policy permissions boundaries in the CodeCommit repository. Invoke deployment through CloudFormation to apply the changes.

**Đáp án**: ___________

---

## Câu 8

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

## Câu 9

**ID**: 263 | **Loại**: Single Choice

A company deploys an application to Amazon EC2 instances. The application runs Amazon Linux 2 and uses AWS CodeDeploy. The application has the following file structure for its code repository:The appspec.yml file has the following contents in the files section:What will the result be for the deployment of the config.txt file?

A. The config.txt file will be deployed to only /var/www/html/config/config.txt.

B. The config.txt file will be deployed to /usr/local/src/config.txt and to /var/www/html/config/config.txt.

C. The config.txt file will be deployed to only /usr/local/src/config.txt.

D. The config.txt file will be deployed to /usr/local/src/config.txt and to /var/www/html/application/web/config.txt.

**Đáp án**: ___________

---

## Câu 10

**ID**: 264 | **Loại**: Multiple Choice

A company has set up AWS CodeArtifact repositories with public upstream repositories. The company's development team consumes open source dependencies from the repositories in the company's internal network.The company's security team recently discovered a critical vulnerability in the most recent version of a package that the development team consumes. The security team has produced a patched version to fix the vulnerability. The company needs to prevent the vulnerable version from being downloaded. The company also needs to allow the security team to publish the patched version.Which combination of steps will meet these requirements? (Choose two.)

A. Update the status of the affected CodeArtifact package version to unlisted.

B. Update the status of the affected CodeArtifact package version to deleted.

C. Update the status of the affected CodeArtifact package version to archived.

D. Update the CodeArtifact package origin control settings to allow direct publishing and to block upstream operations.

E. Update the CodeArtifact package origin control settings to block direct publishing and to allow upstream operations.

**Đáp án**: ___________

---

## Câu 11

**ID**: 265 | **Loại**: Single Choice

A company is running a custom-built application that processes records. All the components run on Amazon EC2 instances that run in an Auto Scaling group. Each record's processing is a multistep sequential action that is compute-intensive. Each step is always completed in 5 minutes or less.A limitation of the current system is that if any steps fail, the application has to reprocess the record from the beginning. The company wants to update the architecture so that the application must reprocess only the failed steps.What is the MOST operationally efficient solution that meets these requirements?

A. Create a web application to write records to Amazon S3. Use S3 Event Notifications to publish to an Amazon Simple Notification Service (Amazon SNS) topic. Use an EC2 instance to poll Amazon SNS and start processing. Save intermediate results to Amazon S3 to pass on to the next step.

B. Perform the processing steps by using logic in the application. Convert the application code to run in a container. Use AWS Fargate to manage the container instances. Configure the container to invoke itself to pass the state from one step to the next.

C. Create a web application to pass records to an Amazon Kinesis data stream. Decouple the processing by using the Kinesis data stream and AWS Lambda functions.

D. Create a web application to pass records to AWS Step Functions. Decouple the processing into Step Functions tasks and AWS Lambda functions.

**Đáp án**: ___________

---

## Câu 12

**ID**: 266 | **Loại**: Single Choice

A company is migrating its on-premises Windows applications and Linux applications to AWS. The company will use automation to launch Amazon EC2 instances to mirror the on-premises configurations. The migrated applications require access to shared storage that uses SMB for Windows and NFS for Linux.The company is also creating a pilot light disaster recovery (DR) environment in another AWS Region. The company will use automation to launch and configure the EC2 instances in the DR Region. The company needs to replicate the storage to the DR Region.Which storage solution will meet these requirements?

A. Use Amazon S3 for the application storage. Create an S3 bucket in the primary Region and an S3 bucket in the DR Region. Configure S3 Cross-Region Replication (CRR) from the primary Region to the DR Region.

B. Use Amazon Elastic Block Store (Amazon EBS) for the application storage. Create a backup plan in AWS Backup that creates snapshots of the EBS volumes that are in the primary Region and replicates the snapshots to the DR Region.

C. Use a Volume Gateway in AWS Storage Gateway for the application storage. Configure Cross-Region Replication (CRR) of the Volume Gateway from the primary Region to the DR Region.

D. Use Amazon FSx for NetApp ONTAP for the application storage. Create an FSx for ONTAP instance in the DR Region. Configure NetApp SnapMirror replication from the primary Region to the DR Region.

**Đáp án**: ___________

---

## Câu 13

**ID**: 267 | **Loại**: Multiple Choice

A company's application uses a fleet of Amazon EC2 On-Demand Instances to analyze and process data. The EC2 instances are in an Auto Scaling group. The Auto Scaling group is a target group for an Application Load Balancer (ALB). The application analyzes critical data that cannot tolerate interruption. The application also analyzes noncritical data that can withstand interruption.The critical data analysis requires quick scalability in response to real-time application demand. The noncritical data analysis involves memory consumption. A DevOps engineer must implement a solution that reduces scale-out latency for the critical data. The solution also must process the noncritical data.Which combination of steps will meet these requirements? (Choose two.)

A. For the critical data, modify the existing Auto Scaling group. Create a warm pool instance in the stopped state. Define the warm pool size. Create a new version of the launch template that has detailed monitoring enabled. Use Spot Instances.

B. For the critical data, modify the existing Auto Scaling group. Create a warm pool instance in the stopped state. Define the warm pool size. Create a new version of the launch template that has detailed monitoring enabled. Use On-Demand Instances.

C. For the critical data, modify the existing Auto Scaling group. Create a lifecycle hook to ensure that bootstrap scripts are completed successfully. Ensure that the application on the instances is ready to accept traffic before the instances are registered. Create a new version of the launch template that has detailed monitoring enabled.

D. For the noncritical data, create a second Auto Scaling group that uses a launch template. Configure the launch template to install the unified Amazon CloudWatch agent and to configure the CloudWatch agent with a custom memory utilization metric. Use Spot Instances. Add the new Auto Scaling group as the target group for the ALB. Modify the application to use two target groups for critical data and noncritical data.

E. For the noncritical data, create a second Auto Scaling group. Choose the predefined memory utilization metric type for the target tracking scaling policy. Use Spot Instances. Add the new Auto Scaling group as the target group for the ALB. Modify the application to use two target groups for critical data and noncritical data.

**Đáp án**: ___________

---

## Câu 14

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

## Câu 15

**ID**: 269 | **Loại**: Single Choice

A company's video streaming platform usage has increased from 10,000 users each day to 50,000 users each day in multiple countries. The company deploys the streaming platform on Amazon Elastic Kubernetes Service (Amazon EKS). The EKS workload scales up to thousands of nodes during peak viewing time.The company's users report occurrences of unauthorized logins. Users also report sudden interruptions and logouts from the platform.The company wants additional security measures for the entire platform. The company also needs a summarized view of the resource behaviors and interactions across the company's entire AWS environment. The summarized view must show login attempts, API calls, and network traffic. The solution must permit network traffic analysis while minimizing the overhead of managing logs. The solution must also quickly investigate any potential malicious behavior that is associated with the EKS workload.Which solution will meet these requirements?

A. Enable Amazon GuardDuty for EKS Audit Log Monitoring. Enable AWS CloudTrail logs. Store the EKS audit logs and CloudTrail log files in an Amazon S3 bucket. Use Amazon Athena to create an external table. Use Amazon QuickSight to create a dashboard.

B. Enable Amazon GuardDuty for EKS Audit Log Monitoring. Enable Amazon Detective in the company's AWS account. Enable EKS audit logs from optional source packages in Detective.

C. Enable Amazon CloudWatch Container Insights. Enable AWS CloudTrail logs. Store the EKS audit logs and CloudTrail log files in an Amazon S3 bucket. Use Amazon Athena to create an external table. Use Amazon QuickSight to create a dashboard.

D. Enable Amazon GuardDuty for EKS Audit Log Monitoring. Enable Amazon CloudWatch Container Insights and VPC Flow Logs. Enable AWS CloudTrail logs.

**Đáp án**: ___________

---

## Câu 16

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

## Câu 17

**ID**: 271 | **Loại**: Multiple Choice

A company uses an organization in AWS Organizations that has all features enabled. The company uses AWS Backup in a primary account and uses an AWS Key Management Service (AWS KMS) key to encrypt the backups.The company needs to automate a cross-account backup of the resources that AWS Backup backs up in the primary account. The company configures cross-account backup in the Organizations management account. The company creates a new AWS account in the organization and configures an AWS Backup backup vault in the new account. The company creates a KMS key in the new account to encrypt the backups. Finally, the company configures a new backup plan in the primary account. The destination for the new backup plan is the backup vault in the new account.When the AWS Backup job in the primary account is invoked, the job creates backups in the primary account. However, the backups are not copied to the new account's backup vault.Which combination of steps must the company take so that backups can be copied to the new account's backup vault? (Choose two.)

A. Edit the backup vault access policy in the new account to allow access to the primary account.

B. Edit the backup vault access policy in the primary account to allow access to the new account.

C. Edit the backup vault access policy in the primary account to allow access to the KMS key in the new account.

D. Edit the key policy of the KMS key in the primary account to share the key with the new account.

E. Edit the key policy of the KMS key in the new account to share the key with the primary account.

**Đáp án**: ___________

---

## Câu 18

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

## Câu 19

**ID**: 273 | **Loại**: Multiple Choice

A company uses the AWS Cloud Development Kit (AWS CDK) to define its application. The company uses a pipeline that consists of AWS CodePipeline and AWS CodeBuild to deploy the CDK application.The company wants to introduce unit tests to the pipeline to test various infrastructure components. The company wants to ensure that a deployment proceeds if no unit tests result in a failure.Which combination of steps will enforce the testing requirement in the pipeline? (Choose two.)

A. Update the CodeBuild build phase commands to run the tests then to deploy the application. Set the OnFailure phase property to ABORT.

B. Update the CodeBuild build phase commands to run the tests then to deploy the application. Add the --rollback true flag to the cdk deploy command.

C. Update the CodeBuild build phase commands to run the tests then to deploy the application. Add the --require-approval any-change flag to the cdk deploy command.

D. Create a test that uses the AWS CDK assertions module. Use the template.hasResourceProperties assertion to test that resources have the expected properties.

E. Create a test that uses the cdk diff command. Configure the test to fail if any resources have changed.

**Đáp án**: ___________

---

## Câu 20

**ID**: 274 | **Loại**: Single Choice

A company has an application that runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The EC2 instances are in multiple Availability Zones. The application was misconfigured in a single Availability Zone, which caused a partial outage of the application.A DevOps engineer made changes to ensure that the unhealthy EC2 instances in one Availability Zone do not affect the healthy EC2 instances in the other Availability Zones. The DevOps engineer needs to test the application's failover and shift where the ALB sends traffic. During failover, the ALB must avoid sending traffic to the Availability Zone where the failure has occurred.Which solution will meet these requirements?

A. Turn off cross-zone load balancing on the ALB. Use Amazon Route 53 Application Recovery Controller to start a zonal shift away from the Availability Zone.

B. Turn off cross-zone load balancing on the ALB’s target group. Use Amazon Route 53 Application Recovery Controller to start a zonal shift away from the Availability Zone.

C. Create an Amazon Route 53 Application Recovery Controller resource set that uses the DNS hostname of the ALB. Start a zonal shift for the resource set away from the Availability Zone.

D. Create an Amazon Route 53 Application Recovery Controller resource set that uses the ARN of the ALB’s target group. Create a readiness check that uses the ElbV2TargetGroupsCanServeTraffic rule.

**Đáp án**: ___________

---

## Câu 21

**ID**: 275 | **Loại**: Single Choice

A company sends its AWS Network Firewall flow logs to an Amazon S3 bucket. The company then analyzes the flow logs by using Amazon Athena.The company needs to transform the flow logs and add additional data before the flow logs are delivered to the existing S3 bucket.Which solution will meet these requirements?

A. Create an AWS Lambda function to transform the data and to write a new object to the existing S3 bucket. Configure the Lambda function with an S3 trigger for the existing S3 bucket. Specify all object create events for the event type. Acknowledge the recursive invocation.

B. Enable Amazon EventBridge notifications on the existing S3 bucket. Create a custom EventBridge event bus. Create an EventBridge rule that is associated with the custom event bus. Configure the rule to react to all object create events for the existing S3 bucket and to invoke an AWS Step Functions workflow. Configure a Step Functions task to transform the data and to write the data into a new S3 bucket.

C. Create an Amazon EventBridge rule that is associated with the default EventBridge event bus. Configure the rule to react to all object create events for the existing S3 bucket. Define a new S3 bucket as the target for the rule. Create an EventBridge input transformation to customize the event before passing the event to the rule target.

D. Create an Amazon Kinesis Data Firehose delivery stream that is configured with an AWS Lambda transformer. Specify the existing S3 bucket as the destination. Change the Network Firewall logging destination from Amazon S3 to Kinesis Data Firehose.

**Đáp án**: ___________

---

## Câu 22

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

## Câu 23

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

## Câu 24

**ID**: 278 | **Loại**: Single Choice

A company uses an organization in AWS Organizations that a security team and a DevOps team manage. Both teams access the accounts by using AWS IAM Identity Center.A dedicated group has been created for each team. The DevOps team's group has been assigned a permission set named DevOps. The permission set has the AdministratorAccess managed IAM policy attached. The permission set has been applied to all accounts in the organization.The security team wants to ensure that the DevOps team does not have access to IAM Identity Center in the organization's management account. The security team has attached the following SCP to the organization root:After implementing the policy, the security team discovers that the DevOps team can still access IAM Identity Center.Which solution will fix the problem?

A. In the organization's management account, create a new OU. Move the organization's management account to the new OU. Detach the SCP from the organization root. Attach the SCP to the new OU.

B. In the organization's management account, update the SCP condition reference to the ARN of the DevOps team's group role to include the AWS account ID of the organization's management account.

C. In IAM Identity Center, create a new permission set. Ensure that the assigned policy has full access but explicitly denies permission for the sso:* action and the sso-directory:* action. Update the assigned permission set for the DevOps team's group role in the organization's management account. Delete the SCP.

D. In IAM Identity Center, update the DevOps permission set. Ensure that the assigned policy has full access but explicitly denies permission for the sso:* action and the sso-directory:* action. In the Deny statement, add a StringEquals condition that compares the aws:SourceAccount global condition context key with the organization's management account IDelete the SCP.

**Đáp án**: ___________

---

## Câu 25

**ID**: 279 | **Loại**: Single Choice

An Amazon EC2 Auto Scaling group manages EC2 instances that were created from an AMI. The AMI has the AWS Systems Manager Agent installed. When an EC2 instance is launched into the Auto Scaling group, tags are applied to the EC2 instance.EC2 instances that are launched by the Auto Scaling group must have the correct operating system configuration.Which solution will meet these requirements?

A. Create a Systems Manager Run Command document that configures the desired instance configuration. Set up Systems Manager Compliance to invoke the Run Command document when the EC2 instances are not in compliance with the most recent patches.

B. Create a Systems Manager State Manager association that links to the Systems Manager command document. Create a tag query that runs immediately.

C. Create a Systems Manager Run Command task that specifies the desired instance configuration. Create a maintenance window in Systems Manager Maintenance Windows that runs daily. Register the Run Command task against the maintenance window. Designate the targets.

D. Create a Systems Manager Patch Manager patch baseline and a patch group that use the same tags that the Auto Scaling group applies. Register the patch group with the patch baseline. Define a Systems Manager command document to patch the instances Invoke the document by using Systems Manager Run Command.

**Đáp án**: ___________

---

## Câu 26

**ID**: 280 | **Loại**: Single Choice

A company uses AWS Organizations to manage its AWS accounts. The organization root has a child OU that is named Department. The Department OU has a child OU that is named Engineering. The default FullAWSAccess policy is attached to the root, the Department OU, and the Engineering OU.The company has many AWS accounts in the Engineering OU. Each account has an administrative IAM role with the AdministratorAccess IAM policy attached. The default FullAWSAccessPolicy is also attached to each account.A DevOps engineer plans to remove the FullAWSAccess policy from the Department OU. The DevOps engineer will replace the policy with a policy that contains an Allow statement for all Amazon EC2 API operations.What will happen to the permissions of the administrative 1AM roles as a result of this change?

A. All API actions on all resources will be allowed.

B. All API actions on EC2 resources will be allowed. All other API actions will be denied.

C. All API actions on all resources will be denied.

D. All API actions on EC2 resources will be denied. All other API actions will be allowed.

**Đáp án**: ___________

---

## Câu 27

**ID**: 281 | **Loại**: Single Choice

A company manages AWS accounts in AWS Organizations. The company needs a solution to send Amazon CloudWatch Logs data to an Amazon S3 bucket in a dedicated AWS account. The solution must support all existing and future CloudWatch Logs log groups.Which solution will meet these requirements?

A. Enable Organizations backup policies to back up all log groups to a dedicated S3 bucket. Add an S3 bucket policy that allows access from all accounts that belong to the company.

B. Create a backup plan in AWS Backup. Specify a dedicated S3 bucket as a backup vault. Assign all CloudWatch Logs log group resources to the backup plan. Create resource assignments in the backup plan for all accounts that belong to the company.

C. Create a backup plan in AWS Backup. Specify a dedicated S3 bucket as a backup vault. Assign all existing log groups to the backup plan. Create resource assignments in the backup plan for all accounts that belong to the company. Create an AWS Systems Manager Automation runbook to assign log groups to a backup plan. Create an AWS Config rule that has an automatic remediation action for all noncompliant log groups. Specify the runbook as the rule's target.

D. Create a CloudWatch Logs destination and an Amazon Kinesis Data Firehose delivery stream in the dedicated AWS account. Specify the S3 bucket as the destination of the delivery stream. Create subscription filters for all existing log groups in all accounts. Create an AWS Lambda function to call the CloudWatch Logs PutSubscriptionFilter API operation. Create an Amazon EventBridge rule to invoke the Lambda function when a CreateLogGroup event occurs.

**Đáp án**: ___________

---

## Câu 28

**ID**: 282 | **Loại**: Multiple Choice

A DevOps engineer manages a Java-based application that runs in an Amazon Elastic Container Service (Amazon ECS) cluster on AWS Fargate. Auto scaling has not been configured for the application.The DevOps engineer has determined that the Java Virtual Machine (JVM) thread count is a good indicator of when to scale the application. The application serves customer traffic on port 8080 and makes JVM metrics available on port 9404.Application use has recently increased. The DevOps engineer needs to configure auto scaling for the application.Which solution will meet these requirements with the LEAST operational overhead? (Choose two.)

A. Deploy the Amazon CloudWatch agent as a container sidecar. Configure the CloudWatch agent to retrieve JVM metrics from port 9404. Create CloudWatch alarms on the JVM thread count metric to scale the application. Add a step scaling policy in Fargate to scale up and scale down based on the CloudWatch alarms.

B. Deploy the Amazon CloudWatch agent as a container sidecar. Configure a metric filter for the JVM thread count metric on the CloudWatch log group for the CloudWatch agent. Add a target tracking policy in Fargate. Select the metric from the metric filter as a scale target.

C. Create an Amazon Managed Service for Prometheus workspace. Deploy AWS Distro for OpenTelemetry as a container sidecar to publish the JVM metrics from port 9404 to the Prometheus workspace. Configure rules for the workspace to use the JVM thread count metric to scale the application. Add a step scaling policy in Fargate. Select the Prometheus rules to scale up and scaling down.

D. Create an Amazon Managed Service for Prometheus workspace. Deploy AWS Distro for OpenTelemetry as a container sidecar to retrieve JVM metrics from port 9404 to publish the JVM metrics from port 9404 to the Prometheus workspace. Add a target tracking policy in Fargate. Select the Prometheus metric as a scale target.

**Đáp án**: ___________

---

## Câu 29

**ID**: 283 | **Loại**: Single Choice

A company has an application that runs in a single AWS Region. The application runs on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster and connects to an Amazon Aurora MySQL cluster. The application is built in an AWS CodeBuild project. The container images are published to Amazon Elastic Container Registry (Amazon ECR).The company needs to replicate the state of the application for the container images and the database to a second Region.Which solution will meet these requirements in the MOST operationally efficient way?

A. Turn on Amazon S3 Cross-Region Replication (CRR) on the bucket that holds the ECR container images. Deploy the application to an EKS cluster in the second Region by referencing the new S3 bucket object URL for the container image in a Kubernetes deployment file. Configure a cross-Region Aurora Replica in the second Region. Configure the new application deployment to use the endpoints for the cross-Region Aurora Replica.

B. Create an Amazon EventBridge rule that reacts to image pushes to the ECR repository. Configure the EventBridge rule to invoke an AWS Lambda function to replicate the image to a new ECR repository in the second Region. Deploy the application to an EKS cluster in the second Region by referencing the new ECR repository in a Kubernetes deployment file. Configure a cross-Region Aurora Replica in the second Region. Configure the new application deployment to use the endpoints for the cross-Region Aurora Replica.

C. Turn on Cross-Region Replication to replicate the ECR repository to the second Region. Deploy the application to an EKS cluster in the second Region by referencing the new ECR repository in a Kubernetes deployment file. Configure an Aurora global database with clusters in the initial Region and the second Region. Configure the new application deployment to use the endpoints for the second Region's cluster in the Aurora global database.

D. Configure the CodeBuild project to also push the container image to an ECR repository in the second Region. Deploy the application to an EKS cluster in the second Region by referencing the new ECR repository in a Kubernetes deployment file. Configure an Aurora MySQL cluster in the second Region as the target for binary log replication from the Aurora MySQL cluster in the initial Region. Configure the new application deployment to use the endpoints for the second Region's cluster.

**Đáp án**: ___________

---

## Câu 30

**ID**: 284 | **Loại**: Single Choice

A company is building a serverless application that uses AWS Lambda functions to process data.A BeginResponse Lambda function initializes data in response to specific application events. The company needs to ensure that a large number of Lambda functions are invoked after the BeginResponse Lambda function runs. Each Lambda function must be invoked in parallel and depends on only the outputs of the BeginResponse Lambda function. Each Lambda function has retry logic for invocation and must be able to fine-tune concurrency without losing data.Which solution will meet these requirements with the MOST operational efficiency?

A. Create an Amazon Simple Notification Service (Amazon SNS) topic. Modify the BeginResponse Lambda function to publish to the SNS topic before the BeginResponse Lambda function finishes running. Subscribe all Lambda functions that need to invoke after the BeginResponse Lambda function runs to the SNS topic. Subscribe any new Lambda functions to the SNS topic.

B. Create an Amazon Simple Queue Service (Amazon SQS) queue for each Lambda function that needs to run after the BeginResponse Lambda function runs. Subscribe each Lambda function to its own SQS queue. Create an Amazon Simple Notification Service (Amazon SNS) topic. Subscribe each SQS queue to the SNS topic. Modify the BeginResponse function to publish to the SNS topic when it finishes running.

C. Create an Amazon Simple Queue Service (Amazon SQS) queue for each Lambda function that needs to run after the BeginResponse Lambda function runs. Subscribe the Lambda function to the SQS queue. Create an Amazon Simple Notification Service (Amazon SNS) topic for each SQS queue. Subscribe the SQS queues to the SNS topics. Modify the BeginResponse function to publish to the SNS topics when the function finishes running.

D. Create an AWS Step Functions Standard Workflow. Configure states in the workflow to invoke the Lambda functions sequentially. Create an Amazon Simple Notification Service (Amazon SNS) topic. Modify the BeginResponse Lambda function to publish to the SNS topic before the Lambda function finishes running. Create a new Lambda function that is subscribed to the SNS topic and that invokes the Step Functions workflow.

**Đáp án**: ___________

---

## Câu 31

**ID**: 285 | **Loại**: Single Choice

A company operates a globally deployed product out of multiple AWS Regions. The company's DevOps team needs to use Amazon API Gateway to deploy an API to support the product.The API must be deployed redundantly. The deployment must provide independent availability from each company location. The deployment also must respond to a custom domain URL and must optimize performance for the API user requests.Which solution will meet these requirements?

A. Deploy an API Gateway edge-optimized API endpoint in the us-east-1 Region. Create an API Gateway custom domain for the API. Create an Amazon Route 53 record set with a geoproximity routing policy for the API's custom domain. Increase the geographic bias to the maximum allowed value.

B. Deploy an API Gateway regional API endpoint in the us-east-1 Region. Integrate the API Gateway API with a public Application Load Balancer (ALB). Create an AWS Global Accelerator standard accelerator. Associate the endpoint with the ALCreate an Amazon Route 53 alias record set that points the custom domain name to the DNS name that is assigned to the accelerator.

C. Deploy an API Gateway regional API endpoint in every AWS Region where the company's product is deployed. Create an API Gateway custom domain in each Region for the deployed API Gateway API. Create an Amazon Route 53 record set that has a latency routing policy for every deployed API Gateway custom domain.

D. Deploy an API Gateway edge-optimized API endpoint in the us-east-1 Region. Create an Amazon CloudFront distribution. Configure the CloudFront distribution with an alternate domain name. Specify the API Gateway Invoke URL as the origin domain. Create an Amazon Route 53 alias record set with a simple routing policy. Point the routing policy to the CloudFront distribution domain name.

**Đáp án**: ___________

---

## Câu 32

**ID**: 286 | **Loại**: Single Choice

A DevOps engineer uses AWS CodeBuild to frequently produce software packages. The CodeBuild project builds large Docker images that the DevOps engineer can use across multiple builds.The DevOps engineer wants to improve build performance and minimize costs.Which solution will meet these requirements?

A. Store the Docker images in an Amazon Elastic Container Registry (Amazon ECR) repository. Implement a local Docker layer cache for CodeBuild.

B. Cache the Docker images in an Amazon S3 bucket that is available across multiple build hosts. Expire the cache by using an S3 Lifecycle policy.

C. Store the Docker images in an Amazon Elastic Container Registry (Amazon ECR) repository. Modify the CodeBuild project runtime configuration to always use the most recent image version.

D. Create custom AMIs that contain the cached Docker images. In the CodeBuild build, launch Amazon EC2 instances from the custom AMIs.

**Đáp án**: ___________

---

## Câu 33

**ID**: 287 | **Loại**: Single Choice

A large company recently acquired a small company. The large company invited the small company to join the large company's existing organization in AWS Organizations as a new OU.A DevOps engineer determines that the small company needs to launch t3.small Amazon EC2 instance types for the company's application workloads. The small company needs to deploy the instances only within US-based AWS Regions.The DevOps engineer needs to use an SCP in the small company's new OU to ensure that the small company can launch only the required instance types.Which solution will meet these requirements?

A. Configure a statement to deny the ec2:RunInstances action for all EC2 instance resources when the ec2:InstanceType condition is not equal to t3.small.Configure another statement to deny the ec2:RunInstances action for all EC2 instance resources when the aws:RequestedRegion condition is not equal to us-*.

B. Configure a statement to allow the ec2:RunInstances action for all EC2 instance resources when the ec2:InstanceType condition is not equal to t3.small.Configure another statement to allow the ec2:RunInstances action for all EC2 instance resources when the aws:RequestedRegion condition is not equal to us-*.

C. Configure a statement to deny the ec2:RunInstances action for all EC2 instance resources when the ec2:InstanceType condition is equal to t3.small.Configure another statement to deny the ec2:RunInstances action for all EC2 instance resources when the aws:RequestedRegion condition is equal to us-*.

D. Configure a statement to allow the ec2:RunInstances action for all EC2 instance resources when the ec2:InstanceType condition is equal to t3.small.Configure another statement to allow the ec2:RunInstances action for all EC2 instance resources when the aws:RequestedRegion condition is equal to us-*.

**Đáp án**: ___________

---

## Câu 34

**ID**: 288 | **Loại**: Single Choice

A DevOps team manages infrastructure for an application. The application uses long-running processes to process items from an Amazon Simple Queue Service (Amazon SQS) queue. The application is deployed to an Auto Scaling group.The application recently experienced an issue where items were taking significantly longer to process. The queue exceeded the expected size, which prevented various business processes from functioning properly. The application records all logs to a third-party tool.The team is currently subscribed to an Amazon Simple Notification Service (Amazon SNS) topic that the team uses for alerts. The team needs to be alerted if the queue exceeds the expected size.Which solution will meet these requirements with the MOST operational efficiency?

A. Create an Amazon CloudWatch metric alarm with a period of 1 hour and a static threshold to alarm if the average of the ApproximateNumberOfMessagesDelayed metric is greater than the expected value. Configure the alarm to notify the SNS topic.

B. Create an Amazon CloudWatch metric alarm with a period of 1 hour and a static threshold to alarm if the sum of the ApproximateNumberOfMessagesVisible metric is greater than the expected value. Configure the alarm to notify the SNS topic.

C. Create an AWS Lambda function that retrieves the ApproximateNumberOfMessages SQS queue attribute value and publishes the value as a new CloudWatch custom metric. Create an Amazon EventBridge rule that is scheduled to run every 5 minutes and that invokes the Lambda function. Configure a CloudWatch metrics alarm with a period of 1 hour and a static threshold to alarm if the sum of the new custom metric is greater than the expected value.

D. Create an AWS Lambda function that checks the ApproximateNumberOfMessagesDelayed SQS queue attribute and compares the value to a defined expected size in the function. Create an Amazon EventBridge rule that is scheduled to run every 5 minutes and that invokes the Lambda function. When the ApproximateNumberOfMessagesDelayed SQS queue attribute exceeds the expected size, send a notification the SNS topic.

**Đáp án**: ___________

---

## Câu 35

**ID**: 289 | **Loại**: Single Choice

A large company runs critical workloads in multiple AWS accounts. The AWS accounts are managed under AWS Organizations with all features enabled. The company stores confidential customer data in an Amazon S3 bucket. Access to the S3 bucket requires multiple levels of approval.The company wants to monitor when the S3 bucket is accessed by using the AWS CLI. The company also wants insights into the various activities performed by other users on all other S3 buckets in the AWS accounts to detect any issues.Which solution will meet these requirements?

A. Create an AWS CloudTrail trail that is delivered to Amazon CloudWatch in each AWS account. Enable data events logs for all S3 buckets. Use Amazon GuardDuty for anomaly detection in all the AWS accounts. Use Amazon Athena to perform SQL queries on the custom metrics created from the CloudTrail logs.

B. Create an AWS CloudTrail organization trail that is delivered to Amazon CloudWatch in the Organizations management account. Enable data events logs for all S3 buckets. Use Amazon CloudWatch anomaly detection in all the AWS accounts. Use Amazon Athena to perform SQL queries on the custom metrics created from the CloudTrail logs.

C. Create an AWS CloudTrail organization trail that is delivered to Amazon CloudWatch in the Organizations management account. Enable data events logs for all S3 buckets. Use Amazon CloudWatch anomaly detection in all the AWS accounts. Use Amazon CloudWatch Metrics Insights to perform SQL queries on the custom metrics created from the CloudTrail logs.

D. Create an AWS CloudTrail trail that is delivered to Amazon CloudWatch in each AWS account. Enable data events logs for all S3 buckets. Use a custom solution for anomaly detection in all the AWS accounts. Use Amazon CloudWatch Metrics Insights to perform SQL queries on the custom metrics created from the CloudTrail logs.

**Đáp án**: ___________

---

## Câu 36

**ID**: 290 | **Loại**: Single Choice

A DevOps team is deploying microservices for an application on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. The cluster uses managed node groups. The DevOps team wants to enable auto scaling for the microservice Pods based on a specific CPU utilization percentage. The DevOps team has already installed the Kubernetes Metrics Server on the cluster.Which solution will meet these requirements in the MOST operationally efficient way?

A. Edit the Auto Scaling group that is associated with the worker nodes of the EKS cluster. Configure the Auto Scaling group to use a target tracking scaling policy to scale when the average CPU utilization of the Auto Scaling group reaches a specific percentage.

B. Deploy the Kubernetes Horizontal Pod Autoscaler (HPA) and the Kubernetes Vertical Pod Autoscaler (VPA) in the cluster. Configure the HPA to scale based on the target CPU utilization percentage. Configure the VPA to use the recommender mode setting.

C. Run the AWS Systems Manager AWS-UpdateEKSManagedNodeGroup Automation document. Modify the values for NodeGroupDesiredSize, NodeGroupMaxSize, and NodeGroupMinSize to be based on an estimate for the required node size.

D. Deploy the Kubernetes Horizontal Pod Autoscaler (HPA) and the Kubernetes Cluster Autoscaler in the cluster. Configure the HPA to scale based on the target CPU utilization percentage. Configure the Cluster Autoscaler to use the auto-discovery setting.

**Đáp án**: ___________

---

## Câu 37

**ID**: 292 | **Loại**: Single Choice

A security team wants to use AWS CloudTrail to monitor all actions and API calls in multiple accounts that are in the same organization in AWS Organizations. The security team needs to ensure that account users cannot turn off CloudTrail in the accounts.Which solution will meet this requirement?

A. Apply an SCP to all OUs to deny the cloudtrail:StopLogging action and the cloudtrail:DeleteTrail action.

B. Create IAM policies in each account to deny the cloudtrail:StopLogging action and the cloudtrail:DeleteTrail action.

C. Set up Amazon CloudWatch alarms to notify the security team when a user disables CloudTrail in an account.

D. Use AWS Config to automatically re-enable CloudTrail if a user disables CloudTrail in an account.

**Đáp án**: ___________

---

## Câu 38

**ID**: 293 | **Loại**: Single Choice

A DevOps engineer needs to configure a blue/green deployment for an existing three-tier application. The application runs on Amazon EC2 instances and uses an Amazon RDS database. The EC2 instances run behind an Application Load Balancer (ALB) and are in an Auto Scaling group.The DevOps engineer has created launch templates, Auto Scaling groups, and ALB target groups for the blue environment and the green environment. Each target group specifies which application version, blue or green, will be loaded on the EC2 instances. An Amazon Route 53 record for www.example.com points to the ALB.The deployment must shift traffic all at once from the blue environment to the green environment.Which solution will meet these requirements?

A. Starta rolling restart of the Auto Scaling group for the green environment to deploy the new application version to the green environment's EC2 instances. When the rolling restart is complete, use an AWS CLI command to update the ALB to send traffic to the green environment's target group.

B. Use an AWS CLI command to update the ALB to send traffic to the green environments target group. Start a rolling restart of the Auto Scaling group for the green environment to deploy the new application version to the green environment's EC2 instances.

C. Update the launch template to deploy the green environment's application version to the blue environment's EC2 instances. Do not change the target groups or the Auto Scaling groups in either environment. Perform a rolling restart of the blue environments EC2 instances.

D. Starta rolling restart of the Auto Scaling group for the green environment to deploy the new application version to the green environment's EC2 instances. When the rolling restart is complete, update Route 53 to point to the green environment's endpoint on the ALB.

**Đáp án**: ___________

---

## Câu 39

**ID**: 294 | **Loại**: Single Choice

A company has an application that runs on Amazon EC2 instances in an Auto Scaling group. The application processes a high volume of messages from an Amazon Simple Queue Service (Amazon SQS) queue.A DevOps engineer noticed that the application took several hours to process a group of messages from the SQS queue. The average CPU utilization of the Auto Scaling group did not cross the threshold of a target tracking scaling policy when processing the messages. The application that processes the SQS queue publishes logs to ‘Amazon CloudWatch Logs.The DevOps engineer needs to ensure that the queue is processed quickly.Which solution meets these requirements with the LEAST operational overhead?

A. Create an AWS Lambda function. Configure the Lambda function to publish a custom metric by using the ApproximateNumberOfMessagesVisible SQS queue attribute and the GroupInServiceInstances Auto Scaling group attribute to publish the queue messages for each instance. Schedule an Amazon EventBridge rule to run the Lambda function every hour. Create a target tracking scaling policy for the Auto Scaling group that uses the custom metric to scale in and out.

B. Create an AWS Lambda function. Configure the Lambda function to publish a custom metric by using the ApproximateNumberOfMessagesVisible SQS queue attribute and the GroupInServiceInstances Auto Scaling group attribute to publish the queue messages for each instance. Create a CloudWatch subscription filter for the application logs with the Lambda function as the target. Create a target tracking scaling policy for the Auto Scaling group that uses the custom metric to scale in and out.

C. Create a target tracking scaling policy for the Auto Scaling group. In the target tracking policy, use the ApproximateNumberOfMessagesVisible SQS queue attribute and the GroupInServiceInstances Auto Scaling group attribute to calculate how many messages are in the queue for each number of instances by using metric math. Use the calculated attribute to scale in and out.

D. Create an AWS Lambda function that logs the ApproximateNumberOfMessagesVisible attribute of the SQS queue to a CloudWatch Logs log group. Schedule an Amazon EventBridge rule to run the Lambda function every 5 minutes. Create a metric filer to count the number of log events from a CloudWatch logs group. Create a target tracking scaling policy for the Auto Scaling group that uses the custom metric to scale in and out.

**Đáp án**: ___________

---

## Câu 40

**ID**: 295 | **Loại**: Single Choice

A company has a single AWS account that runs hundreds of Amazon EC2 instances in a single AWS Region. The company launches and terminates new EC2 instances every hour. The account includes existing EC2 instances that have been running for longer than a week.The company's security policy requires all running EC2 instances to have an EC2 instance profile attached. The company has created a default EC2 instance profile. The default EC2 instance profile must be attached to any EC2 instances that do not have a profile attached.Which solution will meet these requirements?

A. Configure an Amazon EventBridge rule that matches the Amazon EC2 RunInstances API calls. Configure the rule to invoke an AWS Lambda function to attach the default instance profile to the EC2 instances.

B. Configure AWS Config. Deploy an AWS Config ec2-instance-profile-attached managed rule. Configure an automatic remediation action that invokes an AWS Systems Manager Automation runbook to attach the default instance profile to the EC2 instances.

C. Configure an Amazon EventBridge rule that matches the Amazon EC2 StartInstances API calls. Configure the rule to invoke an AWS Systems Manager Automation runbook to attach the default instance profile to the EC2 instances.

D. Configure AWS Config. Deploy an AWS Config iam-role-managed-policy-check managed rule. Configure an automatic remediation action that invokes an AWS Lambda function to attach the default instance profile to the EC2 instances.

**Đáp án**: ___________

---

## Câu 41

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

## Câu 42

**ID**: 297 | **Loại**: Single Choice

A company uses an Amazon Aurora PostgreSQL global database that has two secondary AWS Regions. A DevOps engineer has configured the database parameter group to guarantee an RPO of 60 seconds. Write operations on the primary cluster are occasionally blocked because of the RPO setting.The DevOps engineer needs to reduce the frequency of blocked write operations.Which solution will meet these requirements?

A. Add an additional secondary cluster to the global database.

B. Enable write forwarding for the global database.

C. Remove one of the secondary clusters from the global database.

D. Configure synchronous replication for the global database.

**Đáp án**: ___________

---

## Câu 43

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

## Câu 44

**ID**: 299 | **Loại**: Single Choice

A company stores its Python-based application code in AWS CodeCommit. The company uses AWS CodePipeline to deploy the application. The CodeCommit repository and the CodePipeline pipeline are deployed to the same AWS account.The company's security team requires all code to be scanned for vulnerabilities before the code is deployed to production. If any vulnerabilities are found, the deployment must stop.Which solution will meet these requirements?

A. Create a new CodeBuild project. Configure the project to run a security scan on the code by using Amazon CodeGuru Security. Configure the CodeBuild project to raise an error if CodeGuru Security finds vulnerabilities. Create a new IAM role that has sufficient permissions to run CodeGuru Security scans. Assign the role to the CodeBuild project. In the CodePipeline pipeline, add a new stage before the deployment stage. Select AWS CodeBuild as the action provider for the new stage. Use the source artifact from the CodeCommit repository. Configure the action to use the CodeBuild project.

B. Create a new CodeBuild project. Configure the project to run a security scan on the code by using Amazon Inspector. Configure the CodeBuild project to raise an error if Amazon Inspector finds vulnerabilities. Create a new IAM role that has sufficient permissions to run Amazon Inspector scans. Assign the role to the CodeBuild project. In the CodePipeline pipeline, add a new stage before the deployment stage. Select AWS CodeBuild as the action provider for the new stage. Use the source artifact from the CodeCommit repository. Configure the action to use the CodeBuild project.

C. Update the IAM role that is attached to CodePipeline to include sufficient permissions to invoke Amazon DevOps Guru. In the CodePipeline pipeline, add a new stage before the deployment stage. Select DevOps Guru as the action provider for the new stage. Use the source artifact from the CodeCommit repository.

D. Update the IAM role that is attached to CodePipeline to include sufficient permissions to invoke Amazon DevOps Guru. In the CodePipeline pipeline, add a new stage before the deployment stage. Select CodeGuru Security as the action provider for the new stage. Use the source artifact from the CodeCommit repository.

**Đáp án**: ___________

---

## Câu 45

**ID**: 300 | **Loại**: Single Choice

A DevOps engineer deploys an application to a fleet of Amazon Linux EC2 instances. The DevOps engineer needs to monitor system metrics across the fleet. The DevOps engineer wants to monitor the relationship between network traffic and memory utilization for the application code. The DevOps engineer wants to track the data on a 60 second interval.Which solution will meet these requirements?

A. Use Amazon CloudWatch basic monitoring to collect the NetworkIn metric and the MemoryBytesUsed metric. Graph the metrics in CloudWatch.

B. Use Amazon CloudWatch detailed monitoring to collect the NetworkIn metric and the MemoryBytesUsed metric. Graph the metrics in CloudWatch.

C. Use Amazon CloudWatch detailed monitoring to collect the NetworkIn metric. Install the CloudWatch agent on the EC2 instances to collect the mem_used metric. Graph the metrics in CloudWatch.

D. Use Amazon CloudWatch basic monitoring to collect the built-in NetworkIn metric. Install the CloudWatch agent on the EC2 instances to collect the mem_used metric. Graph the metrics in CloudWatch.

**Đáp án**: ___________

---

## Câu 46

**ID**: 301 | **Loại**: Single Choice

A company uses AWS Systems Manager to manage a fleet of Amazon Linux EC2 instances that have SSM Agent installed. All EC2 instances are configured to use Instance Metadata Service Version 2 (IMDSv2) and are running in the same AWS account and AWS Region. Company policy requires developers to use only Amazon Linux.The company wants to ensure that all new EC2 instances are automatically managed by Systems Manager after creation.Which solution will meet these requirements with the MOST operational efficiency?

A. Create an IAM role that has a trust policy that allows Systems Manager to assume the role. Attach the AmazonSSMManagedEC2InstanceDefaultPolicy policy to the role. Configure the default-ec2-instance-management-role SSM service setting to use the role.

B. Ensure that AWS Config is set up. Create an AWS Config rule that validates if an EC2 instance has SSM Agent installed. Configure the rule to run on EC2 configuration changes. Configure automatic remediation for the rule to run the AWS-InstallSSMAgent SSM document to install SSM Agent.

C. Configure Systems Manager Patch Manager. Create a patch baseline that automatically installs SSM Agent on all new EC2 instances. Create a patch group for all EC2 instances. Attach the patch baseline to the patch group. Create a maintenance window and maintenance window task to start installing SSM Agent daily.

D. Create an EC2 instance role that has a trust policy that allows Amazon EC2 to assume the role. Attach the AmazonSSMManagedInstanceCore policy to the role. Ensure that AWS Config is set up. Use the ec2-instance-profile-attached managed AWS Config rule to validate if an EC2 instance has the role attached. Configure the rule to run on EC2 configuration changes. Configure automatic remediation for the rule to run the AWS-SetupManagedRoleOnEc2Instance SSM document to attach the role to the EC2 instance.

**Đáp án**: ___________

---

## Câu 47

**ID**: 302 | **Loại**: Single Choice

A company configured an Amazon S3 event source for an AWS Lambda function. The company needs the Lambda function to run when a new object is created or an existing object is modified in a specific S3 bucket. The Lambda function will use the S3 bucket name and the S3 object key of the incoming event to read the contents of the new or modified S3 object. The Lambda function will parse the contents and save the parsed contents to an Amazon DynamoDB table.The Lambda function's execution role has permissions to read from the S3 bucket and to write to the DynamoDB table. During testing, a DevOps engineer discovers that the Lambda function does not run when objects are added to the S3 bucket or when existing objects are modified.Which solution will resolve these problems?

A. Create an S3 bucket policy for the S3 bucket that grants the S3 bucket permission to invoke the Lambda function.

B. Create a resource policy for the Lambda function to grant Amazon S3 permission to invoke the Lambda function on the S3 bucket.

C. Configure an Amazon Simple Queue Service (Amazon SQS) queue as an OnFailure destination for the Lambda function. Update the Lambda function to process messages from the SQS queue and the S3 event notifications.

D. Configure an Amazon Simple Queue Service (Amazon SQS) queue as the destination for the S3 bucket event notifications. Update the Lambda function's execution role to have permission to read from the SQS queue. Update the Lambda function to consume messages from the SQS queue.

**Đáp án**: ___________

---

## Câu 48

**ID**: 303 | **Loại**: Multiple Choice

A company recently configured AWS Control Tower in its organization in AWS Organizations. The company enrolled all existing AWS accounts in AWS Control Tower. The company wants to ensure that all new AWS accounts are automatically enrolled in AWS Control Tower.The company has an existing AWS Step Functions workflow that creates new AWS accounts and performs any actions required as part of account creation. The Step Functions workflow is defined in the same AWS account as AWS Control Tower.Which combination of steps should the company add to the Step Functions workflow to meet these requirements? (Choose two.)

A. Create an Amazon EventBridge event that has an aws.controltower source and a CreateManagedAccount detail-type. Add the details of the new AWS account to the detail field of the event.

B. Create an Amazon EventBridge event that has an aws.controltower source and a SetupLandingZone detail-type. Add the details of the new AWS account to the detail field of the event.

C. Create an AWSControlTowerExecution role in the new AWS account. Configure the role to allow the AWS Control Tower administrator account to assume the role.

D. Call the AWS Service Catalog ProvisionProduct API operation with the details of the new AWS account.

E. Call the Organizations EnableAWSServiceAccess API operation with the controltower.amazonaws.com service name and the details of the new AWS account.

**Đáp án**: ___________

---

## Câu 49

**ID**: 304 | **Loại**: Single Choice

A company's web application uses an Application Load Balancer (ALB) to direct traffic to Amazon EC2 instances across three Availability Zones.The company has deployed a newer version of the application to one Availability Zone for testing. If a problem is detected with the application, the company wants to direct traffic away from the affected Availability Zone until the deployment has been rolled back. The application must remain available and maintain static stability during the rollback.Which solution will meet these requirements with the MOST operational efficiency?

A. Disable cross-zone load balancing on the ALB's target group. Initiate a zonal shift on the ALB to direct traffic away from the affected Availability Zone.

B. Disable cross-zone load balancing on the ALB's target group. Manually remove instances in the target group that belong to the affected Availability Zone.

C. Configure cross-zone load balancing on the ALB's target group to inherit settings from the ALB. Initiate a zonal shift on the ALB to direct traffic away from the affected Availability Zone.

D. Configure cross-zone load balancing on the ALB's target group to inherit settings from the ALB. Remove the subnet that is associated with the affected Availability Zone.

**Đáp án**: ___________

---

## Câu 50

**ID**: 305 | **Loại**: Single Choice

A company has several AWS accounts. An Amazon Connect instance runs in each account. The company uses an Amazon EventBridge default event bus in each account for event handling.A DevOps team needs to receive all the Amazon Connect events in a single DevOps account.Which solution meets these requirements?

A. Update the resource-based policy of the default event bus in each account to allow the DevOps account to replay events. Configure an EventBridge rule in the DevOps account that matches Amazon Connect events and has a target of the default event bus in the other accounts.

B. Update the resource-based policy of the default event bus in each account to allow the DevOps account to receive events. Configure an EventBridge rule in the DevOps account that matches Amazon Connect events and has a target of the default event bus in the other accounts.

C. Update the resource-based policy of the default event bus in the DevOps account. Update the policy to allow events to be received from the accounts. Configure an EventBridge rule in each account that matches Amazon Connect events and has a target of the DevOps account's default event bus.

D. Update the resource-based policy of the default event bus in the DevOps account. Update the policy to allow events to be replayed by the accounts. Configure an EventBridge rule in each account that matches Amazon Connect events and has a target of the DevOps account's default event bus.

**Đáp án**: ___________

---

## Câu 51

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

## Câu 52

**ID**: 307 | **Loại**: Single Choice

A company discovers that its production environment and disaster recovery (DR) environment are deployed to the same AWS Region. All the production applications run on Amazon EC2 instances and are deployed by AWS CloudFormation. The applications use an Amazon FSx for NetApp ONTAP volume for application storage. No application data resides on the EC2 instances.A DevOps engineer copies the required AMIs to a new DR Region. The DevOps engineer also updates the CloudFormation code to accept a Region as a parameter. The storage needs to have an RPO of 10 minutes in the DR Region.Which solution will meet these requirements?

A. Create an Amazon S3 bucket in both Regions. Configure S3 Cross-Region Replication (CRR) for the S3 buckets. Create a scheduled AWS Lambda function to copy any new content from the FSx for ONTAP volume to the S3 bucket in the production Region.

B. Use AWS Backup to create a backup vault and a custom backup plan that has a 10-minute frequency. Specify the DR Region as the target Region. Assign the EC2 instances in the production Region to the backup plan.

C. Create an AWS Lambda function to create snapshots of the instance store volumes that are attached to the EC2 instances. Configure the Lambda function to copy the snapshots to the DR Region and to remove the previous copies. Create an Amazon EventBridge scheduled rule that invokes the Lambda function every 10 minutes.

D. Create an FSx for ONTAP instance in the DR Region. Configure a 5-minute schedule for a volume-level NetApp SnapMirror to replicate the volume from the production Region to the DR Region.

**Đáp án**: ___________

---

## Câu 53

**ID**: 308 | **Loại**: Single Choice

During a security audit, a company discovered that some security groups allow SSH traffic from 0.0.0.0/0. A security team must implement a solution to detect and remediate this issue as soon as possible. The company uses one organization in AWS Organizations to manage all the company's AWS accounts.Which solution will meet these requirements?

A. Enable AWS Config for all AWS accounts. Use a periodic trigger to activate the vpe-sg-port-restriction-check AWS Config rule. Create an AWS Lambda function to remediate any noncompliant rules.

B. Create an AWS Lambda function in each AWS account to delete all the security group rules. Create an Amazon EventBridge rule to match security group update events or creation events. Set the Lambda function in each account as a target for the rule.

C. Enable AWS Config for all AWS accounts. Create a custom AWS Config rule to run on the restricted-ssh configuration change trigger. Configure the rule to invoke an AWS Lambda function to remediate any noncompliant resources.

D. Create an AWS Systems Manager Automation document in each account to inspect all security groups and to delete noncompliant rules. Use an Amazon EventBridge rule to run the Automation document every hour.

**Đáp án**: ___________

---

## Câu 54

**ID**: 309 | **Loại**: Single Choice

A company's DevOps engineer must install a software package on 30 on-premises VMs and 15 Amazon EC2 instances.The DevOps engineer needs to ensure that all VMs receive the package in a process that is auditable and that any configuration drift on the VMs is automatically identified and alerted on. The company uses AWS Direct Connect to connect its on-premises data center to AWS.Which solution will meet these requirements with the MOST operational efficiency?

A. Write a script that iterates through the list of VMs once a week. Configure the script to check for the package and install the package if the package is not found. Configure the script to send an email message notification to the system administrator if the package is not found.

B. Install the AWS Systems Manager Agent (SSM Agent) on all VMs. Use the SSM Agent to install the package. Use AWS Config to monitor for configuration drift. Use Amazon Simple Notification Service (Amazon SNS) to notify the system administrator if any drift is found.

C. Write a script that checks if the package is installed across the environment. Configure the script to create a list of all VMs that are noncompliant. Configure the script to send the list to the system administrator, who will install the package on the noncompliant VMs.

D. Log in to each VM. Use a local package manager to install the package. Use AWS Config to monitor the AWS resources for configuration changes. Write a script to monitor the on-premises resources.

**Đáp án**: ___________

---

## Câu 55

**ID**: 310 | **Loại**: Multiple Choice

A company has an AWS CodePipeline pipeline in the eu-west-1 Region. The pipeline stores the build artifacts in an Amazon S3 bucket. The pipeline builds and deploys an AWS Lambda function by using an AWS CloudFormation deploy action.A DevOps engineer needs to update the existing pipeline to also deploy the Lambda function to the us-east-1 Region. The pipeline has already been updated to create an additional artifact to deploy to us-east-1.Which combination of steps should the DevOps engineer take to meet these requirements? (Choose two.)

A. Modify the CloudFormation template to include a parameter for the Lambda function code's .zip file location. Create a new CloudFormation deploy action for us-east-1 in the pipeline. Configure the new deploy action to pass in the us-east-1 artifact location as a parameter override.

B. Create a new CloudFormation deploy action for us-east-1 in the pipeline. Configure the new deploy action to use the CloudFormation template from the additional artifact that was created for us-east-1.

C. Create an S3 bucket in us-east-1. Configure the S3 bucket policy to allow CodePipeline to have read and write access.

D. Create an S3 bucket in us-east-1. Configure S3 Cross-Region Replication (CRR) from the S3 bucket in eu-west-1 to the S3 bucket in us-east-1.

E. Modify the pipeline to include the S3 bucket for us-east-1 as an artifact store. Create a new CloudFormation deploy action for us-east-1 in the pipeline. Configure the new deploy action to use the CloudFormation template from the us-east-1 artifact.

**Đáp án**: ___________

---

## Câu 56

**ID**: 311 | **Loại**: Single Choice

A company uses an AWS Cloud Development Kit (AWS CDK) application for its infrastructure. The AWS CDK application creates AWS Lambda functions and the IAM roles that are attached to the functions. The company also uses AWS Organizations. The company's developers can assume the AWS CDK application deployment role.The company's security team discovered that the developers and the role used to deploy the AWS CDK application have more permissions than necessary. The security team also discovered that the roles attached to the Lambda functions that the CDK application creates have more permissions than necessary. The developers must not have the ability to grant additional permissions.Which solution will meet these requirements with the LEAST operational overhead?

A. Create an SCP that denies the iam:CreateRole action and the iam:UpdateRole action for the developer role and the AWS CDK application deployment role. Centrally create new IAM roles to attach to the Lambda functions for the developers to use to provision Lambda functions.

B. Create an IAM permission boundary policy. Define the maximum actions that the AWS CDK application requires in the policy. Update the account's AWS CDK bootstrapping to use the permission boundary. Update the configuration in the AWS CDK application for the default permissions boundary to use the policy.

C. Create an IAM permission boundary policy. Define the maximum actions that the AWS CDK application requires in the policy. Instruct the developers to use the permission boundary policy name when they create a role in the AWS CDK application code.

D. Create an SCP that denies the iam:CreateRole action and the iam:UpdateRole action for the developer role. Give the AWS CDK deployment role access to create roles associated with Lambda functions. Run AWS Identity and Access Management Access Analyzer to verify that the Lambda functions role does not have permissions.

**Đáp án**: ___________

---

## Câu 57

**ID**: 312 | **Loại**: Single Choice

A company uses Amazon Elastic Container Registry (Amazon ECR) private registries to store container images.A DevOps team needs to ensure that the container images are regularly scanned for software package vulnerabilities.Which solution will meet this requirement?

A. Enable enhanced scanning for private registries in Amazon ECR.

B. Enable basic continuous scanning for private registries in Amazon ECR.

C. Create an AWS System Manager Automation document to scan images by using the AWS SDK. Configure the Automation document to run when a new image is pushed to an ECR registry.

D. Create an AWS Lambda function that scans all images in Amazon ECR by using the AWS SDK. Create an Amazon EventBridge rule to invoke the Lambda function each day.

**Đáp án**: ___________

---

## Câu 58

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

## Câu 59

**ID**: 314 | **Loại**: Single Choice

A company's DevOps engineer uses AWS Systems Manager to perform maintenance tasks. The company has a few Amazon EC2 instances that require a restart after notifications from AWS Health.The DevOps engineer must implement an automated solution that uses Amazon EventBridge to remediate the notifications during the company's scheduled maintenance windows.How should the DevOps engineer configure an EventBridge rule to meet these requirements?

A. Configure an event source of AWS Health. Configure event types that indicate scheduled instance termination and retirement. Target the AWS-RestartEC2Instance Systems Manager Automation runbook to restart the EC2 instances.

B. Configure an event source of Systems Manager. Configure an event type that indicates a maintenance window. Target the AWS-RestartEC2Instance Systems Manager Automation runbook to restart the EC2 instances.

C. Configure an event source of AWS Health. Configure event types that indicate scheduled instance termination and retirement. Target a newly created AWS Lambda function that registers a Systems Manager maintenance window task to restart the EC2 instances.

D. Configure an event source of EC2. Configure an event type that indicates instance state notification. Target a newly created AWS Lambda function that registers a Systems Manager maintenance window task to restart the EC2 instances.

**Đáp án**: ___________

---

## Câu 60

**ID**: 315 | **Loại**: Single Choice

A DevOps engineer manages an AWS CodePipeline pipeline that builds and deploys a web application on AWS. The pipeline has a source stage, a build stage, and a deploy stage. When deployed properly, the web application responds with a 200 OK HTTP response code when the URL of the home page is requested.The home page recently returned a 503 HTTP response code after CodePipeline deployed the application. The DevOps engineer needs to add an automated test into the pipeline. The automated test must ensure that the application returns a 200 OK HTTP response code after the application is deployed. The pipeline must fail if the response code is not present during the test. The DevOps engineer has added a CheckURL stage after the deploy stage in the pipeline.What should the DevOps engineer do next to implement the automated test?

A. Configure the CheckURL stage to use an Amazon CloudWatch action. Configure the action to use a canary synthetic monitoring check on the application URL and to report a success or failure to CodePipeline.

B. Create an AWS Lambda function to check the response code status of the URL and to report a success or failure to CodePipeline. Configure an action in the CheckURL stage to invoke the Lambda function.

C. Configure the CheckURL stage to use an AWS CodeDeploy action. Configure the action with an input artifact that is the URL of the application and to report a success or failure to CodePipeline.

D. Deploy an Amazon API Gateway HTTP API that checks the response code status of the URL and that reports success or failure to CodePipeline. Configure the CheckURL stage to use the AWS Device Farm test action and to provide the API Gateway HTTP API as an input artifact.

**Đáp án**: ___________

---

## Câu 61

**ID**: 316 | **Loại**: Single Choice

A company has an application that uploads access logs to an Amazon CloudWatch Logs log group. The fields in the log lines include the response code and the application name.The company wants to create a CloudWatch metric to track the number of requests by response code in a specific range and with a specific application name.Which solution will meet these requirements?

A. Create a CloudWatch Logs log event filter on the CloudWatch Logs log stream to match the response code range. Configure the log event filter to increment a metric. Set the response code and application name as dimensions.

B. Create a CloudWatch Logs metric filter on the CloudWatch Logs log group to match the response code range. Configure the metric filter to increment a metric. Set the response code and application name as dimensions.

C. Create a CloudWatch Contributor Insights rule on the CloudWatch Logs log stream with a filter to match the response code range. Configure the Contributor Insights rule to increment a CloudWatch metric with the response code and application name as dimensions.

D. Create a CloudWatch Logs Insights query on the CloudWatch Logs log group to match the response code range. Configure the Logs Insights query to increment a CloudWatch metric with the response code and application name as dimensions.

**Đáp án**: ___________

---

## Câu 62

**ID**: 317 | **Loại**: Single Choice

A DevOps engineer provisioned an Amazon Elastic Kubernetes Service (Amazon EKS) cluster with managed node groups. The DevOps engineer associated an OpenID Connect (OIDC) issuer with the cluster.The DevOps engineer is configuring Amazon Elastic Block Store (Amazon EBS) General Purpose SSD (gp3) volumes for the cluster. The DevOps engineer attempts to initiate a PersistentVolumeClaim (PVC) request but is unable to provision a volume. To troubleshoot the issue, the DevOps engineer runs the kubectl describe pyc command. The DevOps engineer receives a failed to provision volume with StorageClass error and a could not create volume in EC2:UnauthorizedOperation error.Which solution will resolve these errors?

A. Create a Kubernetes cluster role that allows the persistent volumes to perform get, list, watch, create, and delete operations. Configure the cluster role to allow get, list, and watch operations for storage in the cluster.

B. Create an Amazon EBS Container Storage Interface (CSI) driver IAM role that has the required permissions and trust relationships. Attach the IAM role to the Amazon EBS CSI driver add-on in the cluster.

C. Add the ebs.csi.aws.com/volumeType:gp3 annotation to the PersistentVolumeClaim object in the cluster.

D. Create a Kubernetes storage class object. Set the provisioner value to ebs.csi.aws.com. Set the volumeBindingMode value to WaitForFirstConsumer in the luster.

**Đáp án**: ___________

---

## Câu 63

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

## Câu 64

**ID**: 319 | **Loại**: Single Choice

A company is using Amazon Elastic Kubernetes Service (Amazon EKS) to run its applications. The EKS cluster is successfully running multiple pods. The company stores the pod images in Amazon Elastic Container Registry (Amazon ECR).The company needs to configure Pod Identity access for the EKS cluster. The company has already updated the node IAM role by using the permissions for Pod Identity access.Which solution will meet these requirements?

A. Create an IAM OpenID Connect (OIDC) provider for the EKS cluster.

B. Ensure that the nodes can reach the EKS Auth API. Add and configure the EKS Pod Identity Agent add-on for the EKS cluster.

C. Create an EKS access entry that uses the API_AND-CONFIG_MAP cluster authentication mode.

D. Configure the AWS Security Token Service (AWS STS) endpoint for the Kubernetes service account that the pods in the EKS cluster use.

**Đáp án**: ___________

---

## Câu 65

**ID**: 320 | **Loại**: Single Choice

A company has multiple AWS accounts in an organization in AWS Organizations that has all features enabled. The company’s DevOps administrator needs to improve security across all the company's AWS accounts. The administrator needs to identify the top users and roles in use across all accounts.Which solution will meet these requirements with the MOST operational efficiency?

A. Create a new organization trail in AWS CloudTrail. Configure the trail to send log events to Amazon CloudWatch Logs. Create a CloudWatch Contributor Insights rule for the userIdentity.arn log field. View the results in CloudWatch Contributor Insights.

B. Create an unused access analysis for the organization by using AWS Identity and Access Management Access Analyzer. Review the analyzer results and determine if each finding has the intended level of permissions required for the workload.

C. Create a new organization trail in AWS CloudTrail. Create a table in Amazon Athena that uses partition projection. Load the Athena table with CloudTrail data. Query the Athena table to find the top users and roles.

D. Generate a Service access report for each account by using Organizations. From the results, pull the last accessed date and last accessed by account fields to find the top users and roles.

**Đáp án**: ___________

---

## Câu 66

**ID**: 321 | **Loại**: Single Choice

A company has an organization in AWS Organizations with many Oils that contain many AWS accounts. The organization has a dedicated delegated administrator AWS account.The company needs the accounts in one OU to have server-side encryption enforced for all Amazon Elastic Block Store (Amazon EBS) volumes and Amazon Simple Queue Service (Amazon SQS) queues that are created or updated on an AWS CloudFormation stack.Which solution will enforce this policy before a CloudFormation stack operation in the accounts of this OU?

A. Activate trusted access to CloudFormation StackSets. Create a CloudFormation Hook that enforces server-side encryption on EBS volumes and SQS queues. Deploy the Hook across the accounts in the OU by using StackSets.

B. Set up AWS Config in all the accounts in the OU. Use AWS Systems Manager to deploy AWS Config rules that enforce server-side encryption for EBS volumes and SQS queues across the accounts in the OU.

C. Write an SCP to deny the creation of EBS volumes and SQS queues unless the EBS volumes and SQS queues have server-side encryption. Attach the SCP to the OU.

D. Create an AWS Lambda function in the delegated administrator account that checks whether server-side encryption is enforced for EBS volumes and SQS queues. Create an IAM role to provide the Lambda function access to the accounts in the OU.

**Đáp án**: ___________

---

## Câu 67

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

## Câu 68

**ID**: 323 | **Loại**: Multiple Choice

A company has a continuous integration pipeline where the company creates container images by using AWS CodeBuild. The created images are stored in Amazon Elastic Container Registry (Amazon ECR).Checking for and fixing the vulnerabilities in the images takes the company too much time. The company wants to identify the image vulnerabilities quickly and notify the security team of the vulnerabilities.Which combination of steps will meet these requirements with the LEAST operational overhead? (Choose two.)

A. Activate Amazon Inspector enhanced scanning for Amazon ECR. Configure the enhanced scanning to use continuous scanning. Set up a topic in Amazon Simple Notification Service (Amazon SNS).

B. Create an Amazon EventBridge rule for Amazon Inspector findings. Set an Amazon Simple Notification Service (Amazon SNS) topic as the rule target.

C. Activate AWS Lambda enhanced scanning for Amazon ECR. Configure the enhanced scanning to use continuous scanning. Set up a topic in Amazon Simple Email Service (Amazon SES).

D. Create a new AWS Lambda function. Invoke the new Lambda function when scan findings are detected.

E. Activate default basic scanning for Amazon ECR for all container images. Configure the default basic scanning to use continuous scanning. Set up a topic in Amazon Simple Notification Service (Amazon SNS).

**Đáp án**: ___________

---

## Câu 69

**ID**: 324 | **Loại**: Single Choice

A DevOps administrator is configuring a repository to store a company's container images. The administrator needs to configure a lifecycle rule that automatically deletes container images that have a specific tag and that are older than 15 days.Which solution will meet these requirements with the MOST operational efficiency?

A. Create a repository in Amazon Elastic Container Registry (Amazon ECR). Add a lifecycle policy to the repository to expire images that have the matching tag after 15 days.

B. Create a repository in AWS CodeArtifact. Add a repository policy to the CodeArtifact repository to expire old assets that have the matching tag after 15 days.

C. Create a bucket in Amazon S3. Add a bucket lifecycle policy to expire old objects that have the matching tag after 15 days

D. Create an EC2 Image Builder container recipe. Add a build component to expire the container that has the matching tag after 15 days.

**Đáp án**: ___________

---

## Câu 70

**ID**: 325 | **Loại**: Multiple Choice

A company uses Amazon Redshift as its data warehouse solution. The company wants to create a dashboard to view changes to the Redshift users and the queries the users perform.Which combination of steps will meet this requirement? (Choose two.)

A. Create an Amazon CloudWatch log group. Create an AWS CloudTrail trail that writes to the CloudWatch log group.

B. Create a new Amazon S3 bucket. Configure default audit logging on the Redshift cluster. Configure the S3 bucket as the target.

C. Configure the Redshift cluster database audit logging to include user activity logs. Configure Amazon CloudWatch as the target.

D. Create an Amazon CloudWatch dashboard that has a log widget. Configure the widget to display user details from the Redshift logs.

E. Create an AWS Lambda function that uses Amazon Athena to query the Redshift logs. Create an Amazon CloudWatch dashboard that has a custom widget type that uses the Lambda function.

**Đáp án**: ___________

---

## Câu 71

**ID**: 326 | **Loại**: Single Choice

A company uses an organization in AWS Organizations to manage its 500 AWS accounts. The organization has all features enabled. The AWS accounts are in a single OU. The developers need to use the CostCenter tag key for all resources in the organization's member accounts. Some teams do not use the CostCenter tag key to tag their Amazon EC2 instances.The cloud team wrote a script that scans all EC2 instances in the organization's member accounts. If the EC2 instances do not have a CostCenter tag key, the script will notify AWS account administrators. To avoid this notification, some developers use the CostCenter tag key with an arbitrary string in the tag value.The cloud team needs to ensure that all EC2 instances in the organization use a CostCenter tag key with the appropriate cost center value.Which solution will meet these requirements?

A. Create an SCP that prevents the creation of EC2 instances without the CostCenter tag key. Create a tag policy that requires the CostCenter tag to be values from a known list of cost centers for all EC2 instances. Attach the policy to the OU. Update the script to scan the tag keys and tag values. Modify the script to update noncompliant resources with a default approved tag value for the CostCenter tag key.

B. Create an SCP that prevents the creation of EC2 instances without the CostCenter tag key. Attach the policy to the OU. Update the script to scan the tag keys and tag values and notify the administrators when the tag values are not valid.

C. Create an SCP that prevents the creation of EC2 instances without the CostCenter tag key. Attach the policy to the OU. Create an IAM permission boundary in the organization's member accounts that restricts the CostCenter tag values to a list of valid cost centers.

D. Create a tag policy that requires the CostCenter tag to be values from a known list of cost centers for all EC2 instances. Attach the policy to the OU. Configure an AWS Lambda function that adds an empty CostCenter tag key to an EC2 instance. Create an Amazon EventBridge rule that matches events to the RunInstances API action with the Lambda function as the target.

**Đáp án**: ___________

---

## Câu 72

**ID**: 327 | **Loại**: Multiple Choice

A DevOps engineer uses a pipeline in AWS CodePipeline. The pipeline has a build action and a deploy action for a single-page web application that is delivered to an Amazon S3 bucket. Amazon CloudFront serves the web application. The build action creates an artifact for the web application.The DevOps engineer has created an AWS CloudFormation template that defines the S3 bucket and configures the S3 bucket to host the application. The DevOps engineer has configured a CloudFormation deploy action before the S3 action. The CloudFormation deploy action creates the S3 bucket. The DevOps engineer needs to configure the S3 deploy action to use the S3 bucket from the CloudFormation template.Which combination of steps will meet these requirements? (Choose two.)

A. Add an output named BucketName to the CloudFormation template. Set the output's value to refer to the S3 bucket from the CloudFormation template. Configure the output value to export to an AWS::SSM::Parameter resource named Stackvariables.

B. Add an output named BucketName to the CloudFormation template. Set the output's value to refer to the S3 bucket from the CloudFormation template. Set the CloudFormation action's namespace to StackVariables in the pipeline.

C. Configure the output artifacts of the CloudFormation action in the pipeline to be an AWS Systems Manager Parameter Store parameter named StackVariables. Name the artifact BucketName.

D. Configure the build artifact from the build action as the input to the CodePipeline S3 deploy action. Configure the deploy action to deploy to the S3 bucket by using the StackVariables.BucketName variable.

E. Configure the build artifact from the build action and the AWS Systems Manager parameter as the inputs to the deploy action. Configure the deploy action to deploy to the S3 bucket by using the StackVariables.BucketName variable.

**Đáp án**: ___________

---

## Câu 73

**ID**: 328 | **Loại**: Single Choice

A company used a lift and shift strategy to migrate a workload to AWS. The company has an Auto Scaling group of Amazon EC2 instances. Each EC2 instance runs a web application, a database, and a Redis cache.Users are experiencing large variations in the web application's response times. Requests to the web application go to a single EC2 instance that is under significant load. The company wants to separate the application components to improve availability and performance.Which solution will meet these requirements?

A. Create a Network Load Balancer and an Auto Scaling group for the web application. Migrate the database to an Amazon Aurora Serverless database. Create an Application Load Balancer and an Auto Scaling group for the Redis cache.

B. Create an Application Load Balancer and an Auto Scaling group for the web application. Migrate the database to an Amazon Aurora database that has a Multi-AZ deployment. Create a Network Load Balancer and an Auto Scaling group in a single Availability Zone for the Redis cache.

C. Create a Network Load Balancer and an Auto Scaling group for the web application. Migrate the database to an Amazon Aurora Serverless database. Create an Amazon ElastiCache (Redis OSS) cluster for the cache. Create a target group that has a DNS target type that contains the ElastiCache (Redis OSS) cluster hostname.

D. Create an Application Load Balancer and an Auto Scaling group for the web application. Migrate the database to an Amazon Aurora database that has a Multi-AZ deployment. Create an Amazon ElastiCache (Redis OSS) cluster for the cache.

**Đáp án**: ___________

---

## Câu 74

**ID**: 329 | **Loại**: Single Choice

A company is using AWS Organizations and wants to implement a governance strategy with the following requirements:• AWS resource access is restricted to the same two Regions for all accounts.• AWS services are limited to a specific group of authorized services for all accounts.• Authentication is provided by Active Directory.• Access permissions are organized by job function and are identical in each account.Which solution will meet these requirements?

A. Establish an organizational unit (OU) with group policies in the management account to restrict Regions and authorized services. Use AWS CloudFormation StackSets to provision roles with permissions for each job function, including an IAM trust policy for IAM identity provider authentication in each account.

B. Establish a permission boundary in the management account to restrict Regions and authorized services. Use AWS CloudFormation StackSets to provision roles with permissions for each job function, including an IAM trust policy for IAM identity provider authentication in each account.

C. Establish a service control policy in the management account to restrict Regions and authorized services. Use AWS Resource Access Manager (AWS RAM) to share management account roles with permissions for each job function, including AWS IAM Identity Center for authentication in each account.

D. Establish a service control policy in the management account to restrict Regions and authorized services. Use AWS CloudFormation StackSets to provision roles with permissions for each job function, including an IAM trust policy for IAM identity provider authentication in each account.

**Đáp án**: ___________

---

## Câu 75

**ID**: 330 | **Loại**: Single Choice

A company detects unusual login attempts in many of its AWS accounts. A DevOps engineer must implement a solution that sends a notification to the company's security team when multiple failed login attempts occur. The DevOps engineer has already created an Amazon Simple Notification Service (Amazon SNS) topic and has subscribed the security team to the SNS topic.Which solution will provide the notification with the LEAST operational effort?

A. Configure AWS CloudTrail to send management events to an Amazon CloudWatch Logs log group. Create a CloudWatch Logs metric filter to match failed ConsoleLogin events. Create a CloudWatch alarm that is based on the metric filter. Configure an alarm action to send messages to the SNS topic.

B. Configure AWS CloudTrail to send management events to an Amazon S3 bucket. Create an Amazon Athena query that returns a failure if the query finds failed logins in the logs in the S3 bucket. Create an Amazon EventBridge rule to periodically run the query. Create a second EventBridge rule to detect when the query fails and to send a message to the SNS topic.

C. Configure AWS CloudTrail to send data events to an Amazon CloudWatch Logs log group. Create a CloudWatch logs metric filter to match failed ConsoleLogin events. Create a CloudWatch alarm that is based on the metric filter. Configure an alarm action to send messages to the SNS topic.

D. Configure AWS CloudTrail to send data events to an Amazon S3 bucket. Configure an Amazon S3 event notification for the s3:ObjectCreated event type. Filter the event type by ConsoleLogin failed events. Configure the event notification to forward to the SNS topic.

**Đáp án**: ___________

---

## Câu 76

**ID**: 331 | **Loại**: Single Choice

A company has deployed a new REST API by using Amazon API Gateway. The company uses the API to access confidential data. The API must be accessed from only specific VPCs in the company.Which solution will meet these requirements?

A. Create and attach a resource policy to the API Gateway API. Configure the resource policy to allow only the specific VPC IDs.

B. Add a security group to the API Gateway API. Configure the inbound rules to allow only the specific VPC IP address ranges.

C. Create and attach an IAM role to the API Gateway API. Configure the IAM role to allow only the specific VPC IDs.

D. Add an ACL to the API Gateway API. Configure the outbound rules to allow only the specific VPC IP address ranges.

**Đáp án**: ___________

---

## Câu 77

**ID**: 332 | **Loại**: Single Choice

A company runs a website by using an Amazon Elastic Container Service (Amazon ECS) service that is connected to an Application Load Balancer (ALB). The service was in a steady state with tasks responding to requests successfully.A DevOps engineer updated the task definition with a new container image and deployed the new task definition to the service. The DevOps engineer noticed that the service is frequently stopping and starting new tasks because the ALB healtth checks are failing.What should the DevOps engineer do to troubleshoot the failed deployment?

A. Ensure that a security group associated with the service allows traffic from the ALB.

B. Increase the ALB health check grace period for the service.

C. Increase the service minimum healthy percent setting.

D. Decrease the ALB health check interval.

**Đáp án**: ___________

---

## Câu 78

**ID**: 333 | **Loại**: Single Choice

A company that uses electronic patient health records runs a fleet of Amazon EC2 instances with an Amazon Linux operating system. The company must continuously ensure that the EC2 instances are running operating system patches and application patches that are in compliance with current privacy regulations. The company uses a custom repository to store application patches.A DevOps engineer needs to automate the deployment of operating system patches and application patches. The DevOps engineer wants to use both the default operating system patch repository and the custom patch repository.Which solution will meet these requirements with the LEAST effort?

A. Use AWS Systems Manager to create a new custom patch baseline that includes the default operating system repository and the custom repository. Run the AWS-RunPatchBaseline document by using the Run command to verify and install patches. Use the BaselineOverride API to configure the new custom patch baseline.

B. Use AWS Direct Connect to integrate the custom repository with the EC2 instances. Use Amazon EventBridge events to deploy the patches.

C. Use the yum-config-manager command to add the custom repository to the /etc/yum.repos.d configuration. Run the yum-config-manager-enable command to activate the new repository.

D. Use AWS Systems Manager to create a patch baseline for the default operating system repository and a second patch baseline for the custom repository. Run the AWS-RunPatchBaseline document by using the Run command to verify and install patches. Use the BaselineOverride API to configure the default patch baseline and the custom patch baseline.

**Đáp án**: ___________

---

## Câu 79

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

## Câu 80

**ID**: 335 | **Loại**: Single Choice

A company runs an application in an Auto Scaling group of Amazon EC2 instances behind an Application Load Balancer (ALB). The EC2 instances run Docker containers that make requests to a MySQL database that runs on separate EC2 instances.A DevOps engineer needs to update the application to use a serverless architecture.Which solution will meet this requirement with the FEWEST changes?

A. Replace the containers that run on EC2 instances and the ALB with AWS Lambda functions. Replace the MySQL database with an Amazon Aurora Serverless v2 database that is compatible with MySQL.

B. Replace the containers that run on EC2 instances with AWS Fargate. Replace the MySQL database with an Amazon Aurora Serverless v2 database that is compatible with MySQL.

C. Replace the containers that run on EC2 instances and the ALB with AWS Lambda functions. Replace the MySQL database with Amazon DynamoDB tables.

D. Replace the containers that run on EC2 instances with AWS Fargate. Replace the MySQL database with Amazon DynamoDB tables.

**Đáp án**: ___________

---

## Câu 81

**ID**: 336 | **Loại**: Single Choice

A company uses an organization in AWS Organizations to manage 10 AWS accounts. All features are enabled, and trusted access for AWS CloudFormation is enabled.A DevOps engineer needs to use CloudFormation to deploy an IAM role to the Organizations management account and all member accounts in the organization.Which solution will meet these requirements with the LEAST operational overhead?

A. Create a CloudFormation StackSet that has service-managed permissions. Set the root OU as a deployment target.

B. Create a CloudFormation StackSet that has service-managed permissions. Set the root OU as a deployment target. Deploy a separate CloudFormation stack in the Organizations management account.

C. Create a CloudFormation StackSet that has self-managed permissions. Set the root OU as a deployment target.

D. Create a CloudFormation StackSet that has self-managed permissions. Set the root OU as a deployment target. Deploy a separate CloudFormation stack in the Organizations management account.

**Đáp án**: ___________

---

## Câu 82

**ID**: 337 | **Loại**: Multiple Choice

A company runs an application that stores artifacts in an Amazon S3 bucket. The application has a large user base. The application writes a high volume of objects to the S3 bucket. The company has enabled event notifications for the S3 bucket.When the application writes an object to the S3 bucket, several processing tasks need to be performed simultaneously. The company's DevOps team needs to create an AWS Step Functions workflow to orchestrate the processing tasks.Which combination of steps should the DevOps team take to meet these requirements with the LEAST operational overhead? (Choose two.)

A. Create a Standard workflow that contains a parallel state that defines the processing tasks. Create an Asynchronous Express workflow that contains a parallel state that defines the processing tasks.

B. Create a Synchronous Express workflow that contains a map state that defines the processing tasks.

C. Create an Amazon EventBridge rule to match when a new S3 object is created. Configure the EventBridge rule to invoke an AWS Lambda function. Configure the Lambda function to start the processing workflow.

D. Create an Amazon EventBridge rule to match when a new S3 object is created. Configure the EventBridge rule to start the processing workflow.

**Đáp án**: ___________

---

## Câu 83

**ID**: 338 | **Loại**: Multiple Choice

A DevOps team supports an application that runs in an Amazon Elastic Container Service (Amazon ECS) cluster behind an Application Load Balancer (ALB). Currently, the DevOps team uses AWS CodeDeploy to deploy the application by using a blue/green all-at-once strategy. Recently, the DevOps team had to roll back a deployment when a new version of the application dramatically increased response times for requests.The DevOps team needs use to a deployment strategy that will allow the team to monitor a new version of the application before the team shifts all traffic to the new version. If a new version of the application increases response times, the deployment should be rolled back as quickly as possible.Which combination of steps will meet these requirements? (Choose two.)

A. Modify the CodeDeploy deployment to use the CodeDeployDefault.ECSCanary10Percent5Minutes configuration.

B. Modify the CodeDeploy deployment to use the CodeDeployDefault.ECSLinear10PercentEvery3Minutes configuration.

C. Create an Amazon CloudWatch alarm to monitor the UnHealthyHostCount metric for the ALB. Set the alarm to activate if the metric is higher than the desired value. Associate the alarm with the CodeDeploy deployment group. Modify the deployment group to roll back when a deployment fails.

D. Create an Amazon CloudWatch alarm to monitor the TargetResponseTime metric for the ALB. Set the alarm to activate if the metric is higher than the desired value. Associate the alarm with the CodeDeploy deployment group. Modify the deployment group to roll back when alarm thresholds are met.

E. Create an Amazon CloudWatch alarm to monitor the TargetConnectionErrorCount metric for the ALB. Set the alarm to activate if the metric is higher than the desired value. Associate the alarm with the CodeDeploy deployment group. Modify the deployment group to roll back when alarm thresholds are met.

**Đáp án**: ___________

---

## Câu 84

**ID**: 339 | **Loại**: Single Choice

A security team must record the configuration of AWS resources, detect issues, and send notifications for findings. The main workload in the AWS account consists of an Amazon EC2 Auto Scaling group that scales in and out several times during the day.The team wants to be notified within 2 days if any Amazon EC2 security group allows traffic on port 22 for 0.0.0.0/0. The team also needs a snapshot of the configuration of the AWS resources to be taken routinely.The security team has already created and subscribed to an Amazon Simple Notification Service (Amazon SNS) topic.Which solution meets these requirements?

A. Configure AWS Config to use periodic recording for the AWS account. Deploy the vpc-sg-port-restriction-check AWS Config managed rule. Configure AWS Config to use the SNS topic as the target for notifications.

B. Configure AWS Config to use configuration change recording for the AWS account. Deploy the vpc-sg-open-only-to-authorized-ports AWS Config managed rule. Configure AWS Config to use the SNS topic as the target for notifications.

C. Configure AWS Config to use configuration change recording for the AWS account. Deploy the ssh-restricted AWS Config managed rule. Configure AWS Config to use the SNS topic as the target for notifications.

D. Create an AWS Lambda function to evaluate security groups and publish a message to the SNS topic. Use an Amazon EventBridge rule to schedule the Lambda function to run once a day.

**Đáp án**: ___________

---

## Câu 85

**ID**: 340 | **Loại**: Single Choice

A company has proprietary data available by using an Amazon CloudFront distribution. The company needs to ensure that the distribution is accessible by only users from the corporate office that have a known set of IP address ranges. An AWS WAF web ACL is associated with the distribution and has a default action set to Count.Which solution will meet these requirements with the LEAST operational overhead?

A. Create a new regex pattern set. Add the regex pattern set to a new rule group. Create a new web ACL that has a default action set to Block. Associate the web ACL with the CloudFront distribution. Add a rule that allows traffic based on the new rule group.

B. Create an AWS WAF IP address set that matches the corporate office IP address range. Create a new web ACL that has a default action set to Allow. Associate the web ACL with the CloudFront distribution. Add a rule that allows traffic from the IP address set.

C. Create a new regex pattern set. Add the regex pattern set to a new rule group. Set the default action on the existing web ACL to Allow. Add a rule that has priority 0 that allows traffic based on the regex pattern set.

D. Create a WAF IP address set that matches the corporate office IP address range. Set the default action on the existing web ACL to Block. Add a rule that has priority 0 that allows traffic from the IP address set.

**Đáp án**: ___________

---

## Câu 86

**ID**: 341 | **Loại**: Single Choice

A company runs several applications in the same AWS account. The applications send logs to Amazon CloudWatch.A data analytics team needs to collect performance metrics and custom metrics from the applications. The analytics team needs to transform the metrics data before storing the data in an Amazon S3 bucket. The analytics team must automatically collect any new metrics that are added to the CloudWatch namespace.Which solution will meet these requirements with the LEAST operational overhead?

A. Configure a CloudWatch metric stream to include metrics from the application and the CloudWatch namespace. Configure the metric stream to deliver the metrics to an Amazon Data Firehose delivery stream. Configure the Firehose delivery stream to invoke an AWS Lambda function to transform the data. Configure the delivery stream to send the transformed data to the S3 bucket.

B. Configure a CloudWatch metrics stream to include all the metrics and to deliver the metrics to an Amazon Data Firehose delivery stream. Configure the Firehose delivery stream to invoke an AWS Lambda function to transform the data. Configure the delivery stream to send the transformed data to the S3 bucket.

C. Configure metric filters for the CloudWatch logs to create custom metrics. Configure a CloudWatch metric stream to deliver the application metrics to the S3 bucket.

D. Configure subscription filters on the application log groups to target an Amazon Data Firehose delivery stream. Configure the Firehose delivery stream to invoke an AWS Lambda function to transform the data. Configure the delivery stream to send the transformed data to the S3 bucket.

**Đáp án**: ___________

---

## Câu 87

**ID**: 342 | **Loại**: Single Choice

A company uses an HPC platform to run analysis jobs for data. The company uses AWS CodeBuild to create container images and store the images on Amazon Elastic Container Registry (Amazon ECR). The images are then deployed on Amazon Elastic Kubernetes Service (Amazon EKS).To maintain compliance, the company needs to ensure that the images are signed before the images are deployed on Amazon EKS. The signing keys must be rotated periodically and must be managed automatically. The company needs to track who generates the signatures.Which solution will meet these requirements with the LEAST operational effort?

A. Use CodeBuild to retrieve the image that was previously pushed to Amazon ECR. Use AWS Signer to sign the image. Use AWS CloudTrail to track who generates the signatures.

B. Use AWS Lambda to retrieve the image that was previously pushed to Amazon ECR. Use a Lambda function to sign the image. Use Amazon CloudWatch to track who generates the signatures.

C. Use AWS Lambda to retrieve the image that was previously pushed to Amazon ECR. Use AWS Signer to sign the image. Use Amazon CloudWatch to track who generates the signatures.

D. Use CodeBuild to build the image. Sign the image by using AWS Signer before pushing the image to Amazon ECR. Use AWS CloudTrail to track who generates the signatures.

**Đáp án**: ___________

---

## Câu 88

**ID**: 343 | **Loại**: Single Choice

A company uses an AWS CodeArtifact repository to store Python packages that the company developed internally. A DevOps engineer needs to use AWS CodeDeploy to deploy an application to an Amazon EC2 instance. The application uses a Python package that is stored in the CodeArtifact repository. A BeforeInstall lifecycle event hook will install the package.The DevOps engineer needs to grant the EC2 instance access to the CodeArtifact repository.Which solution will meet this requirement?

A. Create a service-linked role for CodeArtifact. Associate the role with the EC2 instance. Use the aws codeartifact get-authorization-token CLI command on the instance.

B. Configure a resource-based policy for the CodeArtifact repository that allows the ReadFromRepository action for the EC2 instance principal.

C. Configure ACLs on the CodeArtifact repository to allow the EC2 instance to access the Python package.

D. Create an instance profile that contains an IAM role that has access to CodeArtifact. Associate the instance profile with the EC2 instance. Use the aws codeartifact login CLI command on the instance.

**Đáp án**: ___________

---

## Câu 89

**ID**: 344 | **Loại**: Single Choice

A company has a file-reading application that saves files to a database that runs on Amazon EC2 instances. Regulations require the company to delete files from EC2 instances every day at a specific time. The company must delete database records that are older than 60 days.The database record deletion must occur after the file deletions. The company has created scripts to delete files and database records. The company needs to receive an email notification for any failure of the deletion scripts.Which solution will meet these requirements with the LEAST development effort?

A. Use AWS Systems Manager State Manager to automatically invoke a Systems Manager Automation document at the specified time each day. Configure the Automation document to use a run command to run the deletion scripts in sequential order. Create an Amazon EventBridge rule to use Amazon Simple Notification Service (Amazon SNS) to send failure notifications to the company.

B. Use AWS Systems Manager State Manager to automatically invoke a Systems Manager Automation document at the specified time each day. Configure the Automation document to use a run command to run the deletion scripts in sequential order. Create a conditional statement inside the Automation document as the last step to check for errors. Use Amazon Simple Email Service (Amazon SES) to send failure notifications as email messages to the company.

C. Create an Amazon EventBridge rule that invokes an AWS Lambda function at the specified time. Add the necessary permissions for the invocation to the Lambda function's resource-based policy. Configure the Lambda function to run the deletion scripts in sequential order. Configure the Lambda function to use Amazon Simple Notification Service (Amazon SNS) to send failure notifications to the company.

D. Create an Amazon EventBridge rule that invokes an AWS Lambda function at the specified time. Add the necessary permissions for the invocation to the Lambda function's resource-based policy. Configure the Lambda function to run the deletion scripts in sequential order. Configure the Lambda function to use Amazon Simple Email Service (Amazon SES) to send failure notifications as email messages to the company.

**Đáp án**: ___________

---

## Câu 90

**ID**: 345 | **Loại**: Single Choice

A company uses an organization in AWS Organizations that has all features enabled to manage its AWS accounts. Amazon EQ instances run in the AWS accounts.The company requires that all current EC2 instances must use Instance Metadata Service Version 2 (IMDSv2). The company needs to block AWS API calls that originate from EC2 instances that do not use IMDSv2.Which solution will meet these requirements?

A. Create a new SCP statement that denies the ec2:RunInstances action when the ec2:MetadataHttpTokens condition key is not equal to the value of required. Attach the SCP to the root of the organization.

B. Create a new SCP statement that denies the ec2:RunInstances action when the ec2:MetadataHttpPutResponseHopLimit condition key value is greater than two. Attach the SCP to the root of the organization.

C. Create a new SCP statement that denies "*" when the ec2:RoleDelivery condition key value is less than two. Attach the SCP to the root of the organization.

D. Create a new SCP statement that denies when the ec2:MetadataHttpTokens condition key value is not equal to required. Attach the SCP to the root of the organization.

**Đáp án**: ___________

---

## Câu 91

**ID**: 346 | **Loại**: Multiple Choice

A DevOps team supports an application that runs on a large number of Amazon EC2 instances in an Auto Scaling group. The DevOps team uses AWS CloudFormation to deploy the EC2 instances. The application recently experienced an issue. A single instance returned errors to a large percentage of requests. The EC2 instance responded as healthy to both Amazon EC2 and Elastic Load Balancing health checks.The DevOps team collects application logs in Amazon CloudWatch by using the embedded metric format. The DevOps team needs to receive an alert if any EC2 instance is responsible for more than half of all errors.Which combination of steps will meet these requirements with the LEAST operational overhead? (Choose two.)

A. Create a CloudWatch Contributor Insights rule that groups logs from the CloudWatch application logs based on instance ID and errors.

B. Create a resource group in AWS Resource Groups. Use the CloudFormation stack to group the resources for the application. Add the application to CloudWatch Application Insights. Use the resource group to identify the application.

C. Create a metric filter for the application logs to count the occurrence of the term "Error.'' Create a CloudWatch alarm that uses the METRIC_COUNT function to determine whether errors have occurred. Configure the CloudWatch alarm to send a notification to an Amazon Simple Notification Service (Amazon SNS) topic to notify the DevOps team.

D. Create a CloudWatch alarm that uses the INSIGHT_RULE_METRIC function to determine whether a specific instance is responsible for more than half of all errors reported by EC2 instances. Configure the CloudWatch alarm to send a notification to an Amazon Simple Notification Service (Amazon SNS) topic to notify the DevOps team.

E. Create a CloudWatch subscription filter for the application logs that filters for errors and invokes an AWS Lambda function. Configure the Lambda function to send the instance ID and error and in a notification to an Amazon Simple Notification Service (Amazon SNS) topic to notify the DevOps team.

**Đáp án**: ___________

---

## Câu 92

**ID**: 347 | **Loại**: Single Choice

A company is using AWS CloudFormation to perform deployments of its application environment. A deployment failed during a recent update to the existing CloudFormation stack. A DevOps engineer discovered that some resources in the stack were manually modified.The DevOps engineer needs a solution that detects manual modification of resources and sends an alert to the DevOps lead.Which solution will meet these requirements with the LEAST operational effort?

A. Create an Amazon Simple Notification Service (Amazon SNS) topic. Subscribe the DevOps lead to the topic by using an email address. Create an AWS Config managed rule that has the CLOUDFORMATION_STACK_DRIFT_DETECTION_CHECK identifier. Create an Amazon EventBridge rule that is invoked on the NON_COMPLIANT resources status. Set the SNS topic as the rule target.

B. Tag all CloudFormation resources with a specific tag. Create an AWS Config custom rule by using the AWS Config Rules Development Kit Library (RDKlib) that checks all resource changes that have the specific tag. Configure the custom rule to mark all the tagged resource changes as NON_COMPLIANT when the change is not performed by CloudFormation. Create an Amazon EventBridge rule that is invoked on the NON_COMPUANT resources status. Create an AWS Lambda function that sends an email message to the DevOps lead. Set the Lambda function as the rule target.

C. Create an Amazon Simple Notification Service (Amazon SNS) topic. Subscribe the DevOps lead to the topic by using an email address. Create an AWS Config managed rule that has the CLOUDFORMATION_STACK_DRIFT_DETECTION_CHECK identifier. Create an Amazon EventBridge rule that is invoked on the COMPLIANT resources status. Set the SNS topic as the rule target.

D. Create an AWS Config managed rule that has the CLOUDFORMATION_STACK_DRIFT_DETECTION_CHECK identifier. Create an Amazon EventBridge rule that is invoked on the NON_COMPLIANT resources status. Create an AWS Lambda function that sends an email message to the DevOps lead. Set the Lambda function as the rule target.

**Đáp án**: ___________

---

## Câu 93

**ID**: 348 | **Loại**: Single Choice

A DevOps engineer deployed multiple AWS accounts by using AWS Control Tower to support different business, technical, and administrative units in a company. A security team needs the DevOps engineer to automate AWS Control Tower guardrails for the company. The guardrails must be applied to all accounts in an OU of the company's organization in AWS Organizations.The security team needs a solution that has version control and can be reviewed and rolled back if necessary. The security team will maintain the management of the solution in its OU. The security team wants to limit the type of guardrails that are allowed and allow only new guardrails that are approved by the security team.Which solution will meet these requirements with the MOST operational efficiency?

A. Create individual AWS CloudFormation templates that align to a guardrail. Store the templates in an AWS CodeCommit repository. Create an AWS::ControlTower::EnableControl logical resource in the template for each OU in the organization. Configure an AWS Code Build project that an Amazon EventBridge rule will invoke for the security team's AWS CodeCommit changes.

B. Create individual AWS CloudFormation templates that align to a guardrail. Store the templates in an AWS CodeCommit repository. Create an AWS::ControlTower::EnableControl logical resource in the template for each account in the organization. Configure an AWS CodePipeline pipeline in the security team's account. Advise the security team to invoke the pipeline and provide these parameters when starting the pipeline.

C. Create individual AWS CloudFormation templates that align to a guardrail. Store the templates in an AWS CodeCommit repository. Create an AWS::ControlTower::EnableControl logical resource in the template for each OU in the organization. Configure an AWS CodePipeline pipeline in the security team's account that an Amazon EventBridge rule will invoke for the security team's CodeCommit changes.

D. Configure an AWS CodePipeline pipeline in the security team's account that an Amazon EventBridge rule will invoke for PutObject events to an Amazon S3 bucket. Create individual AWS CloudFormation templates that align to a guardrail. Store the templates in the S3 bucket. Create an AWS::ControlTower::EnableControl logical resource in the template for each OU in the organization.

**Đáp án**: ___________

---

## Câu 94

**ID**: 349 | **Loại**: Single Choice

A company runs a web application on Amazon Elastic Kubernetes Service (Amazon EKS). The company uses Amazon CloudFront to distribute the application. The company recently enabled AWS WAF. The company set up Amazon CloudWatch Logs to send logs to an aws-waf-logs log group.The company wants a DevOps engineer to receive alerts if there are sudden changes in blocked traffic. The company does not want to receive alerts for other changes in AWS WAF log behavior. The company will tune AWS WAF rules over time.The DevOps engineer is currently subscribed to an Amazon Simple Notification Service (Amazon SNS) topic in the environment.Which solution will meet these requirements?

A. Create a CloudWatch Logs metrics filter for blocked requests on the AWS WAF log group to create a custom metric. Create a CloudWatch alarm by using CloudWatch anomaly detection and the published custom metric. Configure the alarm to notify the SNS topic to alert the DevOps engineer.

B. Create a CloudWatch anomaly detector for the log group. Create a CloudWatch alarm by using metrics that the CloudWatch anomaly detector publishes. Use the high setting for the LogAnomalyPriority metric. Configure the alarm to go into alarm state if a static threshold of one anomaly is detected. Configure the alarm to notify the SNS topic to alert the DevOps engineer.

C. Create a CloudWatch metrics filter for counted requests on the AWS WAF log group to create a custom metric. Create a CloudWatch alarm that activates when the sum of blocked requests in the custom metric during a period of 1 hour is greater than a static estimate for the acceptable number of blocked requests in 1 hour. Configure the alarm to notify the SNS topic to alert the DevOps engineer.

D. Create a CloudWatch anomaly detector for the log group. Create a CloudWatch alarm by using metrics that the CloudWatch anomaly detector publishes. Use the medium setting for the LogAnomalyPriority metric. Configure the alarm to go into alarm state if a sum of anomalies over 1 hour is greater than an expected value. Configure the alarm to notify the SNS topic to alert the DevOps engineer.

**Đáp án**: ___________

---

## Câu 95

**ID**: 350 | **Loại**: Single Choice

A video platform company is migrating its video catalog to AWS. The company will host MP4 videos files in an Amazon S3 bucket. The company will use Amazon CloudFront and Amazon EC2 instances to serve the video files.Users first connect to a frontend application that redirects to a video URL. The video URL contains an authorization token in CloudFront. The cache is activated on the CloudFront distribution. Authorization token check activity needs to be logged in Amazon CloudWatch.The company wants to prevent direct access to video files on CloudFront and Amazon S3 and wants to implement checks of the authorization token that the frontend application provides. The company also wants to perform regular rolling updates of the code that checks the authorization token signature.Which solution will meet these requirements with the LEAST operational effort?

A. Implement an authorization token check in Lambda@Edge as a trigger on the CloudFront distribution. Enable CloudWatch logging for the Lambda@Edge function. Attach the Lambda@Edge function to the CloudFront distribution. Implement CloudFront continuous deployment to perform updates.

B. Implement an authorization token check in CloudFront Functions. Enable CloudWatch logging for the CloudFront function. Attach the CloudFront function to the CloudFront distribution. Implement CloudFront continuous deployment to perform updates.

C. Implement an authorization token check in the application code that is installed on the EC2 instances. Install the CloudWatch agent on the EC2 instances. Configure the application to log to the CloudWatch agent. Implement a second CloudFront distribution. Migrate the traffic from the first CloudFront distribution by using Amazon Route 53 weighted routing.

D. Implement an authorization token check in CloudFront Functions. Enable CloudWatch logging for the CloudFront function. Attach the CloudFront function to the CloudFront distribution. Implement a second CloudFront distribution. Migrate the traffic from the first CloudFront distribution by using Amazon Route 53 weighted routing.

**Đáp án**: ___________

---

## Câu 96

**ID**: 351 | **Loại**: Multiple Choice

A company uses an organization in AWS Organizations to manage multiple AWS accounts in a hierarchical structure. An SCP that is associated with the organization root allows IAM users to be created.A DevOps team must be able to create IAM users with any level of permissions. Developers must also be able to create IAM users. However, developers must not be able to grant new IAM users excessive permissions. The developers have the CreateAndManageUsers role in each account. The DevOps team must be able to prevent other users from creating IAM users.Which combination of steps will meet these requirements? (Choose two.)

A. Create an SCP in the organization to deny users the ability to create and modify IAM users. Attach the SCP to the root of the organization. Attach the CreateAndManageUsers role to developers.

B. Create an SCP in the organization to grant users that have the DeveloperBoundary policy attached the ability to create new IAM users and to modify IAM users. Configure the SCP to require users to attach the PermissionBoundaries policy to any new IAM user. Attach the SCP to the root of the organization.

C. Create an IAM permissions policy named PermissionBoundaries within each account. Configure the PermissionBoundaries policy to specify the maximum permissions that a developer can grant to a new IAM user.

D. Create an IAM permissions policy named PermissionBoundaries within each account. Configure PermissionsBoundaries to allow users who have the PermissionBoundaries policy to create new IAM users.

E. Create an IAM permissions policy named DeveloperBoundary within each account. Configure the DeveloperBoundary policy to allow developers to create IAM users and to assign policies to IAM users of only if the developer includes the PermissionBoundaries policy as the permissions boundary. Attach the DeveloperBoundary policy to the CreateAndManageUsers role within each account.

**Đáp án**: ___________

---

## Câu 97

**ID**: 352 | **Loại**: Single Choice

A company has deployed a landing zone that has a well-defined AWS Organizations structure and an SCP. The company's development team can create their AWS resources only by using AWS CloudFormation and the AWS Cloud Development Kit (AWS CDK).A DevOps engineer notices that Amazon Simple Queue Service (Amazon SQS) queues that are deployed in different CloudFormation stacks have different configurations. The DevOps engineer also notices that the application cost allocation tag is not always set.The DevOps engineer needs a solution that will enforce tagging and promote the reuse of code. The DevOps engineer needs to avoid different configurations for the deployed SQS queues.What should the DevOps engineer do to meet these requirements?

A. Create an Organizations tag policy to enforce the cost allocation tag in CloudFormation stacks. Instruct the development team to use CloudFormation to define SQS queues. Instruct the development team to deploy the SQS queues by using CloudFormation StackSets.

B. Update the SCP to enforce the cost allocation tag in CloudFormation stacks. Instruct the development team to use CloudFormation modules to define SQS queues. Instruct the development team to deploy the SQS queues by using CloudFormation stacks.

C. Use AWS CDK tagging to enforce the cost allocation tag in CloudFormation StackSets. Instruct the development team to use the AWS CDK to define SQS queues. Instruct the development team to deploy the SQS queues by using CDK stacks.

D. Use AWS CDK tagging to enforce the cost allocation tag in CloudFormation stacks. Instruct the development team to use the AWS CDK to define SQS queues. Instruct the development team to deploy the SQS queues by using CDK feature flags.

**Đáp án**: ___________

---

## Câu 98

**ID**: 353 | **Loại**: Single Choice

A DevOps team manages a company's AWS account. The company wants to ensure that specific AWS resource configuration changes are automatically reverted.Which solution will meet this requirement?

A. Use AWS Config rules to detect changes in resource configurations. Configure remediation action that uses AWS Systems Manager Automation documents to revert the configuration changes.

B. Use Amazon CloudWatch alarms to monitor resource metrics. When an alarm is activated, use an Amazon Simple Notification Service (Amazon SNS) topic to notify an administrator to manually reverts the configuration changes.

C. Use AWS CloudFormation to create a stack that deploys the necessary configuration changes. Update the stack when configuration changes need to be reverted.

D. Use AWS Trusted Advisor to check for noncompliant configurations. Manually apply necessary changes based on Trusted Advisor recommendations.

**Đáp án**: ___________

---

## Câu 99

**ID**: 354 | **Loại**: Single Choice

A company hosts an application in its AWS account. The application uses an Amazon S3 bucket to store objects that contain sensitive information.The company needs to capture object-level S3 API calls, including calls that are rejected because the calls were made by using credentials that are not valid.Which solution will meet these requirements?

A. Create an AWS CloudTrail trail in the account. Enable S3 data events logging. Configure the trail to log to Amazon CloudWatch.

B. Create a new S3 bucket. Configure access logging on the application's S3 bucket. Deliver the access logs to the new S3 bucket.

C. Configure Amazon GuardDuty with S3 protection enabled for the account. Create an Amazon EventBridge rule that matches findings that are associated with the S3 bucket. Configure the rule to use an Amazon Simple Queue Service (Amazon SQS) queue as the target.

D. Create an AWS CloudTrail trail and a new S3 bucket in the account. Configure the trail to log to the S3 new bucket.

**Đáp án**: ___________

---

## Câu 100

**ID**: 355 | **Loại**: Single Choice

A DevOps administrator is responsible for managing the security of a company's Amazon CloudWatch Logs log groups. The company's security policy states that employee IDs must not be visible in logs except by authorized personnel. Employee IDs follow the pattern of Emp-XXXXXX, where each X is a digit.An audit discovered that employee IDs are found in a single log file. The log file is available to engineers, but the engineers are not authorized to view employee IDs. Engineers currently have an AWS IAM Identity Center permission that allows logs:* on all resources in the account.The administrator must mask the employee ID so that new log entries that contain the employee ID are not visible to unauthorized personnel.Which solution will meet these requirements with the MOST operational efficiency?

A. Create a new data protection policy on the log group. Add an Emp-\d{6} custom data identifier configuration. Create an IAM policy that has a Deny action for the Action":"logs:Unmask" permission on the resource. Attach the policy to the engineering accounts.

B. Create a new data protection policy on the log group. Add managed data identifiers for the personal data category. Create an IAM policy that has a Deny action for the "NotAction":"logs:Unmask" permission on the resource. Attach the policy to the engineering accounts.

C. Create an AWS Lambda function to parse a log file entry, remove the employee ID, and write the results to a new log file. Create a Lambda subscription filter on the log group and select the Lambda function. Grant the lambda:InvokeFunction permission to the log group.

D. Create an Amazon Data Firehose delivery stream that has an Amazon S3 bucket as the destination. Create a Firehose subscription filter on the log group that uses the Firehose delivery stream. Remove the "logs:*" permission on the engineering accounts. Create an Amazon Macie job on the S3 bucket that has an Emp-\d{6} custom identifier.

**Đáp án**: ___________

---

## Câu 101

**ID**: 356 | **Loại**: Single Choice

A company uses an organization in AWS Organizations to manage many AWS accounts. The company has enabled all features for the organization. The company uses AWS CloudFormation StackSets to deploy configurations to the accounts. The company uses AWS Config to monitor an Amazon S3 bucket.The company needs to ensure that all object uploads to the S3 bucket use AWS Key Management Service (AWS KMS) encryption.Which solution will meet these requirements?

A. Create an AWS Config conformance pack that includes the s3-bucket-server-side-encryption-enabled rule. Deploy the conformance pack to the accounts. Configure the rule to target an Amazon Simple Notification Service (Amazon SNS) topic.

B. Create an SCP that includes a deny statement for the s3:createBucket action and a condition statement where s3:x-amz-server-side-encryption is not aws:kms. Attach the SCP to the root of the organization.

C. Create an AWS CloudFormation stack set to enable an AWS CloudTrail trail to capture S3 data events for the organization. In the stack set, create an Amazon EventBridge rule to match S3 PutObject events that do not use AWS KMS encryption. Configure the rule to target an Amazon Simple Notification Service (Amazon SNS) topic.

D. Create an SCP that includes a deny statement for the s3:putObject action and a condition where s3:x-amz-server-side-encryption is not aws:kms. Attach the SCP to the root of the organization.

**Đáp án**: ___________

---

## Câu 102

**ID**: 357 | **Loại**: Single Choice

A company uses an Amazon Aurora PostgreSQL DB cluster and loads transactional data into the database every 5 hours. Data analysts use the Aurora PostgreSQL database to run short-running queries, create complex aggregated queries, and create simple reports that use the data. The data analysts also manually update the data, including deleting and inserting data.The data analysts have reported performance issues. The database team recently identified a long-running idle transaction connection that affected performance by blocking other queries and preventing VACUUM operations. The team wants to be proactively notified about these potential operational issues and about the recommended actions to fix the issues.The company's AWS account uses Amazon DevOps Guru to monitor all the applications in the account.Which solution will meet these requirements?

A. Turn on Performance Insights and DevOps Guru in the existing Aurora PostgreSQL DB cluster. Configure DevOps Guru to send notifications to the database team by using Amazon Simple Notification Service (Amazon SNS).

B. Turn on Performance Insights in the existing Aurora PostrgreSQL DB cluster. Configure Amazon EventBridge to receive events from the existing Aurora PostgreSQL DB cluster. Configure the Aurora PostgreSQL DB cluster to send notifications to the database team by using Amazon Simple Notification Service (Amazon SNS).

C. Turn on Performance Insights and DevOps Guru in the existing Aurora PostgreSQL DB cluster. Configure the Aurora PostgreSQL DB cluster to send notifications to the database team by using Amazon Simple Email Service (Amazon SES).

D. Turn on Performance Insights in the existing Aurora PostrgreSQL DB cluster. Configure Amazon EventBridge to receive events from the existing Aurora PostgreSQL DB cluster. Configure DevOps Guru to send notifications to the database team by using Amazon Simple Notification Service (Amazon SNS).

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

## Câu 104

**ID**: 359 | **Loại**: Single Choice

A company runs applications on Amazon EC2 instances that are in an Amazon EC2 Auto Scaling group. The EC2 instances are behind an Application Load Balancer (ALB). Users recently began to experience errors when traffic was directed to some of the EC2 instances.A DevOps engineer discovers that the Auto Scaling group reports the problematic instances are healthy despite the application errors. User experience returns to normal after the DevOps engineer resolves the application errors on the problematic instances.The company wants to ensure that traffic is routed only to healthy instances that are not experiencing application errors. The company also wants a support team to receive a notification if the traffic routing configuration changes.Which solution will meet these requirements?

A. Configure the Auto Scaling group to use ELB health checks. Enable AWS Config. Create an AWS Config rule to ensure that any new Auto Scaling group will use ELB health checks. Create an Amazon Simple Notification Service (Amazon SNS) topic to notify the support team if the traffic routing configuration changes. Configure the AWS Config rule to send a notification to the topic.

B. Configure the Auto Scaling group to use EC2 health checks. Enable AWS Config. Create an AWS Config rule to ensure that any new Auto Scaling group will use EC2 health checks. Create an Amazon Simple Notification Service (Amazon SNS) topic to notify the support team if the traffic routing configuration changes. Configure the AWS Config rule to send a notification to the topic.

C. Configure the Auto Scaling group to use EC2 health checks. Create an Amazon CloudWatch synthetic canary to monitor the application. Create a CloudWatch alarm that is triggered when the CloudWatch canary fails. Configure the alarm to notify the support team when the alarm state is in alarm.

D. Configure the Auto Scaling group to use ELB health checks. Create an Amazon CloudWatch synthetic canary to monitor the application. Create a CloudWatch alarm that is triggered when the CloudWatch canary fails. Configure the alarm to notify the support team when the alarm state is in alarm.

**Đáp án**: ___________

---

## Câu 105

**ID**: 360 | **Loại**: Single Choice

A DevOps engineer needs to troubleshoot a pipeline that uses a GitHub code repository. The pipeline contains a source stage, a build stage, and a deploy stage. The pipeline also has an AWS CodeStar connection to the GitHub code repository.The build stage uses an AWS CodeBuild build project. The build project needs to perform a git clone of the repository as part of the build process.The DevOps engineer validates that the source stage is working properly. However, the build stage fails each time the pipeline runs.What is the reason that the build stage fails in the pipeline?

A. The build stage within the pipeline needs to use the AWS CodeStar connection action.

B. The AWS CodeStar connection to GitHub contains incorrect credentials.

C. The AWS CodePipeline service role does not have permission to use the AWS CodeStar connection.

D. The AWS CodeBuild service role does not have permission to use the AWS CodeStar connection.

**Đáp án**: ___________

---

## Câu 106

**ID**: 361 | **Loại**: Single Choice

A company's DevOps team uses Node Package Manager (NPM) open source libraries to build applications. The DevOps team runs its application build process in an AWS CodeBuild project that downloads the NPM libraries from public NPM repositories.The company wants to host the NPM libraries in private NPM repositories. The company also needs to be able to run checks on new versions of the libraries before the DevOps team uses the libraries.Which solution will meet these requirements with the LEAST operational effort?

A. Create an AWS CodeArtifact repository with an upstream repository named npm-store. Configure the application build process to use the CodeArtifact repository as the default source for NPM. Create an AWS CodePipeline pipeline to perform the required checks on package versions in the CodeArtifact repository. Set the package status to unlisted if a failure occurs.

B. Enable Amazon S3 caching in the CodeBuild project configuration. Add a step in the buildspec.yaml config file to perform the required checks on the package versions in the cache.

C. Create an AWS CodeCommit repository for each library. Clone the required NPM libraries to the appropriate CodeCommit repository. Modify the CodeBuild  appspec.yaml config file to use the private CodeCommit repositories. Add a step to perform the required checks on the package versions.

D. Create an AWS CodeCommit repository for each library. Clone the required NPM libraries to the appropriate CodeCommit repository. Modify the CodeBuild buildspec.yaml config file so that NPM uses the private CodeCommit repositories. Add an AWS CodePipeline pipeline that performs the required checks on the package versions for each new commit to the repositories. Configure the pipeline to revert to the most recent commit in the event of a failure.

**Đáp án**: ___________

---

## Câu 107

**ID**: 362 | **Loại**: Single Choice

A company has a search application that has a web interface. The company uses Amazon CloudFront, Application Load Balancers (ALBs), and Amazon EC2 instances in an Auto Scaling group with a desired capacity of 3. The company uses prebaked AMIs. The application starts in 1 minute. The application queries an Amazon OpenSearch Service cluster.The application is deployed to multiple Availability Zones. Because of compliance requirements, the application needs to have a disaster recovery (DR) environment in a separate AWS Region. The company wants to minimize the ongoing cost of the DR environment and requires an RTO and an RPO of under 30 minutes. The company has created an ALB in the DR Region.Which solution will meet these requirements?

A. Add the new ALB as an origin in the CloudFront distribution. Configure origin failover functionality. Copy the AMI to the DR Region. Create a launch template and an Auto Scaling group with a desired capacity of 0 in the DR Region. Create a new OpenSearch Service cluster in the DR Region. Set up cross-cluster replication for the cluster.

B. Create a new CloudFront distribution in the DR Region and add the new ALB as an origin. Use Amazon Route 53 DNS for Regional failover. Copy the AMI to the DR Region. Create a launch template and an Auto Scaling group with a desired capacity of 0 in the DR Region. Reconfigure the OpenSearch Service cluster as a Multi-AZ with Standby deployment. Ensure that the standby nodes are in the DR Region.

C. Create a new CloudFront distribution in the DR Region and add the new ALB as an origin. Use Amazon Route 53 DNS for Regional failover. Copy the AMI to the DR Region. Create a launch template and an Auto Scaling group with a desired capacity of 3 in the DR Region. Reconfigure the OpenSearch Service cluster as a Multi-AZ with Standby deployment. Ensure that the standby nodes are in the DR Region.

D. Add the new ALB as an origin in the CloudFront distribution. Configure origin failover functionality. Copy the AMI to the DR Region. Create a launch template and an Auto Scaling group with a desired capacity of 3 in the DR Region. Create a new OpenSearch Service cluster in the DR Region. Set up cross-cluster replication for the cluster.

**Đáp án**: ___________

---

## Câu 108

**ID**: 363 | **Loại**: Single Choice

A DevOps engineer uses AWS WAF to manage web ACLs across an AWS account. The DevOps engineer must ensure that AWS WAF is enabled for all Application Load Balancers (ALBs) in the account. The DevOps engineer uses an AWS CloudFormation template to deploy an individual ALB and AWS WAF as part of each application stack's deployment process. If AWS WAF is removed from the ALB after the ALB is deployed, AWS WAF must be added to the ALB automatically.Which solution will meet these requirements with the MOST operational efficiency?

A. Enable AWS Config. Add the alb-waf-enabled managed rule. Create an AWS Systems Manager Automation document to add AWS WAF to an ALB. Edit the rule to automatically remediate. Select the Systems Manager Automation document as the remediation action.

B. Enable AWS Config. Add the alb-waf-enabled managed rule. Create an Amazon EventBridge rule to send all AWS Config ConfigurationItemChangeNotification notification types to an AWS Lambda function. Configure the Lambda function to call the AWS Config start-resource-evaluation API in detective mode.

C. Configure an Amazon EventBridge rule to periodically call an AWS Lambda function that calls the detect-stack-drift API on the CloudFormation template. Configure the Lambda function to modify the ALB attributes with waf.fail_open.enabled set to true if the AWS::WAFv2::WebACLAssociation resource shows a status of drifted.

D. Configure an Amazon EventBridge rule to periodically call an AWS Lambda function that calls the detect-stack-drift API on the CloudFormation template. Configure the Lambda function to delete and redeploy the CloudFormation stack if the AWS::WAFv2::WebACLAssociation resource shows a status of drifted.

**Đáp án**: ___________

---


# Đáp Án

**Câu 1** (ID 255): B, D

**Câu 2** (ID 256): C, E

**Câu 3** (ID 257): A

**Câu 4** (ID 258): C

**Câu 5** (ID 259): A, D, F

**Câu 6** (ID 260): A

**Câu 7** (ID 261): D

**Câu 8** (ID 262): B, C, D

**Câu 9** (ID 263): B

**Câu 10** (ID 264): C, D

**Câu 11** (ID 265): D

**Câu 12** (ID 266): D

**Câu 13** (ID 267): B, D

**Câu 14** (ID 268): A, C, E

**Câu 15** (ID 269): B

**Câu 16** (ID 270): A, D, F

**Câu 17** (ID 271): A, D

**Câu 18** (ID 272): A, B, C

**Câu 19** (ID 273): A, D

**Câu 20** (ID 274): A

**Câu 21** (ID 275): D

**Câu 22** (ID 276): A, D, E

**Câu 23** (ID 277): B, D, E

**Câu 24** (ID 278): D

**Câu 25** (ID 279): B

**Câu 26** (ID 280): B

**Câu 27** (ID 281): D

**Câu 28** (ID 282): A, D

**Câu 29** (ID 283): C

**Câu 30** (ID 284): B

**Câu 31** (ID 285): C

**Câu 32** (ID 286): A

**Câu 33** (ID 287): A

**Câu 34** (ID 288): B

**Câu 35** (ID 289): C

**Câu 36** (ID 290): D

**Câu 37** (ID 292): A

**Câu 38** (ID 293): A

**Câu 39** (ID 294): C

**Câu 40** (ID 295): B

**Câu 41** (ID 296): B, D, F

**Câu 42** (ID 297): C

**Câu 43** (ID 298): A, C, F

**Câu 44** (ID 299): A

**Câu 45** (ID 300): C

**Câu 46** (ID 301): A

**Câu 47** (ID 302): B

**Câu 48** (ID 303): C, D

**Câu 49** (ID 304): A

**Câu 50** (ID 305): C

**Câu 51** (ID 306): A, C, F

**Câu 52** (ID 307): D

**Câu 53** (ID 308): C

**Câu 54** (ID 309): B

**Câu 55** (ID 310): C, E

**Câu 56** (ID 311): B

**Câu 57** (ID 312): A

**Câu 58** (ID 313): A, B, E

**Câu 59** (ID 314): A

**Câu 60** (ID 315): B

**Câu 61** (ID 316): B

**Câu 62** (ID 317): B

**Câu 63** (ID 318): C, D, E

**Câu 64** (ID 319): B

**Câu 65** (ID 320): C

**Câu 66** (ID 321): A

**Câu 67** (ID 322): C, E, F

**Câu 68** (ID 323): A, B

**Câu 69** (ID 324): A

**Câu 70** (ID 325): C, D

**Câu 71** (ID 326): A

**Câu 72** (ID 327): B, D

**Câu 73** (ID 328): D

**Câu 74** (ID 329): D

**Câu 75** (ID 330): A

**Câu 76** (ID 331): A

**Câu 77** (ID 332): B

**Câu 78** (ID 333): A

**Câu 79** (ID 334): A, E, F

**Câu 80** (ID 335): B

**Câu 81** (ID 336): B

**Câu 82** (ID 337): A, D

**Câu 83** (ID 338): A, D

**Câu 84** (ID 339): C

**Câu 85** (ID 340): D

**Câu 86** (ID 341): A

**Câu 87** (ID 342): D

**Câu 88** (ID 343): D

**Câu 89** (ID 344): A

**Câu 90** (ID 345): D

**Câu 91** (ID 346): A, D

**Câu 92** (ID 347): A

**Câu 93** (ID 348): C

**Câu 94** (ID 349): A

**Câu 95** (ID 350): B

**Câu 96** (ID 351): C, E

**Câu 97** (ID 352): C

**Câu 98** (ID 353): A

**Câu 99** (ID 354): B

**Câu 100** (ID 355): A

**Câu 101** (ID 356): D

**Câu 102** (ID 357): D

**Câu 103** (ID 358): A, B

**Câu 104** (ID 359): D

**Câu 105** (ID 360): D

**Câu 106** (ID 361): A

**Câu 107** (ID 362): A

**Câu 108** (ID 363): A

