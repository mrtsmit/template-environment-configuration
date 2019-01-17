from jinja2 import Template #this may require a pip install jinja2
from distutils.dir_util import copy_tree

#replaces values into the templated file, to add a value add curly braces: ex - {{value}}
aws_account = input("Enter your AWS Account Number (without hypens): ")
aws_opp_account = input("Enter your AWS Operations Account Number (without hypens): ")
environment_type = input("Enter your Environment Type (e.g. test, production): ")
role_name = input("Enter your Role Name (ex - arn:aws:iam::<account inherited from above>:role/<<role_name>>): ")
region = input("Enter your AWS Region: ")
product_domain_name = input("Enter the Product Domain Name: ")
jenkins_config_url = input ("Enter the Jenkins Config URL: ")
http_proxy = input("Enter the HTTP Proxy: ")
vpc_id = input("Enter your VPC ID (must be pre-created): ")

## potentially calculate subnets using a vpc_id
## would require an import of the boto library or CLI
# 
# boto 
# client = boto3.resource("ec2")
# for vpc in client.vpcs.filter(id=vpc_id):
#     for subnet in vpc.subnets.filters(Tag:Name=*public*):
#         print(vpc, "all:", subnet)
# CLI
# filter by tag-key where it's public (needs to be in subnet name)
# aws ec2 describe-subnets --filters Name=vpc-id,Values=<vpc_id> Name=tag:Name,Values=*public* 
# loop through output to get the subnet ID's 


subnet1_id = input("Enter your Subnet AZ1 (must be pre-created): ")
subnet2_id = input("Enter your Subnet AZ2 (must be pre-created): ")
subnet3_id = input("Enter your Subnet AZ3 (must be pre-created): ")
jenkins_subnet_id = input("Enter your Jenkins Subnet ID (must be pre-created): ")

#parameters yaml for jenkins
gitUsername = input("Enter your git username: ")
gitApiToken = input("Enter your git API Token: ")
gitProviderUrl = input("Enter your git Provider URL: ")
gitBitbucketServer = input("Enter your git Bitbucket Server: ")
jxDomainHostedZoneID = input("JX Domain Hosted Zone: ")
jxDomainAliasPrefix = input("JX Domain Alias Prefix: ")

# copy new folder structure
fromDirectory = "operations/region"
toDirectory = "operations/" + region + "/"
copy_tree(fromDirectory, toDirectory)

fromDirectory = "application/region"
toDirectory = "application/" + region + "/"
copy_tree(fromDirectory, toDirectory)

TEMPLATE_FILE = "operations/region/terraform.tfvars.template"
with open(TEMPLATE_FILE) as file_:
    template = Template(file_.read())
#add value from top section here if newly added    
rendered_file = template.render(aws_account=aws_account,environment_type=environment_type,role_name=role_name,aws_opp_account=aws_opp_account,region=region,vpc_id=vpc_id,subnet1_id=subnet1_id,subnet2_id=subnet2_id,subnet3_id=subnet3_id,jenkins_subnet_id=jenkins_subnet_id,product_domain_name=product_domain_name,jxDomainHostedZoneID=jxDomainHostedZoneID,jxDomainAliasPrefix=jxDomainAliasPrefix,http_proxy=http_proxy,jenkins_config_url=jenkins_config_url)
f = open("operations/" + region + "/terraform.tfvars" , "w")
f.write(rendered_file)
print(rendered_file)


TEMPLATE_FILE = "application/" + region + "/terraform.tfvars.template"
with open(TEMPLATE_FILE) as file_:
    template = Template(file_.read())
#add value from top section here if newly added    
rendered_file = template.render(aws_account=aws_account,environment_type=environment_type,role_name=role_name,aws_opp_account=aws_opp_account,region=region,vpc_id=vpc_id,subnet1_id=subnet1_id,subnet2_id=subnet2_id,subnet3_id=subnet3_id,product_domain_name=product_domain_name,http_proxy=http_proxy)
f = open("application/" + region + "/terraform.tfvars" , "w")
f.write(rendered_file)
print(rendered_file)

TEMPLATE_FILE = "operations/region/env/jenkins/parameters.yaml.template"
with open(TEMPLATE_FILE) as file_:
    template = Template(file_.read())
#add value from top section here if newly added    
rendered_file = template.render(gitUsername=gitUsername,gitApiToken=gitApiToken,gitProviderUrl=gitProviderUrl,gitBitbucketServer=gitBitbucketServer,jxDomainHostedZoneID=jxDomainHostedZoneID,jxDomainAliasPrefix=jxDomainAliasPrefix)
f = open("operations/" + region + "/env/jenkins/parameters.yaml" , "w")
f.write(rendered_file)
print(rendered_file)