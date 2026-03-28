# 🐘 Ansible Role: PostgreSQL (Containerized & Multi-Instance)

This Ansible role deploys isolated and high-performance **PostgreSQL** instances using **Podman** in **rootless mode**. It is designed as a reusable "Lego block" infrastructure component, allowing multiple independent databases to coexist on the same host without configuration conflicts.

## 🛠 Key Features

*   **Total Isolation**: Deploy multiple independent databases by simply adjusting the `postgres_instance` variable.
*   **Rootless Security**: Operates without `sudo` privileges, utilizing **Podman Secrets** to mask sensitive credentials from `inspect` or `ps` commands.
*   **Native Healthcheck**: Leverages `pg_isready` to ensure the database is fully initialized before dependent services (like Airflow) attempt to connect.
*   **Agnostic Design**: Zero hardcoded dependencies. The role does not "know" its clients; it receives all configuration via dynamic variables.
*   **Lifecycle Management**: Includes a dedicated `clean.yml` for standardized resource decommissioning (containers, secrets, and volumes).


## 📋 Prerequisites

*   **Target Host**: Podman installed and configured in rootless mode.
*   **Control Node**: Ansible 2.15+ and `containers.podman` collection (v1.15.0+).
*   **Network**: A pre-existing Podman network (defined via `postgres_network`).


## ⚙️ Role Variables

### Configuration Parameters (`defaults/main.yml`)

| Variable | Default | Description |
| :--- | :--- | :--- |
| `postgres_instance` | `postgres_standalone` | Unique container name and resource prefix. |
| `postgres_image` | `postgres:16-alpine` | Official PostgreSQL Docker image. |
| `postgres_db_name` | `postgres_db` | Initial database name. |
| `postgres_db_user` | `postgres_user` | Database owner username. |
| `postgres_db_pass` | `change_me` | Database password (should be passed via Vault). |
| `postgres_port` | `5432` | Port exposed on the host. |
| `postgres_network` | `infra_net` | Shared or dedicated Podman network. |
| `postgres_volume` | `postgres_data` | Named volume for data persistence. |


## 🚀 Standalone Deployment Example

To integrate this role into a specific project, call the role by mapping your global project variables to the role variables:

```yaml
- name: "Deploy Postgres for Airflow"
  ansible.builtin.include_role:
    name: postgres
  vars:
    postgres_instance: "airflow_postgres"
    postgres_db_name: "airflow_db"
    postgres_db_user: "airflow_admin"
    postgres_db_pass: "{{ vault_postgres_password }}"
    postgres_network: "airflow_net"
```

## 🧹 Cleanup Procedure

The role supports clean decommissioning through a dedicated tasks file:

```yaml
- name: "Emergency Clean"
  ansible.builtin.include_role:
    name: postgres
    tasks_from: clean.yml
  vars:
    postgres_instance: "airflow_postgres"
```

## 🧪 Automated Testing (Molecule)

The role is validated via Molecule across Debian, Ubuntu, Fedora, and Rocky Linux.

```bash
# Run the full test suite
task postgres:test
```

Verifications performed:

- **Security**: Ensures no password leaks in container metadata (`inspect`).
- **Idempotence**: Guarantees that a second execution results in zero changes.
- **Readiness**: Validates connectivity using real SQL queries via `psql`.


## 📄 License
MIT


## 👤 Author Information
addonol
Infrastructure Architect & Automation Specialist
