import deck


class Player:
    def __init__(self):
        self.win_count = 0
        self.hands = []
        self.card_total_score_main = 0
        self.card_total_score_sub = 0

    def draw_card(self, num=1):
        self.hands.append(deck.draw_card(num))

    def rank_to_value(self, card_rank):
        """
        カードのRANKから数値を返す
        Aは1, 11、JQKは10としてスコア計算

        Parameters
        ----------
        card_rank : int, default 1
            カードのRANK（A23〜JQK）

        Returns
        --------
        card_value_list : list
            カードの数値リスト

        Examples
        --------
        >>> rank_to_value('♣️-Q')
        [10]
        >>> rank_to_value('♣️-A')
        [1, 11]
        """
        # ♣️-9 → 9
        card_number = card_rank.split("-")[1]
        if card_number == "A":
            card_value_list = [1, 11]
        elif card_number in [*"JQK"]:
            card_value_list = [10]
        else:
            card_value_list = [int(card_number)]
        return card_value_list

    # def calc_total_score(self):
        # return


if __name__ == '__main__':
    player = Player()
    deck = deck.Deck(1)
    player.draw_card()
    # print(player.hands)
    print(player.rank_to_value('♣️-Q'))
