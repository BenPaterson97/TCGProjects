from utils.card_class import Card, MTGCard
from typing import Optional
import random

class Deck():
    def __init__(
        self,
        name: str = "New Deck",
        max_deck_count: Optional[int] = None,
        min_deck_count: Optional[int] = None,
        deck_list: list = []
    ) -> None:
        self.name: str = name
        self.max_deck_count: Optional[int] = max_deck_count
        self.min_deck_count: Optional[int] = min_deck_count
        self.deck_list: list = deck_list
        self.current_deck_list: list = deck_list
        self.empty_deck_message: str = "You lose the game!"

        if self.max_deck_count is not None and self.min_deck_count is not None:
            if self.max_deck_count < self.min_deck_count:
                raise ValueError("The min deck count must be less than the max deck count.")

    def display(self) -> None:
        for card in self.current_deck_list:
            card.display()
        print(f"Card Count: {len(self.current_deck_list)}")
    
    def shuffle(self) -> None:
        random.shuffle(self.current_deck_list)
        print(f"{self.name}: Deck shuffled!")

    def _get_top_card(self) -> Optional[Card]:
        if len(self.current_deck_list) > 0:
            return self.current_deck_list[-1]
        else:
            print("Cannot get the top card of the deck since it has no cards.")
            return None

    def reveal_top_card(self) -> Optional[Card]:
        top_card: Optional[Card] = self._get_top_card()
        if top_card is not None:
            top_card.display()
        return top_card

    def _draw(self) -> None:
        # Draws one card
        if len(self.current_deck_list) == 0:
            print(f"You are attempting to draw from an empty deck. {self.empty_deck_message}")
        else:
            self.current_deck_list.pop()

    def draw(self, cards_to_draw: int = 1) -> None:
        if cards_to_draw <= 0:
            print(f"{cards_to_draw} is an inappropriate number of cards to draw.")
            return
        for _ in range(cards_to_draw):
            self._draw()

    def selvala_flip(self) -> int:
        # Resolves a selvala flip for 1 deck. Returns the mana produced.
        top_card: Optional[Card] = self.reveal_top_card()
        if top_card is None or top_card.get_is_land():
            mana_produced: int = 0
        else:
            mana_produced = 1
        self.draw()
        return mana_produced

class MTGDeck(Deck):
    def __init__(
        self,
        colour_identity: str,
        name: str = "New MTG Deck",
        min_deck_count: int = 60,
        max_deck_count: Optional[int] = None,
        deck_list: list = []
    ):
        super().__init__(name, max_deck_count, min_deck_count, deck_list)
        self.colour_identity: str = colour_identity

    def initialise_deck_list(
        self,
        land_count: int,
        card_count: Optional[int] = None
    ):
        total_card_count: int = self.min_deck_count if card_count is None else card_count
        base_list: list[MTGCard] = [MTGCard(is_land=True) for _ in range(land_count)]
        for _ in range(land_count, total_card_count):
            base_list.append(MTGCard())
        if self.max_deck_count is not None and len(base_list) > self.max_deck_count:
            raise ValueError(f"Deck list cannot exceed {self.max_deck_count}.")
        self.deck_list = base_list
        self.current_deck_list = base_list

class CommanderDeck(MTGDeck):
    def __init__(
        self,
        name: str = "New Commander Deck",
        colour_identity: str = "Generic",
        min_deck_count: int = 99,
        max_deck_count: Optional[int] = None,
        deck_list: list = []
    ):
        super().__init__(colour_identity, name, min_deck_count, max_deck_count, deck_list)
