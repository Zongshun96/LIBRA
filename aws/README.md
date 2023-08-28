# LIBRA on AWS
The experiment to distribute computation requests among EC2 instances and Lambda Function

To run the experiment, 
1. First build your VM Launch Template / Configuration, Lambda Function and [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/tutorial-application-load-balancer-cli.html).
1. Now configure your experiment in `configuration.py` i.e input log file path, ALB url, autoscaling and alarm configurations ([simple](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html), [target](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)), etc.
1. And then please [setup your AWS credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#interactive-configuration) so that our script can setup autoscaling automatically.
1. After that run `python3 run_experiment.py`. Monitor your autoscaling group as its `desire replica` is changing. And there will be a log file for each requests in the dir you run the script.

# Files
`run_experiment.py`
```
This is the entry point of the experiments. It creates services with utility functions and calls manager to generate traffic.
```

Utility Functions(`req_utils.py` and `VM_utils.py`)
```
To send requests, create EC2 autoscaling group and cloudwatch alarms
```

`configuration.py`
```
The experiment settings
```

requirements
```
requests
boto3
pytz
```