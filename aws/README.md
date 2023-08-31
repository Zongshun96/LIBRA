# LIBRA on AWS

LIBRA is a load-balancing method that considers cloud services with different cost models to serve transient versus persistent traffic.
Using AWS EC2 (for persistent traffic) and AWS Lambda (for transient traffic), we have presented LIBRA with WITS traffic data in the [paper](https://doi.ieeecomputersociety.org/10.1109/IC2E52221.2021.00028).
This repository contains the data and artifacts needed to reproduce our results.
A more extensive evaluation for the robustness and cost-saving of our load balancing strategy can be performed by configuring different load balancing threshold values (CIP) and cloud services, e.g., spot instances, containers, or serverless. One can also experiment with prewarming containers and other prefetching techniques.


To run the experiment, 
1. First build a VM Launch Template / Configuration (E.g., [sample app](https://github.com/Zongshun96/EC2_application/tree/1SecImgLoad/simple_python_MT_server)), deploy a Lambda Function(e.g., [sample app](https://github.com/Zongshun96/EC2_application/tree/1SecImgLoad/lambda_ImgLoad1Sec)) and create an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/tutorial-application-load-balancer-cli.html).
    1. [Launch Template](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html) will be used by the autoscaling group created by our script to create new VM instances. The template name will be used in `configuration.py`, so please remember this name. For the sample app in VM, we can write a script in the `user data` in template to start the python server during launching a VM instance.
    [Here](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#advanced-settings-for-your-launch-template) is a tutorial.
    1. We also need to create a [Lambda Function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html) available to invoke before the experiment. One way is to create an `archive.zip` using the [sample app](https://github.com/Zongshun96/EC2_application/tree/1SecImgLoad/lambda_ImgLoad1Sec) for Lambda deployment. [Here](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html) is a tutorial.
1. Now configure experiment in `configuration.py`, i.e workload file path (e.g., `self.log_file_name = '/home/cc/LIBRA/traces/wits_logs.txt'`), ALB url, autoscaling and alarm configurations ([simple](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html), [target](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)), etc. More information about the parameters is documented in the file.
1. And then please [setup your AWS credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#interactive-configuration) so that our script can setup autoscaling automatically.
1. After that run `python3 run_experiment.py`. Check your autoscaling group as its `desire replica` is changing. And there will be a log file for each requests in the dir you run the script.
1. Finally, we can plot the cost and statistics using our [plotting script](https://github.com/Zongshun96/AWS_EC2_Evaluations). The results should corresponding to our plots in the paper. 


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

`requirements.txt`
```
Dependancies for the scripts
```