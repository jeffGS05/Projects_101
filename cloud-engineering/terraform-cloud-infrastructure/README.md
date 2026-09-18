# Terraform Multi-Cloud Infrastructure

A hands-on Infrastructure as Code project that provisions a small, secure, and reproducible cloud environment across AWS, Microsoft Azure, and Google Cloud Platform using Terraform.

The project implements the same high-level infrastructure requirements on each cloud provider while documenting provider-specific architecture, configuration, and operational differences.

---

## Objectives

The primary objectives of this project are to:

* Learn and demonstrate Terraform Infrastructure as Code.
* Provision infrastructure reproducibly.
* Implement equivalent infrastructure on AWS, Azure, and GCP.
* Understand differences between cloud provider architectures.
* Apply basic cloud security principles.
* Validate infrastructure before deployment.
* Document infrastructure and operational procedures.
* Practice creating and destroying infrastructure safely.
* Build a reusable foundation for future cloud projects.

---

## Cloud Providers

This project covers:

| Provider        | Terraform Provider | Scope             |
| --------------- | ------------------ | ----------------- |
| AWS             | AWS Provider       | Network + Compute |
| Microsoft Azure | AzureRM Provider   | Network + Compute |
| Google Cloud    | Google Provider    | Network + Compute |

The implementations are intentionally separated so that each cloud environment can be deployed and tested independently.

---

## Architecture

Each cloud implementation follows the same general objective:

```text
                    Internet
                       │
                       ▼
                ┌──────────────┐
                │ Cloud Network│
                └──────┬───────┘
                       │
              ┌────────┴────────┐
              │                 │
              ▼                 ▼
       Public Network     Private Network
              │                 │
              ▼                 ▼
         Linux VM/EC2      Future Workloads
```

The exact implementation differs according to the networking and compute models provided by each cloud platform.

---

## Project Structure

```text
terraform-cloud-infrastructure/
│
├── README.md
│
├── architecture/
│   ├── aws.md
│   ├── azure.md
│   └── gcp.md
│
├── aws/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── versions.tf
│
├── azure/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── versions.tf
│
├── gcp/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── versions.tf
│
├── scripts/
│
└── tests/
```

---

## Engineering Workflow

Each implementation follows this lifecycle:

```text
Terraform Configuration
        │
        ▼
terraform fmt
        │
        ▼
terraform validate
        │
        ▼
terraform plan
        │
        ▼
Review
        │
        ▼
terraform apply
        │
        ▼
Test Infrastructure
        │
        ▼
terraform destroy
```

Infrastructure should not be deployed without reviewing the Terraform plan first.

---

## Security Principles

The project will follow basic security practices including:

* Least-privilege access where applicable.
* No hard-coded cloud credentials.
* No credentials committed to Git.
* Sensitive values managed outside source control.
* Restricted network access.
* Minimal exposed services.
* Small cloud resources suitable for laboratory use.
* Infrastructure destroyed when no longer required.

---

## Prerequisites

The development environment will require:

* Git
* Terraform
* AWS CLI
* Azure CLI
* Google Cloud CLI
* An AWS account
* An Azure account
* A Google Cloud account

Authentication will be performed using the recommended CLI/provider authentication mechanisms rather than storing credentials in the repository.

---

## Implementation Phases

### Phase 1 — Terraform Fundamentals

* Install and configure Terraform.
* Understand providers.
* Understand resources.
* Understand variables.
* Understand outputs.
* Understand Terraform state.
* Validate Terraform configuration.

### Phase 2 — AWS

Build the initial infrastructure using AWS.

Planned components:

* VPC
* Subnet
* Internet connectivity
* Security controls
* Linux compute instance
* Terraform outputs

### Phase 3 — Azure

Implement the equivalent architecture using Azure resources.

Planned components:

* Resource Group
* Virtual Network
* Subnet
* Network security controls
* Linux virtual machine
* Terraform outputs

### Phase 4 — GCP

Implement the equivalent architecture using Google Cloud resources.

Planned components:

* VPC network
* Subnet
* Firewall rules
* Linux compute instance
* Terraform outputs

### Phase 5 — Validation

For each cloud provider:

* Format Terraform configuration.
* Validate configuration.
* Generate and review Terraform plan.
* Deploy infrastructure.
* Test connectivity and resources.
* Capture results.
* Destroy infrastructure.

### Phase 6 — Documentation

Document:

* Architecture
* Deployment procedure
* Authentication
* Configuration
* Testing
* Troubleshooting
* Security considerations
* Cloud provider differences
* Lessons learned

---

## Cost Management

This project is designed as a learning laboratory.

Cloud resources should be kept small and should not remain deployed unnecessarily.

The normal lifecycle is:

```text
Create
  ↓
Test
  ↓
Document
  ↓
Destroy
```

Before applying infrastructure, the Terraform plan should be reviewed to identify unexpected resources or configuration changes.

---

## Future Improvements

Potential future enhancements include:

* Terraform modules
* Remote state
* State locking
* CI/CD integration
* Automated security scanning
* Policy as Code
* Cloud monitoring
* Cost estimation
* Automated testing
* Multi-environment support
* Infrastructure deployment through GitHub Actions

---

## Learning Outcomes

By completing this project, I aim to demonstrate practical understanding of:

* Infrastructure as Code
* Terraform
* Cloud networking
* Cloud compute
* Cloud security
* Infrastructure lifecycle management
* Multi-cloud architecture
* Infrastructure validation
* Automation
* Technical documentation
* Git-based engineering workflows

