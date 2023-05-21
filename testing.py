from code.deepsqueak.info_data import recordings, info_per_location, total_runtime, observations_per_location_no_interval

path_deepsqueak = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/flevopark_csv'
#running_time(path_deepsqueak, 'flevopark')
#info_per_location(path_deepsqueak, 'flevopark')
#observations_per_location(path_deepsqueak)
#df = recordings(path_deepsqueak, 'flevopark')
#total_runtime(df)

observations_per_location_no_interval(path_deepsqueak, 60)


#24 april
"""eindelijk gelukt om de naam van de datafiles van de images te koppelen"""

#25 april
"""gelukt de namen in een dataframe op een goede plek in te voegen!!!"""

#26 april
"""
- matlab naar pandas dataframe geprobeerd via scipy.io, mat73, h5py
--> niet gelukt, dus via r geprobeerd.
"""