from airflow.sdk import dag, task
from pendulum import datetime
from airflow.timetables.events import EventsTimetable


special_dates = EventsTimetable(
    event_dates= [
    datetime(2026,1,27),
    datetime(2026,12,13),
    datetime(2026,3,18),
    datetime(2026,8,13)
])


@dag(
        dag_id = '12_incremental_special_schedule',
        schedule= special_dates,
        start_date=datetime(2026,1,1,tz="America/Sao_Paulo"),
        end_date=datetime(2026,9,30,tz="America/Sao_Paulo"),
        catchup=True
)
def special_dates_dag():

    @task.python
    def special_event_task(**kwargs):
        execution_date = kwargs['logical_date']
        print(f"Running task for special event on {execution_date}")

    special_event = special_event_task()

special_dates_dag()