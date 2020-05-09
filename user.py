import deck
# 2次元のリストを平坦化
import itertools


class Player:
    def __init__(self):
        self.win_count = 0
        self.hands = []
        self.card_total_list_main = []
        self.card_total_score_sub = []

    def draw_card(self, num=1):
        """
        カードをデッキからドローし手札に加える
        ※異なる枚数がドローされてもok

        Parameters
        ----------
        num : int, default 1
            カードをドローする回数

        Examples
        --------
        >>> player.draw_card(2) # 2枚ドロー
        [♠︎-J, ♠︎-10]
        >>> player.draw_card(3)
        [♦︎-9, ♣️-10, ♠︎-2]
        >>> print(player.hands)
        [♠︎-J, ♠︎-10, ♦︎-9, ♣️-10, ♠︎-2]
        """
        self.hands_store = deck.draw_card(num)
        # print(self.hands_store)
        self.hands.extend(self.hands_store)

    def rank_to_value(self, card_rank):
        """
        カードのRANKから数値を返す
        Aは1、JQKは10としてスコア計算

        Parameters
        ----------
        card_rank : int, default 1
            カードのRANK（A23〜JQK）

        Returns
        --------
        card_value : int
            カードの数値

        Examples
        --------
        >>> rank_to_value('♣️-Q')
        10
        >>> rank_to_value('♣️-A')
        1
        """
        # ♣️-9 → 9
        card_number = card_rank.split("-")[1]
        if card_number == "A":
            card_value = 1
        elif card_number in [*"JQK"]:
            card_value = 10
        else:
            card_value = int(card_number)
        self.card_total_list_main.append(card_value)
        return card_value

    # def calc_total_score(self):
        # return


if __name__ == '__main__':
    player = Player()
    dealer = Player()

    deck = deck.Deck(1)

    player.draw_card()
    player.draw_card()
    dealer.draw_card()
    dealer.draw_card()

    # player's hands : [♦︎-J, ♦︎-8]
    print(f"player's hands : {player.hands}")
    # dealer's hands : [♣️-5, ♦︎-K]
    print(f"dealer's hands : {dealer.hands}")
