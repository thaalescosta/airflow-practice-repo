from airflow.sdk import dag, task
from airflow.providers.standard.operators.bash import BashOperator

@dag(
        dag_id = 'operators'
)
def operators():

    @task.python
    def first_task():
        print('This is the first task')
        
    @task.python
    def second_task():
        print('This is the second task')
    
    @task.python
    def third_task():
        print('This is the third task')
    
    @task.bash
    def bash_task_modern():
        return "echo Hello World!"

    bash_operator_old_school = BashOperator(
    task_id="bash_operator_old",
    bash_command="echo 'Hello Old World!'",
)

    # Defining the task dependencies
    first = first_task()
    second = second_task()
    third = third_task()
    bash1 = bash_task_modern()

    first >> second >> third >> bash1 >> bash_operator_old_school

operators()