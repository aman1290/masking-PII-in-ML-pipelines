import pandas as pd

filepath ="C:/Users/anand/Desktop/dps_poject/masking-PII-in-ML-pipelines/data/raw_data.csv"
def load_data(filepath):
    return pd.read_csv(filepath)
