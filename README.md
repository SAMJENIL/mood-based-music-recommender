#

# Mood-Based Music Recommendation System

## 📌 Project Overview

The **Mood-Based Music Recommendation System** is an AI-powered web application that suggests songs based on the user's emotions. It uses **Natural Language Processing (NLP)** to analyze text input, classify emotions, and fetch music recommendations from **Spotify API**.

## 🚀 How It Works

1. **User Inputs Text** → (e.g., "I feel happy today!")
2. **Sentiment Analysis (NLP)** → Determines mood (Happy, Sad, Angry, Relaxed, Neutral)
3. **Mood-to-Genre Mapping** → Assigns a relevant music genre
4. **Spotify API Fetches Songs** → Retrieves songs matching the mood
5. **Displays Recommended Songs** → Shows track names, artists, and Spotify links

## 📷 System Architecture

```
User Input → Sentiment Analysis (NLTK) → Mood Classification → Genre Mapping → Spotify API → Recommended Songs
```

## 🛠️ Technologies Used

| Component            | Technology                          |
| -------------------- | ----------------------------------- |
| **Frontend**         | HTML, CSS, JavaScript               |
| **Backend**          | Flask (Python)                      |
| **Machine Learning** | NLTK (Sentiment Intensity Analyzer) |
| **Music API**        | Spotipy (Spotify API)               |
| **Data Format**      | JSON                                |

## 📂 Folder Structure

```
mood-based-music-recommender/
│── app.py                # Main Flask backend
│── templates/            # HTML frontend
│   ├── index.html        # Web interface
│── static/               # CSS and JS files
│   ├── style.css         # Styles for UI
│── sentiment_analysis.py # NLP-based sentiment detection
│── spotify_recommender.py # Fetches songs from Spotify API
│── config.py             # API keys and settings
│── requirements.txt      # Dependencies
│── README.md             # Documentation
```

## ⚙️ Installation & Setup

### 🔹 Prerequisites

- Python 3.x
- Spotify Developer Account (Get API credentials from [Spotify Developer Dashboard](https://developer.spotify.com/))

### 🔹 Steps to Run the Project

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/SAMJENIL/mood-based-music-recommender.git
cd mood-based-music-recommender
```

#### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3️⃣ Set Up Spotify API Credentials

- Open `config.py` and enter your **Spotify Client ID and Secret**:

```python
SPOTIFY_CLIENT_ID = "your_client_id"
SPOTIFY_CLIENT_SECRET = "your_client_secret"
```

#### 4️⃣ Run the Flask App

```bash
python app.py
```

#### 5️⃣ Open in Browser

Go to: **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

## 📌 Features

✅ **AI-Powered Sentiment Analysis** – Detects user mood from text input\
✅ **Spotify API Integration** – Fetches songs based on detected mood\
✅ **Dynamic Genre Mapping** – Maps emotions to relevant music genres\
✅ **User-Friendly Web Interface** – Simple input box with instant recommendations\
✅ **Structured Output (JSON)** – Can be extended for mobile apps or voice assistants

## 🎯 Example Usage

#### **Input:**

```
User: "I am feeling really stressed today."
```

#### **Output:**

```
Detected Mood: Relaxed
Recommended Songs:
1. "Lo-Fi Chill Beats" - Artist: XYZ [🔗 Listen](#)
2. "Jazz Vibes" - Artist: ABC [🔗 Listen](#)
3. "Piano Relaxation" - Artist: DEF [🔗 Listen](#)
```

## 📌 Limitations

⚠️ **Requires Internet Connection** – Since it fetches data from Spotify API\
⚠️ **Spotify API Rate Limits** – Limited number of song requests per day\
⚠️ **Basic Sentiment Analysis** – May not detect complex emotions accurately

## 🔮 Future Enhancements

🔹 **Advanced Sentiment Analysis** – Using deep learning models like BERT\
🔹 **User Authentication** – Save personalized song preferences\
🔹 **Support for More Music Platforms** – Apple Music, YouTube Music, etc.

## 📌 Contribution

Want to improve this project? Feel free to fork, enhance, and submit a **Pull Request (PR)**!

## 📜 License

This project is licensed under the **MIT License**.

## 🔗 Useful Links

- 🎵 **Spotify API Documentation**: [Spotify Developer](https://developer.spotify.com/)
- 📚 **NLTK Sentiment Analysis Guide**: [NLTK Docs](https://www.nltk.org/)

## 👨‍💻 Author

Developed by **Sam Jenil**\
GitHub: [SAMJENIL](https://github.com/SAMJENIL)

