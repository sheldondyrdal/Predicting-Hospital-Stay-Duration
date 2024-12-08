import numpy as np
import pandas as pd
import pickle

from transformations import transform_X, drop_high_corr
from flask import Flask, request, render_template
from waitress import serve

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # get data
    features = dict(request.form)  
    
    categorical_features = ["sykdom_underkategori", "kreft", "kjønn", "etnisitet", "diabetes", "demens"]
    numeric_features = ["alder", "utdanning", "blodtrykk", "hvite_blodlegemer", "hjertefrekvens", "respirasjonsfrekvens", 
                        "kroppstemperatur", "lungefunksjon", "kreatinin", "natrium", "blod_ph", "antall_komorbiditeter", 
                        "koma_score", "fysiologisk_score", "apache_fysiologisk_score", "overlevelsesestimat_2mnd", 
                        "overlevelsesestimat_6mnd", "lege_overlevelsesestimat_2mnd", "lege_overlevelsesestimat_6mnd"]
    
    wrong_input = []
    non_negative_input = []
    
    # handle wrong input
    def to_numeric(key, value, numeric_features = numeric_features, wrong_input = wrong_input, non_negative_input = non_negative_input):
        # Hvis kategorisk
        if key not in numeric_features:
            return value
        # Hvis numerisk
        # Bytt ut , med . f.eks. 1,0 --> 1.0
        if "," in value:
            value = value.replace(",", ".")
        # Prøv å gjør om til int eller flyttall
        try:
            if key == "antall_komorbiditeter":
                value = int(value)
            else:
                value = float(value)
            
            if value < 0:
                non_negative_input.append(key)
            
            return value
        # Hvis ikke, gjør om til NaN
        except:
            if value:
                wrong_input.append(key)
            
            return np.nan
    
    features = {key: to_numeric(key, value) for key, value in features.items()}

    # Output til brukeren ved feil input
    if len(wrong_input) != 0:
        print(f"{wrong_input=}")
        return render_template("index.html", prediction_text=f"OBS! Må være et tall:\n{wrong_input}")
    elif len(non_negative_input) != 0:
        print(f"{non_negative_input=}")
        return render_template("index.html", prediction_text=f"OBS! Skal ikke være negative verdier:\n{non_negative_input}")
    
    # prepare for prediction
    features_df = pd.DataFrame(features, index=[0]).loc[:, numeric_features + categorical_features]
    print(features_df)
    
    # predict
    prediction = model.predict(features_df)[0]
    print(f"{prediction=}")
    
    return render_template("index.html", prediction_text=f"Predikert oppholdslengde: {round(prediction, None)} dager")
    
if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080)