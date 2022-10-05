# 2D Video Based Exercise Classification 

## Overview

This project aims to create an exercise detection algorithm that only requires 2D video of an individual performing the exercise. The algorithm combines elements of coordinate-based, velocity-based, and probabilistic approaches through a data-driven model. A time series model is created, using coordinate- and velocity-based features to predict the likelihood of an exercise being performed.

## Background and Motivation

Current computational methods as well as large publicly available datasets enable pose estimation algorithms such as OpenPose, PoseNet and UniPose to produce estimates of body posture from standard video across varying lighting, activity, age, skin color, and angleof-view.  Pose estimation software outputs estimates of the two-dimensional (2D) image-plane positions of joints (e.g., hips and knees) and other anatomical locations in each frame of a video. These estimates of 2D planar projections can be too noisy or biased.  The accumulated errors cannot be used to extract any sort of useful information when compared to 3D metrics.

The motivation for this project is to overcome these limitations, by using a few machine learning models to learn complex relationships between keypoints and joint angles when performing particular movement patterns.  Given the robustness of the dataset, this strategy should be capable of handling video shot an various angles. The method used capitalizes on 2D pose estimates from video to return a prediction on the type of movement pattern being performed and ultimately classify the pattern into one of the exercise categories.

## Goals

1. Develop a working model
2. Deploy a web application for video upload
3. Configure a mobile application to allow for real-time exercise classifaction
4. Expand exercise suite to allow for more exercises to be recognized 

## Datasets

This project used publicly available video footage of numerous individuals performing 5 common exercises. The datasets are available in their [raw](https://drive.google.com/drive/folders/1A9l2agr-vH47Ka-0sNSCWGHg8ZNNzUwJ?usp=sharing) and [processes](https://drive.google.com/drive/folders/1s-H1MJ2RzYzeVfOQikYDZ_T20dsnMDQ8?usp=sharing) formats. Some classes are underrepresented in their representation (e.g., not covering all camera angles). The dataset consists of atleast 25 videos of individuals performing the following 5 common exercises: 

- Burpees
- Squats
- Jumping Jacks
- Mountain Climbers
- Pushups

![exercises_collage](https://user-images.githubusercontent.com/63820705/188683690-c37e7862-db58-4479-86cb-d55682443a7b.jpg)

Sample Video: https://user-images.githubusercontent.com/63820705/188673997-b3b7a8e2-262f-4f95-b7c0-1bd07913e641.mp4



https://user-images.githubusercontent.com/63820705/194172708-5e1c203d-14f0-46bc-b9c3-a511979fce3c.mp4



## Practical and Potential Applications

- Could be extended to suggest other exercies based on range of movement and ultimately promote exercise variety
- Could be extended to add a repetition counter to aid indvidual with counting reps
- Could be extended to aid individuals in fixing their form while performing repetitions
- Could be extended for exercise monitoring to help in goal setting and preparing individualized plans
- Could be extended to be an accountability partner to help maintain workout routine
  
## Milestones

### :white_check_mark: Phase 1 :
Develop pre-processing pipeline and model that can take a video of the correct format as input and output a prediction

### :white_square_button: Phase 2 :
Create a web app that allows users to upload or record relevant videos for classification

### :white_square_button: Phase 3 : 
Configure a mobile application to allow for real-time exercise classifaction

### :white_square_button: Phase 4 :
Expand exercise suite to allow for more exercises to be recognized 

## Reference

- [Computer Vision and Pose Estimation - Paper #1](https://arxiv.org/pdf/2005.03194.pdf)
- [Computer Vision and Pose Estimation - Paper #2](https://www.researchgate.net/publication/333625301_Workout_Type_Recognition_and_Repetition_Counting_with_CNNs_from_3D_Acceleration_Sensed_on_the_Chest)
- [Computer Vision and Pose Estimation - Paper #3](https://eprints.leedsbeckett.ac.uk/id/eprint/5932/1/AutomaticRecognitionofPhysicalExercisesPerformedbyStrokeSurvivorstoImproveRemoteRehabilitationAM-MONEKOSSO.pdf)

