import pandas as pd
import config
import os
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
import json
import re

if __name__ == "__main__":
    def get_file(file, folder=None):
        if folder is None:
            file_path = os.path.join(current_directory, '..', file)
        else:
            file_path = os.path.join(current_directory, '..', f'{folder}\{file}')
        return os.path.abspath(file_path)

    current_directory = os.path.dirname(__file__)
    json_file_path = get_file(file='credentials.json')

    # connect to localhost SQL Server
    con , cur = config.connect_sql_server(json_file_path)

    employee_data = pd.read_csv('.\\task2_etl\\task2_dataset\\employee_data.csv')
    print(employee_data.head())

    with open(json_file_path, 'r') as f:
        data = json.load(f)

    connection_url = URL.create(
        "mssql+pyodbc",
        username=data['sql_server']['USERNAME'],
        password=data['sql_server']['PWD'],
        host=data['sql_server']['SERVER'],
        port=data['sql_server']['PORT'],
        database=data['sql_server']['DATABASE'],
        query={
            "driver": re.sub('[{}]','', data['sql_server']['DRIVER']),
            "TrustServerCertificate": data['sql_server']['Trusted_Connection'],
            "authentication": "ActiveDirectoryIntegrated",
        },
    )
    engine = create_engine(connection_url)
    employee_data.to_sql('employee_dataset',con=engine, if_exists='replace', index=False)