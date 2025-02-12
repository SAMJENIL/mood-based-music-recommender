from flask import Flask, request, jsonify, render_template
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import random

# Initialize Flask app
app = Flask(__name__)

# Download NLTK resources
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Spotify API credentials (Replace with your actual credentials)
SPOTIPY_CLIENT_ID = "167e5c78dcaf42a5a8ef32bb0fe3047e"
SPOTIPY_CLIENT_SECRET = "860edfe1034a4bdfad9b57992d66882a"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                           client_secret=SPOTIPY_CLIENT_SECRET))

# Function to analyze mood
def get_mood(text):
    sentiment_score = sia.polarity_scores(text)["compound"]
    if sentiment_score >= 0.05:
        return "happy"
    elif sentiment_score <= -0.05:
        return "sad"
    else:
        return "neutral"

# Function to recommend songs
def recommend_songs(mood):
    # Expanded mood-to-genre mapping for more diversity
    mood_to_genres = {
        "happy": ["pop", "dance", "funk", "electronic"],
        "sad": ["acoustic", "blues", "folk", "classical"],
        "neutral": ["chill", "ambient", "indie", "lofi"],
        "angry": ["rock", "metal", "punk"],
        "relaxed": ["jazz", "soul", "rnb"]
    }

    # Pick a random genre from the list
    genres = mood_to_genres.get(mood, ["pop"])
    selected_genre = random.choice(genres)
    
    # Search for songs in the selected genre
    results = sp.search(q=f"genre:{selected_genre}", type="track", limit=10)

    # Extract song details
    songs = [{"name": track["name"], "artist": track["artists"][0]["name"], "url": track["external_urls"]["spotify"]}
             for track in results["tracks"]["items"]]
    
    return songs

# Flask Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    user_input = data.get("text", "")
    
    if not user_input:
        return jsonify({"error": "No text provided"}), 400
    
    mood = get_mood(user_input)
    songs = recommend_songs(mood)
    
    return jsonify({"mood": mood, "songs": songs})

if __name__ == "__main__":
    app.run(debug=True)
