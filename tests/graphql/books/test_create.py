import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.domain.books.models import Book
from tests.graphql.client import GraphQLClient

QUERY = """
mutation CreateBook($input: BookCreateInput!) {
    createBook(input: $input) {
        result {
            id
            title
        }
        error {
            __typename
            ... on Error {
                message
            }
        }
    }
}
"""


async def test_book_already_exists(graphql_client: GraphQLClient, book: Book) -> None:
    response = await graphql_client(QUERY, variables={"input": {"title": book.title}})
    assert response == {
        "data": {
            "createBook": {
                "result": None,
                "error": {
                    "__typename": "EntityAlreadyExistsError",
                    "message": "Entity already exists",
                },
            },
        },
    }


async def test_create_book(
    graphql_client: GraphQLClient,
    session: AsyncSession,
) -> None:
    title = str(uuid.uuid4())
    response = await graphql_client(QUERY, variables={"input": {"title": title}})

    book = (await session.scalars(select(Book))).one()

    assert response == {
        "data": {
            "createBook": {
                "result": {
                    "id": str(book.id),
                    "title": title,
                },
                "error": None,
            },
        },
    }
