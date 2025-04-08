import pandas as pd
from modules.PII_masker import mask_pii
from modules.model import train_model, evaluate_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def run_pipeline():
    # Load raw data
    df = pd.read_csv('data/raw_data.csv')

    # Mask sensitive columns
    df_masked = mask_pii(df, columns_to_mask=['Name', 'Email'])

    # Prepare features and target
    y = df_masked['Purchased']
    X = df_masked.drop(columns=['Name', 'Email', 'Purchased'])

    # Encode categorical variables
    if 'City' in X.columns:
        le = LabelEncoder()
        X['City'] = le.fit_transform(X['City'])

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train and evaluate model
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

if __name__ == '__main__':
    run_pipeline()
