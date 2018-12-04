module "jenkins" {
  source = "github.com/kentrikos/terraform-aws-bootstrap-jenkins"

  product_domain_name = "${var.product_domain_name}"
  environment_type    = "${var.environment_type}"
  ec2_instance_type   = "${var.jenkins_ec2_instance_type}"

  vpc_id                  = "${var.vpc_id}"
  subnet_id               = "${var.jenkins_subnet_id}"
  http_proxy              = "${var.http_proxy}"
  jenkins_proxy_http_port = "${var.http_proxy_port}"

  ssh_allowed_cidrs  = "${var.jenkins_ssh_allowed_cidrs}"
  http_allowed_cidrs = "${var.jenkins_http_allowed_cidrs}"

  jenkins_config_repo_url = "${var.jenkins_config_repo_url}"
}