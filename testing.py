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
from interface import remove_results

import sys

deployments_csv = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Flevopark/deployments.csv'
media_csv = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Flevopark/media.csv'
observations_csv = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Flevopark/observations.csv'

deepsqueak_path_folder = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/flevopark_csv'

folder_results = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/data'



def main():
    location: str = input("location: ")
    interval: int = int(input("Interval (seconds): "))
    interval_camera_audio: int = int(input("Interval between audio and video (seconds): ")) 
    answer = input("want to remove results? Yes (y) or No(n)")
    if answer.lower() == 'y':
        remove_results(folder_results)
    #agouti
    filtered_dataframe: Dataframe = filter_data_agouti(observations_csv, media_csv, deployments_csv, location)
    runtime_agouti: Dataframe = total_runningtime(deployments_csv, location)
    agouti_data: dict[str, pd.DataFrame] = agoutidata_to_dict(filtered_dataframe)

    #deepsqueak
    runtime_deepsqueak: Dataframe = runtime(deepsqueak_path_folder, location)
    files_per_location: dict[str, list[str]] = deepsquakfiledata_to_dict(deepsqueak_path_folder)

    #matchingdates
    dates = matching_dates(runtime_agouti, runtime_deepsqueak)

    #filesmatchingdates
    locatoin_rows_agouti = agouti_rows(dates, agouti_data)
    location_files_deepsqueak = deepsqueak_files(dates, files_per_location)

    #hits
    observations_deepsqueak = deepsqueak_observations(location_files_deepsqueak, interval)
    observations_agouti = agouti_observations(locatoin_rows_agouti, interval)

    #overlaps
    chances(observations_deepsqueak, observations_agouti, interval_camera_audio )


if __name__ == '__main__':
    main()


"""eindelijk gelukt om de naam van de datafiles van de images te koppelen"""

#25 april
"""gelukt de namen in een dataframe op een goede plek in te voegen!!!"""

#26 april
"""
- matlab naar pandas dataframe geprobeerd via scipy.io, mat73, h5py
--> niet gelukt, dus via r geprobeerd.
"""