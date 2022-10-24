from httpx import AsyncClient
from starlette import status


async def test_healthcheck(http_client: AsyncClient) -> None:
    response = await http_client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() is None
