# AWS DevOps Professional - Day 1 Labs

## Lab 1: CloudWatch Metrics from Lambda with Custom Dimensions

**📋 Maps to Question 1**  
**🎯 Purpose**: Track API operations by version and response code from Lambda logs  
**🔧 Services Used**: Lambda, ALB, CloudWatch Logs, CloudWatch Metrics  
**💡 Key Concept**: Custom CloudWatch metrics with dimensions from structured log data  

**Scenario**: Track API operations by version and response code

### Setup:
```bash
# Create Lambda function
aws lambda create-function \
  --function-name api-metrics-demo \
  --runtime python3.9 \
  --role arn:aws:iam::ACCOUNT:role/lambda-execution-role \
  --handler index.handler \
  --zip-file fileb://function.zip
```

### Lambda Code:
```python
import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Extract from user-agent header
    user_agent = event.get('headers', {}).get('user-agent', 'unknown')
    version = extract_version(user_agent)
    operation = event.get('path', 'unknown')
    
    # Simulate response
    response_code = 200
    
    # Log structured data for CloudWatch metric filter
    logger.info(f"API_METRIC operation={operation} version={version} response_code={response_code}")
    
    return {
        'statusCode': response_code,
        'body': json.dumps({'message': 'success'})
    }

def extract_version(user_agent):
    # Extract version from user-agent
    return user_agent.split('/')[-1] if '/' in user_agent else 'v1.0'
```

### CloudWatch Metric Filter:
```bash
# Create log group
aws logs create-log-group --log-group-name /aws/lambda/api-metrics-demo

# Create metric filter
aws logs put-metric-filter \
  --log-group-name /aws/lambda/api-metrics-demo \
  --filter-name api-operations-filter \
  --filter-pattern '[timestamp, request_id, level="INFO", message="API_METRIC", operation_field, version_field, response_field]' \
  --metric-transformations \
    metricName=APIOperations,metricNamespace=CustomApp,metricValue=1,defaultValue=0,metricValueField=$operation_field,metricDimensions='{Operation=$operation_field,Version=$version_field,ResponseCode=$response_field}'
```

---

## Lab 2: Lambda Provisioned Concurrency with Auto Scaling

**📋 Maps to Question 2**  
**🎯 Purpose**: Reduce Lambda cold start latency with dynamic scaling  
**🔧 Services Used**: Lambda, API Gateway, DynamoDB, Application Auto Scaling  
**💡 Key Concept**: Provisioned concurrency + auto scaling for consistent performance  

**Scenario**: Reduce cold start latency with dynamic scaling

### Setup Provisioned Concurrency:
```bash
# Publish version
aws lambda publish-version \
  --function-name api-function \
  --description "Production version"

# Create alias
aws lambda create-alias \
  --function-name api-function \
  --name prod \
  --function-version 1

# Configure provisioned concurrency
aws lambda put-provisioned-concurrency-config \
  --function-name api-function \
  --qualifier prod \
  --provisioned-concurrency-count 1
```

### Auto Scaling Configuration:
```bash
# Register scalable target
aws application-autoscaling register-scalable-target \
  --service-namespace lambda \
  --resource-id function:api-function:prod \
  --scalable-dimension lambda:function:ProvisionedConcurrency \
  --min-capacity 1 \
  --max-capacity 100

# Create scaling policy
aws application-autoscaling put-scaling-policy \
  --service-namespace lambda \
  --resource-id function:api-function:prod \
  --scalable-dimension lambda:function:ProvisionedConcurrency \
  --policy-name lambda-scaling-policy \
  --policy-type TargetTrackingScaling \
  --target-tracking-scaling-policy-configuration '{
    "TargetValue": 70.0,
    "PredefinedMetricSpecification": {
      "PredefinedMetricType": "LambdaProvisionedConcurrencyUtilization"
    }
  }'
```

---

## Lab 3: CodeDeploy with Environment Variables

**📋 Maps to Question 3**  
**🎯 Purpose**: Dynamic application configuration based on deployment group  
**🔧 Services Used**: CodeDeploy, EC2, Auto Scaling Group, Apache/Tomcat  
**💡 Key Concept**: Using DEPLOYMENT_GROUP_NAME environment variable for dynamic config  

**Scenario**: Dynamic configuration based on deployment group

### AppSpec.yml:
```yaml
version: 0.0
os: linux
files:
  - source: /
    destination: /var/www/html
hooks:
  BeforeInstall:
    - location: scripts/configure_logging.sh
      timeout: 300
      runas: root
  ApplicationStart:
    - location: scripts/start_server.sh
      timeout: 300
      runas: root
```

### Configuration Script:
```bash
#!/bin/bash
# scripts/configure_logging.sh

# Use CodeDeploy environment variable
DEPLOYMENT_GROUP=$DEPLOYMENT_GROUP_NAME

case $DEPLOYMENT_GROUP in
  "dev-group")
    LOG_LEVEL="DEBUG"
    ;;
  "staging-group")
    LOG_LEVEL="INFO"
    ;;
  "prod-group")
    LOG_LEVEL="WARN"
    ;;
  *)
    LOG_LEVEL="INFO"
    ;;
esac

# Update Apache configuration
sed -i "s/LogLevel .*/LogLevel $LOG_LEVEL/" /etc/httpd/conf/httpd.conf

echo "Configured log level: $LOG_LEVEL for deployment group: $DEPLOYMENT_GROUP"
```

### CodeDeploy Setup:
```bash
# Create application
aws deploy create-application \
  --application-name MyWebApp \
  --compute-platform Server

# Create deployment group
aws deploy create-deployment-group \
  --application-name MyWebApp \
  --deployment-group-name dev-group \
  --service-role-arn arn:aws:iam::ACCOUNT:role/CodeDeployServiceRole \
  --auto-scaling-groups MyAutoScalingGroup
```

---

## Lab 4: AWS Config Rule for EBS Volume Tagging

**📋 Maps to Question 4**  
**🎯 Purpose**: Ensure all EBS volumes have required backup tags with auto-remediation  
**🔧 Services Used**: AWS Config, EC2/EBS, Systems Manager Automation, Lambda  
**💡 Key Concept**: Config managed rules + automatic remediation for compliance  

**Scenario**: Ensure all EBS volumes have Backup_Frequency tag

### Custom Config Rule Lambda:
```python
import boto3
import json

def lambda_handler(event, context):
    config = boto3.client('config')
    ec2 = boto3.client('ec2')
    
    # Get configuration item
    configuration_item = event['configurationItem']
    
    if configuration_item['resourceType'] != 'AWS::EC2::Volume':
        return {
            'complianceType': 'NOT_APPLICABLE'
        }
    
    volume_id = configuration_item['resourceId']
    
    # Check if Backup_Frequency tag exists
    tags = configuration_item.get('tags', {})
    
    if 'Backup_Frequency' in tags:
        compliance_type = 'COMPLIANT'
    else:
        compliance_type = 'NON_COMPLIANT'
    
    # Put evaluation
    config.put_evaluations(
        Evaluations=[
            {
                'ComplianceResourceType': 'AWS::EC2::Volume',
                'ComplianceResourceId': volume_id,
                'ComplianceType': compliance_type,
                'OrderingTimestamp': configuration_item['configurationItemCaptureTime']
            }
        ],
        ResultToken=event['resultToken']
    )
    
    return {'complianceType': compliance_type}
```

### Systems Manager Automation Document:
```yaml
schemaVersion: '0.3'
description: Apply default Backup_Frequency tag to EBS volume
assumeRole: '{{ AutomationAssumeRole }}'
parameters:
  VolumeId:
    type: String
    description: EBS Volume ID
  AutomationAssumeRole:
    type: String
    description: IAM role for automation
mainSteps:
  - name: TagVolume
    action: 'aws:executeAwsApi'
    inputs:
      Service: ec2
      Api: CreateTags
      Resources:
        - '{{ VolumeId }}'
      Tags:
        - Key: Backup_Frequency
          Value: weekly
```

---

## Lab 5: Aurora Multi-AZ with Reader Endpoint

**📋 Maps to Question 5**  
**🎯 Purpose**: High availability Aurora cluster with minimal maintenance downtime  
**🔧 Services Used**: Aurora MySQL, RDS, VPC, Security Groups  
**💡 Key Concept**: Reader instances + separate endpoints for read/write operations  

**Scenario**: High availability Aurora cluster setup

### CloudFormation Template:
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  AuroraCluster:
    Type: AWS::RDS::DBCluster
    Properties:
      Engine: aurora-mysql
      MasterUsername: admin
      MasterUserPassword: !Ref DBPassword
      DatabaseName: myapp
      VpcSecurityGroupIds:
        - !Ref DBSecurityGroup
      DBSubnetGroupName: !Ref DBSubnetGroup
      
  AuroraWriter:
    Type: AWS::RDS::DBInstance
    Properties:
      DBClusterIdentifier: !Ref AuroraCluster
      DBInstanceClass: db.r5.large
      Engine: aurora-mysql
      
  AuroraReader:
    Type: AWS::RDS::DBInstance
    Properties:
      DBClusterIdentifier: !Ref AuroraCluster
      DBInstanceClass: db.r5.large
      Engine: aurora-mysql

Outputs:
  ClusterEndpoint:
    Description: Aurora cluster endpoint for writes
    Value: !GetAtt AuroraCluster.Endpoint.Address
    
  ReaderEndpoint:
    Description: Aurora reader endpoint for reads
    Value: !GetAtt AuroraCluster.ReadEndpoint.Address
```

### Application Configuration:
```python
import pymysql

class DatabaseConnection:
    def __init__(self):
        self.write_endpoint = "cluster-endpoint.cluster-xxx.region.rds.amazonaws.com"
        self.read_endpoint = "cluster-endpoint.cluster-ro-xxx.region.rds.amazonaws.com"
        
    def get_write_connection(self):
        return pymysql.connect(
            host=self.write_endpoint,
            user='admin',
            password='password',
            database='myapp'
        )
        
    def get_read_connection(self):
        return pymysql.connect(
            host=self.read_endpoint,
            user='admin',
            password='password',
            database='myapp'
        )
```

---

## Lab 6: Cross-Account AMI Sharing with KMS Encryption

**📋 Maps to Question 6**  
**🎯 Purpose**: Securely share encrypted AMIs across AWS accounts  
**🔧 Services Used**: EC2, AMI, KMS, IAM, Auto Scaling  
**💡 Key Concept**: KMS key policies + grants for cross-account encrypted AMI access  

**Scenario**: Share encrypted AMI between accounts

### Source Account - Encrypt and Share AMI:
```bash
# Copy unencrypted AMI to encrypted
aws ec2 copy-image \
  --source-image-id ami-12345678 \
  --source-region us-east-1 \
  --name "encrypted-app-ami" \
  --description "Encrypted version of app AMI" \
  --encrypted \
  --kms-key-id arn:aws:kms:us-east-1:SOURCE-ACCOUNT:key/key-id

# Share encrypted AMI
aws ec2 modify-image-attribute \
  --image-id ami-encrypted123 \
  --launch-permission "Add=[{UserId=TARGET-ACCOUNT-ID}]"
```

### KMS Key Policy Update:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::TARGET-ACCOUNT:root"
      },
      "Action": [
        "kms:CreateGrant",
        "kms:Decrypt",
        "kms:DescribeKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "ec2.us-east-1.amazonaws.com"
        }
      }
    }
  ]
}
```

### Target Account - Create Grant:
```bash
# Create KMS grant for Auto Scaling
aws kms create-grant \
  --key-id arn:aws:kms:us-east-1:SOURCE-ACCOUNT:key/key-id \
  --grantee-principal arn:aws:iam::TARGET-ACCOUNT:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling \
  --operations Decrypt DescribeKey CreateGrant
```

---

## Lab 7: CodePipeline with CodeDeploy Integration

**📋 Maps to Question 7**  
**🎯 Purpose**: Complete CI/CD pipeline with automated deployment to EC2 fleet  
**🔧 Services Used**: CodePipeline, CodeBuild, CodeDeploy, CodeCommit, EC2, Auto Scaling  
**💡 Key Concept**: Pipeline integration with CodeDeploy for in-place deployments  

**Scenario**: Automated deployment pipeline

### Pipeline CloudFormation:
```yaml
Resources:
  CodePipeline:
    Type: AWS::CodePipeline::Pipeline
    Properties:
      RoleArn: !GetAtt CodePipelineRole.Arn
      Stages:
        - Name: Source
          Actions:
            - Name: SourceAction
              ActionTypeId:
                Category: Source
                Owner: AWS
                Provider: CodeCommit
                Version: 1
              Configuration:
                RepositoryName: !Ref RepoName
                BranchName: main
              OutputArtifacts:
                - Name: SourceOutput
                
        - Name: Build
          Actions:
            - Name: BuildAction
              ActionTypeId:
                Category: Build
                Owner: AWS
                Provider: CodeBuild
                Version: 1
              Configuration:
                ProjectName: !Ref BuildProject
              InputArtifacts:
                - Name: SourceOutput
              OutputArtifacts:
                - Name: BuildOutput
                
        - Name: Deploy
          Actions:
            - Name: DeployAction
              ActionTypeId:
                Category: Deploy
                Owner: AWS
                Provider: CodeDeploy
                Version: 1
              Configuration:
                ApplicationName: !Ref CodeDeployApplication
                DeploymentGroupName: !Ref DeploymentGroup
              InputArtifacts:
                - Name: BuildOutput
```

### BuildSpec.yml:
```yaml
version: 0.2
phases:
  install:
    runtime-versions:
      python: 3.9
  build:
    commands:
      - echo Build started on `date`
      - # Build your application
      - rpmbuild -ba myapp.spec
artifacts:
  files:
    - '**/*'
  name: myapp-$(date +%Y-%m-%d)
```

---

## Lab 8: AWS Firewall Manager for WAF

**📋 Maps to Question 8**  
**🎯 Purpose**: Centralized WAF management across multiple AWS accounts  
**🔧 Services Used**: Firewall Manager, WAF, ALB, API Gateway, Organizations  
**💡 Key Concept**: Delegated admin + centralized security policy enforcement  

**Scenario**: Centralized WAF management across accounts

### Firewall Manager Policy:
```json
{
  "PolicyName": "ALB-WAF-Policy",
  "SecurityServiceType": "WAFV2",
  "ResourceType": "AWS::ElasticLoadBalancingV2::LoadBalancer",
  "ResourceTags": [
    {
      "Key": "Environment",
      "Value": "Production"
    }
  ],
  "ExcludeResourceTags": false,
  "RemediationEnabled": true,
  "SecurityServicePolicyData": {
    "Type": "WAFV2",
    "ManagedServiceData": {
      "type": "WAFV2",
      "preProcessRuleGroups": [],
      "postProcessRuleGroups": [],
      "defaultAction": {
        "type": "ALLOW"
      },
      "overrideCustomerWebACLAssociation": false
    }
  }
}
```

### Setup Commands:
```bash
# Enable Firewall Manager
aws fms put-admin-account --admin-account SECURITY-ACCOUNT-ID

# Create policy
aws fms put-policy --policy file://waf-policy.json
```

---

## Lab 9: AWS Config Custom Rule for KMS Key Rotation

**📋 Maps to Question 9**  
**🎯 Purpose**: Monitor and alert on KMS keys not rotated within 90 days  
**🔧 Services Used**: AWS Config, KMS, Lambda, SNS  
**💡 Key Concept**: Custom Config rules for compliance monitoring with notifications  

**Scenario**: Monitor KMS key rotation compliance

### Lambda Function:
```python
import boto3
import json
from datetime import datetime, timedelta

def lambda_handler(event, context):
    config = boto3.client('config')
    kms = boto3.client('kms')
    
    # Get all KMS keys
    keys = kms.list_keys()
    evaluations = []
    
    for key in keys['Keys']:
        key_id = key['KeyId']
        
        try:
            # Get key metadata
            key_metadata = kms.describe_key(KeyId=key_id)
            
            # Skip AWS managed keys
            if key_metadata['KeyMetadata']['KeyManager'] == 'AWS':
                continue
                
            creation_date = key_metadata['KeyMetadata']['CreationDate']
            days_old = (datetime.now(creation_date.tzinfo) - creation_date).days
            
            # Check if key is older than 90 days
            compliance_type = 'NON_COMPLIANT' if days_old > 90 else 'COMPLIANT'
            
            evaluations.append({
                'ComplianceResourceType': 'AWS::KMS::Key',
                'ComplianceResourceId': key_id,
                'ComplianceType': compliance_type,
                'OrderingTimestamp': datetime.now()
            })
            
        except Exception as e:
            print(f"Error processing key {key_id}: {e}")
    
    # Submit evaluations
    if evaluations:
        config.put_evaluations(
            Evaluations=evaluations,
            ResultToken=event['resultToken']
        )
    
    return {'evaluationsCount': len(evaluations)}
```

---

## Lab 10: Secure CodeBuild with S3 Access

**📋 Maps to Question 10**  
**🎯 Purpose**: Secure artifact access in build process without unauthenticated requests  
**🔧 Services Used**: CodeBuild, S3, IAM  
**💡 Key Concept**: Service roles + least privilege access for secure builds  

**Scenario**: CodeBuild accessing S3 with proper IAM permissions

### IAM Role Policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::my-build-artifacts/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-build-artifacts"
      ]
    }
  ]
}
```

### BuildSpec with S3 Download:
```yaml
version: 0.2
phases:
  pre_build:
    commands:
      - echo Downloading database script
      - aws s3 cp s3://my-build-artifacts/db-populate.sql ./scripts/
  build:
    commands:
      - echo Build started
      - chmod +x ./scripts/db-populate.sql
      - # Run your build commands
```

### S3 Bucket Policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::my-build-artifacts",
        "arn:aws:s3:::my-build-artifacts/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
```

---

## Practice Commands

### Test các lab:
```bash
# Lab 1: Test CloudWatch metrics
aws logs filter-log-events --log-group-name /aws/lambda/api-metrics-demo

# Lab 2: Check provisioned concurrency
aws lambda get-provisioned-concurrency-config --function-name api-function --qualifier prod

# Lab 4: Test Config rule
aws configservice get-compliance-details-by-resource --resource-type AWS::EC2::Volume

# Lab 9: Test KMS key age
aws kms list-keys
aws kms describe-key --key-id KEY-ID
```

Mỗi lab này sẽ giúp bạn thực hành hands-on với các concept trong từng câu hỏi. Bạn có thể chạy từng lab để hiểu rõ hơn về cách các dịch vụ AWS hoạt động trong thực tế.

## Additional Question References (Not covered in detailed labs above):

**Question 11**: IAM Identity Center + Control Tower + External IdP  
**Question 12**: Lambda concurrency + SQS + DynamoDB scaling issues  
**Question 13**: AWS Config + EventBridge for EC2 instance profile compliance  
**Question 14**: SAM + CodeDeploy canary deployments for serverless  
**Question 15**: VPC endpoints + private subnets for secure deployments  
**Question 16**: EventBridge rules for CodePipeline triggers  
**Question 17**: EventBridge + Lambda for security group monitoring  
**Question 18**: ALB + IPv6 + dual-stack configuration

---

## Lab 11: IAM Identity Center with Control Tower

**📋 Maps to Question 11**  
**🎯 Purpose**: Robust permission model with external IdP and least privilege  
**🔧 Services Used**: Control Tower, IAM Identity Center, External IdP (SAML), Organizations  
**💡 Key Concept**: Permission sets + attribute-based access control + principal tags  

### Control Tower Setup:
```bash
# Enable Control Tower (via Console - no CLI command)
# Set up landing zone with organizational units

# Configure IAM Identity Center
aws sso-admin create-permission-set \
  --instance-arn arn:aws:sso:::instance/ssoins-1234567890abcdef \
  --name DevOpsTeamPermissionSet \
  --description "DevOps team permissions with principal tag conditions"
```

### Permission Set with Principal Tags:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:*",
        "s3:*",
        "lambda:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalTag/Team": "${aws:PrincipalTag/Team}",
          "aws:RequestedRegion": "us-east-1"
        }
      }
    }
  ]
}
```

### Attribute Mapping Configuration:
```json
{
  "AttributeMap": {
    "Team": "${path:enterprise.department}",
    "Project": "${path:enterprise.division}",
    "Role": "${path:enterprise.title}"
  }
}
```

---

## Lab 12: Lambda Concurrency and DynamoDB Scaling Issues

**📋 Maps to Question 12**  
**🎯 Purpose**: Resolve order processing delays in Lambda + SQS + DynamoDB system  
**🔧 Services Used**: Lambda, SQS, DynamoDB, CloudWatch  
**💡 Key Concept**: Monitor ApproximateAgeOfOldestMessage + WriteThrottleEvents metrics  

### Check SQS Metrics:
```bash
# Monitor SQS queue age
aws cloudwatch get-metric-statistics \
  --namespace AWS/SQS \
  --metric-name ApproximateAgeOfOldestMessage \
  --dimensions Name=QueueName,Value=order-processing-queue \
  --start-time 2024-01-01T00:00:00Z \
  --end-time 2024-01-01T01:00:00Z \
  --period 300 \
  --statistics Average
```

### Increase Lambda Concurrency:
```bash
# Check current reserved concurrency
aws lambda get-function-concurrency --function-name order-processor

# Increase reserved concurrency
aws lambda put-function-concurrency \
  --function-name order-processor \
  --reserved-concurrent-executions 100
```

### Monitor DynamoDB Throttling:
```bash
# Check DynamoDB write throttles
aws cloudwatch get-metric-statistics \
  --namespace AWS/DynamoDB \
  --metric-name WriteThrottleEvents \
  --dimensions Name=TableName,Value=orders \
  --start-time 2024-01-01T00:00:00Z \
  --end-time 2024-01-01T01:00:00Z \
  --period 300 \
  --statistics Sum
```

### Update DynamoDB Auto Scaling:
```bash
# Increase max write capacity
aws application-autoscaling put-scaling-policy \
  --service-namespace dynamodb \
  --resource-id table/orders \
  --scalable-dimension dynamodb:table:WriteCapacityUnits \
  --policy-name orders-write-scaling-policy \
  --policy-type TargetTrackingScaling \
  --target-tracking-scaling-policy-configuration '{
    "TargetValue": 70.0,
    "PredefinedMetricSpecification": {
      "PredefinedMetricType": "DynamoDBWriteCapacityUtilization"
    }
  }'
```

---

## Lab 13: AWS Config for EC2 Instance Profile Compliance

**📋 Maps to Question 13**  
**🎯 Purpose**: Ensure all EC2 instances have instance profiles attached  
**🔧 Services Used**: AWS Config, EC2, Systems Manager  
**💡 Key Concept**: Config managed rule + automatic remediation for compliance  

### Config Rule Setup:
```bash
aws configservice put-config-rule \
  --config-rule '{
    "ConfigRuleName": "ec2-instance-profile-attached",
    "Source": {
      "Owner": "AWS",
      "SourceIdentifier": "EC2_INSTANCE_PROFILE_ATTACHED"
    }
  }'
```

---

## Lab 14: SAM with CodeDeploy Canary Deployments

**📋 Maps to Question 14**  
**🎯 Purpose**: Serverless deployment with gradual rollout and monitoring  
**🔧 Services Used**: SAM, CodeDeploy, Lambda, CloudWatch Alarms  
**💡 Key Concept**: Canary deployments with automatic rollback on alarms  

### SAM Template:
```yaml
Transform: AWS::Serverless-2016-10-31
Globals:
  Function:
    AutoPublishAlias: live
    DeploymentPreference:
      Type: Canary10Percent15Minutes
      Alarms:
        - !Ref ErrorAlarm
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: app.handler
      Runtime: python3.9
  ErrorAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      MetricName: Errors
      Namespace: AWS/Lambda
      Statistic: Sum
      Threshold: 0
```

---

## Lab 15: VPC Endpoints for Private Deployments

**📋 Maps to Question 15**  
**🎯 Purpose**: Deploy applications without internet access using VPC endpoints  
**🔧 Services Used**: VPC, S3, VPC Endpoints, EC2, IAM  
**💡 Key Concept**: Private connectivity to AWS services via VPC endpoints  

### VPC Endpoint for S3:
```bash
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-12345678 \
  --service-name com.amazonaws.us-east-1.s3 \
  --route-table-ids rtb-12345678
```

### User Data Script:
```bash
#!/bin/bash
aws s3 cp s3://my-artifacts/app.tar.gz /tmp/
tar -xzf /tmp/app.tar.gz -C /opt/
systemctl start myapp
```

---

## Lab 16: EventBridge Rules for CodePipeline Triggers

**📋 Maps to Question 16**  
**🎯 Purpose**: Troubleshoot pipeline not triggering on CodeCommit changes  
**🔧 Services Used**: EventBridge, CodeCommit, CodePipeline  
**💡 Key Concept**: EventBridge rules for repository change events  

### EventBridge Rule:
```bash
aws events put-rule \
  --name codecommit-main-branch \
  --event-pattern '{
    "source": ["aws.codecommit"],
    "detail-type": ["CodeCommit Repository State Change"],
    "detail": {
      "referenceType": ["branch"],
      "referenceName": ["main"]
    }
  }'
```

---

## Lab 17: EventBridge + Lambda for Security Group Monitoring

**📋 Maps to Question 17**  
**🎯 Purpose**: Detect and remediate unrestricted security group rules  
**🔧 Services Used**: EventBridge, Lambda, EC2, SNS  
**💡 Key Concept**: Real-time security compliance with event-driven remediation  

### EventBridge Rule:
```bash
aws events put-rule \
  --name security-group-changes \
  --event-pattern '{
    "source": ["aws.ec2"],
    "detail-type": ["AWS API Call via CloudTrail"],
    "detail": {
      "eventSource": ["ec2.amazonaws.com"],
      "eventName": ["AuthorizeSecurityGroupIngress", "CreateSecurityGroup"]
    }
  }'
```

### Lambda Function:
```python
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    sns = boto3.client('sns')
    
    sg_id = event['detail']['responseElements']['groupId']
    
    # Get security group rules
    response = ec2.describe_security_groups(GroupIds=[sg_id])
    sg = response['SecurityGroups'][0]
    
    # Check for 0.0.0.0/0 rules
    for rule in sg['IpPermissions']:
        for ip_range in rule.get('IpRanges', []):
            if ip_range.get('CidrIp') == '0.0.0.0/0':
                # Remove unrestricted rule
                ec2.revoke_security_group_ingress(
                    GroupId=sg_id,
                    IpPermissions=[rule]
                )
                # Send notification
                sns.publish(
                    TopicArn='arn:aws:sns:region:account:security-alerts',
                    Message=f'Removed unrestricted rule from {sg_id}'
                )
```

---

## Lab 18: ALB with IPv6 Support

**📋 Maps to Question 18**  
**🎯 Purpose**: Configure ALB to accept IPv6 client requests  
**🔧 Services Used**: ALB, VPC, EC2, CloudFormation  
**💡 Key Concept**: Dual-stack configuration for IPv4/IPv6 support  

### CloudFormation Template:
```yaml
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      
  IPv6Block:
    Type: AWS::EC2::VPCCidrBlock
    Properties:
      VpcId: !Ref VPC
      AmazonProvidedIpv6CidrBlock: true
      
  PublicSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.1.0/24
      Ipv6CidrBlock: !Select [0, !Cidr [!Select [0, !GetAtt VPC.Ipv6CidrBlocks], 256, 64]]
      
  LoadBalancer:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      IpAddressType: dualstack
      Subnets: [!Ref PublicSubnet]
      
  Listener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      LoadBalancerArn: !Ref LoadBalancer
      Port: 443
      Protocol: HTTPS
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref TargetGroup
```
