# 2D Video Based Exercise Classification 

## Overview

This project aims to create an exercise detection algorithm that only requires 2D video of an individual performing the exercise. The algorithm combines elements of coordinate-based, velocity-based, and probabilistic approaches through a data-driven model. A time series model is created, using coordinate- and velocity-based features to predict the likelihood of an exercise being performed.

## Background and Motivation

Current computational methods as well as large publicly available datasets enable pose estimation algorithms such as OpenPose, PoseNet and UniPose to produce estimates of body posture from standard video across varying lighting, activity, age, skin color, and angleof-view.  Pose estimation software outputs estimates of the two-dimensional (2D) image-plane positions of joints (e.g., ankles and knees) and other anatomical locations in each frame of a video. These estimates of 2D planar projections are too noisy and biased, due to manually annotated ground truth and planar projection errors, to be used directly for extracting clinically meaningful information such as three-dimensional (3D) gait metrics.

To overcome these limitations, this project uses a few machine learning models to learn complex, and potentially nonlinear, relationships between inputs and outputs which have been shown to be an effective tool for making robust predictions. The method used capitalizes on 2D pose estimates from video to return a prediction on the type of movement pattern being performed and ultimately classify the pattern into one of the exercise categories.

## Goals

1. Develop a working model
2. Deploy a web application for video upload
3. Configure a mobile application to allow for real-time exercise classifaction
4. Expand exercise suite to allow for more exercises to be recognized 

## Datasets

This project used publicly available video footage of numerous individuals performing 5 common exercises. The datasets are available in their [raw](https://drive.google.com/drive/folders/1A9l2agr-vH47Ka-0sNSCWGHg8ZNNzUwJ?usp=sharing) and [processes](https://drive.google.com/drive/folders/1s-H1MJ2RzYzeVfOQikYDZ_T20dsnMDQ8?usp=sharing) formats. The dataset consists of atleast 25 videos of individuals performing the following 5 common exercises: 

- Burpees
- Squats
- Jumping Jacks
- Mountain Climbers
- Pushups

![exercises_collage](https://user-images.githubusercontent.com/63820705/188683690-c37e7862-db58-4479-86cb-d55682443a7b.jpg)

Sample Video: https://user-images.githubusercontent.com/63820705/188673997-b3b7a8e2-262f-4f95-b7c0-1bd07913e641.mp4

## Practical and Potential Applications

- Could be extended to suggest other exercies based on range of movement and ultimately promote exercise variety
- Could be extended to add a repetition counter to aid indvidual with counting reps
- Could be extended to aid individuals in fixing their form while performing repetitions
- Could be extended for exercise monitoring to help in goal setting and preparing individualized plans
- Could be extended to be an accountability partner to help maintain workout routine
  
## Milestones

## Reference
