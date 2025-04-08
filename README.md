
🔒 Masking PII in ML Pipelines
This project demonstrates how to safely train machine learning models on datasets containing Personally Identifiable Information (PII) like names and emails by masking (hashing) sensitive data before using it in the ML pipeline.

📌 Features
✅ Masks PII fields using SHA-256 hashing

✅ Clean modular Python structure

✅ End-to-end ML pipeline using Pandas & Scikit-learn

✅ Model training and evaluation

🖥️ Ready to extend with CLI or Streamlit interface



⚙️ How it Works
PII Masking
The pii_masker module hashes sensitive fields like Name and Email.

Preprocessing
Drops masked PII columns, encodes categorical variables (e.g., City).

Model Training
Uses RandomForestClassifier from Scikit-learn to predict the Purchased label.

Evaluation
Outputs model accuracy on the test data.



🧠 Why This Matters
This project is important for:

Data privacy & compliance (GDPR, HIPAA, etc.)

Building secure machine learning pipelines

Training models without exposing real identities

