from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from config import CLIENT_ID, CLIENT_SECRET

class SpotifyHandler:
    def __init__(self):
        self._client = Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
            )
        )

    def get_spotify_link(self, song_name: str, artist_name: str):
        """Sök en låt och returnera dess Spotify-länk (eller None)."""
        if not song_name or not artist_name:
            return None
        query = f"track:{song_name} artist:{artist_name}"
        results = self._client.search(q=query, type="track", limit=1)
        items = results.get("tracks", {}).get("items", [])
        if items:
            return items[0]["external_urls"]["spotify"]
        return None
