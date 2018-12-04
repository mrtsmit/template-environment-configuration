variable "region" {
  description = "AWS region"
}

variable "product_domain_name" {
  description = "Name of product domain, will be used to create other names"
}

variable "environment_type" {
  description = "Type of environment (e.g. test, production)"
}

variable "operation_aws_account_number" {
  description = "AWS operation account number (without hyphens)"
}

variable "application_aws_account_number" {
  description = "AWS application account number (without hyphens)"
}

variable "k8s_cluster_name_postfix" {
  description = "Domain name of Kubernetes cluster (currently only k8s.local is supported)"
  default     = "k8s.local"
}

variable "logs_not_resource" {
  description = "List of resources that log police will NotResource, empty least mean that Resource * is set"
  default     = []
  type        = "list"
}