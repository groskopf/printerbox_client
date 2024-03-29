from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.file_path import FilePath
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    booking_code: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/name_tags/{booking_code}".format(client.base_url, booking_code=booking_code)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[HTTPValidationError, List[FilePath]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FilePath.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HTTPValidationError, List[FilePath]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    booking_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[HTTPValidationError, List[FilePath]]]:
    """Get Name Tags

    Args:
        booking_code (str):

    Returns:
        Response[Union[HTTPValidationError, List[FilePath]]]
    """

    kwargs = _get_kwargs(
        booking_code=booking_code,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    booking_code: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[HTTPValidationError, List[FilePath]]]:
    """Get Name Tags

    Args:
        booking_code (str):

    Returns:
        Response[Union[HTTPValidationError, List[FilePath]]]
    """

    return sync_detailed(
        booking_code=booking_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    booking_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[HTTPValidationError, List[FilePath]]]:
    """Get Name Tags

    Args:
        booking_code (str):

    Returns:
        Response[Union[HTTPValidationError, List[FilePath]]]
    """

    kwargs = _get_kwargs(
        booking_code=booking_code,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    booking_code: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[HTTPValidationError, List[FilePath]]]:
    """Get Name Tags

    Args:
        booking_code (str):

    Returns:
        Response[Union[HTTPValidationError, List[FilePath]]]
    """

    return (
        await asyncio_detailed(
            booking_code=booking_code,
            client=client,
        )
    ).parsed
