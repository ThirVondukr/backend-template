import strawberry


@strawberry.interface(name="Error")
class ErrorGQL:
    message: str


@strawberry.type(name="EntityAlreadyExistsError")
class EntityAlreadyExistsErrorGQL(ErrorGQL):
    message: str = "Entity already exists"
