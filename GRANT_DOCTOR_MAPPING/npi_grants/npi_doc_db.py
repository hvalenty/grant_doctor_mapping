import pandas as pd
import sqlalchemy

from GRANT_DOCTOR_MAPPING.npi_grants import grants_reader
from GRANT_DOCTOR_MAPPING.npi_grants import npi_data


def db():
    engine = sqlalchemy.create_engine('sqlite:///data/npi_datatable.db')
    # C:/Users/Valenty/grant_doctor_mapping/grant_doctor_mapping-1/
    conn = engine.connect()
    return conn


def npi_csv_to_db():
    df = npi_data.read('data/npidata_pfile_20240205-20240211.csv')
    df.to_sql('npi',
              db(),
              if_exists='append',
              index=False)


#def grants_csv_to_db(csv_path: str):
#    df = grants_reader.read_grants_year(22)
#    df.to_sql('npi',
#              db(),
#              if_exists='append',
#              index=False)
#data types match (definitions), and only pass columns you want
    # make two tables one for npi and other for grants and then one as a bridge table

if __name__ == '__main__':
    npi_csv_to_db()
