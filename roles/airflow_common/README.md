# 🚀 Ansible Role: Airflow Common (Core Configuration & Initialization)

This Ansible role manages the core configuration and database initialization for an **Airflow 3** stack using **Podman** in **rootless mode**. It acts as the infrastructure orchestrator, handling database migrations and secure administrative user provisioning before any services are launched.

## 🛠 Key Features

*   **Airflow 3 Native**: Implements the latest `db migrate` logic and the new CLI syntax for user management.
*   **Security-First Initialization**: Admin user creation utilizes **Podman Secrets** to prevent sensitive credentials from appearing in process lists (`ps aux`) or container metadata.
*   **Dynamic DNS Mapping**: Uses `etc_hosts` to resolve standalone database and broker instances within the Podman network, ensuring a "Name or service not known" free deployment.
*   **Stateless Execution**: Uses one-shot containers for initialization that are automatically removed after success, keeping the environment clean.
*   **Decoupled Architecture**: Separates the application configuration (secrets) from the execution layer (Webserver, Scheduler, Workers).


## 📋 Prerequisites

*   **Infrastructure**: A running PostgreSQL instance (compatible with the `postgres` role).
*   **Infrastructure**: A running RabbitMQ broker (compatible with the `rabbitmq` role).
*   **Target Host**: Podman installed and configured in rootless mode.
*   **Collection**: `containers.podman` (v1.15.0+).

## ⚙️ Role Variables

### Configuration Parameters (`defaults/main.yml`)

| Variable | Default | Description |
| :--- | :--- | :--- |
| `airflow_common_image` | `apache/airflow:3.1.7-python3.12` | Official Airflow 3 image. |
| `airflow_common_network` | `infra_net` | Shared network for DB and Broker connectivity. |
| `airflow_common_admin_user` | `admin` | Primary administrative username. |
| `airflow_common_admin_email` | `admin@example.com` | Primary administrative email. |
| `airflow_common_postgres_instance` | `airflow_postgres` | Target PostgreSQL container name for DNS resolution. |
| `airflow_common_rabbitmq_instance` | `airflow_rabbitmq` | Target RabbitMQ container name for DNS resolution. |
| `airflow_common_config` | `airflow_config` | Name of the Podman secret storing `airflow.cfg`. |


### Sensitive Variables (Passed via Vault)


| Variable | Source | Description |
| :--- | :--- | :--- |
| `airflow_common_admin_pass` | `vault.yml` | Password for the initial admin user. |
| `airflow_common_fernet_key` | `vault.yml` | Encryption key for connection metadata. |
| `airflow_common_webserver_secret_key` | `vault.yml` | Secret key for Flask/FastAPI session and JWT signing. |


## 🚀 Airflow 3 Hybrid Architecture

This repository supports both the legacy **Flask** (FAB) and the modern **FastAPI** architectures. You can toggle between them using the `airflow_use_fastapi` variable.

### Authentication Modes


| Mode | Variable | Auth Manager | Backend |
| :--- | :--- | :--- | :--- |
| **Legacy (Flask)** | `airflow_use_fastapi: false` | `FabAuthManager` | Flask-AppBuilder (DB-based) |
| **Modern (FastAPI)** | `airflow_use_fastapi: true` | `SimpleAuthManager` | FastAPI Native (JSON-based) |

### Configuration Details

- **FastAPI Mode**: In this mode, users are defined via a secure JSON secret. The legacy `airflow users create` command is skipped as authentication is handled statelessly by the API Server.
- **Security**: Passwords and JWT secrets are managed via **Podman Secrets** to prevent exposure in `podman inspect` logs.
- **JWT Secret**: Ensure your `airflow_common_jwt_secret` is at least 64 characters long to avoid signature verification errors between the API Server and Workers.


## 🚀 Deployment Workflow

This role must be executed **after** the database/broker deployment but **before** any Airflow services. It performs two critical one-shot tasks:

1.  **DB Migration**: Upgrades the database schema to the latest Airflow 3 version.
2.  **Admin Provisioning**: Creates the first "Admin" user securely.


```yaml
- name: "Initialize Airflow Core"
  ansible.builtin.include_role:
    name: airflow_common
  vars:
    airflow_common_admin_user: "dev_admin"
    airflow_common_admin_pass: "{{ vault_airflow_pass }}"
```

## 🧹 Cleanup Procedure

The role supports standardized resource decommissioning:

```yaml
- name: "Remove Airflow Core Resources"
  ansible.builtin.include_role:
    name: airflow_common
    tasks_from: clean.yml
```

## 🧪 Automated Testing (Molecule)

The role is validated via Molecule across Debian, Ubuntu, Fedora, and Rocky Linux.

```bash
# Run the core initialization test suite
task airflow_common:test
```

Verifications performed:

- **Connectivity**: Validates the migration container can resolve and reach `airflow_postgres`.
- **Idempotence**: Ensures re-running initialization does not create duplicate users or errors.
- **Integrity**: Confirms the admin user is successfully injected into the db_user table.


## 📄 License
MIT


## 👤 Author Information
addonol
Infrastructure Architect & Automation Specialist
