import pyodbc
import json
import os
import datetime

def connect_sql_server(cred):
    
    with open(cred, 'r') as f:
        data = json.load(f)
    
    conn_str = (
        f"DRIVER={data['sql_server']['DRIVER']};"
        f"SERVER={data['sql_server']['SERVER']};"
        f"DATABASE={data['sql_server']['DATABASE']};"
        f"Trusted_Connection={data['sql_server']['Trusted_Connection']};"
    )
    
    con = pyodbc.connect(conn_str, autocommit=True)
    cur = con.cursor()
    print(f'[{datetime.datetime.now}: Connected to SQL Server]')
    return con, cur;