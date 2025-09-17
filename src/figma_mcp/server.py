from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Authentication
FIGMA_API_TOKEN = os.getenv("FIGMA_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {FIGMA_API_TOKEN}"}

# Rate Limiting
RATE_LIMIT_FILES = 2  # requests per second
RATE_LIMIT_OTHERS = 3  # requests per second

# Error Handling
@app.exception_handler(httpx.HTTPStatusError)
async def http_exception_handler(request: Request, exc: httpx.HTTPStatusError):
    return HTTPException(status_code=exc.response.status_code, detail=exc.response.text)

@app.get("/")
async def root():
    return {"message": "Welcome to the Figma MCP Server"}

# Example endpoint
@app.get("/v1/files/{key}")
async def get_file_data(key: str):
    url = f"https://api.figma.com/v1/files/{key}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()