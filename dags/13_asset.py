from airflow.sdk import dag, task, asset
from pendulum import now
import os

@asset(
    # dag_id= '13_asset',
    schedule="@daily",
    # This is optional but good to include for clarity about the asset's location
    uri="/usr/local/airflow/logs/data/data_extract.txt",
    name="fetch_data"
)
def fetch_data(self):
    #Ensure the directory exists
    os.makedirs(os.path.dirname(self.uri), exist_ok=True)

    # Simulate data fetching by writing to a file
    with open(self.uri, 'w') as f:
        f.write(f"Data fetched on {now("America/Sao_Paulo")}")

    print(f"Data written to {self.uri}")