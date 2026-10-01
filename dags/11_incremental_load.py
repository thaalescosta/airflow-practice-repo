from airflow.sdk import dag, task
from pendulum import datetime
from airflow.timetables.interval import CronDataIntervalTimetable


@dag(
        dag_id = '11_incremental_load',
        schedule= CronDataIntervalTimetable("@daily", timezone="America/Sao_Paulo"),
        start_date=datetime(2026,9,26,tz="America/Sao_Paulo"),
        end_date=datetime(2026,9,30,tz="America/Sao_Paulo"),
        catchup=True
)
def incremental_load_dag():

    @task.python
    def incremental_data_fetch(**kwargs):
        date_interval_start = kwargs['data_interval_start']
        date_interval_end = kwargs['data_interval_end']
        print(f"Fetching data from {date_interval_start} to {date_interval_end}")
        
    @task.bash
    def incremental_data_process():
        return "echo 'Fetching data from {{data_interval_start}} to {{data_interval_end}}'"

    fetch_task = incremental_data_fetch()
    process_task = incremental_data_process()

    fetch_task >> process_task

incremental_load_dag()