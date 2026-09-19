variable "aws_region" {
  description = "AWS region where the infrastructure will be deployed."
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name used to identify project resources."
  type        = string
  default     = "terraform-cloud-infrastructure"
}

variable "environment" {
  description = "Environment name."
  type        = string
  default     = "lab"
}

variable "admin_cidr" {
  description = "CIDR block allowed to access the instance over SSH."
  type        = string

  validation {
    condition     = can(cidrhost(var.admin_cidr, 0))
    error_message = "admin_cidr must be a valid IPv4 CIDR block."
  }
}

variable "instance_type" {
  description = "EC2 instance type for the lab instance."
  type        = string
  default     = "t3.micro"
}

variable "ssh_public_key_path" {
  description = "Path to the SSH public key used for EC2 access."
  type        = string
}
