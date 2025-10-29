import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"


sp = spotipy.Spotify(auth=)

load_dotenv()

CLIENT_ID = os.getenv("client_id")
CLIENT_SECRET = os.getenv("client_server")


endpoint = "https://www.billboard.com/charts/hot-100/"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}

response = requests.get(endpoint, headers=header)
billboard_website = response.text

soup = BeautifulSoup(billboard_website,"html.parser")

songs = soup.select("li ul li h3")

songs_name = [song.getText(strip=True) for song in songs]

