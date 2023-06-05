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

folder_agouti: str = '/Users/yanickidsinga/Documents/flevopark-20230202124032'
folder_deepsqueak: str = ''

location_data: str = 'amsterdao'
name_dataset: str = 'hij'

INTERVAL_AGOUTI: int = 0
INTERVAL_DEEPSQUEAK: int = 0
INTERVAL_OVERLAP: int = 0
"""
def run(paths_agouti, interval_agouti, interval_deepsqueak, interval_overlap):
    #agouti_paths('/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/agouti/Artis')
    location: str = input("location: ")
    interval: int = int(input("Interval (seconds): "))
    interval_camera_audio: int = int(input("Interval between audio and video (seconds): ")) 
    answer = input("want to remove results? Yes (y) or No(n)")
    if answer.lower() == 'y':
        remove_results(folder_results)
    #agouti
    filtered_dataframe: Dataframe = filter_data_agouti(observations_csv, media_csv, deployments_csv, location, path_results)
    runtime_agouti: Dataframe = total_runningtime(deployments_csv, location, path_results)
    agouti_data: dict[str, pd.DataFrame] = agoutidata_to_dict(filtered_dataframe)

    #deepsqueak
    runtime_deepsqueak: Dataframe = runtime(deepsqueak_path_folder, path_results)
    files_per_location: dict[str, list[str]] = deepsquakfiledata_to_dict(deepsqueak_path_folder)

    #matchingdates
    dates = matching_dates(runtime_agouti, runtime_deepsqueak, path_results)

    #filesmatchingdates
    locatoin_rows_agouti = agouti_rows(dates, agouti_data)
    location_files_deepsqueak = deepsqueak_files(dates, files_per_location)

    #hits
    observations_deepsqueak = deepsqueak_observations(location_files_deepsqueak, interval, path_results)
    observations_agouti = agouti_observations(locatoin_rows_agouti, interval, path_results)

    #overlaps
    chances(observations_deepsqueak, observations_agouti, interval_camera_audio )
"""