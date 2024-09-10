import pandas as pd
import config
import os
from sqlalchemy.engine import URL
from sqlalchemy import create_engine

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

    employee_data = pd.read_csv('task2_dataset/employee_data.csv')
    print(employee_data.head())
    connection_url = URL.create(
        "mssql+pyodbc",
        username="",
        password="",
        host="localhost\\SQLEXPRESS",
        port=1433,
        database="AdventureWorksLT",
        query={
            "driver": "SQL Server",
            "TrustServerCertificate": "yes",
            "authentication": "ActiveDirectoryIntegrated",
        },
    )
    engine = create_engine(connection_url)
    employee_data.to_sql('employee_dataset',con=engine, if_exists='replace', index=False)