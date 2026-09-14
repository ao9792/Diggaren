from fastapi import FastAPI, HTTPException as FastAPIHTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import uvicorn

from mashup import api_router
from pages import page_router
from error import (
    http_exception_handler,                
    starlette_http_exception_handler,      
    validation_exception_handler,
    general_exception_handler
)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_router)
app.include_router(page_router)

app.add_exception_handler(FastAPIHTTPException, http_exception_handler)
app.add_exception_handler(StarletteHTTPException, starlette_http_exception_handler)

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
