# 🐘 Ansible Role: PostgreSQL (Podman Rootless)

This Ansible role deploys and manages a **PostgreSQL** container instance using **Podman** in rootless mode. It is specifically optimized to serve as the metadata database for **Apache Airflow**, ensuring security and idempotency.

## 🌟 Key Features
*   **100% Rootless**: Runs without `sudo` privileges using Podman user namespaces.
*   **Security First**: Uses **Podman Secrets** for sensitive data (passwords) instead of environment variables.
*   **Full Lifecycle**: Manages networks, secrets, volumes, and container states.
*   **Molecule Tested**: Includes a robust test suite for automated validation.

## 🛠 Requirements
*   **Podman** (Rootless mode must be configured on the host).
*   **Ansible Collection**: `containers.podman` (v1.15.0+).
*   **Python 3.12+** on the control node (managed via `uv`).

## 📦 Role Variables

Variables are organized to allow easy overriding via `group_vars` or playbook parameters.

### Default Variables (`defaults/main.yml`)


| Variable | Default Value | Description |
| :--- | :--- | :--- |
| `postgres_container_name` | `postgres_db` | Name of the Podman container. |
| `postgres_db_name` | `custom_app_db` | Name of the database to create. |
| `postgres_db_user` | `dev_user` | Primary database user. |
| `postgres_network` | `postgres_net` | Podman network to attach to. |
| `postgres_image` | `postgres:16-alpine` | Docker image to pull and run. |

### Sensitive Variables (Ansible Vault)


| Variable | Source | Description |
| :--- | :--- | :--- |
| `vault_postgres_password` | `vault.yml` | Encrypted master password for the database. |

## 🔗 Dependencies
None. This is a standalone infrastructure role.

## 🚀 Example Playbook

To deploy a standard PostgreSQL instance for Airflow:

```yaml
- name: Deploy Database Tier
  hosts: localhost
  roles:
    - role: postgres
      vars:
        postgres_db_name: "custom_app_db"
        postgres_db_user: "dev_user"
```

## 🧪 Testing with Molecule

This role includes a comprehensive Molecule test suite. It validates that the database is not only running but also accessible and correctly initialized.

To run the full test sequence:

```bash
# Navigate to the role directory
cd roles/postgres

# Run the test suite using uv
uv run molecule test
```

The test cycle covers:

- Prepare: Injecting dummy secrets into the test container.
- Converge: Applying the role using delegate_to: localhost.
- Verify: Running psql queries inside the container via podman exec.


## 📄 License
MIT


## 👤 Author Information
addonol
Infrastructure Architect & Automation Specialist
