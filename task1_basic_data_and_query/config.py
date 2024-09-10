import pyodbc
import json

def connect_sql_server(cred):
    with open('credentials.json') as f:
        data = json.load(f)
    
    conn_str = (
        f"DRIVER={data['sql_server']['DRIVER']};"
        f"SERVER={data['sql_server']['SERVER']};"
        f"DATABASE={data['sql_server']['DATABASE']};"
        f"Trusted_Connection={data['sql_server']['Trusted_Connection']};"
    )
    con = pyodbc.connect(conn_str)
    cur = con.cursor()
    return con, cur;