import pandas as pd
import sqlalchemy

from GRANT_DOCTOR_MAPPING.npi_grants import grants_reader
from GRANT_DOCTOR_MAPPING.npi_grants import npi_data


def db():
    engine = sqlalchemy.create_engine('sqlite:///data/double_grants_npi.db')
    # C:/Users/Valenty/grant_doctor_mapping/grant_doctor_mapping-1/
    conn = engine.connect()
    return conn

def grants_csv_to_db():
    df = grants_reader.read_grants_year(22)
    df.to_sql('grants',   #object type?
              db(),
              if_exists='append',
              index=False)
    
def npi_csv_to_db():
    df = npi_data.read('data/npidata_pfile_20240205-20240211.csv')
    df.to_sql('npi',
              db(),
              if_exists='append',
              index=False)

if __name__ == '__main__':
    grants_csv_to_db()
    npi_csv_to_db()