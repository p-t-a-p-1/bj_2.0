import deck
# 2次元のリストを平坦化
import itertools


class Player:
    def __init__(self):
        self.win_count = 0
        self.hands = []
        self.card_curennt_score = 0

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
        return card_value

    def calc_curennt_score(self, current_hands):
        for card in current_hands:
            card_value = self.rank_to_value(str(card))
            self.card_curennt_score += card_value

    def want_draw(self):
        return self.card_curennt_score < 17


if __name__ == '__main__':
    # playerとdealer作成
    player = Player()
    dealer = Player()

    # 山札セット（セット数を決める）
    deck = deck.Deck(1)

    # 最初は２枚ずつドロー
    player.draw_card(2)
    dealer.draw_card(2)

    # 初期ドロー時のスコア表示（dealer側の1枚は伏せる）
    print(f"dealer's hands : [{dealer.hands[0]}, *-*]")
    print()
    print(f"player's hands : {player.hands}")
    player.calc_curennt_score(player.hands)
    print(f"players's total_socre : {player.card_curennt_score}")

    # playerに hit or stand 決めさせる
    hit_flg = True
    while hit_flg is True:
        hit_or_stand_msg = "\nHit(1) or Stand(2) : "
        hit_or_stand_res = input(hit_or_stand_msg)
        if hit_or_stand_res == "1":
            # hit の場合は1枚ドロー
            player.draw_card()
            print(f"dealer's hands : {dealer.hands[0]} , *-*")
            print(f"players's total_socre : {player.card_curennt_score}")
            print(f"player draw card is : {player.hands[-1]}")
            player.calc_curennt_score(player.hands)
            print(f"players's total_socre : {player.card_curennt_score}")
        elif hit_or_stand_res == "2":
            hit_flg = False
        else:
            print("ダメです")
