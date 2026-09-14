from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from jinja2 import TemplateNotFound
import httpx

page_router = APIRouter()
templates = Jinja2Templates(directory="templates")

CHANNEL_NAMES = {
    "p3": "Sveriges Radio P3",
    "p4": "P4 Stockholm"
}

@page_router.get("/channels/{channel}", response_class=HTMLResponse)
async def render_channel_page(request: Request, channel: str):
    """Renderar kanalsida med data från APIet, hämtar info från /api/channels/{channel} och skickar vidare till Jinja2-template """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://127.0.0.1:8080/api/channels/{channel}")
        channel_name = CHANNEL_NAMES.get(channel.lower(), channel.upper())
        
        if response.status_code != 200:
            return templates.TemplateResponse("error.html", {
                "request": request,
                "error": f"Kanal '{channel}' hittades inte (API-svar: {response.status_code})."
            }, status_code=404)

        data = response.json()
    try:
        return templates.TemplateResponse("channel.html", {
            "request": request,
            "channel": channel,
            "channel_name": channel_name,
            "current_title": data['current_song']['title'],
            "current_artist": data['current_song']['artist'],
            "spotify_link": data['current_song']['spotify_link'],
            "previous_title": data['previous_song']['title'],
            "previous_artist": data['previous_song']['artist'],
            "previous_spotify_link": data['previous_song']['spotify_link']
        })
    except TemplateNotFound:
        return templates.TemplateResponse("error.html", {
            "request": request,
            "error": f"Mallfilen '{channel}.html' finns inte."
        }, status_code=404)


@page_router.get("/")
def home(request: Request):
    """Renderar startsidan (startsida.html)"""
    return templates.TemplateResponse("startsida.html", {"request": request})

@page_router.get("/diggaren")
def diggaren(request: Request):
    """Renderar sidan diggaren.html"""
    return templates.TemplateResponse("diggaren.html", {"request": request})

@page_router.get("/kontakta")
def kontakta(request: Request):
    """Renderar sidan kontakta.html"""
    return templates.TemplateResponse("kontakta.html", {"request": request})