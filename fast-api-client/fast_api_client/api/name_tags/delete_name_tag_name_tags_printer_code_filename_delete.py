from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.details import Details
from ...models.file_path import FilePath
from ...models.http_validation_error import HTTPValidationError
from ...models.printer_code import PrinterCode
from ...types import Response


def _get_kwargs(
    printer_code: PrinterCode,
    filename: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/name_tags/{printer_code}/{filename}".format(client.base_url, printer_code=printer_code, filename=filename)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Details, FilePath, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = FilePath.from_dict(response.json())

        return response_200
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
    printer_code: PrinterCode,
    filename: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Details, FilePath, HTTPValidationError]]:
    """Delete Name Tag

    Args:
        printer_code (PrinterCode): An enumeration.
        filename (str):

    Returns:
        Response[Union[Details, FilePath, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        printer_code=printer_code,
        filename=filename,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    printer_code: PrinterCode,
    filename: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Details, FilePath, HTTPValidationError]]:
    """Delete Name Tag

    Args:
        printer_code (PrinterCode): An enumeration.
        filename (str):

    Returns:
        Response[Union[Details, FilePath, HTTPValidationError]]
    """

    return sync_detailed(
        printer_code=printer_code,
        filename=filename,
        client=client,
    ).parsed


async def asyncio_detailed(
    printer_code: PrinterCode,
    filename: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Details, FilePath, HTTPValidationError]]:
    """Delete Name Tag

    Args:
        printer_code (PrinterCode): An enumeration.
        filename (str):

    Returns:
        Response[Union[Details, FilePath, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        printer_code=printer_code,
        filename=filename,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    printer_code: PrinterCode,
    filename: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Details, FilePath, HTTPValidationError]]:
    """Delete Name Tag

    Args:
        printer_code (PrinterCode): An enumeration.
        filename (str):

    Returns:
        Response[Union[Details, FilePath, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            printer_code=printer_code,
            filename=filename,
            client=client,
        )
    ).parsed
