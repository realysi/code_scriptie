from code.read_data import read_xlsx
from classes.dataframe_extension import Data
import datetime
import pandas as pd


agouti_data_xlsx = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/data_agouti.xlsx"
df_step_5 = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/temp_df.xlsx"
media_path = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/media.csv"
df_media = Data(pd.read_csv(media_path))
#now reads in all the data 3 times --> very slow
#can fix it by selecting out of library, but is less neat
#1: load in data into pandas df

if __name__ == "__main__":
    df = pd.read_excel(df_step_5)
    df = Data(df)
    """data: list[Dataframe] = read_xlsx(agouti_data_xlsx, ['media', 'observations', 'deployments'])
    df_media = data[0]
    df_observations = data[1]
    df_deployments = data[2]

    #2: filter observations on Rattus norvegicus
    df_observations.df = df_observations.select_rows_by_columnvalue(dataframe=df_observations.df, columnname='scientificName', columnvalue='Rattus norvegicus')
    #print(df_observations.df[['timestamp']].head(5).to_string(index=False))

    #3: Time to utc
    df_observations.df = df_observations.localized_time_to_utc(df_observations.df, columnname_timestamp="timestamp")
    #print(df_observations.df[['timestamp']].head(5).to_string(index=False))

    #4: Time to epoch
    df_observations.df = df_observations.to_epoch_time(df_observations.df, columnname_timestamp="timestamp")
    #print(df_observations.df[['timestamp']].head(5).to_string(index=False))

    #5: add 2 minute interval
    df_observations.df = df_observations.interval(df_observations.df, "timestamp", 2)
    #print(df_observations.df[['timestamp', 'min_2_interval', 'max_2_interval']].head(5).to_string(index=False))

    df_observations.df.to_excel("/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/temp_df.xlsx")"""

    #6: koppel media, observations via sequence code --> file name
    df.df = df.pair_observations_media(df.df, df_media.df, "sequenceID", "fileName")
    df.df.to_excel("/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/temp_df_2.xlsx")
    #print(df.df[['fileName']].head(5).to_string(index=False))


    #20220929114756-artis_18_wildlifecamera1_2022-08-19_02-45-12_(113).JPG
    # 20220707095303-ME-SY2103000168-SYFR0412.JPG


#24 april
"""eindelijk gelukt om de naam van de datafiles van de images te koppelen"""

#25 april
"""gelukt de namen in een dataframe op een goede plek in te voegen!!!"""

#26 april
"""
- matlab naar pandas dataframe geprobeerd via scipy.io, mat73, h5py
--> niet gelukt, dus via r geprobeerd.
"""