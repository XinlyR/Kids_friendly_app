import re
import string
import joblib
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from textblob import TextBlob
import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer, SnowballStemmer, LancasterStemmer
from nltk.corpus import stopwords, wordnet
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.tokenize import word_tokenize
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score,precision_recall_curve
from sklearn.model_selection import train_test_split
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from sklearn.utils import resample
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import GridSearchCV
import seaborn as sns
import matplotlib.pyplot as plt
import json
from pytrends.request import TrendReq
nltk.download("punkt") 
nltk.download("averaged_perceptron_tagger")
nltk.download('wordnet')
nltk.download('stopwords')


# Function to get places 
def get_places_by_arrondissement(lat, lng, keyword, radius, api_key):
    places = []
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&keyword={keyword}&key={api_key}"
    
    while True:
        # Envoyer la requête
        response = requests.get(url)
        results = response.json()
        
        # Vérifier les résultats
        if 'status' in results and results['status'] == 'OK':
            places.extend(results['results'])
            
            # Vérifier si un next_page_token existe
            if 'next_page_token' in results:
                # Attendre quelques secondes pour que le next_page_token soit actif
                time.sleep(2)  # Google recommande d'attendre quelques secondes
                next_page_token = results['next_page_token']
                url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={next_page_token}&key={api_key}"
            else:
                # Pas de page suivante, sortir de la boucle
                break
        else:
            print(f"Erreur: {results.get('status', 'Unknown error')} pour la requête.")
            break
    
    return places
# Functions to get details 
def get_place_details(place_id, api_key):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,rating,vicinity,opening_hours,types,review,user_ratings_total,formatted_address,website,formatted_phone_number&key={api_key}"
    response = requests.get(url)
    details = response.json().get('result', {})
    return details

# Function to extract postal code using regex
def extract_zipcode(address):
    match = re.search(r'\b75[0-2]\d{2}\b', address)  # Pattern to match 75001-75020
    return match.group(0) if match else None

# Function to get places by arrondissement
def get_places_by_arrondissement(lat, lng, keyword, radius, api_key):
    places = []
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&keyword={keyword}&key={api_key}"
    
    while True:
        # Request
        response = requests.get(url)
        results = response.json()
        
        # Vérifier les résultats
        if 'status' in results and results['status'] == 'OK':
            places.extend(results['results'])
            
            # Vérifier si un next_page_token existe
            if 'next_page_token' in results:
                # Attendre quelques secondes pour que le next_page_token soit actif
                time.sleep(2)  # Google recommande d'attendre quelques secondes
                next_page_token = results['next_page_token']
                url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={next_page_token}&key={api_key}"
            else:
                # Pas de page suivante, sortir de la boucle
                break
        else:
            print(f"Erreur: {results.get('status', 'Unknown error')} pour la requête.")
            break
    
    return places




# Functions to get de details and reviews
def get_place_details(place_id, api_key):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,rating,vicinity,opening_hours,types,review,user_ratings_total,formatted_address,website,formatted_phone_number&key={api_key}"
    response = requests.get(url)
    details = response.json().get('result', {})
    return details


# Function to analyze the sentiment of a review
def analyze_sentiment(review_text):
    blob = TextBlob(review_text)
    return blob.sentiment.polarity  # Polarity ranges from -1 (negative) to +1 (positive)


# Function to analyze if a review is "kids-friendly" based on keyword presence
def analyze_kids_friendly_score(review_text):
    if pd.isna(review_text):  # Checks if the review is empty
        return 0, 0
    
    # Split review into sentences to capture relevant mentions for kids-friendliness
    sentences = review_text.split('.')
    relevant_reviews = [sentence for sentence in sentences if any(keyword in sentence.lower() for keyword in keywords_for_kids)]
    
    # If no relevant review is found, return 0 (no kids-friendly mentions)
    if not relevant_reviews:
        return 0, 0
    
    # Analyze the sentiment of relevant sentences
    sentiment_scores = [TextBlob(sentence).sentiment.polarity for sentence in relevant_reviews]
    
    # Calculate the average sentiment score for kids-friendliness and the count of mentions
    avg_kids_friendly_sentiment = sum(sentiment_scores) / len(sentiment_scores)
    kids_mentions_count = len(relevant_reviews)
    
    return avg_kids_friendly_sentiment, kids_mentions_count

#Adding column zip_code
def extract_zip_code(address):
    match = re.search(r'\b(75|91|92|93|94|95)\d{3}\b', address)
    if match:
        return match.group(0)
    return None


# Function to get the restaurants of each city
def fetch_restaurants(city):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": "restaurants in " + city,
        "key": api_key,
        "radius": radius
    }
    
    all_results = []
    while True:
        response = requests.get(url, params=params)
        results = response.json().get("results", [])
        all_results.extend(results)
        
        # Check if there is a next page
        next_page_token = response.json().get("next_page_token")
        if not next_page_token:
            break
        else:
            
            time.sleep(2)
            params['pagetoken'] = next_page_token
            
    return all_results

def fetch_reviews(place_id):
    details_url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "key": api_key,
        "fields": "name,rating,user_ratings_total,reviews"
    }
    response = requests.get(details_url, params=params)
    result = response.json().get("result", {})
    return result



# Function to get the coffees shop
def fetch_coffees(city):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": "coffee in " + city,
        "key": api_key,
        "radius": radius
    }
    
    all_results = []
    while True:
        response = requests.get(url, params=params)
        results = response.json().get("results", [])
        all_results.extend(results)
        
        # Check if there is a next_page
        next_page_token = response.json().get("next_page_token")
        if not next_page_token:
            break
        else:
            
            time.sleep(2)
            params['pagetoken'] = next_page_token
            
    return all_results


# Function to get the places by type & neighborhood
def get_places_by_type_and_location(lat, lng, place_type, radius, api_key):
    places = []
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={place_type}&key={api_key}"
    
    while True:
        # Request
        response = requests.get(url)
        results = response.json()
        
        # Checking the reply
        if 'status' in results and results['status'] == 'OK':
            places.extend(results['results'])
            
            # Checking if a next_page_token exists
            if 'next_page_token' in results:
                # Wait to get the next_page_token active
                time.sleep(2)  
                next_page_token = results['next_page_token']
                url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={next_page_token}&key={api_key}"
            else:
                # If there isn't next_page , break the loop
                break
        else:
            print(f"Erreur: {results.get('status', 'Unknown error')} pour {place_type}")
            break
    
    return places




# To use POS with lemmatization we need to create a function

def get_wordnet_pos(word):
  tag = nltk.pos_tag([word], lang="eng")[0][1][0]
  tag_dict = {"R": wordnet.ADV,
              "N": wordnet.NOUN,
              "V": wordnet.VERB,
              "J": wordnet.ADJ}

  return tag_dict.get(tag, wordnet.NOUN)

def tokenize(row):
  tokens = word_tokenize(row)
  return [word.lower() for word in tokens if word.isalpha()]

def lemmatizer_with_pos(row):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in row]

def remove_sw(row):
  return [word for word in row if (word not in stopwords.words("english") and len(word)>1)]


