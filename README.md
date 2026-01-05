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

## 🛠️ Installation

Follow these steps to set up the project in your local environment.

### 1. Clone the Repository
```bash
git clone [https://github.com/yusufemircomert/FuzzyLogic.git](https://github.com/yusufemircomert/FuzzyLogic.git)
cd FuzzyLogic
