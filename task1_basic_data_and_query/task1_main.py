import pandas as pd
import config
import sqlparse
import os

if __name__ == "__main__":
    
    con, cur = config.connect_sql_server('./etl_employee_and_training_data/credentials.json')
    check = pd.read_sql(""" select * from employee
        """, con)
    print(check)
    cur.close()
    con.close()
