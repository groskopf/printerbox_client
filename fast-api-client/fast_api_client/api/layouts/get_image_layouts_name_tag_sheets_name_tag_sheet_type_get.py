from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.details import Details
from ...models.http_validation_error import HTTPValidationError
from ...models.name_tag_sheet_layouts import NameTagSheetLayouts
from ...models.name_tag_sheet_type import NameTagSheetType
from ...types import Response


def _get_kwargs(
    name_tag_sheet_type: NameTagSheetType,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/layouts/name_tag_sheets/{name_tag_sheet_type}".format(
        client.base_url, name_tag_sheet_type=name_tag_sheet_type
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Details, HTTPValidationError, NameTagSheetLayouts]]:
    if response.status_code == 200:
        response_200 = NameTagSheetLayouts.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Details.from_dict(response.json())

        return response_404
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Details, HTTPValidationError, NameTagSheetLayouts]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    name_tag_sheet_type: NameTagSheetType,
    *,
    client: Client,
) -> Response[Union[Details, HTTPValidationError, NameTagSheetLayouts]]:
    """Get Image

    Args:
        name_tag_sheet_type (NameTagSheetType): An enumeration.

    Returns:
        Response[Union[Details, HTTPValidationError, NameTagSheetLayouts]]
    """

    kwargs = _get_kwargs(
        name_tag_sheet_type=name_tag_sheet_type,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    name_tag_sheet_type: NameTagSheetType,
    *,
    client: Client,
) -> Optional[Union[Details, HTTPValidationError, NameTagSheetLayouts]]:
    """Get Image

    Args:
        name_tag_sheet_type (NameTagSheetType): An enumeration.

    Returns:
        Response[Union[Details, HTTPValidationError, NameTagSheetLayouts]]
    """

    return sync_detailed(
        name_tag_sheet_type=name_tag_sheet_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    name_tag_sheet_type: NameTagSheetType,
    *,
    client: Client,
) -> Response[Union[Details, HTTPValidationError, NameTagSheetLayouts]]:
    """Get Image

    Args:
        name_tag_sheet_type (NameTagSheetType): An enumeration.

    Returns:
        Response[Union[Details, HTTPValidationError, NameTagSheetLayouts]]
    """

    kwargs = _get_kwargs(
        name_tag_sheet_type=name_tag_sheet_type,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    name_tag_sheet_type: NameTagSheetType,
    *,
    client: Client,
) -> Optional[Union[Details, HTTPValidationError, NameTagSheetLayouts]]:
    """Get Image

    Args:
        name_tag_sheet_type (NameTagSheetType): An enumeration.

    Returns:
        Response[Union[Details, HTTPValidationError, NameTagSheetLayouts]]
    """

    return (
        await asyncio_detailed(
            name_tag_sheet_type=name_tag_sheet_type,
            client=client,
        )
    ).parsed
