from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.layout import Layout
from ..models.name_tag_sheet_type import NameTagSheetType

T = TypeVar("T", bound="NameTagSheetLayouts")


@attr.s(auto_attribs=True)
class NameTagSheetLayouts:
    """
    Attributes:
        name_tag_sheet_type (NameTagSheetType): An enumeration.
        layouts (List[Layout]):
    """

    name_tag_sheet_type: NameTagSheetType
    layouts: List[Layout]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name_tag_sheet_type = self.name_tag_sheet_type.value

        layouts = []
        for layouts_item_data in self.layouts:
            layouts_item = layouts_item_data.value

            layouts.append(layouts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name_tag_sheet_type": name_tag_sheet_type,
                "layouts": layouts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name_tag_sheet_type = NameTagSheetType(d.pop("name_tag_sheet_type"))

        layouts = []
        _layouts = d.pop("layouts")
        for layouts_item_data in _layouts:
            layouts_item = Layout(layouts_item_data)

            layouts.append(layouts_item)

        name_tag_sheet_layouts = cls(
            name_tag_sheet_type=name_tag_sheet_type,
            layouts=layouts,
        )

        name_tag_sheet_layouts.additional_properties = d
        return name_tag_sheet_layouts

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
