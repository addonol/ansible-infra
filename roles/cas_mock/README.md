# 🔑 Ansible Role: CAS Mock (Containerized & Standalone)

This Ansible role deploys an isolated **Apereo CAS** (Central Authentication Service) mock server using **Podman** in **rootless mode**. It is designed as a reusable "Lego block" infrastructure component to simulate an SSO authentication provider for local development, testing, and CI/CD pipelines (like Molecule).

## 🛠 Key Features

*   **Total Isolation**: Deploy independent mock servers by simply adjusting the `cas_mock_hostname` and network variables.
*   **Rootless Security**: Operates without `sudo` privileges, keeping the host system clean and secure.
*   **SSL-Free Spring Boot**: Specifically pre-configured to bypass complex Java keystore requirements and run on pure HTTP (port 8080) for easy integration.
*   **Agnostic Design**: Zero hardcoded dependencies. The role does not "know" its clients; it receives all configuration via dynamic variables.
*   **Lifecycle Management**: Includes a dedicated `clean.yml` for standardized resource decommissioning (containers and networks).


## 📋 Prerequisites

*   **Target Host**: Podman installed and configured in rootless mode.
*   **Control Node**: Ansible 2.15+ and `containers.podman` collection (v1.15.0+).
*   **Network**: A pre-existing Podman network (defined via `cas_mock_network`).


## ⚙️ Role Variables

### Configuration Parameters (`defaults/main.yml`)


| Variable | Default | Description |
| :--- | :--- | :--- |
| `cas_mock_image` | `docker.io/apereo/cas:7.3.5` | Official Apereo CAS Docker image. |
| `cas_mock_hostname` | `{{ ansible_host }}` | Accessible IP or FQDN of the target machine. |
| `cas_mock_port_host` | `8081` | Port exposed on the host machine. |
| `cas_mock_port_container` | `8080` | Internal port used by the Tomcat server. |
| `cas_mock_user` | `admin` | Static username accepted by the CAS mock. |
| `cas_mock_pass` | `admin_password` | Static password accepted by the CAS mock. |
| `cas_mock_network` | `cas_network` | Shared or dedicated Podman network. |


## 🚀 Standalone Deployment Example

To integrate this role into a specific project (like testing SSO with Airflow 3), call the role by mapping your global project variables to the role variables:

```yaml
- name: "Deploy CAS Mock for Airflow SSO"
  ansible.builtin.include_role:
    name: cas_mock
  vars:
    cas_mock_user: "airflow_admin"
    cas_mock_pass: "{{ vault_airflow_sso_pass }}"
    cas_mock_network: "airflow_net"
    cas_mock_port_host: 8081
```

## 🧹 Cleanup Procedure

The role supports clean decommissioning through a dedicated tasks file:

```yaml
- name: "Emergency Clean"
  ansible.builtin.include_role:
    name: cas_mock
    tasks_from: clean.yml
  vars:
    cas_mock_network: "airflow_net"
    cas_mock_purge_network: true
```

## 🧪 Automated Testing (Molecule)

The role is validated via Molecule across Debian, Ubuntu, Fedora, and Rocky Linux.

```bash
# Run the full test suite
task cas:test
```

Verifications performed:

- *Idempotence*: Guarantees that a second execution results in zero changes.
- *Readiness*: Validates connectivity by querying the real `/cas/login` endpoint using curl from within the container.

## 📄 License
MIT

## 👤 Author Information
addonol
Infrastructure Architect & Automation Specialist
