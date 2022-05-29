from enum import Enum


class NameTagSheetType(str, Enum):
    VALUE_0 = "453060"
    VALUE_1 = "454070"
    VALUE_2 = "454075"
    VALUE_3 = "454080"
    VALUE_4 = "454880"
    VALUE_5 = "455190"
    VALUE_6 = "4551105"
    VALUE_7 = "456090"
    VALUE_8 = "4560105"
    VALUE_9 = "4574105"
    VALUE_10 = "463770"
    VALUE_11 = "464764"
    VALUE_12 = "4669100"

    def __str__(self) -> str:
        return str(self.value)
