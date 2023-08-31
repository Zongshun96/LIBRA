# LIBRA
This repos includes both a simulator (`simulator/`) and an implementation with AWS (`aws/`) for LIBRA.
Our work explores the joint usage of IaaS and FaaS to cater the dyanmic need of an application with medium to high popularity.

Our paper has been published at IEEE IC2E2021 (Best Paper Award!) [doi](https://doi.ieeecomputersociety.org/10.1109/IC2E52221.2021.00028).
Please feel free to cite our work with bibtax below
```
@INPROCEEDINGS {9610213,
author = {A. Raza and Z. Zhang and N. Akhtar and V. Isahagian and I. Matta},
booktitle = {2021 IEEE International Conference on Cloud Engineering (IC2E)},
title = {LIBRA: An Economical Hybrid Approach for Cloud Applications with Strict SLAs},
year = {2021},
volume = {},
issn = {},
pages = {136-146},
abstract = {Function-as-a-Service (FaaS) has recently emerged to reduce the deployment cost of running cloud applications compared to Infrastructure-as-a-Service (IaaS). FaaS follows a serverless “pay-as-you-go” computing model; it comes at a higher cost per unit of execution time but typically application functions experience lower provisioning time (startup delay). IaaS requires the provisioning of Virtual Machines, which typically suffer from longer cold-start delays that cause higher queuing delays and higher request drop rates. We present LIBRA, a balanced (hybrid) approach that leverages both VM-based and serverless resources to efficiently manage cloud resources for the applications. LIBRA closely monitors the application demand and provisions appropriate VM and serverless resources such that the running cost is minimized and Service-Level Agreements are met. Unlike state of the art, LIBRA not only hides VM cold-start delays, and hence reduces response time, by leveraging serverless, but also directs a low-rate bursty portion of the demand to serverless where it would be less costly than spinning up new VMs. We evaluate LIBRA on real traces in a simulated environment as well as on the AWS commercial cloud. Our results show that LIBRA outperforms other resource-provisioning policies, including a recent hybrid approach - LIBRA achieves more than 85% reduction in SLA violations and up to 53% cost savings.},
keywords = {cloud computing;costs;conferences;computational modeling;faa;virtual machining;delays},
doi = {10.1109/IC2E52221.2021.00028},
url = {https://doi.ieeecomputersociety.org/10.1109/IC2E52221.2021.00028},
publisher = {IEEE Computer Society},
address = {Los Alamitos, CA, USA},
month = {oct}
}

```

## Traces
The traces folder contains the logs used for evaluation, with each line containing the number of request arrived during particular second (line number indicates the corresponding time (in seconds))


