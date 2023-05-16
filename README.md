# Scriptie program

15 mei: timestamps overlap flevopark gevonden, data mangement, literatuur 

# agouti.py
## data structure
This file processes the data received by the agouti (neural network). The agouti software scans wildlifecamera images for sightings of animals, and labels these. It returns three csv files containing usable information: observations.csv, media.csv and deployments.csv. All three data sheets contain usefull information for this program, which this program links together. Observations.csv contains the columns scientificName and timestamp. scientificName says which animal was spotted and timestamps says at what time (to the exact second). Media.csv contains the column fileName, which displays the filename of the picture from which this information was taken. In the filename, the ID of the camera is inbedded. Deployments.csv contains the columns longitude, latitude, locationName and cameraID. The locationname is for the flevopark data the same as its ID. 

The three datasheets are linked with one another by certain IDs. The media and observation sheets are linked with one another by the sequenceID. When the cameretrap gets triggered, it takes a burst (around 5 photos) of images. From this burst, agouti takes one of those pictures and labels it as an observation. Therefore every observation has its own sequenceID. In media.csv the data is stored of all those burst photos, which share the same sequenceID as the observation. This way the data of observations.csv can be linked to the data of media.csv. 

Both media- and observation.csv are linked to deployments.csv by the deploymentID. When a cameratrap gets placed, it gets its own deploymentID. So untill that camera's battery is empty, all pictures taken with that camera share the same deploymentID.

How the data is organized:
![image](https://github.com/realysi/code_scriptie/assets/116087413/1f5c99b4-ff34-4c38-bf8e-1c82df6b1d10)

How the data sheets are linked to one another:
<img width="495" alt="Screenshot 2023-05-16 at 12 48 09" src="https://github.com/realysi/code_scriptie/assets/116087413/272e9515-e832-4691-8020-67c23ae91b43">

## data processing
1. Filter observations.csv
Frist the observation data gets filtered by only keeping the deploymentID, sequenceID, scientificName and timestamp columns. Then only the rows were the cellvalue of scientificName equeal 'Rattus norvegicus' are kept. Then the columns 'UTC' and 'epoch' are added, which are convertred from the timestamps. The timesettings of the camera's in the flevopark were UTC + 1, and those of Artis in the summer UTC + 2 and in the winter UTC + 1. The table that was filtered with pandas, gets written to a csv file to store.

2. Link deployments.csv and filtered observations.csv data.
The data of deployments.csv and the filtered oberservations.csv gets linked by using the deploymentIDs, which are present in both datafiles. The columns longitude, latitude, locationName and cameraID (only present in artis datafiles) get added to the filtered observation data. This table also gets written to a csv file to store.

3. link media.csv to filtered data (observations & deployments).
The data of media.csv and the filtered data gets linked by using the sequenceIDs, which are present in both datafiles. The column fileName gets added to the filtered observation data. This table also gets written to a csv file to store.

4. The proccessed data is saved in a dictionary
The data of the above steps gets saved in a dictionary by {locationName (flevopark_1): pd.Dataframe with that locationName}. This is done because the deepsqueak data will also be stored in a dictionary, which makes comparing the two data sets a bit more structured.

# deepsqueak.py
## data structure

The deepsqueak software analyses .flac files for sound made by the Rattus norvegicus. The software returns a .mat file which contains three sheets; audiodata, Calls and detection_metadeta. The audiodata sheet contains information about the folowing; Filename, CompresiionM..., NumChannels, SampleRate, TotalSamples, Duraiton, Titile, Comment, Arits (type audiotrap) and BitsPerSample. None of this information is used in this program. The Calls data sheet contains the following information; how many seconds since the start of the recording a 'detectable sound' was made, the lowest frequency of that soundwave, the duration of the sound, the delta of the frequency (lowest + delta = highest), confidence score given by deepsqueak, type and accept. The detection_metadata datasheet contains seeints, start detectiontime, networkselections. The netwerkselection is which neural network has graded the audio data. 

<img width="812" alt="Screenshot 2023-05-08 at 18 50 38" src="https://github.com/realysi/code_scriptie/assets/116087413/fbf641b7-57b5-46d2-ba93-622bd60885d4">

<img width="550" alt="Screenshot 2023-05-08 at 18 51 22" src="https://github.com/realysi/code_scriptie/assets/116087413/8b4c97fa-3a8a-4dca-8ec9-98fdbfc5b739">

<img width="561" alt="Screenshot 2023-05-08 at 18 51 39" src="https://github.com/realysi/code_scriptie/assets/116087413/d969bff9-fa6c-4e7a-b45b-29a94deb4295">

<img width="418" alt="Screenshot 2023-05-08 at 18 52 21" src="https://github.com/realysi/code_scriptie/assets/116087413/40222db6-ba5a-451f-aa4a-aceac957c4cc">
