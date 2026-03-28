# 🐰 Ansible Role: RabbitMQ (Containerized & Multi-Instance)

This Ansible role deploys a fully isolated and dynamic **RabbitMQ** broker with the **Management Plugin** enabled, utilizing **Podman** in **rootless mode**. It is built as a modular infrastructure component, allowing multiple independent brokers to coexist on the same host without configuration or port conflicts.

## 🛠 Key Features

*   **Instance Isolation**: Deploy multiple independent brokers by simply adjusting the `rabbitmq_instance` variable.
*   **Rootless Security**: Operates without `sudo` privileges, using **Podman Secrets** to inject sensitive configuration and credentials securely.
*   **EPMD Stability**: Automatically handles Erlang Port Mapper Daemon (EPMD) resolution within Podman networks to prevent boot failures.
*   **Native Healthcheck**: Leverages `rabbitmq-diagnostics` to ensure the Erlang VM and the broker are fully operational before dependent services start.
*   **Lifecycle Management**: Includes a dedicated `clean.yml` for standardized resource decommissioning (containers, secrets, and volumes).

## 📋 Prerequisites

*   **Target Host**: Podman installed and configured in rootless mode.
*   **Control Node**: Ansible 2.15+ and `containers.podman` collection (v1.15.0+).
*   **Network**: A pre-existing Podman network (defined via `rabbitmq_network`).

## ⚙️ Role Variables

### Configuration Parameters (`defaults/main.yml`)


| Variable | Default | Description |
| :--- | :--- | :--- |
| `rabbitmq_instance` | `rabbitmq_standalone` | Unique container name and resource prefix. |
| `rabbitmq_image` | `rabbitmq:3.13-management-alpine` | Official RabbitMQ Management image. |
| `rabbitmq_user` | `admin` | Primary administrative username. |
| `rabbitmq_pass` | `change_me` | Admin password (should be passed via Vault). |
| `rabbitmq_management_port` | `5672` | AMQP port exposed on the host. |
| `rabbitmq_ui_port` | `15672` | Management UI/API port exposed on the host. |
| `rabbitmq_network` | `infra_net` | Shared or dedicated Podman network. |
| `rabbitmq_volume` | `rabbitmq_data` | Named volume for data persistence. |


## 🚀 Standalone Deployment Example

To integrate this role into a specific project (e.g., a Celery stack), call the role by mapping your global project variables:

```yaml
- name: "Deploy RabbitMQ for Airflow"
  ansible.builtin.include_role:
    name: rabbitmq
  vars:
    rabbitmq_instance: "airflow_rabbitmq"
    rabbitmq_user: "mq_admin"
    rabbitmq_pass: "{{ vault_rabbitmq_password }}"
    rabbitmq_network: "airflow_net"
    rabbitmq_ui_port: 15672
```

## 🧹 Cleanup Procedure

The role supports clean decommissioning through a dedicated tasks file:

```yaml
- name: "Emergency Clean"
  ansible.builtin.include_role:
    name: rabbitmq
    tasks_from: clean.yml
  vars:
    rabbitmq_instance: "airflow_rabbitmq"
    rabbitmq_volume: "airflow_mq_data"
```


## 🧪 Automated Testing (Molecule)

The role is validated via Molecule across Debian, Ubuntu, Fedora, and Rocky Linux.

```bash
# Run the full test suite
task rabbitmq:test
```

The test suite verifies:

- **Readiness**: Ensures the broker reaches a healthy state via podman `inspect`.
- **Security**: Validates that `rabbitmq_pass` is NOT leaked in container metadata.
- **Network**: Confirms EPMD and AMQP ports are correctly bound and reachable.

## 📄 License
MIT

## 👤 Author Information
addonol
Infrastructure Architect & Automation Specialist
