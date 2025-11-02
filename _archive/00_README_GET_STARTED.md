# PoseLab Starter Pack

Welcome! This Starter Pack contains everything you need to dive deep into pose-based exercise analysis.

---

## 📦 What's Inside

### 🎮 **New Demo** (Start Here!)
**`PoseLab_Demo.ipynb`** - Modern, fast demo using MediaPipe.
- Runs in your browser (Google Colab)
- No GPU needed
- See ROM dials instantly
- Upload any video and get instant analysis

### 🔬 **Legacy Pipeline**
**`legacy_xgb_pipeline/`** - Original OpenPose + XGBoost approach.
- Full training pipeline (00-03 notebooks)
- 86% accuracy models
- Feature engineering with cesium library
- Complete preprocessing workflow

### 📊 **Your Data Asset**
**`data/`** - 100+ processed videos across 5 exercises.
- Keypoint trajectories (X, Y coordinates)
- Joint angle time-series
- Ready for your analysis
- Organized by exercise type:
  - Burpees
  - Squats
  - Pushups
  - Jumping Jacks
  - Mountain Climbers

### 🤖 **Trained Models**
**`models/xgb/`** - 8 pre-trained XGBoost classifiers.
- One model per joint (L/R Elbow, Shoulder, Hip, Knee)
- Load and predict immediately
- JSON and pickle formats

---

## 🚀 Quick Start Guide

### Option 1: Try the Modern Demo (Recommended First!)

1. **Open Google Colab**: Go to [colab.research.google.com](https://colab.research.google.com)
2. **Upload** `PoseLab_Demo.ipynb`
3. **Run all cells** → See your ROM analysis in minutes!

### Option 2: Explore the Legacy Pipeline

1. **Open** `legacy_xgb_pipeline/00_Apply_OpenPose_to_Raw_Video.ipynb`
2. **Run through sequentially**: 00 → 01 → 02 → 03
3. **Train models**: Use your own data or ours

### Option 3: Use Pre-trained Models

```python
import pickle
import pandas as pd

# Load a model
with open('models/xgb/L_ELB_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load your joint angle data
df = pd.read_csv('data/squats/squats_01_joint_angles.csv')

# Predict
# (You'll need to extract features first - see 03_XGB notebook)
```

---

## 🔬 The Science Behind It

### The Challenge
2D pose estimation from video is inherently noisy. Traditional 3D reconstruction methods fail because "the accumulated errors cannot be used to extract any sort of useful information when compared to 3D metrics."

### The Innovation
**Don't solve 3D. Learn movement patterns.**

This approach calculates **temporal features** from joint angles:
- **Amplitude**: Range of motion
- **Max slope**: Speed of movement
- **Median absolute deviation**: Consistency
- **Skewness**: Asymmetry
- **Weighted average**: Overall pattern
- And 6 more features...

### Why It Works
The XGBoost models don't try to guess 3D positions. Instead, they learn **how joints move together over time**. This makes them robust to:
- Camera angle variations
- Lighting conditions
- 2D projection noise
- Individual body differences

**Result**: 86% accuracy across 5 exercise types!

---

## 📂 Directory Structure

```
PoseLab_Starter_Pack/
│
├── README.md                           # This file
├── LICENSE.txt                         # License information
│
├── PoseLab_Demo.ipynb                  # 🎮 NEW: Modern demo (MediaPipe)
│
├── legacy_xgb_pipeline/                # 🔬 Original research code
│   ├── 00_Apply_OpenPose_to_Raw_Video.ipynb
│   ├── 00_apply_openpose_to_raw_video.py
│   ├── 01_Apply_Preprocessing_steps.ipynb
│   ├── 01_apply_preprocessing_steps_to_raw_data_and_save_plots.py
│   ├── 02_Calculate_Joint_Angles.ipynb
│   ├── 02_calculate_joint_angles.py
│   ├── 03_XGB_Feature_Generation_and_Model_Creation.ipynb
│   ├── 03_xgb_feature_generation_and_model_creation.py
│   ├── 03_XGB_Model_Testing.ipynb
│   └── 03_xgb_model_testing.py
│
├── models/
│   └── xgb/                            # 🤖 Pre-trained models
│       ├── L_ELB_model.json
│       ├── L_ELB_model.pkl
│       ├── R_ELB_model.json
│       ├── R_ELB_model.pkl
│       ├── L_SHO_model.json
│       ├── L_SHO_model.pkl
│       ├── R_SHO_model.json
│       ├── R_SHO_model.pkl
│       ├── L_HIP_model.json
│       ├── L_HIP_model.pkl
│       ├── R_HIP_model.json
│       ├── R_HIP_model.pkl
│       ├── L_KNE_model.json
│       ├── L_KNE_model.pkl
│       ├── R_KNE_model.json
│       └── R_KNE_model.pkl
│
└── data/                               # 📊 Your processed dataset
    ├── burpees/
    │   ├── burpees_01_joint_angles.csv
    │   ├── burpees_02_joint_angles.csv
    │   └── ...
    ├── squats/
    ├── pushups/
    ├── jumping_jacks/
    └── mountain_climbers/
```

---

## 💡 Next Steps

### Build Your Own Classifier
1. Load data from `data/` folder
2. Follow `legacy_xgb_pipeline/03_XGB_Feature_Generation.ipynb`
3. Extract features using cesium
4. Train XGBoost models
5. Evaluate accuracy

### Add New Exercises
1. Record videos of new exercises
2. Run through 00-02 pipeline
3. Generate joint angle data
4. Add to your training set
5. Retrain models

### Create Custom Visualizations
1. Use joint angle data from `data/`
2. Create your own ROM plots
3. Compare exercises
4. Analyze movement patterns

### Use in Research
- Cite the methodology
- Reference the dataset
- Build on the approach
- Contribute back!

---

## 🐛 Troubleshooting

### "Module not found" errors
```bash
pip install pandas numpy matplotlib scipy cesium xgboost opencv-python mediapipe
```

### Running OpenPose locally
The legacy pipeline uses OpenPose. For local setup:
1. Install CMake, CUDA, cuDNN
2. Clone OpenPose repository
3. Build from source
4. Or use the GPU-enabled Google Colab version

### Model loading issues
Models are in both JSON and pickle formats. Use:
```python
import pickle
model = pickle.load(open('model.pkl', 'rb'))
```

---

## 📚 Additional Resources

### Papers Referenced
- [Computer Vision and Pose Estimation - Paper #1](https://arxiv.org/pdf/2005.03194.pdf)
- [Workout Type Recognition and Repetition Counting](https://www.researchgate.net/publication/333625301_Workout_Type_Recognition_and_Repetition_Counting_with_CNNs_from_3D_Acceleration_Sensed_on_the_Chest)
- [Automatic Recognition of Physical Exercises](https://eprints.leedsbeckett.ac.uk/id/eprint/5932/1/AutomaticRecognitionofPhysicalExercisesPerformedbyStrokeSurvivorstoImproveRemoteRehabilitationAM-MONEKOSSO.pdf)

### Useful Links
- [MediaPipe Documentation](https://google.github.io/mediapipe/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Cesium Library](https://cesium-ml.org/)
- [OpenPose GitHub](https://github.com/CMU-Perceptual-Computing-Lab/openpose)

---

## 🤝 Support

**Need help?**
- Open an issue on GitHub
- Check existing discussions
- Read the code comments

**Found a bug?**
- Report it with steps to reproduce
- Include error messages
- Share your environment details

**Want to contribute?**
- Submit pull requests
- Improve documentation
- Add new features

---

## 📄 License

See LICENSE.txt for complete licensing information.

---

## 🙏 Acknowledgments

Thanks to everyone who has starred, forked, and contributed to this project!

**Special thanks:**
- CMU Perceptual Computing Lab (OpenPose)
- Google MediaPipe team
- The biomechanics research community

---

**Made with ❤️ for researchers, students, and developers pushing the boundaries of human motion analysis.**

*Happy analyzing!* 🎯

