from deck import Deck, Suits

class Hearts:
    def __init__(self, n_players = 0):
        self.used_cards = [False] * 52
        self.trick = 1
        self.n_players = n_players
        self.player_cards = [[] for _ in range(n_players)]

    def play_trick(self, cards):
        if self.n_players == 0:
            self.n_players = len(cards)
            self.player_cards = [[] for _ in range(self.n_players)]
            print(self.player_cards)
        
        if self.n_players != len(cards):
            return -1

        if len(cards) != len(set(cards)):
            return -2

        if self.trick == 1:
            if Deck.C2 in cards:
                self.lead = cards.index(Deck.C2)
            else:
                return -3
        
        lead_suit = cards[self.lead] % 4
        winner = self.lead

        for i in range(self.lead, self.lead + self.n_players):
            index = i % 4
            if self.used_cards[cards[index]]:
                return -4
            if cards[index] % 4 != lead_suit:
                continue
            if cards[index] > cards[winner]:
                winner = index


        for card in cards:
            self.used_cards[card] = True
        self.lead = winner
        self.player_cards[winner] += cards
        self.trick += 1

        return winner

    def check_winner(self):
        if self.trick > 52/self.n_players:
            maximum = -1
            winner = -1
            for i in range(4):
                score = 0
                for card in self.player_cards[i]:
                    if card/4 == Suits.HEARTS:
                        score += 1
                if score > maximum:
                    maximum = score
                    winner = i
            return winner
        else:
            return -1
