# 2D Video Based Exercise Classification → **PoseLab**

> **Thanks for all the stars!** This project has evolved into **PoseLab**, a complete toolkit for pose-based exercise analysis.

---

## 🎮 Try the Free Demo Now

**Run in your browser, right now:**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JRKagumba/2D-video-based-exercise-classification/blob/main/PoseLab_Demo.ipynb)

**What you'll see:**
- Upload any exercise video
- Get instant ROM (Range of Motion) analysis
- Beautiful "ROM Dials" visualization
- Joint angle time-series plots

**No setup, no GPU, just click and run!**

---

## 📦 Get the Full Experience

The demo shows you **the magic**. The **Starter Pack** gives you **everything**.

### 🚀 PoseLab Starter Pack - $20

**Included:**
- ✅ **Full dataset**: 137 processed videos (5 exercises)
- ✅ **Complete codebase**: Modern demo + original research pipeline
- ✅ **Pre-trained models**: 86% accurate XGBoost classifiers
- ✅ **Ready-to-use**: Load and predict immediately
- ✅ **Documentation**: Step-by-step guides

**[👉 Get it on Gumroad](https://kagumba.gumroad.com/l/xksdm)**

Perfect for:
- **Students** learning pose analysis
- **Researchers** needing motion data
- **Developers** building fitness apps

---

## 🔬 The Science (Why It Works)

### The Problem
2D pose estimation from video is noisy. Traditional approaches try to reconstruct 3D depth, but "the accumulated errors cannot be used to extract any sort of useful information when compared to 3D metrics."

### The Solution
**Don't solve 3D reconstruction. Learn movement patterns.**

This project sidesteps the noise problem entirely:

1. **Extract joint angles** from 2D keypoints
2. **Calculate temporal features** (amplitude, speed, variance)
3. **Train XGBoost** on these **domain-specific features**

Result: Models robust to 2D camera noise because they learn **how joints move together over time**, not absolute 3D positions.

### The Models
- **8 joint-specific classifiers**: One for each major joint (L/R Elbow, Shoulder, Hip, Knee)
- **Ensemble accuracy**: 86% on test set
- **Input**: Joint angle time-series features
- **Output**: Exercise class (Burpees, Squats, Pushups, Jumping Jacks, Mountain Climbers)

---

## 📁 Repository Structure

```
├── PoseLab_Demo.ipynb          # ← START HERE: Modern demo (MediaPipe)
├── _archive/
│   └── legacy_xgb_pipeline/    # Original research pipeline
├── models/
│   └── xgb/                    # Pre-trained models
└── README.md                   # You are here
```

---

## 🎯 Use Cases

- **Form analysis**: Compare your ROM to optimal patterns
- **Exercise classification**: Auto-detect workout type
- **Progress tracking**: Measure ROM over time
- **Research**: Motion analysis dataset

---

## 🤝 License & Attribution

See LICENSE.txt in Starter Pack for details.

**Academic use encouraged!** Cite:
```
Kagumba, J. (2023). PoseLab: 2D Video Based Exercise Classification 
[Dataset/Models]. GitHub Repository.
```

---

## 💬 Keep In Touch

- **Issues**: Report bugs, request features
- **Discussions**: Ask questions, share projects
- **Gumroad**: Get the Starter Pack

**Made with ❤️ for the biomechanics community.**
