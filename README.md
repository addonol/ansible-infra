# 🏗️ Ansible Infrastructure (Podman Rootless)


A collection of **high-quality, standalone Ansible roles** designed for modern, secure infrastructure. This project focuses on **Rootless Podman** orchestration, ensuring zero-privilege deployments and production-grade security.

> **Why this repository?**
> Most Ansible roles assume root access. This one is built for security-first environments where **Rootless containers** and **Podman Secrets** are the standard.


## 🌟 Key Features

*   🛡️ **Security First**: 100% Rootless deployments. No `sudo` required.
*   🔐 **Secret Management**: Native integration with **Podman Secrets** (No more passwords in environment variables).
*   🧪 **Bulletproof Testing**: Every role is unit-tested with **Molecule** across Debian, Ubuntu, Fedora, and Rocky Linux.
*   🚀 **Modern Tooling**:
    *   **uv**: Blazing fast Python dependency management.
    *   **Taskfile**: Simple, grouped automation commands.
    *   **Ansible-Lint & Gitleaks**: Industrial-grade quality and security checks.



## 📦 Available Roles


| Role | Status | OS Support | Description |
| :--- | :--- | :--- | :--- |
| [**PostgreSQL**](./roles/postgres) | ✅ Ready | Debian, Ubuntu, Fedora, Rocky | Standalone DB with persistent storage. |
| [**RabbitMQ**](./roles/rabbitmq) | 🚧 WIP | Multi-OS | Message broker with management UI. |
| **Airflow Stack** | 📅 Roadmap | - | Complete Celery-based Airflow cluster. |



## 🛠️ Getting Started

### 1. Prerequisites
Ensure you have the following installed on your control node:
*   [**uv**](https://docs.astral.sh/uv/) (Python manager)
*   [**go-task**](https://taskfile.dev) (Task runner)
*   [**Podman**](https://podman.io) (Rootless mode configured)

### 2. Installation
```bash
# Clone the repo
git clone https://github.com/addonol/ansible-infra.git
cd ansible-infra

# Install dependencies (Python & Collections)
uv sync
```

### 3. Usage
```bash
# List all available commands
task --list

# Deploy a standalone Postgres instance
task postgres:deploy
```

## 🧪 Development & Quality

We take quality seriously. Before any push, we run a full suite of tests.

## Run Molecule Tests
```bash
# Test a specific role (e.g., Postgres) on 4 different OS
task postgres:test
```

## Security & Linting

```bash
# Run all pre-commit hooks (Gitleaks, Ansible-Lint, Ruff)
task test:lint
```

## 🤝 Contributing

Contributions are welcome! Whether it's a bug report, a new feature, or documentation improvement.


## 👤 Author
addonol
Infrastructure Architect & Automation Specialist
