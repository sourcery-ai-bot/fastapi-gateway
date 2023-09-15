from typing import Union, Any, Dict, Optional
from aiohttp import JsonPayload
from fastapi_gateway.utils.form import CustomFormData

T = Union[Dict[str, Any], CustomFormData, JsonPayload]


def create_dict_if_not(data: Optional[T] = None) -> Union[dict, T]:
    return data if data else {}


def create_request_data(
        form: Optional[CustomFormData],
        body: Optional[JsonPayload]
) -> Optional[Union[CustomFormData, JsonPayload]]:

    return form if form else body
