
import pandas as pd

def get_logs():
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQuSPKtgySZXQ85nXNF4RVq4cooYS29g9V0C-gFn0vzqr8nYMWpyOnW-qxMPjVcmkFDRhRDU5gDOVeM/pub?gid=0&single=true&output=csv')
    columns = ['Date','Event',"Type",'Id']
    df.columns = columns
    df.set_index('Id')
    return df
