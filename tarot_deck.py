import random

class TarotDeck:
    def __init__(self):
        self.cards = self.initialize_deck()
        self.shuffle()

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