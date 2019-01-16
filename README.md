# A Product Domain Generic repo for Kentrikos project

This repo contain default structure for project [Kentrikos](https://github.com/kentrikos)

## Usage

This repo should be forked as private and not used directly as described in [aws-bootstrap](https://github.com/kentrikos/aws-bootstrap)

## Configuration

As default this repo take eu-central-1 region as example.

Files that need to be updated :

* application/$REGION/terraform.tfvars
* operations/$REGION/terraform.tfvars
* operations/$REGION/env/jenkins/parameters.yaml (configs for jx installation)

To setup on another region change directories name or copy as new region name and update config files accordingly

Experimental: 

Pre-Req: 
1. Install jinja2 on the machine python is being run on (pip install jinja2)

TF Vars creator, by specifying the required variables it will auto fill values for those files. It can be run by using:

python tf_vars_creator.py 

then by following the prompts, it will autogenerate your files (PLEASE VALIDATE VARIABLES AFTER AND BEFORE EXECUTING)