# Predicting Hospital Readmissions in Diabetic Patients

## Introduction

Diabetes is a significant global health challenge requiring ongoing management to mitigate acute and long-term complications. This project aims to reduce hospital readmissions for diabetic patients, crucial for enhancing patient outcomes and minimizing healthcare system burdens.

## Problem Statement

Hospital readmissions among diabetic patients increase healthcare costs and indicate patient management issues. Specifically, readmissions within 30 days post-discharge are often preventable, underscoring the need for improved treatment plans. This project develops a predictive model to accurately forecast such events, facilitating targeted interventions for improved care and cost efficiency.

## Repository Structure

- `README.md`: Provides an overview of the project, including objectives, and contact information.

- `data/`:
  - `raw/`: Contains the original, unmodified datasets.
  - `interim/`: Houses intermediate data that has been transformed but not yet finalized.
  - `processed/`: Stores the final, processed datasets ready for analysis and modeling.
  - `data_pipeline_processing.py`: Includes functions for data processing such as encodings and scaling.

- `notebooks/`: 
  - `01-Exploratory_data_analysis.ipynb`
  - `02-Data_Manipulation-missing_values_and_outliers.ipynb`
  - `03-Data_Manipulation-handling_categoricals_and_scaling.ipynb`
  - `04-Model_Training_and_Evaluation.ipynb`
  - `00-Complete_ML_Pipeline_for_Diabetic_Readmission_Prediction.ipynb`: A comprehensive guide through the ML pipeline in one notebook.

- `poetry.lock` & `pyproject.toml`: These files manage project dependencies and ensure reproducibility through the Poetry dependency management tool.

## Getting Started

To explore the complete machine learning pipeline from data preprocessing to model evaluation in one go, check out the comprehensive notebook: [Complete ML Pipeline for Diabetic Readmission Prediction](notebooks/00-Complete_ML_Pipeline_for_Diabetic_Readmission_Prediction.ipynb). This notebook provides a step-by-step guide through the entire process, making it an excellent starting point for understanding the project's approach.

## Objectives

- **Predictive Model Development**: A two-tier binary classification system forecasts hospital readmissions.
- **Model Performance Enhancement**: Focus on AUC-ROC scores and recall to accurately detect early readmissions.
- **Impact Analysis**: Assess the model's role in reducing healthcare costs and improving patient care.
- **User-Friendly Solution**: Offer a step-by-step, notebook-based guide through the ML pipeline, demonstrating real-world challenge tackling.

## How to Contribute

Your feedback is highly appreciated! If you have suggestions or would like to contribute, please feel free to reach out:

- [Diego Leon](mailto:diego.leon07@outlook.com)

## Contact

For any questions or collaboration inquiries, please contact:

- [Diego Leon](mailto:diego.leon07@outlook.com)

