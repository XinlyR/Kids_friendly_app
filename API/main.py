from flask import Flask, send_file
import pandas as pd
import io
import os

app = Flask(__name__)

@app.route("/") 
def home():
    return "Welcome to the Kids-Friendly Data API!"

# Download of df_detailed_places
@app.route("/api/download_detailed_places", methods=["GET"])
def download_detailed_places():
    df_detailed_places = pd.read_csv("ddetailed_kids_friendly_places_paris_with_reviews.csv")
    output = io.BytesIO()
    df_detailed_places.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, mimetype='text/csv', as_attachment=True, download_name="detailed_places.csv")

# Download of trends_5years
@app.route("/api/download_trends_5years", methods=["GET"])
def download_trends_5years():
    trends_5years = pd.read_csv("ttrends_kids_friendly_paris_5years.csv")
    output = io.BytesIO()
    trends_5years.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, mimetype='text/csv', as_attachment=True, download_name="trends_5years.csv")

# Download of population France
@app.route("/api/download_population_france", methods=["GET"])
def download_population_france():
    df = pd.read_csv("population_france.csv")
    output = io.BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, mimetype='text/csv', as_attachment=True, download_name="population_france.csv")

# Download of df_parks_with_playground
@app.route("/api/download_parks_with_playground", methods=["GET"])
def download_parks_with_playground():
    df_parks_with_playground = pd.read_excel("espaces_verts.xlsx")
    output = io.BytesIO()
    df_parks_with_playground.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, mimetype='text/csv', as_attachment=True, download_name="parks_with_playground.csv")

# Download ofe df_faire
@app.route("/api/download_faire", methods=["GET"])
def download_faire():
    df_faire = pd.read_csv("qque-faire-a-paris-.csv")
    output = io.BytesIO()
    df_faire.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, mimetype='text/csv', as_attachment=True, download_name="faire.csv")

# Téléchargement de df_paris_data
@app.route("/api/download_paris_data", methods=["GET"])
def download_paris_data():
    df_paris_data = pd.read_csv("population_paris_2021.csv")
    output = io.BytesIO()
    df_paris_data.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, mimetype='text/csv', as_attachment=True, download_name="paris_population_data.csv")

# Download of trends_comparison
@app.route("/api/download_trends_comparison", methods=["GET"])
def download_trends_comparison():
    trends_comparison = pd.read_csv("trends_comparison.csv")
    output = io.BytesIO()
    trends_comparison.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, mimetype='text/csv', as_attachment=True, download_name="trends_comparison.csv")

# Download of data
@app.route("/api/download_gral_df_scores", methods=["GET"])
def download_gral_df_scores():
    data = pd.read_csv("Gral_df_Scores.csv")
    output = io.BytesIO()
    data.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, mimetype='text/csv', as_attachment=True, download_name="gral_df_scores.csv")

# Download ofe df_kf_places_paris
@app.route("/api/download_kf_places_paris", methods=["GET"])
def download_kf_places_paris():
    df_kf_places_paris = pd.read_csv("extra_kfplaces_paris.csv")
    output = io.BytesIO()
    df_kf_places_paris.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, mimetype='text/csv', as_attachment=True, download_name="kf_places_paris.csv")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the port Render specifies
    app.run(host="0.0.0.0", port=port) 