terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.37.0"
    }
  }
}

provider "aws" {
  # Configuration options
region = "us-east-1"

}


resource "aws_instance" "terraform" {
  ami = "ami-09d3b3274b6c5d4aa"
  instance_type = "t2.micro"
  key_name ="mykey"
  tags = {
    "Name" = "EC2-terraform"
  }
}