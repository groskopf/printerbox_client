from enum import Enum


class NameTagType(str, Enum):
    VALUE_0 = "4786103"
    VALUE_1 = "4760100"
    VALUE_2 = "47150106"

    def __str__(self) -> str:
        return str(self.value)
