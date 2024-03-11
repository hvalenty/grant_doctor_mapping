import pandas as pd


class GrantsData:
    def __init__(self, path: str):
        self.df = pd.read_csv(path, compression='zip')

    def read(self) -> pd.DataFrame:
        """Returns a cleaned dataframe"""
        df = self._select_columns(self.df)
        df = self._clean(df)
        # Data can have NaNs
        # Different types (reasonable)
        # Different types (unreasonable)
        return df
        

    @staticmethod
    def _select_columns(df: pd.DataFrame) -> pd.DataFrame:
        """Rename and select columns
        NOTE: Underscored methods are "private methods", otherwise 
        meaning that we should only call them from WITHIN the class.

        Args:
            df (pd.DataFrame): dataframe

        Returns:
            pd.DataFrame: the subset, clean name dataframe
        """
        mapper = {
            'APPLICATION_ID': 'application_id',
            'BUDGET_START': 'budget_start',
            'ACTIVITY': 'grant_type',
            'TOTAL_COST': 'total_cost',
            'PI_NAMEs': 'pi_names',
            'PI_IDS': 'pi_ids',
            'ORG_NAME': 'organization',
            'ORG_CITY': 'city',
            'ORG_STATE': 'state',
            'ORG_COUNTRY': 'country'
        }
        return df.rename(columns=mapper)[mapper.values()]
    
    @staticmethod
    def _clean(df: pd.DataFrame) -> pd.DataFrame:
        """Remove NaNs and other cleaning functions

        Args:
            df (pd.DataFrame): dataframe with subset column names

        Returns:
            pd.DataFrame: dataframe free of NaNs
        """
        df['pi_names'] = df['pi_names'].str.split(';')
        df = df.explode('pi_names')
        df['is_contact'] = df['pi_names'].str.lower().str.contains('(contact)')
        df['pi_names'] = df['pi_names'].str.replace('(contact)', '')
        df['both_names'] = df['pi_names'].apply(lambda x: x.split(',')[:2])
        df[['last_name', 'forename']] = pd.DataFrame(df['both_names'].to_list(), index=df.index)
        return df

        



def read_grants_year(year: int or str) -> pd.DataFrame:
    """Read in Grants Data for a year and return as clean dataframe

    Args:
        year (int | str): year to read

    Returns:
        pd.DataFrame: clean dataframe of grants data
    """
    # We know the filename is: RePORTER_PRJ_C_FY2022.zip
    path = 'data/RePORTER_PRJ_C_FY{year}.zip'
    gd = GrantsData(path.format(year=year))
    return gd.read()

def impute_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Take in a dataframe and replace NaNs for dates in [] with approximation

    Args:
        df (pd.DataFrame): original RePORTER dataframe

    Returns:
        pd.DataFrame: new RePORTER dataframe with replaced NaNs
    """
    print(df)


if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    import datetime
    # '/mnt/search/data/grants/RePORTER_PRJ_C_FY2022.zip'

    # vec1 = [i for i in range(1_000_000)]
    # vec2 = np.arange(1_000_000)
    # gr22 = read_grants_year(2022)
    df = pd.read_csv('data/RePORTER_PRJ_C_FY2022.zip')
    # print(df.columns)
    date_look = df[['AWARD_NOTICE_DATE','BUDGET_START',
                   'PROJECT_START','BUDGET_END','PROJECT_END']]
    print(date_look)
    print((date_look['BUDGET_END'] == date_look['PROJECT_END']).sum())
    a_notify = pd.to_datetime(date_look['AWARD_NOTICE_DATE'])
    b_start = pd.to_datetime(date_look['BUDGET_START'])
    p_start = pd.to_datetime(date_look['PROJECT_START'])
    
    proj_min_budg = p_start - b_start
    award_min_budget = a_notify - b_start
    print((proj_min_budg).mode())
    print(award_min_budget.mode())
    #mean -1515, 5 days | median -716, -2 days | 0 (22403, 27%), 0 (17670, 21%) days | range 18262-(-1458)=19720 , 1968-(-414)=2382
    filler = p_start+pd.to_timedelta(716, 'D')
    # print(filler)
    date_look['BUDGET_START'] = date_look['BUDGET_START'].fillna(filler)
    # print(df2) # still 3275 NaNs in the dataframe
    
    filler2 = a_notify+pd.to_timedelta(2, 'D')
    # print(filler2)
    date_look["BUDGET_START"] = date_look['BUDGET_START'].fillna(filler2)
    print(date_look)
    print(date_look.isna().sum()) 
    # Chose to use median because the range (outliers) was too large for the mean, and the mode
    # did not occur often enough (21%). Filled with median time between the project start and the budget start
    # and then median time between award notice and budget start, but did not reduce NaNs. 
    
    # gd = GrantsData()