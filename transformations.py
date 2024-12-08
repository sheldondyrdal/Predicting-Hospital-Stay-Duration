import pandas as pd
import numpy as np

def calculate_news_score(row):
    score = 0
    
    # Respirasjonsfrekvens 
    if row["respirasjonsfrekvens"] <= 8:
        score += 3
    elif row["respirasjonsfrekvens"] <= 11:
        score += 1
    elif row["respirasjonsfrekvens"] <= 20:
        score += 0
    elif row["respirasjonsfrekvens"] <= 24:
        score += 2
    else:
        score += 3
    
    # Blodtrykk
    if row["blodtrykk"] <= 90:
        score += 3
    elif row["blodtrykk"] <= 100:
        score += 2
    elif row["blodtrykk"] <= 110:
        score += 1
    elif row["blodtrykk"] <= 219:
        score += 0
    else:
        score += 3
    
    # Hjertefrekvens
    if row["hjertefrekvens"] <= 40:
        score += 3
    elif row["hjertefrekvens"] <= 50:
        score += 1
    elif row["hjertefrekvens"] <= 90:
        score += 0
    elif row["hjertefrekvens"] <= 110:
        score += 1
    elif row["hjertefrekvens"] <= 130:
        score += 2
    else:
        score += 3
    
    # Kroppstemperatur
    if row["kroppstemperatur"] <= 35.0:
        score += 3
    elif row["kroppstemperatur"] <= 36.0:
        score += 1
    elif row["kroppstemperatur"] <= 38.0:
        score += 0
    elif row["kroppstemperatur"] <= 39.0:
        score += 1
    else:
        score += 2
    
    return score

def apply_news_score(X_org):
    X = X_org.copy()
    X["NEWS_score"] = X.apply(calculate_news_score, axis=1)
    return X

def categorize_values(X_org):
    X = X_org.copy()
    X.loc[:, "respirasjonsfrekvens_range"] = pd.cut(X["respirasjonsfrekvens"], [0, 9, 12, 21, 25, np.inf], right=False)
    X.loc[:, "blodtrykk_range"] = pd.cut(X["blodtrykk"], [0, 91, 101, 111, 140, 160, 180, np.inf], right=False)
    X.loc[:, "lungefunksjon_range"] = pd.cut(X["lungefunksjon"], [0, 100, 201, 300, np.inf], right=False)
    X = X.drop(["blodtrykk", "respirasjonsfrekvens", "lungefunksjon"], axis=1)
    return X

def transform_X(X_org):
    X = X_org.copy()
    X = apply_news_score(X)
    X = categorize_values(X)
    return X

def high_corr_interaction(X_encoded_org):
    X_encoded = X_encoded_org.copy()
    X_encoded["num__apache_fysiologisk_score_fysiologisk_score_interaction"] = X_encoded["num__apache_fysiologisk_score"] * X_encoded["num__fysiologisk_score"]
    X_encoded["num__lege_overlevelsesestimat_2mnd_lege_overlevelsesestimat_6mnd_interaction"] = X_encoded["num__lege_overlevelsesestimat_2mnd"] * X_encoded["num__lege_overlevelsesestimat_6mnd"]
    X_encoded["num__overlevelsesestimat_2mnd_overlevelsesestimat_6mnd_interaction"] = X_encoded["num__overlevelsesestimat_2mnd"] * X_encoded["num__overlevelsesestimat_6mnd"]
    X_encoded = X_encoded.drop(["num__apache_fysiologisk_score", "num__fysiologisk_score", 
                                "num__lege_overlevelsesestimat_2mnd", "num__lege_overlevelsesestimat_6mnd",
                                "num__overlevelsesestimat_2mnd", "num__overlevelsesestimat_6mnd"
                                ], axis=1)
    return X_encoded

def drop_high_corr(X_encoded_org):
    X_encoded = X_encoded_org.copy()
    X_encoded = X_encoded.drop(["cat__kjønn_female", "cat__sykehusdød_0.0", "cat__dødsfall_0", "cat__demens_0", "cat__diabetes_0"], axis=1)
    X_encoded= high_corr_interaction(X_encoded)
    return X_encoded