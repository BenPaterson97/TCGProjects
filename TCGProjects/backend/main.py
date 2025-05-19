from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import sys
import os

# Add the parent directory to Python path to import selvala_flip
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selvala_flip import CommanderDeck, resolve_selvala_flip

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize decks
selvala_deck = CommanderDeck(name="Selvala cEDH", colour_identity="Selesnya")
blue_farm_deck = CommanderDeck(
    name="Blue Farm", colour_identity="Sans Green", min_deck_count=98
)
winota_deck = CommanderDeck(name="Winota cEDH", colour_identity="Boros")
rodge_si_deck = CommanderDeck(name="Rodger/Silas", colour_identity="Grixis")

# Initialize deck lists
selvala_deck.initialise_deck_list(land_count=21, card_count=99)
blue_farm_deck.initialise_deck_list(land_count=29, card_count=98)
winota_deck.initialise_deck_list(land_count=29, card_count=99)
rodge_si_deck.initialise_deck_list(land_count=26, card_count=99)

# Shuffle decks
selvala_deck.shuffle()
blue_farm_deck.shuffle()
winota_deck.shuffle()
rodge_si_deck.shuffle()


@app.get("/flip")
async def flip():
    mana_produced = resolve_selvala_flip(
        [selvala_deck, blue_farm_deck, winota_deck, rodge_si_deck]
    )
    return {"mana_produced": mana_produced}


@app.post("/reset")
async def reset():
    # Reinitialize and shuffle decks
    selvala_deck.initialise_deck_list(land_count=21, card_count=99)
    blue_farm_deck.initialise_deck_list(land_count=29, card_count=98)
    winota_deck.initialise_deck_list(land_count=29, card_count=99)
    rodge_si_deck.initialise_deck_list(land_count=26, card_count=99)

    selvala_deck.shuffle()
    blue_farm_deck.shuffle()
    winota_deck.shuffle()
    rodge_si_deck.shuffle()

    return {"message": "Decks reset successfully"}
