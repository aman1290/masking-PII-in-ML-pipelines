
import pandas as pd
import hashlib

def hash_string(value):
    return hashlib.sha256(str(value).encode()).hexdigest()

def mask_pii(df, columns_to_mask):   # ✅ Add 'columns_to_mask' parameter
    df_copy = df.copy()
    for col in columns_to_mask:
        df_copy[col] = df_copy[col].apply(hash_string)
    return df_copy
