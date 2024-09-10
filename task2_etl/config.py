import pyodbc
import json
import os
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

def connect_google_api(cred):
    # Define the required scopes
    scope = ['https://www.googleapis.com/auth/spreadsheets']

    creds = ServiceAccountCredentials.from_json_keyfile_name(cred, scope)

    # Authorize the client
    client = gspread.authorize(creds)
    return client;