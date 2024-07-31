from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterable

import httpx
from litestar.repository import AbstractAsyncRepository

if TYPE_CHECKING:
    from litestar.repository.filters import FilterTypes
    import msgspec

    T = msgspec.Struct
    CollectionT = Iterable[T]


def ensure_type(f):
    def checker(self, *args, **kwargs):
        data = args[0]
        if not isinstance(data, list):
            data = [data]
        if not all(isinstance(obj, self.model_type) for obj in data):
            raise TypeError("Mismatched data type!")
        return f(self, *args, **kwargs)

    return checker


class CouchRepository(AbstractAsyncRepository):
    def __init__(self, **kwargs):
        super().__init__()
        self.client = httpx.AsyncClient(
            **kwargs
        )  # TODO: add initialization params (token, db/server uri, etc.)

    def model_from_dict(self, **kwargs):
        data = {
            field_name: kwargs[field_name]
            for field_name in self.model_type[...]  # TODO
        }
        return self.model_type(**data)

    @ensure_type
    async def add(self, data: T) -> T: ...

    @ensure_type
    async def add_many(self, data: list[T]) -> list[T]: ...

    async def count(self, *filters: FilterTypes, **kwargs: Any) -> int: ...

    async def delete(self, item_id: Any) -> T: ...

    async def delete_many(self, item_ids: list[Any]) -> list[T]: ...

    async def exists(self, *filters: FilterTypes, **kwargs: Any) -> bool: ...

    async def get(self, item_id: Any, **kwargs: Any) -> T: ...

    async def get_one(self, **kwargs: Any) -> T: ...

    async def get_or_create(self, **kwargs: Any) -> tuple[T, bool]: ...

    async def get_one_or_none(self, **kwargs: Any) -> T | None: ...

    @ensure_type
    async def update(self, data: T) -> T: ...

    @ensure_type
    async def update_many(self, data: list[T]) -> list[T]: ...

    @ensure_type
    async def upsert(self, data: T) -> T: ...

    @ensure_type
    async def upsert_many(self, data: list[T]) -> list[T]: ...

    async def list_and_count(
        self, *filters: FilterTypes, **kwargs: Any
    ) -> tuple[list[T], int]: ...

    async def list(self, *filters: FilterTypes, **kwargs: Any) -> list[T]: ...

    def filter_collection_by_kwargs(
        self, collection: CollectionT, /, **kwargs: Any
    ) -> CollectionT: ...
