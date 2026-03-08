# 🐰 Ansible Role: RabbitMQ (Containerized & Rootless)

This Ansible role deploys and manages a standalone **RabbitMQ** broker with its **Management Plugin** using **Podman** in **rootless mode**. It is built as a secure, production-ready infrastructure component for message-oriented middleware.

## 🌟 Key Features
*   **Rootless Isolation**: Runs without `sudo` privileges, minimizing the host's attack surface.
*   **Modern Security (v3.13+)**: Password injection via **Podman Secrets** and `default_pass.file` configuration (no sensitive data in environment variables or plain text config).
*   **Full Lifecycle Management**: Handles dedicated networks, persistent volumes, secrets, and container states.
*   **Multi-Platform Validation**: Fully tested via **Molecule** across Debian, Ubuntu, Fedora, and Rocky Linux.

## 🛠 Prerequisites
*   **Target Host**: Podman installed and configured (rootless mode enabled).
*   **Control Node**: Python 3.12+ (managed via `uv` recommended).
*   **Collections**: `containers.podman` (v1.15.0+).

## 📦 Role Variables

Variables are designed to be easily overridden via your inventory or playbooks.

### Configuration Parameters (`defaults/main.yml`)


| Variable | Default | Description |
| :--- | :--- | :--- |
| `rabbitmq_image` | `docker.io/library/rabbitmq:3.13-management-alpine` | Official Management image to use. |
| `rabbitmq_container_name` | `rabbitmq_broker` | Name of the Podman instance. |
| `rabbitmq_user` | `mq_admin` | Primary administrative user. |
| `rabbitmq_network` | `infra_net` | Dedicated Podman network. |
| `rabbitmq_amqp_port` | `5672` | AMQP port exposed on the host. |
| `rabbitmq_ui_port` | `15672` | Management UI/API port exposed on the host. |
| `rabbitmq_volume_name` | `rabbitmq_data` | Persistent volume for message storage. |
| `rabbitmq_secret_pass_name` | `rabbitmq_password` | Name of the Podman secret for the admin password. |

### Sensitive Variables (Encrypted)


| Variable | Source | Description |
| :--- | :--- | :--- |
| `vault_rabbitmq_password` | `vault.yml` | Admin password (Ansible Vault). |

## 🚀 Example Playbook

Standard deployment for a generic message broker:

```yaml
- name: Deploy Messaging Tier
  hosts: mq_servers
  roles:
    - role: rabbitmq
      vars:
        rabbitmq_container_name: "prod_broker"
        rabbitmq_user: "app_service"
        ...
```

## 🧪 Automated Testing (Molecule)

```bash
# Run unit tests on all supported platforms (Debian, Ubuntu, Fedora, Rocky)
task rabbitmq:test
```

The test suite verifies:

- **Integrity**: Secure creation of secrets and persistent volumes on the host.
- **Portability**: Successful deployment across different Linux families.
- **Service Connectivity**: Health checks via rabbitmqctl ping and Management API authentication.

## 📄 License
MIT

## 👤 Author Information
addonol
Infrastructure Architect & Automation Specialist
