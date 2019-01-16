from jinja2 import Template

#inputs into the templated file 
aws_account = raw_input("Enter your AWS Account Number: ")
aws_opp_account = raw_input("Enter your AWS Operations Account Number: ")
environment_type = raw_input("Enter your Environment Type: ")
role_name = raw_input("Enter your Role Name: ")
region = raw_input("Enter your AWS Region: ")
vpc_id = raw_input("Enter your VPC ID (must be pre-created): ")

#potentiall calculate subnets using a vpc_id

subnets = list(ec2.subnets.filter(Filters=filters))


TEMPLATE_FILE = "tf_vars.template"
with open(TEMPLATE_FILE) as file_:
    template = Template(file_.read())
rendered_file = template.render(aws_account=aws_account,environment_type=environment_type,role_name=role_name,aws_opp_account=aws_opp_account,region=region,vpc_id=vpc_id)
f = open("tf_vars", "w")
f.write(rendered_file)
print(rendered_file)