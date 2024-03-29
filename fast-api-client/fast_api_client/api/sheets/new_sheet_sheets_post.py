from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.details import Details
from ...models.file_path import FilePath
from ...models.http_validation_error import HTTPValidationError
from ...models.layout import Layout
from ...models.name_data import NameData
from ...models.sheet_type import SheetType
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: List[NameData],
    sheet_type: SheetType,
    layout: Layout,
) -> Dict[str, Any]:
    url = "{}/sheets/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_sheet_type = sheet_type.value

    params["sheet_type"] = json_sheet_type

    json_layout = layout.value

    params["layout"] = json_layout

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

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
    json_body: List[NameData],
    sheet_type: SheetType,
    layout: Layout,
) -> Response[Union[Details, FilePath, HTTPValidationError]]:
    """New Sheet

    Args:
        sheet_type (SheetType): An enumeration.
        layout (Layout): An enumeration.
        json_body (List[NameData]):

    Returns:
        Response[Union[Details, FilePath, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        sheet_type=sheet_type,
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
    json_body: List[NameData],
    sheet_type: SheetType,
    layout: Layout,
) -> Optional[Union[Details, FilePath, HTTPValidationError]]:
    """New Sheet

    Args:
        sheet_type (SheetType): An enumeration.
        layout (Layout): An enumeration.
        json_body (List[NameData]):

    Returns:
        Response[Union[Details, FilePath, HTTPValidationError]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        sheet_type=sheet_type,
        layout=layout,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: List[NameData],
    sheet_type: SheetType,
    layout: Layout,
) -> Response[Union[Details, FilePath, HTTPValidationError]]:
    """New Sheet

    Args:
        sheet_type (SheetType): An enumeration.
        layout (Layout): An enumeration.
        json_body (List[NameData]):

    Returns:
        Response[Union[Details, FilePath, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        sheet_type=sheet_type,
        layout=layout,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: List[NameData],
    sheet_type: SheetType,
    layout: Layout,
) -> Optional[Union[Details, FilePath, HTTPValidationError]]:
    """New Sheet

    Args:
        sheet_type (SheetType): An enumeration.
        layout (Layout): An enumeration.
        json_body (List[NameData]):

    Returns:
        Response[Union[Details, FilePath, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            sheet_type=sheet_type,
            layout=layout,
        )
    ).parsed
