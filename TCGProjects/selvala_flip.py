from utils.deck_class import CommanderDeck

selvala_deck: CommanderDeck = CommanderDeck(
    name="Selvala cEDH",
    colour_identity="Selesnya"
)

selvala_deck.initialise_deck_list(land_count=21, card_count=99)

blue_farm_deck: CommanderDeck = CommanderDeck(
    name="Blue Farm",
    colour_identity="Sans Green",
    min_deck_count=98
)

blue_farm_deck.initialise_deck_list(land_count=29, card_count=98)

winota_deck: CommanderDeck = CommanderDeck(
    name="Winota cEDH",
    colour_identity="Boros"
)

winota_deck.initialise_deck_list(land_count=29, card_count=99)

rodge_si_deck: CommanderDeck = CommanderDeck(
    name="Rodger/Silas",
    colour_identity="Grixis"
)

rodge_si_deck.initialise_deck_list(land_count=26, card_count=99)

def resolve_selvala_flip(decks: list[CommanderDeck]) -> int:
    # Function that returns the amount of mana produced by a selvala flip
    total_mana_produced: int = 0
    for deck in decks:
        total_mana_produced += deck.selvala_flip()
    print(f"This selvala flip has produced {total_mana_produced} green mana.")
    return total_mana_produced


selvala_deck.shuffle()
blue_farm_deck.shuffle()
winota_deck.shuffle()
rodge_si_deck.shuffle()

mana_pool: int = resolve_selvala_flip([selvala_deck, blue_farm_deck, winota_deck, rodge_si_deck])
