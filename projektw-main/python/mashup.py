from fastapi import APIRouter, HTTPException
from radio import get_current_and_previous_song, RADIO_CHANNELS
from spotify import SpotifyHandler

api_router = APIRouter()
spotify_handler = SpotifyHandler()


@api_router.get("/api/channels")
async def list_channels():
    """Lista alla tillgängliga radiokanaler från RADIO_CHANNELS."""
    return {"channels": list(RADIO_CHANNELS.keys())}

@api_router.get("/api/channels/{channel}")
async def full_channel_info(channel: str):
    """Returnera info om både nuvarande och föregående låt för en kanal."""
    radio_data = await get_current_and_previous_song(channel)
    if radio_data is None:
        raise HTTPException(status_code=404, detail="Channel not found")

    current = get_song_with_spotify_link(radio_data['current'], spotify_handler)
    previous = get_song_with_spotify_link(radio_data['previous'], spotify_handler)

    return {
        "channel": channel,
        "current_song": current,
        "previous_song": previous
    }

@api_router.get("/api/channels/{channel}/current")
async def current_song(channel: str):
    """Returnera endast nuvarande låt för en kanal (inkl. Spotify-länk)."""
    radio_data = await get_current_and_previous_song(channel)
    if radio_data is None:
        raise HTTPException(status_code=404, detail="Channel not found")

    return get_song_with_spotify_link(radio_data["current"], spotify_handler)

@api_router.get("/api/channels/{channel}/previous")
async def previous_song(channel: str):
    """Returnera endast föregående låt för en kanal (inkl. Spotify-länk)."""
    radio_data = await get_current_and_previous_song(channel)
    if radio_data is None:
        raise HTTPException(status_code=404, detail="Channel not found")

    return get_song_with_spotify_link(radio_data["previous"], spotify_handler)

def get_song_with_spotify_link(song: dict, spotify_handler: SpotifyHandler):
    """Lägger till Spotify-länk för en låt baserat på titel och artist"""
    if not song["title"] or not song["artist"]:
        return {"title": "", "artist": "", "spotify_link": None}

    return {
        "title": song["title"],
        "artist": song["artist"],
        "spotify_link": spotify_handler.get_spotify_link(song["title"], song["artist"])
    }