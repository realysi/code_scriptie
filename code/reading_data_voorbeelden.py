import pandas as pd

"""
This file imports the csv data and turns it into panda dataframes.
"""

link_audio_voorbeelden = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Voorbeeld_data_audio.csv"
link_video_voorbeelden = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Voorbeeld_data_video.csv"

def read_data(relative_path: str) -> pd.DataFrame:
    data_df = pd.read_csv(relative_path, delimiter=";")
    return data_df


