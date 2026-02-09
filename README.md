# AI & Data Science Portfolio: Technical Capstones
**Jonathon Miles** | *Purdue University Post-Graduate Program*

This repository contains a curated collection of AI and Machine Learning projects, ranging from safety-critical Computer Vision to high-dimensional marketing analytics. These projects demonstrate a "full-stack" approach to AI: data engineering, model architecture, training, and deployment.

---

## 📂 Project Directory

### 🏎️ 1. Computer Vision & Safety
**Project:** [Automated Driving Object Detection](./Automated_Driving_IDs.ipynb)
* **Goal:** Detect and classify 5 vehicle classes in real-world driving environments.
* **Tech:** YOLOv8 (Ultralytics), PyTorch, Transfer Learning.
* **Results:** Achieved **0.431 mAP50**; implemented custom hyperparameter tuning to overcome significant class imbalance (specifically the "Bus" class).

### 🎬 2. Sequential Modeling & Motion
**Project:** [Hybrid Video Classification](./Video_Classification.ipynb)
* **Goal:** Classify temporal actions in video sequences using a custom deep learning pipeline.
* **Tech:** PyTorch, InceptionV3 (Feature Extraction), Bidirectional GRU, Multi-head Attention, OpenCV.
* **Results:** Developed a robust sampling pipeline for high-dimensional video data, utilizing attention mechanisms to focus on key frames for classification accuracy.

### 💳 3. Unsupervised Learning & Marketing Strategy
**Project:** [Strategic Customer Segmentation](./Credit_Card_Strategic_Marketing.ipynb)
* **Goal:** Group 8,900+ credit card users into behavioral personas to drive targeted marketing spend.
* **Tech:** Scikit-Learn, K-Means Clustering, PCA (Dimensionality Reduction), Seaborn.
* **Results:** Successfully reduced feature dimensionality through PCA and utilized the "Elbow Method" to identify 4 distinct customer personas for high-ROI campaign targeting.

### 🏠 4. Deep Learning & Financial Risk
**Project:** [Home Lending Neural Network](./Home_Lending_Data_Analysis.ipynb)
* **Goal:** Predict loan default risk using large-scale tabular data (300,000+ records).
* **Tech:** TensorFlow, Keras, MLP (Multi-Layer Perceptron), AdamW.
* **Results:** Optimized an MLP architecture with Dropout layers to prevent overfitting; tuned classification thresholds to maximize **F1-Score** for imbalanced risk classes.

---

## 🛠️ Technical Toolkit
* **Languages:** Python (Pandas, NumPy, Scikit-Learn), SQL
* **Deep Learning:** PyTorch, TensorFlow, Keras, YOLOv8
* **Specialized Libraries:** OpenCV (Video/Image), Matplotlib/Seaborn (Visualization), Ultralytics
* **Concepts:** CNNs, RNNs/GRUs, Attention Mechanisms, Feature Engineering, Hyperparameter Optimization

---

## 🚀 How to Use This Repo
1. **Explore the Notebooks:** Each `.ipynb` file contains the full end-to-end pipeline from data cleaning to evaluation.
2. **Requirements:** To replicate the environments, ensure you have the libraries installed:
   ```bash
   pip install torch torchvision ultralytics tensorflow pandas numpy scikit-learn opencv-python seaborn
