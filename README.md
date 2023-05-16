# Scriptie program

15 mei: timestamps overlap flevopark gevonden, data mangement, literatuur 

# agouti.py
This file processes the data received by the agouti (neural network). The agouti software scans wildlifecamera images for sightings of animals, and labels these. It returns three csv files containing usable information: observations.csv, media.csv and deployments.csv. All three data sheets contain usefull information for this program, which this program links together. Observations.csv contains the columns scientificName and timestamp. scientificName says which animal was spotted and timestamps says at what time (to the exact second). Media.csv contains the column fileName, which displays the filename of the picture from which this information was taken. In the filename, the ID of the camera is inbedded. Deployments.csv contains the columns longitude, latitude, locationName and cameraID. The locationname is for the flevopark data the same as its ID. 

The three datasheets are linked with one another by certain IDs. The media and observation sheets are linked with one another by the sequenceID. When the cameretrap gets triggered, it takes a burst (around 5 photos) of images. From this burst, agouti takes one of those pictures and labels it as an observation. Therefore every observation has its own sequenceID. In media.csv the data is stored of all those burst photos, which share the same sequenceID as the observation. This way the data of observations.csv can be linked to the data of media.csv. 

Both media- and observation.csv are linked to deployments.csv by the deploymentID. When a cameratrap gets placed, it gets its own deploymentID. So untill that camera's battery is empty, all pictures taken with that camera share the same deploymentID.

pictures of the three csv files, with their data

![image](https://github.com/realysi/code_scriptie/assets/116087413/1f5c99b4-ff34-4c38-bf8e-1c82df6b1d10)

<img width="694" alt="Screenshot 2023-05-16 at 10 55 45" src="https://github.com/realysi/code_scriptie/assets/116087413/7e1bb8da-6649-459f-81b1-a0f849254560">
