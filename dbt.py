from __future__ import annotations

import datetime

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dbt",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 4, 4, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"],
    params={"example_key": "example_value"},
) as dag:
    run_this_last = EmptyOperator(
        task_id="run_this_last",
    )

    # [START howto_operator_bash]
    run_this = BashOperator(
        task_id="run_dbt",
        bash_command="cd /Users/hiltonma/first_dbt_project/; /Users/hiltonma/anaconda3/bin/dbt run --select my_third_dbt_models",
    )
    # [END howto_operator_bash]

    run_this >> run_this_last

