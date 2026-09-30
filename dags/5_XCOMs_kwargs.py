from airflow.sdk import dag, task


@dag(
        dag_id = '05_xcoms_dag_manual'
)
def xcoms_dag_manual():

    @task.python
    def first_task(**kwargs):
        print('Extracting data.. This is the first task')
        fetched_data = {"data": [1, 2, 3, 4, 5]}
        
        # Extracting 'ti' from kwargs to push XComs manually
        ti = kwargs['ti']
        ti.xcom_push(key = 'return_result', value=fetched_data)

    @task.python
    def second_task(**kwargs):
        # Extracting 'ti' from kwards to pull XComs manually
        ti = kwargs['ti']
        fetched_data = ti.xcom_pull(task_ids = 'first_task', key='return_result')['data']

        transformed_data = fetched_data * 2
        transformed_data_dict = {"trans_data":transformed_data}

        ti.xcom_push(key = 'return_result', value=transformed_data_dict)


    @task.python
    def third_task(**kwargs):
        # Extracting 'ti' from kwards to pull XComs manually
        ti = kwargs['ti']
        load_data = ti.xcom_pull(task_ids = 'second_task', key='return_result')['trans_data']
        ti.xcom_push(key = 'return_result', value=load_data)

    # Defining the task dependencies
    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third

xcoms_dag_manual()