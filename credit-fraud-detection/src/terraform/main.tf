provider "aws" {
  region = var.region
}

module "s3" {
  source = "./s3.tf"
}

module "lambda" {
  source = "./lambda.tf"
}

module "api" {
  source = "./api_gateway.tf"
}
