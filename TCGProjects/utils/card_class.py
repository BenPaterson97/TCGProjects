from typing import Optional

class Card:
    def __init__(self, name: Optional[str] = None):
        self.name = name

    def display(self):
        print(self.name)

class MTGCard(Card):
    def __init__(self, name: Optional[str] = None, is_land: bool = False):
        default_name: str = "Land Card" if is_land else "Non-Land Card"
        super().__init__(name if name is not None else default_name)

        self.is_land: bool = is_land
        self.is_non_land: bool = not is_land

    def get_is_land(self) -> bool:
        return self.is_land

    def get_is_non_land(self) -> bool:
        return self.is_non_land
