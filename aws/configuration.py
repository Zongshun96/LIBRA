import logging


class configuration:
    def __init__(self):
        # logging information
        self.logging_level = logging.INFO

        # manager
        self.alpha = 0.9    # Script sets moving average parameter for workload mean, i.e., (1-alpha) * new observation + alpha * historical data .
        self.mu = self.alpha # Script sets moving average parameter for workload standard deviation(std)
        # self.wait_for_server = True
        self.no_vm_update_freq = 300  # Script sets waiting in sec for LIBRA manager to scale
        self.vm_provison_prop = 0.80  # Script sets expected load percentage: avoid using 100% of resources from the VM.
        

        # experiment
        self.start_time = 1  # Script runs experiment from timestamp 1
        self.end_time = 1800  # Script uses from 1st to 1800th entries in the log to gernerate traffic, where each unit will last self.epoch_time second(s). Here it will last for 30 mins. Options: change according to the experiment scale.
        self.epoch_time = 1 # Script sets 1 second as the unit time for experiment.

        # ===================================================================
        # The corresponding cases in paper:     'vm_cloud_max'  = MAX
        #                                       'serverless'    = Faas
        #                                       'vm_cloud'      = AUTO
        #                                       'hybrid'        = LIBRA
        #                                       'vm_cloud_hide' = SPOCK
        # ===================================================================
        self.policy = 'vm_cloud_hide'    # Script sets the scaling policy used in experiments. Options: 'vm_cloud_max' | 'serverless' | 'vm_cloud' | 'hybrid' | 'vm_cloud_hide'
        

        # traffic_generator
        self.req_config = {'memory': 512, 'cpu': 2.4}  # for logging only

        ## for synthetic data
        # self.total_requests = 10      
        # self.load_type = 'poisson'     # Script sets load type. Options: 'logs' | 'poisson'

        ## for log data
        self.load_type = 'logs' # Script sets load type. Options: 'logs' | 'poisson'
        self.log_file_name = 'traces/wits_logs.txt' # Script sets log file pathname: This log file contains a list of count of messages to be served. Options: traces/berkeley_logs.txt | traces/sin_logs.txt | traces/square_load.txt
        self.LoadFactor=16  # Script sets scale traffic to save experiment cost, e.g., 234 requests per second / self.LoadFactor; Options: change according to the experiment scale.
        

        # vm cloud
        self.vm_state_epoch = 1 # 
        self.NumOfReqPerVM = 4  # Script sets how many requests can be handled within SLA per VM based on offline profiling; Options: change according to the VM configuration.
        # self.WaitingTimeForCloudWatch = 0   # 5 data points before alarm triggers.
        self.scaling_policy_type = "target"   # AWS autoscaling policy type; Options: "target" | "simple"
        self.min_num_instance = 1   # Script sets a minimum number of VMs for the AWS EC2 autoscaling group. Options: with `self.policy = 'hybrid'`, this can be 0. Otherwise, change it according to the experiment scale.
        self.max_num_instance = 9   # Script sets a maximum number of VMs for the AWS EC2 autoscaling group. Options: change it according to the experiment scale.
        self.des_num_instance = 1   # Script sets an initial number of VMs. Options: It sets the number of VM to provision. When `self.policy = 'hybrid'`, it will be changed by `manager.handle_requests()``. Otherwise, it is set by the autoscaling group based on your scaling policy.

        # VM_utils
        self.launch_configuration_name = 't3.medium'    # (Obsoleted by AWS.) Before running the script, preconfigure an EC2 instance launch configuration for autoscaling group to provision new VMs.
        self.launch_template = {                        # Before running the script, we need to set the name of a launch template. It would be used by autoscaling group to provision new VMs. Options: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html
            # 'launchTemplateId': 'lt-018ff0424822f5f4e',
            'LaunchTemplateName': 'LIBRA-Reproducibility',
            'Version': '5'
            }
        self.auto_scaling_group_name = '101_20230825_hybrid_4_req_per_vm_pos_std_1800_total'    # Script creates a new autoscaling group with this name.
        self.DefaultCooldown=300                                                                # Script sets for autoscaling group to wait for another scaling decision. Options: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html
        self.target_group_ARNs=[
                'arn:aws:elasticloadbalancing:us-east-2:123456789012:targetgroup/testing/01234567890123',   # Script attaches the autoscaling group with the target group of an existing Application load balancer created before running the script. Options: https://docs.aws.amazon.com/autoscaling/ec2/userguide/examples-elastic-load-balancing-aws-cli.html
            ]
        self.VPC_zone_identifier='subnet-0a1f3a70, subnet-8b1b96c7, subnet-12da3579'                        # Attach the autoscaling group with the target group of an existing Application load balancer created before running the script. Options: https://docs.aws.amazon.com/autoscaling/ec2/userguide/examples-elastic-load-balancing-aws-cli.html
        # self.service_linked_role_ARN='arn:aws:iam::123456789012:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling'
        self.UpperAlarmName = '101_testingHigh'     # Script creates an alarm for a high threshold for scaling out. This alarm will be used by `simple` autoscaling policy.
        self.LowerAlarmName = '101_testingLow'      # Script creates an alarm for a low threshold for scaling in. This alarm will be used by `simple` autoscaling policy.
        self.PolicyCooldown=300                     # Script sets for autoscaling group to wait for another scaling decision. Options: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html
        self.TargetTrackingConfiguration={          # Script sets target tracking autoscaling policy. Options: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html#target-tracking-policy-creating-aws-cli
                    'PredefinedMetricSpecification': {
                        'PredefinedMetricType': 'ALBRequestCountPerTarget',
                        'ResourceLabel': 'app/LIBRA-Reproducibility/0123456789012/targetgroup/testing/01234567890123'
                    },
                    # 'CustomizedMetricSpecification': {
                    #     'MetricName': 'string',
                    #     'Namespace': 'string',
                    #     'Dimensions': [
                    #         {
                    #             'Name': 'string',
                    #             'Value': 'string'
                    #         },
                    #     ],
                    #     'Statistic': 'Average'|'Minimum'|'Maximum'|'SampleCount'|'Sum',
                    #     'Unit': 'string'
                    # },
                    'TargetValue': 240.0,
                    'DisableScaleIn': False
                }
        self.AlarmDimensions=[  # Script sets the metrics sources. Options: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension
                    {
                        'Name': 'TargetGroup',
                        'Value': 'targetgroup/testing/01234567890123'
                    },
                    {
                        'Name': 'LoadBalancer',
                        'Value': 'app/LIBRA-Reproducibility/0123456789012'
                    },
                ]
        self.UpperAlarmThreshold=100.0  # Script sets high alarm threshold. This alarm will be used by `simple` autoscaling policy. Options: set based on offline profiling. There was a 5 mins delay for the AWS Cloudwatch metrics, so our evaluation show significant over/under provisioning, setting based on expected workload won't provide the best performance and cost.
        self.LowerAlarmThreshold=60.0   # Script sets low alarm threshold. This alarm will be used by `simple` autoscaling policy.

        self.log_file = 'serverless_' + self.policy + '_update_' + str(self.no_vm_update_freq) + '_' + str(self.vm_provison_prop) + '.log' # Script sets logfile name. We will use this log to study requests statitics.

        # req_utils
        self.FunctionName = "ImgLoad1Sec-py39"   # (not practical)Before running the script, we need to deploy the Lambda function first. Here we set the Lambda function name to invoke with boto3.
        self.lambda_url = "https://0123456789.execute-api.us-east-2.amazonaws.com/default/ImgLoad1Sec-py39" # Before running the script, we need to deploy the Lambda function first. Here we set the function url / API gateway to invoke. Options: https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html
        self.alb_url = "http://LIBRA-Reproducibility-01234567.us-east-2.elb.amazonaws.com:8080"  # Before running the script, we need to create an Application Load Balancer with a target group which will be attached to the script created auto scaling group. We will send requests to this ALB url and ALB will distribute requests to all running VMs. Options: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html
        self.payload = ''       # Script sets a payload to invoke function. Options: bigger payload size can lead to longer running time / cost of VMs. While Lambda might not be charged for this extra transmission delay.
        self.headers = {'Content-Type': 'application/json'} # Script sets the HTTP request header.


