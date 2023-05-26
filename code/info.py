import pandas as pd
from code.hits import agouti_observations, deepsqueak_observations
from code.matchingdates import matching_dates
from code.classes.dataframe_extension import Dataframe
import copy

def total_observations(agouti_observation: pd.DataFrame, deepsqueak_observation: pd.DataFrame):
    total_agouti_observations =  len(agouti_observation['timestamps'].tolist())
    total_deepsqueak_observations = len(deepsqueak_observation['timestamps'].tolist())
    return [total_agouti_observations, total_deepsqueak_observations]

def total_runtime(agouti_runtime, deepsqueak_runtime):
    """
    Return total runtime in hours
    """
    dates = matching_dates(agouti_runtime, deepsqueak_runtime)
    total_dates = 0
    for location in dates.keys():
        total_dates += len(dates[location])
    total_hours = total_dates / 24.0
    return total_hours

def observations_location(type_observations):
    """
    Returns total observations per location agouti
    """
    my_dict = {}
    data = Dataframe(type_observations)
    locations = list(set(data.df['locationName'].tolist()))
    for location in locations:
        copy_data = copy.deepcopy(data)
        copy_data.select_rows_by_columnvalue('locationName', location)
        observations = len(copy_data.df)
        my_dict.update({location: observations})
    return my_dict

