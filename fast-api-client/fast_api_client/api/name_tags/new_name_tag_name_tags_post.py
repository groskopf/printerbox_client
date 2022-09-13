from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.details import Details
from ...models.file_path import FilePath
from ...models.http_validation_error import HTTPValidationError
from ...models.layout import Layout
from ...models.name_data import NameData
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: NameData,
    booking_code: str,
    layout: Layout,
) -> Dict[str, Any]:
    url = "{}/name_tags/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["booking_code"] = booking_code

    json_layout = layout.value

    params["layout"] = json_layout

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Details, FilePath, HTTPValidationError]]:
    if response.status_code == 201:
        response_201 = FilePath.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = Details.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = Details.from_dict(response.json())

        return response_404
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Details, FilePath, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: NameData,
    booking_code: str,
    layout: Layout,
) -> Response[Union[Details, FilePath, HTTPValidationError]]:
    """New Name Tag

    Args:
        booking_code (str):
        layout (Layout): An enumeration.
        json_body (NameData):

    Returns:
        Response[Union[Details, FilePath, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        booking_code=booking_code,
        layout=layout,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: NameData,
    booking_code: str,
    layout: Layout,
) -> Optional[Union[Details, FilePath, HTTPValidationError]]:
    """New Name Tag

    Args:
        booking_code (str):
        layout (Layout): An enumeration.
        json_body (NameData):

    Returns:
        Response[Union[Details, FilePath, HTTPValidationError]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        booking_code=booking_code,
        layout=layout,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: NameData,
    booking_code: str,
    layout: Layout,
) -> Response[Union[Details, FilePath, HTTPValidationError]]:
    """New Name Tag

    Args:
        booking_code (str):
        layout (Layout): An enumeration.
        json_body (NameData):

    Returns:
        Response[Union[Details, FilePath, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        booking_code=booking_code,
        layout=layout,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: NameData,
    booking_code: str,
    layout: Layout,
) -> Optional[Union[Details, FilePath, HTTPValidationError]]:
    """New Name Tag

    Args:
        booking_code (str):
        layout (Layout): An enumeration.
        json_body (NameData):

    Returns:
        Response[Union[Details, FilePath, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            booking_code=booking_code,
            layout=layout,
        )
    ).parsed
