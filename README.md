# Claims Processing Automation

## 🚀 Overview
Automatically processes simple insurance claims and prioritizes complex ones for human review.

## 🧠 Features
- ML-based complexity classification using decision trees
- Modular architecture for preprocessing, extraction, classification, and routing
- Visual insights into claim complexity distribution
- GitHub-ready folder structure and codebase

## 🧱 Project Structure
- `main_pipeline.py` — Main script to run the end-to-end pipeline
- `preprocessing/` — Data cleaning and preparation
- `extraction/` — Feature extraction from the dataset
- `classification/` — ML training and model saving
- `decision_engine/` — Routing logic based on prediction
- `visualization/` — Plotting claim complexity insights
- `images/` — Stores saved plots

## ▶️ How to Run

1. Install dependencies:

    pip install -r requirements.txt

2. Run the pipeline:

    python main_pipeline.py

## 📊 Output
- Classification report printed to console
- Sample routing decisions for 5 claims
- Plots saved to `/images/`:
  - `complexity_distribution.png`
  - `claim_amount_vs_complexity.png`

## 📁 Dataset Used
insurance_claims.csv 

## ✅ Author
MUNNURU UMAKANTH
