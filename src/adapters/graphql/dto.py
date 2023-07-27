import abc
from collections.abc import Iterable
from typing import Generic, Protocol, Self, TypeVar

_TModel_contra = TypeVar("_TModel_contra", contravariant=True)
_TType = TypeVar("_TType")


class DTOMixinProtocol(Protocol[_TModel_contra, _TType]):
    @classmethod
    def from_orm_list(cls, models: Iterable[_TModel_contra]) -> list[_TType]:
        ...  # pragma: no coverage


class DTOMixin(Generic[_TModel_contra]):
    @classmethod
    @abc.abstractmethod
    def from_orm(cls, model: _TModel_contra) -> Self:
        raise NotImplementedError

    @classmethod
    def from_orm_optional(
        cls,
        model: _TModel_contra | None,
    ) -> Self | None:  # pragma: no cover
        if model is None:
            return None
        return cls.from_orm(model)

    @classmethod
    def from_orm_list(cls, models: Iterable[_TModel_contra]) -> list[Self]:
        return [cls.from_orm(model) for model in models]  # pragma: no cover
