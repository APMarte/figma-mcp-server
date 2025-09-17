from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
from dotenv import load_dotenv
from figma_mcp.tools import files, exports, projects

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

# Include routers from tools
app.include_router(files.router, prefix="/v1/files")
app.include_router(exports.router, prefix="/v1/images")
app.include_router(projects.router, prefix="/v1/teams")