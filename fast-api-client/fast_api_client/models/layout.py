from enum import Enum


class Layout(str, Enum):
    LAYOUT_1 = "layout_1"
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)
