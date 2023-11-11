from fastapi import FastAPI
import modal
import random
from fastapi import FastAPI, HTTPException

class TarotDeck:
    def __init__(self):
        self.cards = self.initialize_deck()

    def initialize_deck(self):
        # Major Arcana Names
        major_arcana_names = [
            "The Fool", "The Magician", "The High Priestess", "The Empress",
            "The Emperor", "The Hierophant", "The Lovers", "The Chariot",
            "Strength", "The Hermit", "Wheel of Fortune", "Justice",
            "The Hanged Man", "Death", "Temperance", "The Devil",
            "The Tower", "The Star", "The Moon", "The Sun",
            "Judgement", "The World"
        ]
        major_arcana = [f"{name}" for name in major_arcana_names]

        # Minor Arcana Names
        suits = ["Cups", "Pentacles", "Swords", "Wands"]
        ranks = [
            "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
            "Nine", "Ten", "Page", "Knight", "Queen", "King"
        ]
        minor_arcana = [f"{rank} of {suit}" for suit in suits for rank in ranks]

        return major_arcana + minor_arcana

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_cards(self, number):
        return [self.cards.pop() for _ in range(number)]


app = FastAPI(servers=[{
    "url": "https://louis-sanna-perso--agent-fastapi-app.modal.run", 
    "description": "Main (production) server"
}])

@app.get("/tarot/reading/")
async def tarot_reading(num_cards: int = 3):
    tarot_deck = TarotDeck()
    # Validate the number of cards
    if num_cards < 1 or num_cards > len(tarot_deck.cards):
        raise HTTPException(status_code=400, detail="Invalid number of cards requested")

    try:
        tarot_deck.shuffle()
        cards = tarot_deck.draw_cards(num_cards)
        return cards
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Modal setup for deployment
stub = modal.Stub("agent")
image = modal.Image.debian_slim().pip_install("fastapi", "httpx")

@stub.function(image=image, keep_warm=1)
@modal.asgi_app()
def fastapi_app():
    return app