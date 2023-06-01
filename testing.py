from deepsqueak.data import info_per_location, total_runtime
from code.matchingdates import matching_dates
from code.files_matchingdates import deepsqueak_files, agouti_rows
from code.hits import deepsqueak_observations, agouti_observations
from code.overlaps import chances

path_deepsqueak = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/flevopark_csv'

runtime_agouti = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/agouti/runtime/runtime_flevopark.csv'
runtime_deepsqueak = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/deepsqueak/runtime_flevopark.csv'

path_deployments = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/deployments.csv'
path_media = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/media.csv'
path_observatoins = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/observations.csv'
#deepsqueak_files(runtime_agouti, runtime_deepsqueak, path_deepsqueak)

#agouti_rows(runtime_agouti, runtime_deepsqueak, '/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/agouti/final/data_flevopark.csv')
"""
observations_per_location_no_interval2(path_deepsqueak, 600)
deepsqueak_observations(runtime_agouti, runtime_deepsqueak, path_deepsqueak, 600)"""

#agouti_observations(runtime_agouti, runtime_deepsqueak, '/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/agouti/final/data_flevopark.csv', 10)
chances(path_media, path_observatoins, path_deployments, path_deepsqueak, 60, 60, 'flevopark')

"""eindelijk gelukt om de naam van de datafiles van de images te koppelen"""

#25 april
"""gelukt de namen in een dataframe op een goede plek in te voegen!!!"""

#26 april
"""
- matlab naar pandas dataframe geprobeerd via scipy.io, mat73, h5py
--> niet gelukt, dus via r geprobeerd.
"""