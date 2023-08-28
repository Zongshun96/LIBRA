import logging


class configuration:
    def __init__(self):
        # logging information
        self.logging_level = logging.INFO

        # manager
        self.alpha = 0.9
        self.mu = self.alpha
        self.wait_for_server = True
        

        # experiment parameters
        self.start_time = 1  # it should always start from greater than 0
        self.end_time = 1800  # 30 mins
        self.epoch_time = 1

        # ===================================================================
        # The corresponding cases in paper:     'vm_cloud_max'  = MAX
        #                                       'serverless'    = Faas
        #                                       'vm_cloud'      = AUTO
        #                                       'hybrid'        = LIBRA
        #                                       'vm_cloud_hide' = SPOCK
        # ===================================================================
        self.policy = 'hybrid'    # self.policy = 'vm_cloud_max' | 'serverless' | 'vm_cloud'#'hybrid' | 'vm_cloud_hide'
        

        # load
        # self.total_requests = 10
        # self.load_type = 'poisson'
        self.load_type = 'logs'
        self.log_file_name = '/home/cc/LIBRA/traces/wits_logs.txt'
        self.LoadFactor=16  # traffic scale, i.e., 234 requests per second / LoadFactor
        
        self.no_vm_update_freq = 300  # period in sec for scaling manager to scale
        self.vm_provison_prop = 0.80  # expected load percentage: 
        self.req_config = {'memory': 512,   
                           'cpu': 2.4}  # logging
        

        # vm cloud
        self.vm_state_epoch = 1
        self.NumOfReqPerVM = 4  # based on off-line profiling: how many requests can be handled within SLA per VM
        self.WaitingTimeForCloudWatch = 0   # 5 data points before alarm triggers.
        self.scaling_policy_type = "target"   # self.scaling_policy_type = "target" | "simple"
        self.lambda_url = "https://0123456789.execute-api.us-east-2.amazonaws.com/default/ImgLoad1Sec-py39"
        self.alb_url = "http://LIBRA-Reproducibility-01234567.us-east-2.elb.amazonaws.com:8080"  # ALB url
        self.payload = ''
        self.headers = {'Content-Type': 'application/json'}
        self.min_num_instance = 1
        self.max_num_instance = 9
        self.des_num_instance = 1

        # VM_utils
        self.launch_configuration_name = 't3.medium'    # VM image
        self.launch_template = {
            # 'launchTemplateId': 'lt-018ff0424822f5f4e',
            'LaunchTemplateName': 'LIBRA-Reproducibility',
            'Version': '5'
            }
        self.auto_scaling_group_name = '101_20230825_hybrid_4_req_per_vm_pos_std_1800_total'
        self.DefaultCooldown=300
        self.target_group_ARNs=[
                'arn:aws:elasticloadbalancing:us-east-2:123456789012:targetgroup/testing/01234567890123',
            ]
        self.VPC_zone_identifier='subnet-0a1f3a70, subnet-8b1b96c7, subnet-12da3579'
        self.service_linked_role_ARN='arn:aws:iam::123456789012:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling'
        self.UpperAlarmName = '101_testingHigh'
        self.LowerAlarmName = '101_testingLow'
        self.PolicyCooldown=300
        self.TargetTrackingConfiguration={
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
        self.AlarmDimensions=[
                    {
                        'Name': 'TargetGroup',
                        'Value': 'targetgroup/testing/01234567890123'
                    },
                    {
                        'Name': 'LoadBalancer',
                        'Value': 'app/LIBRA-Reproducibility/0123456789012'
                    },
                ]
        self.UpperAlarmThreshold=100.0
        self.LowerAlarmThreshold=60.0

        self.log_file = 'serverless_' + self.policy + '_update_' + str(self.no_vm_update_freq) + '_' + str(
            self.vm_provison_prop) + '.log'

        # req_utils
        self.FunctionName = "ImgLoad1Sec-py39"   # Lambda function name


