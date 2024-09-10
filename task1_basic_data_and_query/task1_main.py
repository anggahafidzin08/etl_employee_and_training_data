import pandas as pd
import config
import sqlparse
import os
import numpy as np

if __name__ == "__main__":
    def get_file(file, folder=None):
        if folder is None:
            file_path = os.path.join(current_directory, '..', file)
        else:
            file_path = os.path.join(current_directory, '..', f'{folder}\{file}')
        return os.path.abspath(file_path)

    current_directory = os.path.dirname(__file__)
    json_file_path = get_file(file='credentials.json')
    create_employee = get_file(file='create_employee.sql', folder='query')
    create_position = get_file(file='create_position_history.sql', folder='query')
    insert_employee = get_file(file='insert_employee_data.sql', folder='query')
    insert_position = get_file(file='insert_position_data.sql', folder='query')
    display = get_file(file='display_employee_position_history.sql', folder='query')

    con, cur = config.connect_sql_server(json_file_path)
    # check = pd.read_sql(""" select * from [AdventureWorksLT].[dbo].[employee]
    #     """, con)
    cur.execute(sqlparse.format(open(create_employee, 'r').read(), strip_comments=True).strip())
    cur.execute(sqlparse.format(open(create_position, 'r').read(), strip_comments=True).strip())
    cur.execute(sqlparse.format(open(insert_employee, 'r').read(), strip_comments=True).strip())
    cur.execute(sqlparse.format(open(insert_position, 'r').read(), strip_comments=True).strip())
    display_all = pd.read_sql(sqlparse.format(open(display, 'r').read(), strip_comments=True).strip(), con)
    print(display_all)
    cur.close()
    con.close()