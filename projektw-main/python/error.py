from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi import HTTPException as FastAPIHTTPException
import difflib

ALLOWED_CHANNEL_ACTIONS = {"current", "previous"}

def suggest_action(action: str):
    """Hitta närmaste giltiga action om användaren stavat fel."""
    matches = difflib.get_close_matches(action, ALLOWED_CHANNEL_ACTIONS, n=1, cutoff=0.6)
    return matches[0] if matches else None

def format_404_for_channels(request: Request):
    """ Kollar om URL matchar /api/channels/{channel}/{action} och action är ogiltig, returnera ett 400-svar med felmeddelande samt förslag."""
    path = request.url.path.rstrip("/")
    parts = path.split("/")
    if len(parts) >= 5 and parts[1] == "api" and parts[2] == "channels":
        action = parts[4]
        if action and action not in ALLOWED_CHANNEL_ACTIONS:
            suggestion = suggest_action(action)
            message = f"Ogiltig action '{action}'. Tillåtna värden: {sorted(ALLOWED_CHANNEL_ACTIONS)}."
            if suggestion:
                message += f" Menade du '{suggestion}'?"
            return JSONResponse(
                status_code=400,
                content={"error": message, "code": 400, "path": request.url.path},
            )
    return None

async def handle_http_error(request: Request, exc):
    """ Hanterar HTTP-fel. Vid 404 på channels kolla stavfel, annars returnera standardfel i JSON-format. """
    if getattr(exc, "status_code", None) == 404:
        custom = format_404_for_channels(request)
        if custom is not None:
            return custom
    detail = getattr(exc, "detail", "Error")
    status = getattr(exc, "status_code", 500)
    return JSONResponse(status_code=status, content={"error": detail, "code": status})

async def http_exception_handler(request: Request, exc: FastAPIHTTPException):
    """Hanterar FastAPI HTTPException via handle_http_error."""
    return await handle_http_error(request, exc)

async def starlette_http_exception_handler(request: Request, exc: StarletteHTTPException):
    """Hanterar Starlette HTTPException via handle_http_error."""
    return await handle_http_error(request, exc)

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Hanterar valideringsfel och svarar med statuskod 422."""
    return JSONResponse(
        status_code=422,
        content={"error": "Validation error", "details": exc.errors(), "code": 422},
    )

async def general_exception_handler(request: Request, exc: Exception):
    """Fångar övriga fel och returnerar 500 med meddelande."""
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "code": 500},
    )
