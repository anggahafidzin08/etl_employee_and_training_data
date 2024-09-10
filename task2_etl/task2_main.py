import pandas as pd
import sqlparse
import config
import os
from gspread_dataframe import get_as_dataframe, set_with_dataframe

if __name__ == "__main__":
    def get_file(file, folder=None):
        if folder is None:
            file_path = os.path.join(current_directory, '..', file)
        else:
            file_path = os.path.join(current_directory, '..', f'{folder}\{file}')
        return os.path.abspath(file_path);
    
    current_directory = os.path.dirname(__file__)
    
    json_file_path = get_file(file='credentials.json')
    
    creds_google = get_file(file='cred_google.json')
    

    # python connect to Google API through service credentials
    client = config.connect_google_api(creds_google)

    # data training = https://docs.google.com/spreadsheets/d/1nfxwUaTRQCVl3QTrBlcfAlQ509X8bXkFlRJdziCdds0
    spreadsheet = client.open_by_key('1nfxwUaTRQCVl3QTrBlcfAlQ509X8bXkFlRJdziCdds0')
    sheet1 = spreadsheet.worksheet('Sheet 1')

    # get data from Google Spreadsheets
    training_df = get_as_dataframe(sheet1)

    # connect to SQL Server to get Employee Dataset
    con, cur = config.connect_sql_server(json_file_path)
    emp_dataset = sqlparse.format(open(get_file(file='get_employee_dataset.sql', folder='query'), 'r').read()
                                  , strip_comments=True).strip()
    employee_df = pd.read_sql_query(emp_dataset, con)
    cur.close()
    con.close()
    
    employee_df['StartDate'] = pd.to_datetime(employee_df['StartDate'])
    employee_df['ExitDate'] = pd.to_datetime(employee_df['ExitDate'])
    
    dmart = employee_df.merge(training_df, how='left', on=['EmpID']).sort_values(by=['EmpID', 'TrainingDate'], ascending=[True, True]).reset_index(drop=True)
    
    report_viz = spreadsheet.worksheet('DMart - Report + Visualizations')
    set_with_dataframe(report_viz, dmart)
