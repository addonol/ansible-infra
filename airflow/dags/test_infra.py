from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    "test_ansible_stack",
    default_args={"retries": 1},
    description="Check of the Airflow 3 stack",
    schedule=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    t1 = BashOperator(
        task_id="check_worker_hostname",
        bash_command="hostname",
    )

    t2 = BashOperator(
        task_id="check_python_version",
        bash_command="python --version",
    )

    t1 >> t2
