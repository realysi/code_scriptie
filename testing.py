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
from code.dates import occupancy_matrix_agouti, occupancy_matrix_deepsqueak,agouti_dates, deepsqueak_dates, all_deepsqueak_dates, all_deepsqueak_dates_list, dates_between
from code.dates import occupancy_matrix_agouti_test, occupancy_matrix_deepsqueak_test
#absolute paths to data
path_folder_agouti: str = '/Users/yanickidsinga/Documents/flevopark-20230202124032'
path_folder_deepsqueak: str = '/Users/yanickidsinga/Documents/deepsqueak_flevopark_csv'

#name of datasets
name_dataset_agouti: str = ''
name_dataset_deepsqueak: str = ''

name_data = 'data'

#location of dataset
location_data: str = 'amsterda'


#interval in seconds
INTERVAL_AGOUTI: int = 0
INTERVAL_DEEPSQUEAK: int = 0
INTERVAL_OVERLAP: int = 0


def main():
    #see if variables above can make this program work.
    paths_agouti = check(path_folder_agouti=path_folder_agouti, path_folder_deepsqueak=path_folder_deepsqueak)
    #check for flags/command line arguments
    flags()

    path_to_results = results_directories(name_data, INTERVAL_AGOUTI, INTERVAL_DEEPSQUEAK, INTERVAL_OVERLAP)
    #move data into folder
    move(path_folder_agouti, 'agouti', name_dataset_agouti)
    move(path_folder_deepsqueak, 'deepsqueak', name_dataset_agouti)
    #move(path_folder_deepsqueak, 'deepsqueak', name_dataset_deepsqueak)
    
    #run program
    filtered_dataframe: Dataframe = filter_data_agouti(path_observations=paths_agouti[2], path_media=paths_agouti[0], path_deployments=paths_agouti[1], location_dataset=location_data, path_results=path_to_results)
    runtime_agouti: Dataframe = total_runningtime(path_deployments=paths_agouti[1], location_dataset=location_data, path_results=path_to_results)
    agouti_data: dict[str, pd.DataFrame] = agoutidata_to_dict(filtered_dataframe)

    
    #deepsqueak
    runtime_deepsqueak: Dataframe = runtime(path_folder=path_folder_deepsqueak, path_results=path_to_results)
    files_per_location: dict[str, list[str]] = deepsquakfiledata_to_dict(path_folder=path_folder_deepsqueak)

    agou_times = runtime_deepsqueak.df['runtime (sec)'].tolist() #all timestamps in a list.
    total = 0
    for i in agou_times:
        total += float(i)
    print(total)
    #USE ALL DATA (between 2021/09 - 2021/12 = season )

    #Get all dates betweeen 2021/09/01 and 2021/12/31
    
    all_dates = dates_study(runtime_agouti, runtime_deepsqueak, path_to_results)

    
    #agouti dates
    dates_agouti = agouti_dates(runtime_agouti)
    dates_deepsqueak = deepsqueak_dates(runtime_deepsqueak)
    
    #all_dates = all_deepsqueak_dates(runtime_deepsqueak)


    dates_dates = all_deepsqueak_dates_list(runtime_deepsqueak)
    #matchingdates
    #dates = matching_dates(runtime_agouti, runtime_deepsqueak, path_to_results)

    #filesmatchingdates
    locatoin_rows_agouti = agouti_rows(all_dates, agouti_data)
    location_files_deepsqueak = deepsqueak_files(all_dates, files_per_location)

    #hits
    observations_deepsqueak = deepsqueak_observations(location_files_deepsqueak, INTERVAL_DEEPSQUEAK, path_to_results)
    observations_agouti = agouti_observations(locatoin_rows_agouti, INTERVAL_AGOUTI, path_to_results)


    #total_occu_agouti = occupancy_matrix_agouti_test(all_dates, dates_dates, observations_agouti, path_to_results, dates_agouti)
    #total_occu_deepsqueak = occupancy_matrix_deepsqueak_test(all_dates, dates_dates, observations_deepsqueak, path_to_results, dates_deepsqueak)

    total_occu_agouti = occupancy_matrix_agouti(all_dates, observations_agouti, path_to_results, dates_agouti)
    total_occu_deepsqueak = occupancy_matrix_deepsqueak(all_dates, observations_deepsqueak, path_to_results, dates_deepsqueak)
    #split total time period up into lenght of all_dates -> note for the day which locations had an observation
    hour_day(observations_agouti, observations_deepsqueak, path_to_results)

    #overlaps
    chances(observations_deepsqueak, observations_agouti, INTERVAL_OVERLAP, path_to_results)

    #print(f"total dates occupied agouti: {total_occu_agouti}")
    #print(f"total dates occupied deepsqueak: {total_occu_deepsqueak}")
    #split total time period up into lenght of all_dates -> note for the day which locations had an observation


if __name__ == '__main__':
    main()
