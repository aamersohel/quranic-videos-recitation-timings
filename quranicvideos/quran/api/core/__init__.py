import requests
import json

from urllib.parse import urlencode
from dataclasses import dataclass, field
from typing import Dict, Type, TypeVar
from pydantic import ValidationError

T = TypeVar("T")


@dataclass
class ApiPoint:
    url: str
    output_key: str
    output_type: Type[T]
    required_args: Dict = field(default_factory=dict)
    optional_args: Dict = field(default_factory=dict)


def getData(point: ApiPoint) -> any:
    optional_args = {
        key: value for key, value in point.optional_args.items() if value is not None
    }
    optionals = "?" + urlencode(optional_args) if bool(optional_args) else ""
    base_url = "https://api.quran.com/api/v4"
    if not point.url.startswith("/"):
        base_url = ""
    url_pattern = point.url.format(**point.required_args)
    url = base_url + url_pattern + optionals
    result = requests.get(url=url)
    data = result.json()
    data = data.get(point.output_key) if bool(point.output_key) else data

    try:
        if type(data) == list:
            result = list(map(lambda item: point.output_type(**item), data))
        else:
            result = point.output_type(**data)
    except ValidationError as e:
        print(e.errors())

    return result
