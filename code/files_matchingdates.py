from code.read_data import read_csv
from code.classes.dataframe_extension import Dataframe
from code.deepsqueak.data import deepsquakfiledata_to_dict
from code.agouti.data import agoutidata_to_dict
from code.agouti.filter import filter_data_agouti
import datetime
import copy
import pandas as pd

from code.matchingdates import matching_dates

def deepsqueak_files(dates, files_per_location):
    """
    Returns filenames of deepsqueak file that have a matching date in their name
    {location: [file, file, file]}
    """
    """dates = matching_dates(path_deployments, location_dataset, folder_deepsqueak)
    files_per_location: dict[str, list[str]] = deepsquakfiledata_to_dict(folder_deepsqueak)
    """
    my_dict = {}
    for location in dates.keys():
        files_with_matching_dates = []
        matching_dates_location: list = dates[location]
        files_location: list = files_per_location[location]

        for file in files_location:
            for date in matching_dates_location:
                if date in file:
                    files_with_matching_dates.append(file)
        my_dict.update({location: files_with_matching_dates})
    return my_dict

def agouti_rows(dates: dict[str, list[str]], agouti_data: dict[str, pd.DataFrame]):
    """
    Returns pd.Dataframe rows that contain matching_dates. It does so in a dictionary
    {location: pd.Dataframe rows}
    """
    my_dict = {}
    for location in dates.keys():
        matching_dates_location: list = dates[location]
        rows_with_matching_location: pd.DataFrame = agouti_data[location]
        agouti_dates = []
        for i in rows_with_matching_location.index:
            cell_value = str(rows_with_matching_location.loc[i, 'UTC timestamp'])
            cell_value = cell_value.split(" ")[0]
            agouti_dates.append(cell_value)
        #rows_with_matching_location['date'] = agouti_dates
        rows_with_matching_location = rows_with_matching_location.assign(date=agouti_dates)

        rows_with_matching_dates = rows_with_matching_location.loc[rows_with_matching_location['date'].isin(matching_dates_location)]
        rows_with_matching_dates = rows_with_matching_dates.drop('date', axis=1)
        my_dict.update({location: rows_with_matching_dates})

    return my_dict

