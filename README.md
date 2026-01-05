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

<div align="center">
  <img width="1006" height="921" alt="_- visual selection (2)" src="https://github.com/user-attachments/assets/306c22b4-adb5-4cc0-b45d-5d46d726ca92" />
</div>


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

To ensure all datasets are available for the notebooks, please execute the files in the following strict order:

### 1️⃣ Data Preparation (Run Scripts First)
Before running any analysis, generate the necessary training and testing subsets by executing the Python scripts.

* **Generate FIS Subsets:**
    ```bash
    python fis_data_creator.py
    ```
    * *Action:* Splits `academicPerformanceData.xlsx` into balanced subsets (`fis_subset_*.csv`) for Method A.

* **Generate ANFIS Datasets (Upsampling):**
    ```bash
    python anfis_data_creator.py
    ```
    * *Action:* Expands the dataset to 50,000 samples using stratified sampling (`anfis_train_*.csv`) to ensure convergence for the Neural Network in Method B.

---

### 2️⃣ Exploratory Data Analysis
* **File:** `data_analysis.ipynb`
* **Description:** Visualizes the raw dataset using Correlation Matrices, Box Plots, and t-SNE. It establishes the "non-linear separability" argument used in the report.

### 3️⃣ Method A: Rule-Based FIS
* **File:** `Method_A_FIS.ipynb`
* **Description:** Implements a Mamdani-type expert system. Uses the `fis_subset` data generated in Step 1.
* **Output:** ~58% Accuracy and Confusion Matrix.

### 4️⃣ Method B: ANFIS Training (Neuro-Fuzzy)
* **File:** `Method_B_ANFIS.ipynb`
* **Description:** Loads the synthetic data created in Step 1 and trains the custom 5-layer ANFIS architecture.
* **Output:** Generates Loss Curves, Learned Membership Function plots, and the final Confusion Matrix.

### 5️⃣ Benchmarking (ML Comparison)
* **File:** `comparison_with_ml.ipynb`
* **Description:** Trains Decision Tree and Random Forest classifiers to provide a baseline comparison against the Fuzzy Logic approaches.
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
