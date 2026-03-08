# 🐘 Ansible Role: PostgreSQL (Containerized & Rootless)

This Ansible role deploys and manages a standalone **PostgreSQL** instance using **Podman** in **rootless mode**. Designed as a modular infrastructure component, it ensures security, data persistence, and multi-OS compliance.

## 🌟 Key Features
*   **Rootless Isolation**: Deploys without `sudo` privileges, enhancing host security.
*   **Security First**: Password injection via **Podman Secrets** (prevents leaks in `process list` or `inspect`).
*   **Full Idempotency**: Manages the entire lifecycle (networks, volumes, secrets, and containers).
*   **Multi-Platform Validation**: Tested via **Molecule** across Debian, Ubuntu, Fedora, and Rocky Linux.

## 🛠 Prerequisites
*   **Target Host**: Podman installed and configured (rootless mode enabled).
*   **Control Node**: Python 3.12+ (managed via `uv` recommended).
*   **Collections**: `containers.podman` (v1.15.0+).

## 📦 Role Variables

Variables are designed to be easily overridden via your inventory or playbooks.

### Configuration Parameters (`defaults/main.yml`)

| Variable | Default | Description |
| :--- | :--- | :--- |
| `postgres_image` | `docker.io/library/postgres:16-alpine` | Official Docker image to use. |
| `postgres_container_name` | `postgres_db` | Name of the Podman instance. |
| `postgres_db_name` | `postgres_db` | Initial database name. |
| `postgres_db_user` | `postgres_user` | Primary database owner. |
| `postgres_network` | `postgres_net` | Dedicated Podman network. |
| `postgres_port_number` | `5432` | Port exposed on the host (127.0.0.1). |
| `postgres_volume_name` | `postgres_data` | Persistent volume for data storage
| `postgres_secret_db_password_name` | `postgres_db_password` | Name of the podman secret

### Sensitive Variables (Encrypted)

| Variable | Source | Description |
| :--- | :--- | :--- |
| `vault_postgres_password` | `vault.yml` | Master password (Ansible Vault). |


## 🚀 Example Playbook

Standard deployment for a generic application:

```yaml
- name: Deploy Database Tier
  hosts: db_servers
  roles:
    - role: postgres
      # Optional
      vars:
        postgres_db_name: "inventory_prod"
        postgres_db_user: "manager"
        ...
```

## 🧪 Automated Testing (Molecule)

The role uses Molecule to validate infrastructure across a heterogeneous environment.

```bash
# Run unit tests on all supported platforms
task postgres:test
```

The test suite verifies:

- **Integrity**: Secure creation of secrets and volumes on the host.
- **Portability**: Successful deployment on Debian, Ubuntu, Fedora, and Rocky Linux.
- **Service**: Execution of real SQL queries to validate availability


## 📄 License
MIT


## 👤 Author Information
addonol
Infrastructure Architect & Automation Specialist
