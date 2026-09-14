import httpx
from config import RADIO_API, RADIO_CHANNELS

class RadioHandler:
    async def fetch_song_info(self, channel_id: int):
        """
        Hämtar låtinfo från Sveriges Radio API (async)
        Returnerar två dictionaries: (current_song, previous_song). Tomma dicts om inget hittas.
        """
        async with httpx.AsyncClient(timeout=8) as client:
            res = await client.get(f"{RADIO_API}?channelid={channel_id}&format=json")
        if res.status_code != 200:
            return {}, {}

        data = res.json().get("playlist", {})
        return data.get("song", {}) or {}, data.get("previoussong", {}) or {}

    def get_channel_id(self, channel: str):
        """Slår upp kanalens ID i RADIO_CHANNELS"""
        return RADIO_CHANNELS.get((channel or "").lower())

radio_handler = RadioHandler()

async def get_current_and_previous_song(channel: str):
    """Hämtar nuvarande och föregående låt för en kanal, samt skriver ut None om kanalen inte finns."""
    channel_id = radio_handler.get_channel_id(channel)
    if not channel_id:
        return None

    current, previous = await radio_handler.fetch_song_info(channel_id)

    return {
        "current": {
            "title": current.get("title", "Ingen låt spelas just nu"),
            "artist": current.get("artist", "Okänd artist")
        },
        "previous": {
            "title": previous.get("title", "Ingen föregående låt hittades"),
            "artist": previous.get("artist", "Okänd artist")
        }
    }
