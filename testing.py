from code.deepsqueak.info_data import recordings, info_per_location, total_runtime, observations_per_location_no_interval
from code.overlaps import matching_dates
path_deepsqueak = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/flevopark_csv'

runtime_agouti = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/agouti/runtime/runtime_flevopark.csv'
runtime_deepsqueak = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/deepsqueak/runtime_flevopark.csv'
#running_time(path_deepsqueak, 'flevopark')
#info_per_location(path_deepsqueak, 'flevopark')
#observations_per_location(path_deepsqueak)
#df = recordings(path_deepsqueak, 'flevopark')
#total_runtime(df)
matching_dates(runtime_agouti, runtime_deepsqueak)
#observations_per_location_no_interval(path_deepsqueak, 60)


#24 april
"""eindelijk gelukt om de naam van de datafiles van de images te koppelen"""

#25 april
"""gelukt de namen in een dataframe op een goede plek in te voegen!!!"""

#26 april
"""
- matlab naar pandas dataframe geprobeerd via scipy.io, mat73, h5py
--> niet gelukt, dus via r geprobeerd.
"""