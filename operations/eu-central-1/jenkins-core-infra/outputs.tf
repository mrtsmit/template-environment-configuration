output "jenkins_private_ip" {
  value = "${module.jenkins.jenkins_private_ip}"
}

output "jenkins_username" {
  value = "${module.jenkins.jenkins_username}"
}

output "jenkins_ssh_connection" {
  value = "${module.jenkins.ssh_connection}"
}

output "jenkins_ssh_private_key" {
  value     = "${module.jenkins.ssh_private_key}"
  sensitive = true
}
