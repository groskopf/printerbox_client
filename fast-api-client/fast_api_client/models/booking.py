import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.name_tag_type import NameTagType
from ..models.printer_code import PrinterCode

T = TypeVar("T", bound="Booking")


@attr.s(auto_attribs=True)
class Booking:
    """
    Attributes:
        start_date (datetime.date):
        end_date (datetime.date):
        printer_code (PrinterCode): An enumeration.
        code (str):
        name_tag_type (NameTagType): An enumeration.
    """

    start_date: datetime.date
    end_date: datetime.date
    printer_code: PrinterCode
    code: str
    name_tag_type: NameTagType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date = self.start_date.isoformat()
        end_date = self.end_date.isoformat()
        printer_code = self.printer_code.value

        code = self.code
        name_tag_type = self.name_tag_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_date": start_date,
                "end_date": end_date,
                "printer_code": printer_code,
                "code": code,
                "name_tag_type": name_tag_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_date = isoparse(d.pop("start_date")).date()

        end_date = isoparse(d.pop("end_date")).date()

        printer_code = PrinterCode(d.pop("printer_code"))

        code = d.pop("code")

        name_tag_type = NameTagType(d.pop("name_tag_type"))

        booking = cls(
            start_date=start_date,
            end_date=end_date,
            printer_code=printer_code,
            code=code,
            name_tag_type=name_tag_type,
        )

        booking.additional_properties = d
        return booking

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
