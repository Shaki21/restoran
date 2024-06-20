import json
from typing import List, Type, TypeVar
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)


def serialize(data: List[T]) -> str:
    return json.dumps([item.dict() for item in data])


def deserialize(data: str, model: Type[T]) -> List[T]:
    json_data = json.loads(data)
    return [model(**item) for item in json_data]
