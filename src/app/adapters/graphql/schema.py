from aioinject.ext.strawberry import AioInjectExtension
from strawberry import Schema
from strawberry.extensions import ParserCache, ValidationCache
from strawberry.tools import merge_types

from app.core.di import create_container

from .apps.books import BookMutation, BookQuery

query = merge_types(
    name="Query",
    types=(BookQuery,),
)

mutation = merge_types(
    name="Mutation",
    types=(BookMutation,),
)

schema = Schema(
    query=query,
    mutation=mutation,
    extensions=[
        ParserCache(maxsize=128),
        ValidationCache(maxsize=128),
        AioInjectExtension(container=create_container()),
    ],
)
