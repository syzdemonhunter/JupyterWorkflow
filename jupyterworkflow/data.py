import os
from urllib.request import urlretrieve

import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
    """Download and cache the fremont data

    Parameters
    ----------
        filename: string (optional)
            location to save the data
        url: string (optional)
            web location of the data
        force_download: bool (optional)
            if True, force redownload of the data

    Returns
    -------
    data: pandas.DataFrame
        The fremont bridge data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)

    data_tmp = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
    data = data_tmp[['Fremont Bridge East Sidewalk', 'Fremont Bridge West Sidewalk']]
    data.columns = ['East', 'West']
    data['Total'] = data['West'] + data['East']

    return data
