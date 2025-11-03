Due to the large size of the dataset, all data has been stored on Google Drive storage. To access, use the following links:

Raw Videos: 
 - https://drive.google.com/drive/folders/1A9l2agr-vH47Ka-0sNSCWGHg8ZNNzUwJ?usp=sharing

Processed Data and Videos:
 - https://drive.google.com/drive/folders/1s-H1MJ2RzYzeVfOQikYDZ_T20dsnMDQ8?usp=sharing
 
 Dataset contains 5 classes of common at home workouts:
 - Burpees
 - Jumping Jacks
 - Mountain Climbers
 - Pushups
 - Squats
 
 
Each class has at least 25 video clips. With each video clip being atleast 10 seconds. Each clip contains content of atleast 1 individual performing an exercise.
 
General Raw Data Structure
```
├── raw
│   ├── Burpees
│   │   ├── Burpees 01
│   │   │   ├── Raw Video
│   │   ├── ...
│   │   ├── Burpees 25+
│   ├── ...
│   ├── Squats
│   │   ├── ...
```

General Processed Data Structure
```
├── processed
│   ├── Burpees
│   │   ├── Burpees 01
│   │   │   ├── Raw csv
│   │   │   ├── Processed csv
│   │   │   ├── Processed video
│   │   ├── ...
│   │   ├── Burpees 25+
│   ├── ...
│   ├── Squats
│   │   ├── ...
```
