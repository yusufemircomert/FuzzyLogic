# Comparative Analysis of Rule-Based (FIS) and Adaptive Neuro-Fuzzy (ANFIS) Approaches for Academic Performance Prediction

**Hacettepe University - Department of AI Engineering**
**Term Project Report**

This project conducts a comparative analysis of two distinct Fuzzy Logic methodologies to predict student academic performance (Grades). It evaluates the performance of a human-driven **Rule-Based Fuzzy Inference System (FIS)** against a data-driven **Adaptive Neuro-Fuzzy Inference System (ANFIS)** architecture.

## 🚀 Project Summary & Results

The study utilizes the `academicPerformanceData.xlsx` dataset. The comparative results are as follows:

| Method | Architecture Type | Accuracy | Description |
| :--- | :--- | :--- | :--- |
| **Method A** | Rule-Based FIS (Mamdani) | **~58.0%** | Static rules failed to distinguish overlapping intermediate grades effectively. |
| **Method B** | ANFIS (Sugeno - PyTorch) | **95.46%** | Successfully learned non-linear boundaries by optimizing Gaussian membership functions. |

---

This directory contains the source code, datasets, and analysis notebooks required to reproduce the study.

```text
FuzzyLogic/
├── academicPerformanceData.xlsx    # Original dataset source provided by the instructor
├── requirements.txt                # List of Python dependencies
├── README.md                       # Project documentation
│
├── data_analysis.ipynb             # Step 1: Exploratory Data Analysis (EDA), Heatmaps, PCA & t-SNE
│
├── fis_data_creator.py             # Data Prep: Splits original data into balanced subsets for FIS testing
├── Method_A_FIS.ipynb              # Step 2: Implementation of Rule-Based FIS (Mamdani)
│
├── anfis_data_creator.py           # Data Augmentation: Generates synthetic data (50k samples) for Deep Learning
├── Method_B_ANFIS.ipynb            # Step 3: ANFIS Model Training & Testing (Custom PyTorch Implementation)
│
└── comparison_with_ml.ipynb        # Benchmarking: Decision Tree & Random Forest implementation for comparison
```

## 🛠️ Installation & Setup

To run this project locally, ensure you have Python installed. Follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/yusufemircomert/FuzzyLogic.git
cd FuzzyLogic
```
### 2. Create a Virtual Environment (Optional but Recommended)
It is best practice to use a virtual environment to avoid conflicts.
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
This project relies on specific versions of libraries like torch, scikit-fuzzy, and pandas. Install them using the provided requirements.txt file:
```bash
pip install -r requirements.txt
```

**Content of `requirements.txt`:**
* `torch`: For building the custom ANFIS neural network layers.
* `scikit-fuzzy`: For the Rule-Based logic in Method A.
* `scikit-learn`: For metrics, PCA, t-SNE, and Benchmark ML models.
* `pandas` & `numpy`: For data manipulation.
* `matplotlib` & `seaborn`: For visualization.

---

## ▶️ Execution Guide (Step-by-Step)

For the correct reproduction of the report results, please execute the files in the following order:

### 1️⃣ Exploratory Data Analysis
* **File:** `data_analysis.ipynb`
* **Description:** Visualizes the dataset using Correlation Matrices, Box Plots, and t-SNE. It establishes the "non-linear separability" argument used in the report.

### 2️⃣ Method A: Rule-Based FIS
* **Pre-requisite:** Run `python fis_data_creator.py` to generate test subsets.
* **File:** `Method_A_FIS.ipynb`
* **Description:** Implements a Mamdani-type system with manual rules (e.g., *If Exam is High, then Grade is 5*).
* **Goal:** To demonstrate the limitations of static expert systems.

### 3️⃣ Dataset Expansion (Upsampling for ANFIS) ⚠️
* **File:** `anfis_data_creator.py`
* **Description:** The ANFIS neural network architecture requires a large number of iterations to converge properly. Since the original dataset is small, this script expands the dataset to 50,000 samples using **stratified sampling with replacement (bootstrapping)**. This ensures the model learns the underlying probability distribution without overfitting to a small sample size.
* **Command:**
    ```bash
    python anfis_data_creator.py
    ```
* *Note: This will create `anfis_train_*.csv` files required for the next step.*


### 4️⃣ Method B: ANFIS Training
* **File:** `Method_B_ANFIS.ipynb`
* **Description:** Loads the synthetic data and trains the custom 5-layer ANFIS architecture.
* **Output:** Generates Loss Curves, Learned Membership Function plots, and the final Confusion Matrix.

### 5️⃣ Benchmarking (ML Comparison)
* **File:** `comparison_with_ml.ipynb`
* **Description:** Trains Decision Tree and Random Forest classifiers on the same dataset to provide a baseline comparison against the Fuzzy Logic approaches.

---

## 🧠 Technical Architecture

### Method A: FIS (Mamdani)
* **Fuzzification:** Input variables are mapped to fuzzy sets (Low, Medium, High).
* **Inference:** Uses weighted rules. The 'Final Exam' feature is assigned a higher weight (6.0) based on correlation analysis.
* **Defuzzification:** Centroid method.

### Method B: ANFIS (Sugeno)
* **Framework:** PyTorch (Custom `nn.Module`).
* **Layers:**
    1.  **Fuzzification Layer:** Learnable Gaussian Bell functions.
    2.  **Rule Layer:** Product of membership degrees.
    3.  **Normalization Layer:** Normalizes firing strengths.
    4.  **Consequent Layer:** Computes linear output parameters.
    5.  **Aggregation:** Sum of weighted outputs.
* **Optimizer:** Adam Optimizer (Learning Rate: 0.01).

---

## 👨‍💻 Author

**Yusuf Emir Cömert**
* **Institution:** Hacettepe University
* **Department:** Artificial Intelligence Engineering
* **GitHub:** [yusufemircomert](https://github.com/yusufemircomert)

---
