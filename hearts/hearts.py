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



h = Hearts()
print(h.play_trick([Deck.C2, Deck.C3, Deck.C4, Deck.C5]))
print(h.play_trick([Deck.C6, Deck.C7, Deck.C8, Deck.C9]))
print(h.play_trick([Deck.C10, Deck.CJ, Deck.CQ, Deck.CK]))
print(h.play_trick([Deck.CA, Deck.D2, Deck.D3, Deck.D4]))
print(h.play_trick([Deck.D5, Deck.D6, Deck.D7, Deck.D8]))
print(h.play_trick([Deck.D9, Deck.D10, Deck.DJ, Deck.DQ]))
print(h.play_trick([Deck.DK, Deck.DA, Deck.H2, Deck.H3]))
print(h.play_trick([Deck.H4, Deck.H5, Deck.H6, Deck.H7]))
print(h.play_trick([Deck.H8, Deck.H9, Deck.H10, Deck.HJ]))
print(h.play_trick([Deck.HQ, Deck.HK, Deck.HA, Deck.S2]))
print(h.play_trick([Deck.S3, Deck.S4, Deck.S5, Deck.S6]))
print(h.play_trick([Deck.S7, Deck.S8, Deck.S9, Deck.S10]))
print(h.play_trick([Deck.SJ, Deck.SQ, Deck.SK, Deck.SA]))

print(h.player_cards)
print(h.check_winner())