class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_card(self, card):
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()