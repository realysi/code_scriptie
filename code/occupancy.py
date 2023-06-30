from code.check import check
from code.interface import flags
from code.move_data import move

from code.agouti.filter import filter_data_agouti
from code.agouti.runtime import total_runningtime
from code.agouti.data import agoutidata_to_dict
from code.classes.dataframe_extension import Dataframe
import pandas as pd
from code.deepsqueak.runtime import runtime
from code.matchingdates import matching_dates
from code.deepsqueak.data import deepsquakfiledata_to_dict 
from code.files_matchingdates import agouti_rows, deepsqueak_files

from code.hits import deepsqueak_observations, agouti_observations

from code.overlaps import chances
from code.interface import clear_folders, results_directories, info, flags
from code.check import check
import sys
import os
from code.info import hour_day
from code.dates import dates_study

#split total time period up into lenght of all_dates -> note for the day which locations had an observation
def occupancy_rate(dates: list[str], agouti_observations: pd.DataFrame, deepsqueak_observations: pd.DataFrame):

    for i in dates:
        if agouti_observations[agouti_observations['timestamps'].str.contains(i)]:
            pass

    """
    # Create a sample DataFrame
    data = {'Column1': ['apple', 'banana', 'orange'],
            'Column2': ['cat', 'dog', 'elephant'],
            'Column3': ['apple pie', 'banana split', 'orange juice']}
    df = pd.DataFrame(data)

    # Check if 'pie' is a substring in 'Column3'
    substring = 'pie'
    result = df[df['Column3'].str.contains(substring)]
    print(result)"""
