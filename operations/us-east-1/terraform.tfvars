application_aws_account_number = "595052274509" # AWS application account number (without hyphens)

auto_IAM_mode = false # Create IAM Policies in AWS (default false)

auto_IAM_path = "/" # IAM path for auto IAM mode uploaded policies

azs = ["us-east-1a", "us-east-1b", "us-east-1c"] # Availability Zones for the cluster (1 master per AZ will be deployed)

environment_type = "dev" # Type of environment (e.g. test, production)

http_proxy = "http://10.81.6.5" # IP of corporate HTTP proxy

http_proxy_port = 8080 # HTTP proxy port to use for access to internet. This is required to install packages on instances deployed in ops AWS accounts.

jenkins_config_repo_url = "ssh://git@git.bmwgroup.net:7999/~qtb8117/mrt-environment-config.git" # Git repo url with Product Domain configuration (Fork of this repo.)

jenkins_ec2_instance_type = "t3.medium" # Instance type for Core Infra Jenkins Master

jenkins_http_allowed_cidrs = ["10.0.0.0/8"] # CIDRs we allow http from (List)

jenkins_iam_policy_names_prefix = "/" # Prefix for policy names created (default /)

jenkins_ssh_allowed_cidrs = ["10.0.0.0/8"] # CIDRs we allow ssh from (List)

jenkins_dns_domain_hosted_zone_ID = "Z2MGR6V51SQEDS" # R53 Hosted Zone ID for domain that will be used by Jenkins master

jenkins_dns_hostname = "Jenkins" # Local part of FQDN for Jenki

jenkins_subnet_id = "subnet-2fad3d65" # ID of existing subnet where Jenkins will be deployed

k8s_cluster_name_postfix = "k8s.local" # Domain name of Kubernetes cluster (currently only k8s.local is supported)

k8s_master_instance_type = "m4.large" # Instance type (size) for master nodes

k8s_masters_iam_policies_arns = [
  "arn:aws:iam:::policy/masters.mrt9-dev-ops.k8s.local",
  "arn:aws:iam:::policy/masters_extra.mrt9-dev-ops.k8s.local",
] # List of existing IAM policies that will be attached to instance profile for master nodes (EC2 instances)

k8s_node_count = "3" # Number of worker nodes in Kubernetes cluster

k8s_node_instance_type = "m4.large" # Instance type (size) for worker nodes

k8s_nodes_iam_policies_arns = [
  "arn:aws:iam:::policy/nodes.mrt9-dev-ops.k8s.local",
  "arn:aws:iam:::policy/AssumeKopsCrossAccount",
] # List of existing IAM policies that will be attached to instance profile for worker nodes (EC2 instances)

k8s_private_subnets = ["subnet-2fad3d65", "subnet-50804c0c", "subnet-c819d3af"] # List of private subnets (matching AZs) where to deploy the cluster (required if existing VPC is used)

logs_not_resource = [] # List of resources that log police will use for NotResource, empty means that Resource * is set

operations_aws_account_number = "090011926616" # AWS operations account number (without hyphens)

product_domain_name = "mrt9" # Name of product domain, will be used to create other names

region = "us-east-1" # AWS region

vpc_id = "vpc-628b8b19" # ID of existing VPC (must be pre-created)