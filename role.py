from bj import BlackJack


class Player:
    """
    子（手動で操作できるプレイヤー）
    """

    def __init__(self):
        self.win_count = 0
        self.hands = []
        self.card_current_score = 0
        self.card_current_score_sub = 0
        self.has_A_card = False

    def keep_drawing_card(self, deck):
        """
        playerに hit or stand 決めさせる
        （stand で player のターンが終了）

        Parameters
        ----------
        deck : deck
            カードひと組
        """
        want_to_draw = True
        while want_to_draw:
            hit_or_stand_msg = "\nHit(1) or Stand(2) : "
            hit_or_stand_res = input(hit_or_stand_msg)
            if hit_or_stand_res == "1":
                # hit の場合は1枚ドロー
                self.draw_card(deck)
                print(f"player draw card is : {self.hands[-1]}")
                BlackJack.calc_current_score(self)
                sub_score = ""
                if self.has_A_card is True:
                    sub_score = \
                        f", {self.card_current_score_sub}"
                print(
                    f"players's total_score : \
{self.card_current_score}{sub_score}")

                # バーストでplayerターン強制終了
                if BlackJack.is_score_bust(int(self.card_current_score)) and \
                    BlackJack.is_score_bust(
                        int(self.card_current_score_sub)):
                    print("player bust!!!")
                    want_to_draw = False

                if self.card_current_score == 21 or \
                        self.card_current_score_sub == 21:
                    # 21になった時点で強制終了
                    want_to_draw = False

            elif hit_or_stand_res == "2":
                # standの場合はターン終了
                want_to_draw = False
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


class Dealer(Player):
    """
    親（自動操作）
    """

    def keep_drawing_card(self, deck):
        """
        dealerは17超えるまで自動でカードを引き続ける
        17超えたら終了

        Parameters
        ----------
        deck : object
            現在の手札
        """
        self.has_A_card = False
        while self.card_current_score < 17 or \
                self.card_current_score_sub < 17:
            self.draw_card(deck)
            print(f"dealer draw card is : {self.hands[-1]}")
            BlackJack.calc_current_score(self)
            sub_score = ""
            if self.has_A_card:
                sub_score = \
                    f", {self.card_current_score_sub}"
            print(
                f"dealer's total_score : {self.card_current_score}{sub_score}")
            if BlackJack.is_score_bust(self.card_current_score) and \
                    BlackJack.is_score_bust(
                    int(self.card_current_score_sub)):
                print("dealer bust!!!")
