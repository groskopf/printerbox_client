import datetime
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.booking import Booking
from ...models.details import Details
from ...models.http_validation_error import HTTPValidationError
from ...models.name_tag_type import NameTagType
from ...models.printer_code import PrinterCode
from ...types import UNSET, Response


def _get_kwargs(
    booking_code: str,
    *,
    client: AuthenticatedClient,
    start_date: datetime.date,
    end_date: datetime.date,
    printer_code: PrinterCode,
    name_tag_type: NameTagType,
) -> Dict[str, Any]:
    url = "{}/bookings/{booking_code}".format(client.base_url, booking_code=booking_code)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    json_printer_code = printer_code.value

    params["printer_code"] = json_printer_code

    json_name_tag_type = name_tag_type.value

    params["name_tag_type"] = json_name_tag_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Booking, Details, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = Booking.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Details.from_dict(response.json())

        return response_404
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Booking, Details, HTTPValidationError]]:
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
    start_date: datetime.date,
    end_date: datetime.date,
    printer_code: PrinterCode,
    name_tag_type: NameTagType,
) -> Response[Union[Booking, Details, HTTPValidationError]]:
    """Update Booking

    Args:
        booking_code (str):
        start_date (datetime.date):
        end_date (datetime.date):
        printer_code (PrinterCode): An enumeration.
        name_tag_type (NameTagType): An enumeration.

    Returns:
        Response[Union[Booking, Details, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        booking_code=booking_code,
        client=client,
        start_date=start_date,
        end_date=end_date,
        printer_code=printer_code,
        name_tag_type=name_tag_type,
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
    start_date: datetime.date,
    end_date: datetime.date,
    printer_code: PrinterCode,
    name_tag_type: NameTagType,
) -> Optional[Union[Booking, Details, HTTPValidationError]]:
    """Update Booking

    Args:
        booking_code (str):
        start_date (datetime.date):
        end_date (datetime.date):
        printer_code (PrinterCode): An enumeration.
        name_tag_type (NameTagType): An enumeration.

    Returns:
        Response[Union[Booking, Details, HTTPValidationError]]
    """

    return sync_detailed(
        booking_code=booking_code,
        client=client,
        start_date=start_date,
        end_date=end_date,
        printer_code=printer_code,
        name_tag_type=name_tag_type,
    ).parsed


async def asyncio_detailed(
    booking_code: str,
    *,
    client: AuthenticatedClient,
    start_date: datetime.date,
    end_date: datetime.date,
    printer_code: PrinterCode,
    name_tag_type: NameTagType,
) -> Response[Union[Booking, Details, HTTPValidationError]]:
    """Update Booking

    Args:
        booking_code (str):
        start_date (datetime.date):
        end_date (datetime.date):
        printer_code (PrinterCode): An enumeration.
        name_tag_type (NameTagType): An enumeration.

    Returns:
        Response[Union[Booking, Details, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        booking_code=booking_code,
        client=client,
        start_date=start_date,
        end_date=end_date,
        printer_code=printer_code,
        name_tag_type=name_tag_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    booking_code: str,
    *,
    client: AuthenticatedClient,
    start_date: datetime.date,
    end_date: datetime.date,
    printer_code: PrinterCode,
    name_tag_type: NameTagType,
) -> Optional[Union[Booking, Details, HTTPValidationError]]:
    """Update Booking

    Args:
        booking_code (str):
        start_date (datetime.date):
        end_date (datetime.date):
        printer_code (PrinterCode): An enumeration.
        name_tag_type (NameTagType): An enumeration.

    Returns:
        Response[Union[Booking, Details, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            booking_code=booking_code,
            client=client,
            start_date=start_date,
            end_date=end_date,
            printer_code=printer_code,
            name_tag_type=name_tag_type,
        )
    ).parsed
