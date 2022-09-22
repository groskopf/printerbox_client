from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.booking import Booking
from ...models.http_validation_error import HTTPValidationError
from ...models.printer_code import PrinterCode
from ...types import Response


def _get_kwargs(
    printer_code: PrinterCode,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/bookings/printer/{printer_code}".format(client.base_url, printer_code=printer_code)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Booking, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = Booking.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Booking, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    printer_code: PrinterCode,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Booking, HTTPValidationError]]:
    """Get Bookings

    Args:
        printer_code (PrinterCode): An enumeration.

    Returns:
        Response[Union[Booking, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        printer_code=printer_code,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    printer_code: PrinterCode,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Booking, HTTPValidationError]]:
    """Get Bookings

    Args:
        printer_code (PrinterCode): An enumeration.

    Returns:
        Response[Union[Booking, HTTPValidationError]]
    """

    return sync_detailed(
        printer_code=printer_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    printer_code: PrinterCode,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Booking, HTTPValidationError]]:
    """Get Bookings

    Args:
        printer_code (PrinterCode): An enumeration.

    Returns:
        Response[Union[Booking, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        printer_code=printer_code,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    printer_code: PrinterCode,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Booking, HTTPValidationError]]:
    """Get Bookings

    Args:
        printer_code (PrinterCode): An enumeration.

    Returns:
        Response[Union[Booking, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            printer_code=printer_code,
            client=client,
        )
    ).parsed
