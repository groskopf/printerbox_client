from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.layout import Layout
from ..models.sheet_type import SheetType

T = TypeVar("T", bound="SheetLayouts")


@attr.s(auto_attribs=True)
class SheetLayouts:
    """
    Attributes:
        sheet_type (SheetType): An enumeration.
        layouts (List[Layout]):
    """

    sheet_type: SheetType
    layouts: List[Layout]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sheet_type = self.sheet_type.value

        layouts = []
        for layouts_item_data in self.layouts:
            layouts_item = layouts_item_data.value

            layouts.append(layouts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sheet_type": sheet_type,
                "layouts": layouts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sheet_type = SheetType(d.pop("sheet_type"))

        layouts = []
        _layouts = d.pop("layouts")
        for layouts_item_data in _layouts:
            layouts_item = Layout(layouts_item_data)

            layouts.append(layouts_item)

        sheet_layouts = cls(
            sheet_type=sheet_type,
            layouts=layouts,
        )

        sheet_layouts.additional_properties = d
        return sheet_layouts

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
