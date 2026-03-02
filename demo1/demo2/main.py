# 如果__init_中什么都没定义，则用如下定义：
# from poker.deck import Deck
# from poker.player import Player

# 定义了可用如下定义：
from poker import Deck, Player

def main():
    deck = Deck()
    deck.shuffle()

    players = [
        Player("East"),
        Player("West"),
        Player("South"),
        Player("North")
    ]

    for _ in range(13):
        for player in players:
            player.get_card(deck.deal())

    for player in players:
        player.arrange()
        print(player.name, player.cards)

if __name__ == "__main__":
    main()