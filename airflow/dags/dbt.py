from airflow import DAG
from airflow_dbt.operators.dbt_operator import (
    DbtSeedOperator,
    DbtRunOperator,
)
from airflow.utils.dates import days_ago

default_args = {
  'dir': '../dbt',
  'start_date': days_ago(0),
  'profiles_dir': '../dbt'
}


with DAG(dag_id='dbt_test', default_args=default_args, schedule_interval='@daily') as dag:

  dbt_seed = DbtSeedOperator(
    task_id='dbt_seed',
  )
  dbt_run = DbtRunOperator(
    task_id='dbt_run',
  )


  dbt_seed >> dbt_run 
