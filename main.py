import stock


class Player:
    def __init__(self):
        self.win_count = 0
        self.hands = []
        self.card_current_score = 0

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
                print(f"\ndealer's hands : {self.hands[0]} , *-*")
                print(f"players's total_score : {self.card_current_score}")
                print(f"player draw card is : {self.hands[-1]}")
                self.calc_current_score(self.hands)
                print(f"players's total_score : {self.card_current_score}")

                # バーストでplayerターン強制終了
                if self.is_score_burst(int(self.card_current_score)):
                    print("player burst!!!")
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
        for card in current_hands:
            card_value = self.rank_to_value(str(card))
            self.card_current_score += card_value

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
    def __init__(self):
        super().__init__()

    def keep_drawing_card(self, deck):
        while self.card_current_score < 17:
            self.draw_card(deck)
            print(f"dealer draw card is : {self.hands[-1]}")
            self.calc_current_score(self.hands)
            print(f"dealer's total_score : {self.card_current_score}")
            if self.is_score_burst(self.card_current_score):
                print("dealer burst!!!")


def main():
    # playerとdealer作成
    player = Player()
    dealer = Dealer()

    # 山札セット（セット数を決める）
    deck = stock.Deck()
    # 最初は２枚ずつドロー
    player.draw_card(deck, 2)
    dealer.draw_card(deck, 2)

    # 初期ドロー時のスコア表示（dealer側の1枚は伏せる）
    print(f"dealer's hands : [{dealer.hands[0]}, *-*]")
    print()
    print(f"player's hands : {player.hands}")
    player.calc_current_score(player.hands)
    print(f"players's total_score : {player.card_current_score}")

    # playerに hit or stand 決めさせる（stand で player のターンが終了）
    player.keep_drawing_card(deck)

    print("\n--result--")

    # dealerの手札オープン
    print(f"dealer's hands : {dealer.hands}")
    dealer.calc_current_score(dealer.hands)
    print(f"dealer's total_score : {dealer.card_current_score}")

    # dealerの手札の合計が17になるまで引く
    dealer.keep_drawing_card(deck)

    # 勝敗判定
    judge_win = ""
    if dealer.card_current_score < player.card_current_score <= 21:
        judge_win = "player win!"
        player.win_count += 1
    elif player.card_current_score <= 21 < dealer.card_current_score:
        judge_win = "player win!"
        player.win_count += 1
    elif player.card_current_score == dealer.card_current_score \
            and player.card_current_score <= 21:
        judge_win = "---draw---"
    else:
        judge_win = "dealer win!"
        dealer.win_count += 1
    print(f"\n/***********/\n/{judge_win}/\n/***********/")


if __name__ == '__main__':
    main()
