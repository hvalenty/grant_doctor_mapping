import pandas as pd
import GRANT_DOCTOR_MAPPING.grants_data as grants_data
import GRANT_DOCTOR_MAPPING.npi_grants.npi_data as npi_data
import GRANT_DOCTOR_MAPPING.npi_grants.string_distance_features as dist


if __name__ == '__main__':
    # read in Grants and NPI data
    gd = grants_data.GrantsData('data/RePORTER_PRJ_C_FY2022.zip')
    npi = npi_data.NpiData('data/npidata_pfile_20240205-20240211.csv')

    gd.read()
    npi.read_npi()

