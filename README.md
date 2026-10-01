# WHAT IS AIRFLOW?

Airflow is an open source framework which can be used as an ORCHESTRATOR.

**What Airflow is not:**
* airflow is **```NOT```** a DARA PROCESSING framework
* Airflow is **```NOT```** a REAL-TIME PROCESSING framework.
* Airflow is **```NOT```** an ETL framework.

## CORE COMPONENTS OF AIRFLOW

* **Metadata DB:** Airflow needs to store all the metadata about the DAGs. For instance, DAG runs, schedule, status, task instance, etc.
* **DAG File Processor:** DAG File processor will go to your dags folder and wil parse it and store the serialized DAG into the DB.
* **API Server:** Frontend and middle man for pretty much all processes.
* **Scheduler:** The scheduler is responsible for WHAT and WHEN tasks need to be executed.
* **Executor:** The executor will decide the HOW and WHERE tasks need to be run.
* **Workers:** Workers are the real layer for execution.
* **Queue:** As the name suggests
* **Triggerer:** Same

## CORE COMPONENTS OF AIRFLOW

* **DAG:** Direct Acyclic Graph. Basically it doesn't loop.
* **Task Instance:** It's just a unit of work or step. The rectangles in the DAG graph.
* **Operator:** An operator is conceptually a template for a predefined Task, that you can just define declaratively inside your DAG

# ASSETS IN AIRFLOW

