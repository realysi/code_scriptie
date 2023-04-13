import pandas as pd

"""
This file imports the csv data and turns it into panda dataframes.
"""

link_audio_voorbeelden = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Voorbeeld_data_audio.csv"
link_video_voorbeelden = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Voorbeeld_data_video.csv"

def read_audio_data(relative_path_audio: str) -> pd.DataFrame:
    audio_df = pd.read_csv(relative_path_audio, delimiter=";")
    return audio_df

def read_video_data(relative_path_video: str) -> pd.DataFrame:
    video_df = pd.read_csv(relative_path_video, delimiter=";")
    return video_df


