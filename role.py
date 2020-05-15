class Player:
    """
    子（手動で操作できるプレイヤー）
    """

    def __init__(self):
        self.win_count = 0
        self.hands = []
        self.card_current_score = 0
        self.card_current_score_sub = 0
        self.draw_A_flg = False

    def keep_drawing_card(self, deck):
        """
        playerに hit or stand 決めさせる
        （stand で player のターンが終了）

        Parameters
        ----------
        deck : deck
            カードひと組
        """
        hit_flg = True
        while hit_flg is True:
            hit_or_stand_msg = "\nHit(1) or Stand(2) : "
            hit_or_stand_res = input(hit_or_stand_msg)
            if hit_or_stand_res == "1":
                # hit の場合は1枚ドロー
                self.draw_card(deck)
                print(f"player draw card is : {self.hands[-1]}")
                self.calc_current_score(self.hands)
                sub_score = ""
                if self.draw_A_flg is True:
                    sub_score = \
                        f", {self.card_current_score_sub}"
                print(
                    f"players's total_score : \
{self.card_current_score}{sub_score}")

                # バーストでplayerターン強制終了
                if self.is_score_burst(int(self.card_current_score)) and \
                    self.is_score_burst(
                        int(self.card_current_score_sub)):
                    print("player burst!!!")
                    hit_flg = False

                if self.card_current_score == 21 or \
                        self.card_current_score_sub == 21:
                    # 21になった時点で強制終了
                    hit_flg = False

            elif hit_or_stand_res == "2":
                # standの場合はターン終了
                hit_flg = False
            else:
                # 1, 2以外のコマンドは再度入力させる
                print("ダメです")

    def draw_card(self, deck, num=1):
        """
        カードをデッキからドローし手札に加える
        ※異なる枚数がドローされてもok

        Parameters
        ----------
        num : int, default 1
            カードをドローする回数

        Examples
        --------
        >>> player.draw_card(2) # 2枚ドロー [♠︎-J, ♠︎-10]
        >>> player.draw_card(3) # [♦︎-9, ♣️-10, ♠︎-2]
        >>> print(player.hands)
        [♠︎-J, ♠︎-10, ♦︎-9, ♣️-10, ♠︎-2]
        """
        self.hands_store = deck.pick_card(num)
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

    def calc_current_score(self, current_hands):
        """
        現在のスコアを計算

        Parameters
        ----------
        current_hands : list
            現在の手札

        Returns
        --------
        card_current_score : int
            現在のスコア
        """
        self.card_current_score = 0
        self.card_current_score_sub = 0
        self.draw_A_flg = False
        for card in current_hands:
            card_value = self.rank_to_value(str(card))
            # Aの時も考慮
            self.card_current_score += card_value
            self.card_current_score_sub += card_value
            if card_value == 1:
                if self.draw_A_flg is True:
                    # Aが連続した時サブスコアで2重でサブスコア加算されるので+10(+11-1)
                    self.card_current_score_sub += 10
                    print(self.card_current_score_sub)
                    continue
                self.draw_A_flg = True
                self.card_current_score_sub += 11

    def is_score_burst(self, total_score):
        """
        現在のスコアを計算

        Parameters
        ----------
        current_hands : list
            現在の手札

        Returns
        --------
        True or False
            バーストでTrue
        """
        return total_score > 21


class Dealer(Player):
    """
    親（自動操作）
    """

    def __init__(self):
        super().__init__()

    def keep_drawing_card(self, deck):
        """
        dealerは17超えるまで自動でカードを引き続ける
        17超えたら終了

        Parameters
        ----------
        deck : object
            現在の手札
        """
        self.draw_A_flg = False
        while self.card_current_score < 17 or \
                self.card_current_score_sub < 17:
            self.draw_card(deck)
            print(f"dealer draw card is : {self.hands[-1]}")
            self.calc_current_score(self.hands)
            sub_score = ""
            if self.draw_A_flg is True:
                sub_score = \
                    f", {self.card_current_score_sub}"
            print(
                f"dealer's total_score : {self.card_current_score}{sub_score}")
            if self.is_score_burst(self.card_current_score) and \
                    self.is_score_burst(
                    int(self.card_current_score_sub)):
                print("dealer burst!!!")
