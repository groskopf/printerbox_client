from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.details import Details
from ...models.http_validation_error import HTTPValidationError
from ...models.sheet_layouts import SheetLayouts
from ...models.sheet_type import SheetType
from ...types import Response


def _get_kwargs(
    sheet_type: SheetType,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/layouts/sheets/{sheet_type}".format(client.base_url, sheet_type=sheet_type)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Details, HTTPValidationError, SheetLayouts]]:
    if response.status_code == 200:
        response_200 = SheetLayouts.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Details.from_dict(response.json())

        return response_404
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Details, HTTPValidationError, SheetLayouts]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    sheet_type: SheetType,
    *,
    client: Client,
) -> Response[Union[Details, HTTPValidationError, SheetLayouts]]:
    """Get Image

    Args:
        sheet_type (SheetType): An enumeration.

    Returns:
        Response[Union[Details, HTTPValidationError, SheetLayouts]]
    """

    kwargs = _get_kwargs(
        sheet_type=sheet_type,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    sheet_type: SheetType,
    *,
    client: Client,
) -> Optional[Union[Details, HTTPValidationError, SheetLayouts]]:
    """Get Image

    Args:
        sheet_type (SheetType): An enumeration.

    Returns:
        Response[Union[Details, HTTPValidationError, SheetLayouts]]
    """

    return sync_detailed(
        sheet_type=sheet_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    sheet_type: SheetType,
    *,
    client: Client,
) -> Response[Union[Details, HTTPValidationError, SheetLayouts]]:
    """Get Image

    Args:
        sheet_type (SheetType): An enumeration.

    Returns:
        Response[Union[Details, HTTPValidationError, SheetLayouts]]
    """

    kwargs = _get_kwargs(
        sheet_type=sheet_type,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    sheet_type: SheetType,
    *,
    client: Client,
) -> Optional[Union[Details, HTTPValidationError, SheetLayouts]]:
    """Get Image

    Args:
        sheet_type (SheetType): An enumeration.

    Returns:
        Response[Union[Details, HTTPValidationError, SheetLayouts]]
    """

    return (
        await asyncio_detailed(
            sheet_type=sheet_type,
            client=client,
        )
    ).parsed
