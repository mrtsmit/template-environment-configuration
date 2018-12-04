module "operations_iam" {
  source = "github.com/kentrikos/terraform-aws-iam-generator//operations"

  region              = "${var.region}"
  product_domain_name = "${var.product_domain_name}"
  environment_type    = "${var.environment_type}"

  operation_aws_account_number   = "${var.operation_aws_account_number}"
  application_aws_account_number = "${var.application_aws_account_number}"

  k8s_cluster_name_postfix = "${var.k8s_cluster_name_postfix}"
  logs_not_resource        = "${var.logs_not_resource}"
}