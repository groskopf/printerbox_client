from enum import Enum


class Layout(str, Enum):
    LAYOUT_1 = "layout_1"
    LAYOUT_2 = "layout_2"
    LAYOUT_2PT = "layout_2PT"
    LAYOUT_2PB = "layout_2PB"
    LAYOUT_2PTL = "layout_2PTL"
    LAYOUT_2PTR = "layout_2PTR"
    LAYOUT_2PBL = "layout_2PBL"
    LAYOUT_2PBR = "layout_2PBR"
    LAYOUT_3 = "layout_3"
    LAYOUT_3PT = "layout_3PT"
    LAYOUT_3PB = "layout_3PB"
    LAYOUT_3PTL = "layout_3PTL"
    LAYOUT_3PTR = "layout_3PTR"
    LAYOUT_3PBL = "layout_3PBL"
    LAYOUT_3PBR = "layout_3PBR"
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)
