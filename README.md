# Ansible Infrastructure (Podman Rootless)

A collection of professional, standalone Ansible roles for secure infrastructure orchestration. This repository focuses on **Rootless Podman** deployments, ensuring zero-privilege security and production-grade reliability.

> **Architecture Note**: Unlike traditional roles that assume root access, this stack is built from the ground up for **Non-Root containers** and **Podman Secrets** integration.

## Core Principles

*   **Security First**: 100% Rootless deployments. No `sudo` required on target hosts.
*   **Secret Management**: Native integration with **Podman Secrets** to prevent credential leaks in environment variables or metadata.
*   **Enterprise Testing**: Every role is validated via **Molecule** across Debian, Ubuntu, Fedora, and Rocky Linux.
*   **Modern Toolchain**: Powered by `uv` for Python dependency management and `Taskfile` for streamlined automation.

## Available Infrastructure Roles

| Role | Status | Targets | Description |
| :--- | :--- | :--- | :--- |
| [**PostgreSQL**](./roles/postgres) | Stable | Debian, Ubuntu, Fedora, Rocky | Standalone DB with persistent storage and health monitoring. |
| [**RabbitMQ**](./roles/rabbitmq) | Stable | Debian, Ubuntu, Fedora, Rocky | Message broker with Management UI and EPMD stability fixes. |
| [**Airflow Common**](./roles/airflow_common) | Stable | Debian, Ubuntu, Fedora, Rocky | Core Airflow 3 initialization, DB migrations, and admin provisioning. |
| [**Airflow Services**](./roles/airflow_services) | Stable | Debian, Ubuntu, Fedora, Rocky | Scalable execution of Webserver, Scheduler, and Celery Workers. |

## Quick Start

### 1. Prerequisites

Ensure the following tools are installed on your control node:
*   [**uv**](https://docs.astral.sh/uv/) (Python package manager)
*   [**go-task**](https://taskfile.dev) (Task runner)
*   [**Podman**](https://podman.io) (Configured in Rootless mode)

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/addonol/ansible-infra.git
cd ansible-infra

# Synchronize virtual environment and install collections
uv sync
ansible-galaxy collection install -r requirements.yml
```

### 3. Basic Usage

```bash
# List all available infrastructure commands
task --list

# Deploy a standalone Postgres instance
task postgres:deploy
```

## Quality Assurance & CI/CD

We enforce strict quality standards through automated testing and linting.

### Molecule Testing

```bash
task postgres:test
```

### Security & Linting

Run the security suite (Gitleaks, Ansible-Lint, Ruff) before pushing:

```bash
task test:lint
```

## License
MIT

## Author
addonol
Infrastructure Architect & Automation Specialist
