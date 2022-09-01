Due to the large size of the data, all data has been stored on Google Drive storage. To access, use the following links:

Raw Videos: 
 - https://drive.google.com/drive/folders/15UjFBfslOEZuyPIMUAsSGkER2M6ijU5D?usp=sharing

Processed Data and Videos:
 - https://drive.google.com/drive/folders/1aMwJaAWk4UOqKriprPE-glR-ie6KSkDb?usp=sharing
 
 Dataset contains 6 classes of NFL football positions:
 - Defensive Back
 - Defensive Line
 - Offensive Line
 - Quarterback
 - Running Back
 - Wide Receiver
 
Each class has 20 video clips of atleast 4 seconds. Each clip contains content of players performing the 40 yard dash at a scouting combine.
 
General Raw Data Structure
```
├── raw
│   ├── Defensive Back
│   │   ├── Defensive Back 01
│   │   │   ├── Raw Video
│   │   ├── ...
│   │   ├── Defensive Back 20
│   ├── ...
│   ├── Wide Receivers
│   │   ├── ...
```

General Processed Data Structure
```
├── processed
│   ├── Defensive Back
│   │   ├── Defensive Back 01
│   │   │   ├── Raw csv
│   │   │   ├── Processed csv
│   │   │   ├── Processed video
│   │   ├── ...
│   │   ├── Defensive Back 20
│   ├── ...
│   ├── Wide Receivers
│   │   ├── ...
```
