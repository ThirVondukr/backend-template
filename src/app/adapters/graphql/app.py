from starlette.requests import Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from strawberry.asgi import GraphQL

from .context import Context
from .dataloaders import create_dataloaders
from .schema import schema


class GraphQLApp(GraphQL[Context, None]):
    async def get_context(
        self,
        request: Request | WebSocket,
        response: Response | WebSocket,
    ) -> Context:
        return Context(
            request=request,
            response=response,
            loaders=create_dataloaders(),
        )


def create_graphql_app() -> GraphQL[Context, None]:
    return GraphQLApp(
        schema=schema,
    )
