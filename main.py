import stock
import role


class Game:
    """
    メインゲーム（インスタンス作成時にplayerとdealerインスタンス作成）

    Examples
    --------
    >>> game = Game()
    >>> game.main() # ゲームスタート（下記の初期フェーズが表示）
    dealer's hands : [❤︎-7, *-*]

    player's hands : [♠︎-9, ♦︎-J]
    players's total_score : 19

    Hit(1) or Stand(2) :
    """

    def __init__(self):
        # playerとdealer作成
        self.player = role.Player()
        self.dealer = role.Dealer()

    def judge_winner(self, dealer, player):
        """
        勝敗判定

        Parameters
        ----------
        dealer : object
            親
        player : object
            子
        """

        judge_win = ""
        if dealer.card_current_score < \
                player.card_current_score <= 21:
            # dealer < player <= 21の時、playerの勝利
            judge_win = "player win!"
            player.win_count += 1
        elif player.card_current_score <= 21 \
                < dealer.card_current_score:
            # player が21以下、dealerがバーストはplayerの勝利
            judge_win = "player win!"
            player.win_count += 1
        elif player.card_current_score == dealer.card_current_score \
                and player.card_current_score <= 21:
            # どちらもバーストせず、同じ数字の場合は引き分け
            judge_win = "---draw---"
        else:
            # それ以外の場合は全部playerの負け
            judge_win = "dealer win!"
            dealer.win_count += 1
        print(f"\n/***********/\n/{judge_win}/\n/***********/")

    def main(self):
        """
        ブラックジャックのメインゲーム関数
        """

        # 山札セット（セット数を決める）
        deck = stock.Deck()
        # 最初は２枚ずつドロー
        self.player.draw_card(deck, 2)
        self.dealer.draw_card(deck, 2)
        # player初期スコア計算
        self.player.calc_current_score(self.player.hands)

        # 初期ドロー時のスコア表示（dealer側の1枚は伏せる）
        print("\n--Game Start--\n")

        first_msg = f"""\
dealer's hands : [{self.dealer.hands[0]}, *-*]
player's hands : {self.player.hands}

players's total_score : {self.player.card_current_score}\
        """
        print(f"{first_msg}")

        # playerに hit or stand 決めさせる（stand で player のターンが終了）
        self.player.keep_drawing_card(deck)

        print("\n--Result--\n")

        # dealerスコア計算
        self.dealer.calc_current_score(self.dealer.hands)
        dealer_msg = f"""\
dealer's hands : {self.dealer.hands}
dealer's total_score : {self.dealer.card_current_score}
        """
        print(f"{dealer_msg}")

        # dealerの手札の合計が17になるまで引く
        self.dealer.keep_drawing_card(deck)

        # 勝敗判定
        self.judge_winner(self.dealer, self.player)

        print("\n--Game End--\n")


if __name__ == '__main__':
    game = Game()
    game.main()
