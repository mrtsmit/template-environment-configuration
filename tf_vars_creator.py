from jinja2 import Template #this may require a pip install jinja2

#replaces values into the templated file, to add a value add curly braces: ex - {{value}}
aws_account = raw_input("Enter your AWS Account Number (without hypens): ")
aws_opp_account = raw_input("Enter your AWS Operations Account Number (without hypens): ")
environment_type = raw_input("Enter your Environment Type (e.g. test, production): ")
role_name = raw_input("Enter your Role Name (ex - arn:aws:iam::<account inherited from above>:role/<<role_name>>): ")
region = raw_input("Enter your AWS Region: ")
vpc_id = raw_input("Enter your VPC ID (must be pre-created): ")

## potentially calculate subnets using a vpc_id
## would require an import of the boto library or CLI
# 
# boto 
# subnets = list(ec2.subnets.filter(Filters=filters))
#
# CLI
# filter by tag-key where it's public (needs to be in subnet name)
# aws ec2 describe-subnets --filters Name=vpc-id,Values=<vpc_id> Name=tag:Name,Values=*public* 
# loop through output to get the subnet ID's 


subnet1_id = raw_input("Enter your Subnet ID 1 (must be pre-created): ")
subnet2_id = raw_input("Enter your Subnet ID 2 (must be pre-created): ")
subnet3_id = raw_input("Enter your Subnet ID 3 (must be pre-created): ")


TEMPLATE_FILE = "tf_vars.template"
with open(TEMPLATE_FILE) as file_:
    template = Template(file_.read())
#add value from top section here if newly added    
rendered_file = template.render(aws_account=aws_account,environment_type=environment_type,role_name=role_name,aws_opp_account=aws_opp_account,region=region,vpc_id=vpc_id,subnet1_id=subnet1_id,subnet2_id=subnet2_id,subnet3_id=subnet3_id)
f = open("tf_vars", "w")
f.write(rendered_file)
print(rendered_file)