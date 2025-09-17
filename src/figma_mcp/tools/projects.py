from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

@router.get("/v1/teams/{team_id}/projects")
async def get_team_projects(team_id: str):
    url = f"https://api.figma.com/v1/teams/{team_id}/projects"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()