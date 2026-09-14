import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

RADIO_API = "http://api.sr.se/api/v2/playlists/rightnow"
RADIO_CHANNELS = {"p3": 164, "p4": 217}  # p4 = P4 Stockholm