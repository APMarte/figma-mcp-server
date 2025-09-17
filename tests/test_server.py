import pytest
from httpx import AsyncClient
from figma_mcp.server import app

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Figma MCP Server"}

@pytest.mark.asyncio
async def test_get_file_data():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/v1/files/dummy_key")
    assert response.status_code == 401  # Assuming invalid token or key

@pytest.mark.asyncio
async def test_get_file_nodes():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/v1/files/dummy_key/nodes?ids=1,2,3")
    assert response.status_code == 401  # Assuming invalid token or key

@pytest.mark.asyncio
async def test_export_images():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/v1/images/dummy_key?ids=1,2,3&format=png")
    assert response.status_code == 401  # Assuming invalid token or key

@pytest.mark.asyncio
async def test_get_team_projects():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/v1/teams/dummy_team_id/projects")
    assert response.status_code == 401  # Assuming invalid token or key
