from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

@router.get("/v1/images/{key}")
async def export_images(key: str, ids: str, format: str = "png"):
    url = f"https://api.figma.com/v1/images/{key}?ids={ids}&format={format}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()