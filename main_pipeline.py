from preprocessing.preprocess import preprocess_claim_data
from extraction.extract_fields import extract_relevant_fields
from classification.complexity_model import train_complexity_model
from decision_engine.router import route_claim

# Load data
df = preprocess_claim_data("/content/insurance_claims.csv")

# Extract features
features_df = extract_relevant_fields(df)

# Train model
model = train_complexity_model(df)

# Route a few sample claims
for idx, row in features_df.head(5).iterrows():
    print(f"Claim {idx+1}: {route_claim(model, row.values)}")