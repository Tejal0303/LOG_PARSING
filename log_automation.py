# liabrary
#from html_table_extractor.extractor import Extractor
from bs4 import BeautifulSoup
import csv
import pandas as pd
import json
import glob
from pathlib import Path 
from IPython.display import display_html
import xlsxwriter 

#soup = BeautifulSoup (open("C:/Users/tc186035/Desktop/Charter/5.01.02/mdmservices.log"), features="lxml")
#soup = BeautifulSoup (open("C:/Users/tc186035/Desktop/Charter/1_log_automation/platform.log"), 'html.parser')
# Enter Path Here 

file_path ='C:/Users/tc186035/Desktop/Charter/1_log_automation/DCR_Service.log'
target_path='C:/Users/tc186035/Desktop/Charter/1_log_automation'

COLUMN_NAMES=['Transaction_Id','TD_SessionId','Thread_Name','Level','Message','Stack_Trace','Call_Trace_Response']
log_table = pd.DataFrame(columns=COLUMN_NAMES) 
import bs4 as bs
soup = BeautifulSoup (open("C:/Users/tc186035/Desktop/Charter/1_log_automation/DCR_Service.log"), 'html.parser')
p=[]
for tr in soup.find_all('tr'):
    td = [td for td in tr.stripped_strings]
    p.append(td)

log_table= pd.DataFrame(p) 

COLUMN_NAMES=['Transaction_Id','TD_SessionId','Thread_Name','Level','Message','Stack_Trace','Call_Trace_Response']
log_table.rename(columns={0:'Transaction_Id'}, inplace=True)
log_table.rename(columns={1:'TD_SessionId'}, inplace=True)
log_table.rename(columns={2:'Thread_Name'}, inplace=True)
log_table.rename(columns={3:'Level'}, inplace=True)
log_table.rename(columns={4:'Message'}, inplace=True)
log_table.rename(columns={5:'Stack_Trace'}, inplace=True)
log_table.rename(columns={6:'Call_Trace_Response'}, inplace=True)

log_table= log_table[log_table.Transaction_Id !='Transaction Id']

xls_file_name =Path(file_path).name
xls_file_name =xls_file_name.split('.')[0]
tmp_path =str(target_path+'/'+xls_file_name+'.xlsx')  
err_log =log_table[log_table.Level=='Error']
exc_log =log_table[log_table.Level=='Exception']

with pd.ExcelWriter(tmp_path) as writer:
    err_log.to_excel(writer, sheet_name='Error')
    exc_log.to_excel(writer, sheet_name='Exception')