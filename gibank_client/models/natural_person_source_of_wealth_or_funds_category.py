from enum import Enum


class NaturalPersonSourceOfWealthOrFundsCategory(str, Enum):
    NATURAL_PERSON_SOURCE_OF_WEALTH_OR_FUNDS = (
        "natural_person_source_of_wealth_or_funds"
    )

    def __str__(self) -> str:
        return str(self.value)
