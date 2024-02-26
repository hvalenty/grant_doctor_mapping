import pandas as pd

class NpiData:

    def read_npi(path: str) -> pd.DataFrame:
        """Read in npi file from path, clean and return."""
        path = 'data/npidata_pfile_20240205-20240211.csv'
        df = pd.read_csv(path)
        #print(df)
        return df


    def select_columns(df: pd.DataFrame) -> pd.DataFrame:
        """Rename and select columns
        NOTE: Underscored methods are "private methods", otherwise 
        meaning that we should only call them from WITHIN the class.

        Args:
            df (pd.DataFrame): dataframe

        Returns:
            pd.DataFrame: the subset, clean name dataframe
        """
        mapper = {
                'NPI': 'npi',
                'Provider Last Name (Legal Name)': 'last_name',
                'Provider First Name': 'first_name',
                'Provider Business Mailing Address City Name': 'city_name',

            }
        df = df.rename(columns=mapper)[mapper.values()]
        return df

    if __name__ == '__main__':
        path = 'data/npidata_pfile_20240205-20240211.csv'
        df = pd.read_csv(path)
        read_npi()
        select_columns(df)

    # for each pairing from the datasets are the people the same from
    # npi and grants datasets
        
    #euclidian distance vs angle distance
        
    # use class for hard to load and use it a lot
        