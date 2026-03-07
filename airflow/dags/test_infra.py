"""
Infrastructure Flow Explainer.

PURPOSE: Demonstrate the physical path of a task.
PATH: Scheduler -> RabbitMQ (Message) -> Worker (Execution) -> Postgres (Result)
"""

import socket
import sys
from datetime import datetime
from typing import Any

from airflow import DAG
from airflow.operators.python import PythonOperator

# Explicit typing for the dictionary to satisfy the Linter
default_args: dict[str, Any] = {
    "owner": "addonol",
    "start_date": datetime(2025, 3, 6),
    "retries": 1,
}

with DAG(
    "infra_explain_flow",
    default_args=default_args,
    description="Educational flow tracing the task from Scheduler to Worker.",
    schedule=None,
    catchup=False,
    tags=["demonstration", "infrastructure"],
) as dag:

    def step_1_scheduler_handoff() -> str:
        """
        Phase 1: The Scheduler.
        The Scheduler serializes this task and pushes it to RabbitMQ.
        """
        print("--- PHASE 1: SCHEDULER ---")
        print("1. Scheduler scanned the DAG file.")
        print("2. Scheduler is now sending a message to RabbitMQ 'default' queue.")
        return f"Message generated at {datetime.now().isoformat()}"

    def step_2_worker_pickup(**kwargs: Any) -> str:
        """
        Phase 2: The Worker.
        The Worker pulls the message from RabbitMQ and executes the Python code.
        """
        # Using kwargs to pull data from Step 1 via XCom (stored in Postgres)
        ti = kwargs["ti"]
        input_value = ti.xcom_pull(task_ids="scheduler_handoff")

        print("--- PHASE 2: WORKER EXECUTION ---")
        print(f"Data retrieved from Postgres: {input_value}")
        print(f"Worker Hostname (Container ID): {socket.gethostname()}")
        print(f"Worker Python Version: {sys.version}")
        return f"Successfully processed by {socket.gethostname()}"

    t1 = PythonOperator(
        task_id="scheduler_handoff",
        python_callable=step_1_scheduler_handoff,
    )

    t2 = PythonOperator(
        task_id="worker_pickup",
        python_callable=step_2_worker_pickup,
    )

    _ = t1 >> t2
