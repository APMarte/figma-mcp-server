from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

@router.get("/v1/files/{key}/nodes")
async def get_file_nodes(key: str, ids: str):
    url = f"https://api.figma.com/v1/files/{key}/nodes?ids={ids}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()

@router.get("/v1/files/{key}/components")
async def get_file_components(key: str):
    url = f"https://api.figma.com/v1/files/{key}/components"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()

@router.get("/v1/files/{key}/styles")
async def get_file_styles(key: str):
    url = f"https://api.figma.com/v1/files/{key}/styles"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()

@router.get("/v1/files/{key}/comments")
async def get_file_comments(key: str):
    url = f"https://api.figma.com/v1/files/{key}/comments"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()