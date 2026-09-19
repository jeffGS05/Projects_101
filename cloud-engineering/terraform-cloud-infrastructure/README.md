# Terraform Cloud Infrastructure

Infrastructure-as-Code project demonstrating the design, deployment, validation, security hardening, and lifecycle management of AWS infrastructure using Terraform.

This project is part of the **Projects_101 Cloud Engineering portfolio**.

---

## Project Status

**Status:** AWS implementation completed

**Azure/GCP:** Planned

**Cloud Provider:** AWS

**Infrastructure as Code:** Terraform

**Region:** `us-east-1`

**Environment:** Lab

**Deployment Model:** Single-region AWS VPC with a public EC2 workload

The AWS infrastructure was successfully deployed, validated, security-hardened, and destroyed after testing to avoid unnecessary cloud costs.

---

## Objectives

The project was designed to demonstrate practical Infrastructure-as-Code skills, including:

* Terraform project organization
* AWS networking fundamentals
* VPC and subnet design
* Internet Gateway and routing
* EC2 provisioning
* Security Group configuration
* SSH access management
* Terraform variables and outputs
* Terraform provider management
* Infrastructure validation
* Security hardening
* Terraform state management
* Infrastructure lifecycle management
* Cloud cost awareness

---

## Architecture

The deployed architecture consisted of a single AWS VPC containing a public subnet and an EC2 instance.

```text
                         Internet
                            |
                            |
                   Internet Gateway
                            |
                            |
                    Public Route Table
                            |
                            |
                    Public Subnet
                   10.10.1.0/24
                            |
                            |
                       EC2 Instance
                        t3.micro
                            |
                    Amazon Linux 2023
```

### Network Design

| Component         | Configuration   |
| ----------------- | --------------- |
| VPC               | `10.10.0.0/16`  |
| Public Subnet     | `10.10.1.0/24`  |
| Availability Zone | `us-east-1a`    |
| Internet Gateway  | Enabled         |
| Public IP         | Enabled for EC2 |
| DNS Support       | Enabled         |
| DNS Hostnames     | Enabled         |

---

## AWS Resources

Terraform managed the following AWS resources:

| Resource                | Purpose                                            |
| ----------------------- | -------------------------------------------------- |
| VPC                     | Provides the isolated AWS network                  |
| Public Subnet           | Hosts the EC2 lab instance                         |
| Internet Gateway        | Provides Internet connectivity                     |
| Route Table             | Routes public traffic through the Internet Gateway |
| Route Table Association | Associates the subnet with the public route table  |
| Security Group          | Controls inbound and outbound traffic              |
| EC2 Key Pair            | Provides SSH authentication                        |
| EC2 Instance            | Provides the Linux compute workload                |

The Terraform configuration also uses an Amazon Linux 2023 AMI data source so that the deployment can dynamically select the latest matching Amazon Linux x86_64 image.

---

## Repository Structure

```text
terraform-cloud-infrastructure/
├── README.md
├── architecture/
│   ├── aws.md
│   ├── azure.md
│   └── gcp.md
├── aws/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── versions.tf
│   └── .terraform.lock.hcl
├── azure/
├── gcp/
├── scripts/
└── tests/
```

The AWS implementation is currently the completed cloud deployment in this project. Azure and GCP directories are reserved for future implementations.

---

## Terraform Configuration

The AWS implementation is separated into Terraform files based on responsibility.

### `main.tf`

Defines the AWS infrastructure resources, including:

* Amazon Linux AMI data source
* VPC
* Public subnet
* Internet Gateway
* Route table
* Route table association
* Security Group
* EC2 key pair
* EC2 instance

### `variables.tf`

Defines configurable parameters such as:

* AWS region
* Project name
* Environment
* Administrator CIDR
* EC2 instance type
* SSH public key path

Sensitive or environment-specific values are supplied locally through `terraform.tfvars`, which is intentionally excluded from Git.

### `outputs.tf`

Provides useful deployment information such as:

* EC2 instance ID
* Public IP address
* Public DNS name
* VPC ID
* Public subnet ID
* Security Group ID

### `versions.tf`

Defines the Terraform and AWS provider requirements.

The AWS provider is constrained to the `6.x` provider series, and `.terraform.lock.hcl` is committed to the repository to maintain provider dependency integrity.

---

## Security Controls

Security was considered during the infrastructure design rather than added only after deployment.

### SSH Access Restriction

SSH access was restricted to the administrator's public IP using a `/32` CIDR.

```text
TCP/22 → administrator public IP only
```

This avoids exposing SSH to the entire Internet.

### HTTP and HTTPS

The Security Group allows:

```text
TCP/80  → 0.0.0.0/0
TCP/443 → 0.0.0.0/0
```

These rules were included to support future web workload testing.

### IMDSv2

EC2 Instance Metadata Service Version 2 was enforced:

```text
http_tokens                 = "required"
http_put_response_hop_limit = 1
```

This prevents the instance from using IMDSv1 and reduces the metadata service hop limit.

### EBS Encryption

The EC2 root volume was configured with encryption enabled:

```text
encrypted = true
```

### Credentials

No AWS credentials are stored in the repository.

The project uses the local AWS CLI credential configuration for Terraform authentication.

The following types of files are intentionally excluded from source control:

```text
*.tfvars
*.tfstate
*.tfstate.*
.terraform/
tfplan
```

---

## Deployment Workflow

The infrastructure lifecycle followed this workflow:

```text
Terraform Configuration
        |
        v
terraform fmt
        |
        v
terraform validate
        |
        v
terraform plan
        |
        v
Review Changes
        |
        v
terraform apply
        |
        v
Infrastructure Validation
        |
        v
Security Hardening
        |
        v
terraform plan -destroy
        |
        v
terraform destroy
```

---

## Validation

Terraform configuration was validated before deployment.

The infrastructure was successfully created with:

```text
Apply complete! Resources: 8 added, 0 changed, 0 destroyed.
```

The EC2 instance was accessed through SSH using the dedicated AWS lab key.

The deployed infrastructure was subsequently hardened to require IMDSv2 and use an encrypted root volume.

Because those hardening changes required replacement of the EC2 instance, Terraform correctly planned:

```text
Plan: 1 to add, 0 to change, 1 to destroy.
```

The replacement completed successfully.

The final infrastructure was then reviewed with:

```bash
terraform state list
```

The Terraform state contained the expected AWS resources.

---

## Infrastructure Cleanup

After testing, the infrastructure was intentionally destroyed to prevent unnecessary AWS charges.

Before destruction, the project used:

```bash
terraform plan -destroy
```

Terraform reported:

```text
Plan: 0 to add, 0 to change, 8 to destroy.
```

The destroy operation completed successfully:

```text
Destroy complete! Resources: 8 destroyed.
```

This demonstrates the complete infrastructure lifecycle:

```text
Create → Validate → Harden → Test → Destroy
```

---

## Cost Management

This is a learning environment rather than a continuously running production environment.

The project follows a **deploy-test-destroy** model.

The infrastructure was destroyed after validation to avoid leaving billable AWS resources running unnecessarily.

The EC2 instance used a small `t3.micro` instance type appropriate for a lightweight lab workload.

---

## Engineering Practices Demonstrated

This project demonstrates practical experience with:

* Infrastructure as Code
* Terraform resource management
* Terraform state
* AWS networking
* EC2 administration
* Linux server access
* SSH key management
* Security Group design
* IMDSv2
* EBS encryption
* Cloud cost management
* Infrastructure validation
* Git-based infrastructure development
* Pull Request workflow
* Reproducible provider dependencies

---

## Lessons Learned

### Infrastructure should be treated as code

Terraform makes infrastructure changes reviewable and repeatable instead of relying exclusively on manual AWS Console operations.

### Security requirements can affect resource lifecycle

Enabling encrypted EBS storage and changing EC2 metadata configuration demonstrated that some infrastructure changes can require resource replacement.

Terraform makes these changes visible during planning before they are applied.

### State is critical

Terraform state provides the mapping between configuration and deployed infrastructure. Protecting state from accidental publication is therefore essential.

### Destroying infrastructure is part of the lifecycle

A cloud lab is not complete simply because resources were successfully deployed. Cleanup is also an important operational practice.

### Small labs can demonstrate production-oriented practices

Even though this is a small environment, the project applies practices that scale to larger environments:

* Version-controlled infrastructure
* Code review
* Security controls
* Change planning
* Validation
* Explicit lifecycle management
* Cost awareness

---

## Future Improvements

Potential future iterations include:

* Private subnet implementation
* NAT Gateway evaluation
* IAM role for EC2
* AWS Systems Manager Session Manager
* Removal of direct SSH access
* Application deployment with user data
* Automated testing
* Terraform modules
* Remote Terraform state
* CI/CD validation with GitHub Actions
* AWS monitoring and logging
* Multi-AZ architecture
* Azure implementation
* GCP implementation

These improvements will be added incrementally as separate portfolio projects or iterations.

---

## Related Portfolio

This project is part of the broader:

**Projects_101**

```text
Cloud Engineering
├── Terraform Cloud Infrastructure
├── Future AWS Projects
├── Future Azure Projects
└── Future GCP Projects

Data Engineering
SRE / DevOps
Cybersecurity
```

The repository is designed to demonstrate practical engineering progression through documented hands-on projects rather than isolated tutorials.

---

## License

This project is intended for educational and portfolio purposes.

