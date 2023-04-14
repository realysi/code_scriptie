import datetime
from .reading_data_voorbeelden import read_data
import pandas as pd

def time_to_seconds(link_audio_data):
    audio_df: pd.DataFrame = read_data(link_audio_data)
    print(audio_df)
    for i in audio_df.index:
        time = audio_df.loc[i, "Tijd begin detectie"]
        hours, minutes, seconds = time.split(":")
        total_seconds = int(datetime.timedelta(hours=int(hours),minutes=int(minutes),seconds=int(seconds)).total_seconds())
        audio_df.loc[i, "Tijd begin detectie"] = total_seconds
    return audio_df

