import pytest

from db.models import Book
from tests.graphql.client import GraphQLClient

pytestmark = [pytest.mark.anyio]

QUERY = """
query GetBookById($id: ID!) {
    book(id: $id) {
        id
        title
    }
}
"""


@pytest.mark.usefixtures("book")
@pytest.mark.parametrize("book_id", ["42", "not integer"])
async def test_book_not_found(graphql_client: GraphQLClient, book_id: str) -> None:
    response = await graphql_client(QUERY, variables={"id": book_id})
    assert response == {
        "data": {
            "book": None,
        },
    }


async def test_get_book(
    graphql_client: GraphQLClient,
    book: Book,
) -> None:
    response = await graphql_client(QUERY, variables={"id": str(book.id)})

    assert response == {
        "data": {
            "book": {
                "id": str(book.id),
                "title": book.title,
            },
        },
    }
