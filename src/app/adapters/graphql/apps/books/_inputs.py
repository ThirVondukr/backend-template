import strawberry

from app.core.domain.books.dto import BookCreateDTO


@strawberry.input
class BookCreateInput:
    title: str

    def to_dto(self) -> BookCreateDTO:
        return BookCreateDTO(title=self.title)
