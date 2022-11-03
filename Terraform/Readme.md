## Build AWS Infrastructure with Terraform
- Hard-coding credentials into any Terraform configuration is not recommended, and risks secret leakage should this file ever be committed to a public version control system. Using AWS credentials in EC2 instance is not recommended.

### Prerequisites

- An AWS account.

- The AWS CLI installed. 

- Your AWS credentials configured locally. 



#####   Commands

- terraform init
- terraform plan
- terraform apply 

- To terminate Ec2, you can use  
    - terraform destroy 



##### Usable Links
- https://registry.terraform.io/providers/hashicorp/aws/latest
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance

