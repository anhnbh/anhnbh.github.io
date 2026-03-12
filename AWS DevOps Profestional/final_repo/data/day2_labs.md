# AWS DevOps Professional - Day 2 Labs

## Lab 1: Account Factory for Terraform (AFT) with Enterprise Support

**📋 Maps to Question 19**  
**🎯 Purpose**: Configure AFT to provision accounts with Enterprise Support plan  
**🔧 Services Used**: Control Tower, AFT, Organizations  
**💡 Key Concept**: AFT feature flags for enterprise support inheritance  

**✅ Correct Answer: Option D - Set the aft_feature_enterprise_support feature flag to True**

**🧠 Why this answer is correct:**
- AFT has built-in feature flags to control account provisioning behavior
- `aft_feature_enterprise_support = true` automatically inherits Enterprise Support from management account
- This is the native AFT way to handle support plan inheritance
- No manual intervention or custom Lambda functions needed

**❌ Why other options are wrong:**
- A: Config rules can't change support plans, only detect compliance
- B: Lambda with support:ResolveCase doesn't create support plans
- C: control_tower_parameters doesn't have AWSEnterpriseSupport parameter

### Setup:
```hcl
# aft-config.tf
module "aft" {
  source = "github.com/aws-ia/terraform-aws-control_tower_account_factory"
  
  # Enable Enterprise Support feature
  aft_feature_enterprise_support = true
  
  ct_management_account_id    = "123456789012"
  log_level                  = "INFO"
  aft_management_account_id  = "123456789013"
  ct_home_region            = "us-east-1"
  tf_backend_secondary_region = "us-west-2"
}
```

---

## Lab 2: EventBridge Automation for AWS Health Events

**📋 Maps to Question 20**  
**🎯 Purpose**: Automate EC2 instance restart based on AWS Health notifications  
**🔧 Services Used**: EventBridge, AWS Health, Systems Manager  
**💡 Key Concept**: Event-driven automation for infrastructure maintenance  

**✅ Correct Answer: Option A - Configure AWS Health as event source, EC2 service, instance maintenance event type, target Systems Manager document**

**🧠 Why this answer is correct:**
- AWS Health is the correct event source for infrastructure maintenance notifications
- EventBridge can directly target Systems Manager documents without Lambda
- This is the most direct and efficient approach
- Systems Manager documents can restart instances directly

**❌ Why other options are wrong:**
- B: Systems Manager isn't an event source for health events
- C: Adding Lambda is unnecessary complexity when SSM can be targeted directly
- D: EC2 service doesn't emit maintenance events directly

### EventBridge Rule:
```bash
aws events put-rule \
  --name "ec2-health-maintenance" \
  --event-pattern '{
    "source": ["aws.health"],
    "detail-type": ["AWS Health Event"],
    "detail": {
      "service": ["EC2"],
      "eventTypeCategory": ["scheduledChange"]
    }
  }'

aws events put-targets \
  --rule "ec2-health-maintenance" \
  --targets '[{
    "Id": "1",
    "Arn": "arn:aws:ssm:us-east-1:123456789012:document/restart-ec2-document",
    "RoleArn": "arn:aws:iam::123456789012:role/EventBridgeSSMRole"
  }]'
```

---

## Lab 3: CodeBuild with Artifact Encryption

**📋 Maps to Question 21**  
**🎯 Purpose**: Replace Jenkins with CodeBuild and encrypt build artifacts  
**🔧 Services Used**: CodeBuild, S3, KMS  
**💡 Key Concept**: Managed CI/CD with built-in encryption  

**✅ Correct Answer: Option D - Use AWS CodeBuild with artifact encryption to replace Jenkins**

**🧠 Why this answer is correct:**
- CodeBuild is fully managed, eliminating patching/upgrading overhead
- Built-in artifact encryption capability meets compliance requirements
- No infrastructure management needed (vs Jenkins on EC2)
- Most maintainable solution as requested

**❌ Why other options are wrong:**
- A: Still requires managing EC2 instances for Jenkins
- B: ECS + S3 doesn't address the Jenkins replacement need
- C: CodePipeline alone doesn't replace Jenkins build functionality

### CodeBuild Project:
```bash
aws codebuild create-project \
  --name "quality-control-build" \
  --source '{
    "type": "GITHUB",
    "location": "https://github.com/company/quality-control-app.git"
  }' \
  --artifacts '{
    "type": "S3",
    "location": "company-build-artifacts",
    "encryptionDisabled": false
  }' \
  --environment '{
    "type": "LINUX_CONTAINER",
    "image": "aws/codebuild/amazonlinux2-x86_64-standard:3.0",
    "computeType": "BUILD_GENERAL1_MEDIUM"
  }'
```

---

## Lab 4: CloudFormation Custom Resource for S3 Cleanup

**📋 Maps to Question 22**  
**🎯 Purpose**: Ensure S3 bucket deletion during CloudFormation stack cleanup  
**🔧 Services Used**: CloudFormation, Lambda, S3  
**💡 Key Concept**: Custom resources for complex cleanup operations  

**✅ Correct Answer: Option B - Add custom resource with Lambda function and DependsOn attribute**

**🧠 Why this answer is correct:**
- S3 buckets can't be deleted if they contain objects
- Custom resource with Lambda can empty bucket before deletion
- DependsOn ensures proper deletion order
- Most efficient automated solution

**❌ Why other options are wrong:**
- A: DeletionPolicy doesn't empty buckets, just forces deletion attempt
- C: Manual process isn't efficient and doesn't prevent future occurrences
- D: OpsWorks is overkill and doesn't solve the core S3 deletion issue

### Lambda Function:
```python
import boto3
import cfnresponse

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['ResourceProperties']['BucketName']
    
    try:
        if event['RequestType'] == 'Delete':
            paginator = s3.get_paginator('list_objects_v2')
            pages = paginator.paginate(Bucket=bucket_name)
            
            for page in pages:
                if 'Contents' in page:
                    objects = [{'Key': obj['Key']} for obj in page['Contents']]
                    s3.delete_objects(
                        Bucket=bucket_name,
                        Delete={'Objects': objects}
                    )
        
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
    except Exception as e:
        cfnresponse.send(event, context, cfnresponse.FAILED, {})
```

---

## Lab 5: Cross-Region CodePipeline Deployment

**📋 Maps to Question 23**  
**🎯 Purpose**: Deploy Lambda application to multiple regions using single pipeline  
**🔧 Services Used**: CodePipeline, CodeBuild, CloudFormation, S3  
**💡 Key Concept**: Multi-region artifact stores and deployment actions  

**✅ Correct Answer: Options C & E - Create S3 bucket in us-east-1 + Modify pipeline with us-east-1 artifact store**

**🧠 Why these answers are correct:**
- C: CodePipeline requires artifact store in each deployment region
- E: Pipeline needs artifact store configuration + new deploy action for us-east-1
- This enables cross-region deployment from single pipeline
- Uses the us-east-1 output artifact from CodeBuild

**❌ Why other options are wrong:**
- A: Parameter approach is more complex than using region-specific artifacts
- B: Missing the artifact store requirement
- D: Cross-Region Replication isn't needed for CodePipeline artifacts

### Pipeline Configuration:
```yaml
ArtifactStores:
  - Region: eu-west-1
    ArtifactStore:
      Type: S3
      Location: !Ref ArtifactStoreEuWest1
  - Region: us-east-1
    ArtifactStore:
      Type: S3
      Location: !Ref ArtifactStoreUsEast1

Stages:
  - Name: Deploy
    Actions:
      - Name: DeployUsEast1
        Region: us-east-1
        ActionTypeId:
          Category: Deploy
          Owner: AWS
          Provider: CloudFormation
        Configuration:
          StackName: lambda-app-us-east-1
          TemplatePath: BuildOutputUsEast1::packaged-template.yaml
```

---

## Lab 6: OpsWorks Auto Healing with S3 Metadata

**📋 Maps to Question 24**  
**🎯 Purpose**: Auto-restart EC2 instances and retrieve metadata from S3  
**🔧 Services Used**: OpsWorks, S3, CloudWatch  
**💡 Key Concept**: OpsWorks lifecycle events for automated recovery  

**✅ Correct Answer: Option B - Configure AWS OpsWorks with auto healing feature and lifecycle events**

**🧠 Why this answer is correct:**
- OpsWorks auto healing automatically replaces unresponsive instances
- Lifecycle events (Setup, Configure) can pull metadata from S3
- Built-in integration between OpsWorks and S3
- Handles both restart and metadata retrieval requirements

**❌ Why other options are wrong:**
- A: CloudWatch recover action doesn't handle metadata retrieval
- C: EC2 Auto Recovery doesn't integrate with S3 for metadata
- D: CloudFormation UserData only runs at initial launch, not restart

### OpsWorks Configuration:
```bash
aws opsworks create-stack \
  --name "auto-healing-stack" \
  --service-role-arn "arn:aws:iam::123456789012:role/aws-opsworks-service-role" \
  --default-instance-profile-arn "arn:aws:iam::123456789012:instance-profile/aws-opsworks-ec2-role" \
  --use-custom-cookbooks \
  --custom-cookbooks-source '{
    "Type": "git",
    "Url": "https://github.com/company/opsworks-cookbooks.git"
  }'

aws opsworks create-layer \
  --stack-id "stack-id" \
  --type "custom" \
  --name "Application Layer" \
  --enable-auto-healing \
  --custom-recipes '{
    "Setup": ["metadata::retrieve"]
  }'
```

---

## Lab 7: Service Control Policies for IAM Protection

**📋 Maps to Question 26**  
**🎯 Purpose**: Protect auditing IAM role from unauthorized modifications  
**🔧 Services Used**: Organizations, SCP, IAM  
**💡 Key Concept**: Preventive controls using SCPs with conditions  

**✅ Correct Answer: Option A - Create SCP with Deny statement and condition for trusted administrator**

**🧠 Why this answer is correct:**
- SCPs provide preventive controls at organization level
- Deny statement with condition allows only trusted admin to modify role
- Attaching to organization root applies to all accounts
- Most effective way to prevent unauthorized role modifications

**❌ Why other options are wrong:**
- B: SCPs can't be attached to services, only OUs/accounts/root
- C: Permissions boundaries are attached to users/roles, not accounts
- D: Same issue as C, permissions boundaries don't work at account level

### Service Control Policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "iam:DeleteRole",
        "iam:UpdateRole",
        "iam:PutRolePolicy",
        "iam:DeleteRolePolicy"
      ],
      "Resource": "arn:aws:iam::*:role/SecurityAuditingRole",
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalArn": "arn:aws:iam::*:role/TrustedAdministratorRole"
        }
      }
    }
  ]
}
```

---

## Lab 8: Blue/Green Deployment with ECS

**📋 Maps to Question 27**  
**🎯 Purpose**: Implement blue/green deployments and A/B testing for Go application  
**🔧 Services Used**: ECS, ALB, CodeDeploy  
**💡 Key Concept**: Blue/green deployment strategy with traffic shifting  

**✅ Correct Answer: Option D - Use AWS Elastic Beanstalk to host the application**

**🧠 Why this answer is correct:**
- Elastic Beanstalk natively supports blue/green deployments
- Built-in A/B testing capabilities with traffic splitting
- Manages underlying infrastructure automatically
- Supports Go applications out of the box
- Most straightforward solution for the requirements

**❌ Why other options are wrong:**
- A: Lambda doesn't support containerized applications directly
- B: CodeArtifact + CodeDeploy + EC2 is more complex than needed
- C: ECS + CodeDeploy works but requires more setup than Beanstalk

### ECS Service Configuration:
```yaml
ECSService:
  Type: AWS::ECS::Service
  Properties:
    Cluster: !Ref ECSCluster
    TaskDefinition: !Ref TaskDefinition
    DesiredCount: 2
    DeploymentConfiguration:
      DeploymentCircuitBreaker:
        Enable: true
        Rollback: true
      MaximumPercent: 200
      MinimumHealthyPercent: 50
    LoadBalancers:
      - ContainerName: go-app
        ContainerPort: 8080
        TargetGroupArn: !Ref TargetGroup

CodeDeployApplication:
  Type: AWS::CodeDeploy::Application
  Properties:
    ApplicationName: go-app-ecs
    ComputePlatform: ECS

DeploymentGroup:
  Type: AWS::CodeDeploy::DeploymentGroup
  Properties:
    ApplicationName: !Ref CodeDeployApplication
    DeploymentGroupName: go-app-dg
    ServiceRoleArn: !GetAtt CodeDeployRole.Arn
    BlueGreenDeploymentConfiguration:
      TerminateBlueInstancesOnDeploymentSuccess:
        Action: TERMINATE
        TerminationWaitTimeInMinutes: 5
      DeploymentReadyOption:
        ActionOnTimeout: CONTINUE_DEPLOYMENT
      GreenFleetProvisioningOption:
        Action: COPY_AUTO_SCALING_GROUP
```

---

## Lab 9: Automated Log Collection from Auto Scaling

**📋 Maps to Question 28**  
**🎯 Purpose**: Collect logs before EC2 termination in Auto Scaling group  
**🔧 Services Used**: Auto Scaling, CloudWatch Logs, Lambda, SNS  
**💡 Key Concept**: Lifecycle hooks for pre-termination log collection  

**✅ Correct Answer: Option D - Use lifecycle hooks with EventBridge rule and Lambda function**

**🧠 Why this answer is correct:**
- Lifecycle hooks put instances in Terminating:Wait state
- EventBridge rule triggers on lifecycle events
- Lambda function can use SSM Run Command to collect logs
- Complete lifecycle action after log collection
- Most automated and reliable approach

**❌ Why other options are wrong:**
- A: CloudWatch Events for ELB health checks don't provide termination timing
- B: CloudWatch subscription filters don't handle lifecycle events
- C: CloudWatch subscription filter approach is less reliable than EventBridge

### Lifecycle Hook:
```bash
aws autoscaling put-lifecycle-hook \
  --lifecycle-hook-name "collect-logs-before-termination" \
  --auto-scaling-group-name "app-asg" \
  --lifecycle-transition "autoscaling:EC2_INSTANCE_TERMINATING" \
  --heartbeat-timeout 300 \
  --notification-target-arn "arn:aws:sns:us-east-1:123456789012:log-collection-topic"
```

### Lambda Function:
```python
import boto3
import json

def lambda_handler(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])
    instance_id = message['EC2InstanceId']
    
    ssm = boto3.client('ssm')
    
    response = ssm.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Parameters={
            'commands': [
                'sudo tar -czf /tmp/app-logs.tar.gz /var/log/application/',
                f'aws s3 cp /tmp/app-logs.tar.gz s3://log-collection-bucket/{instance_id}/'
            ]
        }
    )
```

---

## Lab 10: Cross-Account Operations Team Access

**📋 Maps to Question 29**  
**🎯 Purpose**: Provide operations team admin access across workload accounts  
**🔧 Services Used**: Organizations, IAM, STS  
**💡 Key Concept**: Cross-account role assumption with centralized user management  

**✅ Correct Answer: Options B, D, F - Create SysAdmin role in workload accounts + IAM group in operations account + Add users to group**

**🧠 Why these answers are correct:**
- B: SysAdmin role in each workload account provides admin access
- D: IAM group in operations account centralizes user management
- F: Adding users to group grants cross-account access permissions
- This follows AWS best practices for cross-account access

**❌ Why other options are wrong:**
- A: Users shouldn't be created in workload accounts (violates centralized management)
- C: Cognito is overkill for internal operations team access
- E: Switch role capability alone doesn't provide the access mechanism

### Operations Account Setup:
```yaml
OperationsTeamGroup:
  Type: AWS::IAM::Group
  Properties:
    GroupName: OperationsTeam
    Policies:
      - PolicyName: AssumeWorkloadAccountRoles
        PolicyDocument:
          Version: '2012-10-17'
          Statement:
            - Effect: Allow
              Action: sts:AssumeRole
              Resource: "arn:aws:iam::*:role/OperationsAdminRole"

OperationsUsers:
  Type: AWS::IAM::User
  Properties:
    UserName: ops-user-1
    Groups:
      - !Ref OperationsTeamGroup
```

### Workload Account Role:
```yaml
OperationsAdminRole:
  Type: AWS::IAM::Role
  Properties:
    AssumeRolePolicyDocument:
      Version: '2012-10-17'
      Statement:
        - Effect: Allow
          Principal:
            AWS: !Sub "arn:aws:iam::${OperationsAccountId}:root"
          Action: sts:AssumeRole
    ManagedPolicyArns:
      - arn:aws:iam::aws:policy/AdministratorAccess
```

---

## Lab 11: S3 Block Public Access Monitoring

**📋 Maps to Question 30**  
**🎯 Purpose**: Monitor S3 Block Public Access changes across organization  
**🔧 Services Used**: Config, EventBridge, SNS, Lambda  
**💡 Key Concept**: Organization-wide compliance monitoring with Config rules  

**✅ Correct Answer: Option C - Turn on AWS Config, create SNS topic, deploy conformance pack with Config rule**

**🧠 Why this answer is correct:**
- AWS Config can monitor S3 Block Public Access settings organization-wide
- Conformance packs deploy rules across all accounts automatically
- SNS topic provides notification mechanism for SecOps team
- Config rules can trigger remediation actions
- Most comprehensive solution for organization-wide monitoring

**❌ Why other options are wrong:**
- A: CloudTrail only logs API calls, doesn't monitor configuration compliance
- B: EventBridge alone can't monitor S3 configuration changes proactively
- D: Inspector is for security assessments, not configuration monitoring

### Config Rule:
```bash
aws configservice put-organization-config-rule \
  --organization-config-rule-name "s3-block-public-access-org-rule" \
  --organization-managed-rule-metadata '{
    "RuleIdentifier": "S3_BUCKET_PUBLIC_ACCESS_PROHIBITED",
    "Description": "Checks if S3 buckets have public access blocked"
  }'
```

### EventBridge Rule:
```json
{
  "Name": "s3-block-public-access-changes",
  "EventPattern": {
    "source": ["aws.config"],
    "detail-type": ["Config Rules Compliance Change"],
    "detail": {
      "configRuleName": ["s3-bucket-public-access-prohibited"],
      "newEvaluationResult": {
        "complianceType": ["NON_COMPLIANT"]
      }
    }
  },
  "Targets": [
    {
      "Id": "1",
      "Arn": "arn:aws:sns:us-east-1:123456789012:secops-notifications"
    }
  ]
}
```

---

## Lab 12: EKS Logging with SNS Notifications

**📋 Maps to Question 31**  
**🎯 Purpose**: Establish automated email notifications for EKS components  
**🔧 Services Used**: EKS, CloudWatch Logs, Lambda, SNS  
**💡 Key Concept**: Container logging with intelligent notification routing  

**✅ Correct Answer: Option A - Enable CloudWatch Logs for EKS, configure subscription filter with Lambda**

**🧠 Why this answer is correct:**
- CloudWatch Logs is the native logging solution for EKS
- Subscription filters can trigger Lambda functions for log processing
- Lambda can evaluate log events and route to appropriate SNS topics
- Most direct integration with EKS logging capabilities

**❌ Why other options are wrong:**
- B: S3 logging doesn't provide real-time processing capabilities
- C: S3 PUT events don't provide log content for evaluation
- D: Same issue as C, S3 events don't contain log data

### EKS Cluster Logging:
```yaml
EKSCluster:
  Type: AWS::EKS::Cluster
  Properties:
    Name: production-cluster
    Logging:
      ClusterLogging:
        EnabledTypes:
          - Type: api
          - Type: audit
          - Type: authenticator
          - Type: controllerManager
          - Type: scheduler

LogGroup:
  Type: AWS::Logs::LogGroup
  Properties:
    LogGroupName: /aws/eks/production-cluster/cluster
    RetentionInDays: 30
```

### Lambda Log Processor:
```python
import boto3
import json
import re

def lambda_handler(event, context):
    sns = boto3.client('sns')
    
    for record in event['awslogs']['data']:
        log_events = json.loads(record)
        
        for log_event in log_events['logEvents']:
            message = log_event['message']
            
            # Route based on log content
            if 'api-server' in message:
                topic_arn = 'arn:aws:sns:us-east-1:123456789012:eks-api-alerts'
            elif 'scheduler' in message:
                topic_arn = 'arn:aws:sns:us-east-1:123456789012:eks-scheduler-alerts'
            else:
                topic_arn = 'arn:aws:sns:us-east-1:123456789012:eks-general-alerts'
            
            if 'ERROR' in message or 'FATAL' in message:
                sns.publish(
                    TopicArn=topic_arn,
                    Message=message,
                    Subject=f'EKS Alert: {log_event["timestamp"]}'
                )
```

---

## Lab 13: ECS with ALB Logging to S3

**📋 Maps to Question 32**  
**🎯 Purpose**: Collect application and access logs from ECS with ALB  
**🔧 Services Used**: ECS, ALB, CloudWatch Logs, Kinesis Data Firehose, S3  
**💡 Key Concept**: Multi-layer logging architecture for containers  

**✅ Correct Answer: Options B, D, F - Enable ALB access logs + Configure ECS awslogs driver + Create Kinesis Data Firehose**

**🧠 Why these answers are correct:**
- B: ALB access logs capture load balancer traffic patterns
- D: ECS awslogs driver sends container logs to CloudWatch Logs
- F: Kinesis Data Firehose streams logs from CloudWatch to S3 for analysis
- This creates complete logging pipeline from ALB → ECS → CloudWatch → S3

**❌ Why other options are wrong:**
- A: Target group logs don't exist, ALB logs are at load balancer level
- C: Direct S3 logging from ECS isn't available
- E: CloudWatch subscription filter alone doesn't get to S3 efficiently

### ALB Access Logs:
```yaml
ApplicationLoadBalancer:
  Type: AWS::ElasticLoadBalancingV2::LoadBalancer
  Properties:
    LoadBalancerAttributes:
      - Key: access_logs.s3.enabled
        Value: true
      - Key: access_logs.s3.bucket
        Value: !Ref ALBLogsBucket
      - Key: access_logs.s3.prefix
        Value: alb-logs

ALBLogsBucket:
  Type: AWS::S3::Bucket
  Properties:
    BucketName: !Sub "${AWS::StackName}-alb-logs"
    LifecycleConfiguration:
      Rules:
        - Status: Enabled
          ExpirationInDays: 90
```

### ECS Task Definition with Logging:
```yaml
TaskDefinition:
  Type: AWS::ECS::TaskDefinition
  Properties:
    ContainerDefinitions:
      - Name: web-app
        Image: nginx:latest
        LogConfiguration:
          LogDriver: awslogs
          Options:
            awslogs-group: !Ref ECSLogGroup
            awslogs-region: !Ref AWS::Region
            awslogs-stream-prefix: ecs

ECSLogGroup:
  Type: AWS::Logs::LogGroup
  Properties:
    LogGroupName: /ecs/web-application
    RetentionInDays: 14
```

### Kinesis Data Firehose:
```yaml
DeliveryStream:
  Type: AWS::KinesisFirehose::DeliveryStream
  Properties:
    DeliveryStreamName: ecs-logs-to-s3
    DeliveryStreamType: DirectPut
    S3DestinationConfiguration:
      BucketARN: !GetAtt LogsBucket.Arn
      BufferingHints:
        SizeInMBs: 5
        IntervalInSeconds: 300
      CompressionFormat: GZIP
      Prefix: ecs-logs/year=!{timestamp:yyyy}/month=!{timestamp:MM}/day=!{timestamp:dd}/
```

---

## Lab 14: Systems Manager Patch Management

**📋 Maps to Question 33**  
**🎯 Purpose**: Automate OS and application patching for compliance  
**🔧 Services Used**: Systems Manager, Patch Manager, Maintenance Windows  
**💡 Key Concept**: Automated patch compliance for healthcare workloads  

**✅ Correct Answer: Option A - Use Systems Manager Patch Manager with custom patch baseline**

**🧠 Why this answer is correct:**
- Systems Manager Patch Manager is designed for automated patching
- Custom patch baselines can include corporate repositories
- Maintenance windows provide scheduled patching
- Built-in compliance reporting for healthcare requirements
- Most comprehensive solution for patch management

**❌ Why other options are wrong:**
- B: Manual yum configuration doesn't provide automation or compliance tracking
- C: AWS-AmazonLinuxDefaultPatchBaseline doesn't include custom repositories
- D: Manual yum-config-manager approach lacks automation and reporting

### Patch Baseline:
```bash
# Create custom patch baseline
aws ssm create-patch-baseline \
  --name "Healthcare-Compliance-Baseline" \
  --operating-system "AMAZON_LINUX_2" \
  --approval-rules '{
    "PatchRules": [
      {
        "PatchFilterGroup": {
          "PatchFilters": [
            {
              "Key": "CLASSIFICATION",
              "Values": ["Security", "Bugfix", "Critical"]
            }
          ]
        },
        "ApproveAfterDays": 0,
        "EnableNonSecurity": false
      }
    ]
  }' \
  --approved-patches '["kernel*"]' \
  --rejected-patches '["firefox*"]'
```

### Maintenance Window:
```bash
# Create maintenance window
aws ssm create-maintenance-window \
  --name "Healthcare-Patching-Window" \
  --schedule "cron(0 2 ? * SUN *)" \
  --duration 4 \
  --cutoff 1 \
  --allow-unassociated-targets

# Register targets
aws ssm register-target-with-maintenance-window \
  --window-id "mw-xxxxxxxxx" \
  --target-type "Instance" \
  --targets '[{
    "Key": "tag:Environment",
    "Values": ["production"]
  }]'

# Register patch task
aws ssm register-task-with-maintenance-window \
  --window-id "mw-xxxxxxxxx" \
  --target-type "Instance" \
  --task-arn "AWS-RunPatchBaseline" \
  --task-type "RUN_COMMAND" \
  --max-concurrency "50%" \
  --max-errors "1"
```

---

## Lab 15: CodeDeploy Blue/Green with Testing

**📋 Maps to Question 34**  
**🎯 Purpose**: Implement blue/green deployment with automated testing  
**🔧 Services Used**: CodeDeploy, ECS, Lambda, CloudWatch  
**💡 Key Concept**: Automated testing during deployment with rollback capability  

**✅ Correct Answer: Option C - Add hooks section to AppSpec file, use AfterAllowTestTraffic lifecycle event**

**🧠 Why this answer is correct:**
- AfterAllowTestTraffic is the correct lifecycle event for testing green environment
- Lambda function can run tests and return success/failure
- CodeDeploy automatically handles rollback on Lambda function failure
- This is the native CodeDeploy way to implement testing during deployment

**❌ Why other options are wrong:**
- A: BeforeAllowTraffic runs before traffic is routed, can't test with real traffic
- B: AfterAllowTraffic runs after full traffic shift, too late for testing
- D: Manual CLI commands don't integrate with CodeDeploy's automated rollback

### CodeDeploy Configuration:
```yaml
CodeDeployApplication:
  Type: AWS::CodeDeploy::Application
  Properties:
    ApplicationName: ecs-blue-green-app
    ComputePlatform: ECS

DeploymentGroup:
  Type: AWS::CodeDeploy::DeploymentGroup
  Properties:
    ApplicationName: !Ref CodeDeployApplication
    DeploymentGroupName: ecs-deployment-group
    ServiceRoleArn: !GetAtt CodeDeployRole.Arn
    BlueGreenDeploymentConfiguration:
      TerminateBlueInstancesOnDeploymentSuccess:
        Action: TERMINATE
        TerminationWaitTimeInMinutes: 5
      DeploymentReadyOption:
        ActionOnTimeout: STOP_DEPLOYMENT
        WaitTimeInMinutes: 5
      GreenFleetProvisioningOption:
        Action: COPY_AUTO_SCALING_GROUP
```

### Test Lambda Function:
```python
import boto3
import requests
import json

def lambda_handler(event, context):
    codedeploy = boto3.client('codedeploy')
    
    deployment_id = event['DeploymentId']
    lifecycle_event = event['LifecycleEventHookExecutionId']
    
    try:
        # Get green environment endpoint
        green_endpoint = get_green_endpoint(deployment_id)
        
        # Run tests
        test_results = run_health_checks(green_endpoint)
        
        if test_results['success']:
            # Continue deployment
            codedeploy.put_lifecycle_event_hook_execution_status(
                deploymentId=deployment_id,
                lifecycleEventHookExecutionId=lifecycle_event,
                status='Succeeded'
            )
        else:
            # Stop deployment
            codedeploy.put_lifecycle_event_hook_execution_status(
                deploymentId=deployment_id,
                lifecycleEventHookExecutionId=lifecycle_event,
                status='Failed'
            )
            
    except Exception as e:
        codedeploy.put_lifecycle_event_hook_execution_status(
            deploymentId=deployment_id,
            lifecycleEventHookExecutionId=lifecycle_event,
            status='Failed'
        )

def run_health_checks(endpoint):
    tests = [
        f"{endpoint}/health",
        f"{endpoint}/api/status",
        f"{endpoint}/metrics"
    ]
    
    for test_url in tests:
        response = requests.get(test_url, timeout=30)
        if response.status_code != 200:
            return {'success': False, 'failed_url': test_url}
    
    return {'success': True}
```

---

## Lab 16: Storage Gateway Cache Refresh

**📋 Maps to Question 35**  
**🎯 Purpose**: Ensure Storage Gateway reflects S3 changes from third parties  
**🔧 Services Used**: Storage Gateway, S3, Lambda, EventBridge  
**💡 Key Concept**: Cache invalidation for file gateway synchronization  

**✅ Correct Answer: Option A - Configure a scheduled process to refresh the file gateway cache**

**🧠 Why this answer is correct:**
- File Gateway caches S3 objects locally for performance
- Third-party changes to S3 don't automatically update the cache
- Scheduled refresh ensures cache stays synchronized with S3
- RefreshCache API call updates the gateway's view of S3 objects

**❌ Why other options are wrong:**
- B: Volume gateway mode doesn't solve the file access issue
- C: Same-Region Replication doesn't refresh Storage Gateway cache
- D: File gateway mode is already being used, switching modes isn't the solution

### S3 Event Configuration:
```yaml
S3Bucket:
  Type: AWS::S3::Bucket
  Properties:
    NotificationConfiguration:
      LambdaConfigurations:
        - Event: s3:ObjectCreated:*
          Function: !GetAtt RefreshCacheFunction.Arn
        - Event: s3:ObjectRemoved:*
          Function: !GetAtt RefreshCacheFunction.Arn

RefreshCacheFunction:
  Type: AWS::Lambda::Function
  Properties:
    Runtime: python3.9
    Handler: index.lambda_handler
    Code:
      ZipFile: |
        import boto3
        import json
        
        def lambda_handler(event, context):
            storagegateway = boto3.client('storagegateway')
            
            for record in event['Records']:
                bucket = record['s3']['bucket']['name']
                key = record['s3']['object']['key']
                
                # Refresh file share cache
                storagegateway.refresh_cache(
                    FileShareARN='arn:aws:storagegateway:us-east-1:123456789012:share/share-xxxxxxxx',
                    FolderList=[f'/{key}']
                )
```

### Scheduled Cache Refresh:
```bash
# Create EventBridge rule for daily refresh
aws events put-rule \
  --name "daily-storage-gateway-refresh" \
  --schedule-expression "cron(0 6 * * ? *)"

aws events put-targets \
  --rule "daily-storage-gateway-refresh" \
  --targets '[{
    "Id": "1",
    "Arn": "arn:aws:lambda:us-east-1:123456789012:function:refresh-storage-gateway",
    "Input": "{\"refresh_type\": \"full\"}"
  }]'
```

---

## Lab 17: S3 Cross-Region Replication with Encryption

**📋 Maps to Question 36**  
**🎯 Purpose**: Set up cross-region replication for sensitive S3 objects  
**🔧 Services Used**: S3, KMS, IAM  
**💡 Key Concept**: Cross-account, cross-region replication with encryption  

**✅ Correct Answer: Options A, D, E - Create replication role + Create replication rule in source bucket + Grant permissions in destination bucket policy**

**🧠 Why these answers are correct:**
- A: IAM role with replication permissions is required for S3 to perform replication
- D: Replication rule must be configured in the source bucket
- E: Destination bucket policy must grant permissions to source account's replication role
- This enables cross-account, cross-region replication with proper security

**❌ Why other options are wrong:**
- B: Replication rules are configured in source bucket, not destination
- C: Versioning is already mentioned as enabled in the question
- F: Replication rules go in source bucket, not destination

### Source Bucket Configuration:
```yaml
SourceBucket:
  Type: AWS::S3::Bucket
  Properties:
    BucketName: sensitive-data-source
    VersioningConfiguration:
      Status: Enabled
    ReplicationConfiguration:
      Role: !GetAtt ReplicationRole.Arn
      Rules:
        - Id: ReplicateToDestination
          Status: Enabled
          Prefix: sensitive/
          Destination:
            Bucket: arn:aws:s3:::sensitive-data-destination
            StorageClass: STANDARD_IA
            EncryptionConfiguration:
              ReplicaKmsKeyID: arn:aws:kms:us-west-2:TARGET-ACCOUNT:key/KEY-ID

ReplicationRole:
  Type: AWS::IAM::Role
  Properties:
    AssumeRolePolicyDocument:
      Version: '2012-10-17'
      Statement:
        - Effect: Allow
          Principal:
            Service: s3.amazonaws.com
          Action: sts:AssumeRole
    Policies:
      - PolicyName: ReplicationPolicy
        PolicyDocument:
          Version: '2012-10-17'
          Statement:
            - Effect: Allow
              Action:
                - s3:GetObjectVersionForReplication
                - s3:GetObjectVersionAcl
              Resource: !Sub "${SourceBucket}/*"
            - Effect: Allow
              Action:
                - s3:ReplicateObject
                - s3:ReplicateDelete
              Resource: "arn:aws:s3:::sensitive-data-destination/*"
            - Effect: Allow
              Action:
                - kms:Decrypt
                - kms:GenerateDataKey
              Resource: "*"
```

### Destination Account Bucket Policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::SOURCE-ACCOUNT:role/ReplicationRole"
      },
      "Action": [
        "s3:ReplicateObject",
        "s3:ReplicateDelete"
      ],
      "Resource": "arn:aws:s3:::sensitive-data-destination/*"
    },
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::SOURCE-ACCOUNT:role/ReplicationRole"
      },
      "Action": "s3:GetBucketVersioning",
      "Resource": "arn:aws:s3:::sensitive-data-destination"
    }
  ]
}
```

### Cross-Account KMS Key Policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::SOURCE-ACCOUNT:role/ReplicationRole"
      },
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "*"
    }
  ]
}
```

---

## 🎯 Key Takeaways

**Understanding Why Answers Are Correct:**

1. **AFT Enterprise Support**: Use built-in feature flags rather than custom solutions
2. **Event-Driven Automation**: Direct service integration is more efficient than Lambda layers
3. **Managed Services**: Choose managed solutions (CodeBuild) over self-managed (Jenkins on EC2)
4. **CloudFormation Cleanup**: Custom resources handle complex deletion scenarios automatically
5. **Multi-Region Deployments**: Artifact stores are required in each deployment region
6. **Auto Healing**: OpsWorks provides integrated lifecycle management with S3 integration
7. **Preventive Controls**: SCPs work at organization level, permissions boundaries at user/role level
8. **Blue/Green Deployments**: Use native service capabilities rather than building custom solutions
9. **Lifecycle Management**: Hooks provide timing control for data preservation operations
10. **Cross-Account Access**: Centralized identity management with distributed role assumption
11. **Compliance Monitoring**: Config rules provide proactive monitoring vs reactive logging
12. **Container Logging**: Native integrations (CloudWatch Logs) are more efficient than custom solutions
13. **Patch Management**: Systems Manager provides comprehensive automation and compliance tracking
14. **Deployment Testing**: Use correct lifecycle events (AfterAllowTestTraffic) for testing phases
15. **Cache Management**: Understand when manual refresh is needed vs automatic synchronization
16. **Cross-Region Replication**: Source bucket configuration with proper IAM permissions
17. **Security Best Practices**: Always consider least privilege and proper encryption in transit/at rest

**Common Wrong Answer Patterns:**
- Choosing manual processes over automation
- Adding unnecessary complexity (Lambda when direct integration exists)
- Misunderstanding service capabilities and limitations
- Confusing reactive monitoring with proactive compliance
- Not considering cross-account/cross-region requirements properly
