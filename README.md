
# Extract Transform Load Employee Data

Here is a simple project to enhance  my knowledges in processing RAW data and developing data pipeline.


## Appendix

- **Author Introduction**
- **Project Objectives**
- **Getting Started**
- **Usages**


## Hi, I'm Angga Hafidzin! 👋
A Data Analyst in the retail industry, with two years experience. I’ve honed my skills in managing extensive datasets and delivering actionable insights through comprehensive reports and analytical dashboards.
#### Let's connect! 
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anggaph/)

## 🛠 Project Objectives
### **Task 1**: Create and Insert data into SQL Server
In this task, I have delegated to build 2 relational table related to Employee and Position History data. Here are the appropriate values that I have to store in SQL Server

- Employee

  ![image](https://github.com/user-attachments/assets/bea8d50b-7e57-4917-a8be-c127edd092b3)

- Position History

  ![image](https://github.com/user-attachments/assets/0f760f62-898a-4d04-815c-15aaf6169fa4)
  ![image](https://github.com/user-attachments/assets/4076f920-611e-42f5-9fb6-6a87b803ab54)

### **Task 2**: ETL, Data Warehouse and Analytics Task
For this task, I have to create a data pipeline that will extract and transform a table data from Azure SQL Server and  another one from GCP (in this case using Google Spreadsheet as data platform). The data extracted from 2 different sources will be used on Looker Studio as an [Employee Monitoring Dashboard](https://lookerstudio.google.com/reporting/da25f3a4-d158-409d-a357-c26df808a839).

In this project I used Kaggle public datasets:
- [Employee Data](https://www.kaggle.com/datasets/ravindrasinghrana/employeedataset?resource=download&select=employee_data.csv)
- [Training & Development](https://www.kaggle.com/datasets/ravindrasinghrana/employeedataset?resource=download&select=training_and_development_data.csv)



## 📌 Getting Started
### Installing Python Libraries
There is `requirements.txt` file that contains all python libraries needed for this projects, such as ([PyODBC](https://pypi.org/project/pyodbc/), [GSpread](https://pypi.org/project/gspread/), etc)
```
pip install -r requirements.txt
```

### Prepare SQL Server Credentials
I have a credential data that allow me to access my local database on SQL Server, I stored it on JSON format:
```
{"sql_server":
    {
        "DRIVER":"your_driver"
        , "SERVER":"your_server"
        , "DATABASE":"your_database"
        , "USERNAME":"your_username"
        , "PWD":"your_password"
    }
}
```

### Prepare Google API & Services Credentials
To be able accessing data from Google Spreadsheets, one of the secure way is using Google APIs & Services, so I create my Service Accounts and enable Google Sheet API then stored the credentials into this JSON format:
```
{
  "type": "",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "angga-xxx@xxx.iam.gserviceaccount.com",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "",
  "auth_provider_x509_cert_url": "",
  "client_x509_cert_url": "",
  "universe_domain": ""
}

```
