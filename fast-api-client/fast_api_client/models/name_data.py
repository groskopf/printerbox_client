from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NameData")


@attr.s(auto_attribs=True)
class NameData:
    """
    Attributes:
        line_1 (str):
        line_2 (Union[Unset, str]):
        line_3 (Union[Unset, str]):
        line_4 (Union[Unset, str]):
        line_5 (Union[Unset, str]):
        image_name (Union[Unset, str]):
        qr_code (Union[Unset, str]):
    """

    line_1: str
    line_2: Union[Unset, str] = UNSET
    line_3: Union[Unset, str] = UNSET
    line_4: Union[Unset, str] = UNSET
    line_5: Union[Unset, str] = UNSET
    image_name: Union[Unset, str] = UNSET
    qr_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_1 = self.line_1
        line_2 = self.line_2
        line_3 = self.line_3
        line_4 = self.line_4
        line_5 = self.line_5
        image_name = self.image_name
        qr_code = self.qr_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "line_1": line_1,
            }
        )
        if line_2 is not UNSET:
            field_dict["line_2"] = line_2
        if line_3 is not UNSET:
            field_dict["line_3"] = line_3
        if line_4 is not UNSET:
            field_dict["line_4"] = line_4
        if line_5 is not UNSET:
            field_dict["line_5"] = line_5
        if image_name is not UNSET:
            field_dict["imageName"] = image_name
        if qr_code is not UNSET:
            field_dict["qr_code"] = qr_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line_1 = d.pop("line_1")

        line_2 = d.pop("line_2", UNSET)

        line_3 = d.pop("line_3", UNSET)

        line_4 = d.pop("line_4", UNSET)

        line_5 = d.pop("line_5", UNSET)

        image_name = d.pop("imageName", UNSET)

        qr_code = d.pop("qr_code", UNSET)

        name_data = cls(
            line_1=line_1,
            line_2=line_2,
            line_3=line_3,
            line_4=line_4,
            line_5=line_5,
            image_name=image_name,
            qr_code=qr_code,
        )

        name_data.additional_properties = d
        return name_data

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
