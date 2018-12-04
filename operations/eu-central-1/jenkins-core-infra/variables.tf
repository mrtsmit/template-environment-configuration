# JENKINS SECTION:

variable "region" {
  description = "AWS region"
}

variable "product_domain_name" {
  description = "Name of product domain, will be used to create other names"
}

variable "environment_type" {
  description = "Type of environment (e.g. test, production)"
}

variable "jenkins_ec2_instance_type" {
  description = "Instance type for Core Infra Jenkins Master"
}

variable "vpc_id" {
  description = "ID of existing VPC (must be pre-created with a portal)"
}

variable "jenkins_subnet_id" {
  description = "ID of existing subnet where Jenkins will be deployed"
}

variable "http_proxy" {
  description = "IP of corporate HTTP proxy"
}

variable "http_proxy_port" {
  description = "(Optional) HTTP proxy port to use for access to internet. This is required to install packages on instances deployed in ops AWS accounts."
}

variable "jenkins_ssh_allowed_cidrs" {
  description = "CIDRs we allow ssh from"
  type        = "list"
}

variable "jenkins_http_allowed_cidrs" {
  description = "CIDRs we allow http from"
  type        = "list"
}

variable "jenkins_config_repo_url" {
  description = "Git repo url with Product Domain configuration (Fork of this repo.)"
}