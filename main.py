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

    def get_nearest_score(self, score_list):
        """
        メインスコアとサブスコアから21以下で21にもっとも近い数字を返す
        どちらも21超えてる場合は0を返す

        Parameters
        ----------
        score_list : list
            メインスコアとサブスコアのリスト

        Returns
        --------
        main_score : int
            2つのスコアのうち21に近い数字（どちらも21より大きい場合は0）
        """
        main_score = 0
        for score in score_list:
            if score > 21:
                # 21より大きい数字はバースト
                continue
            elif main_score < score:
                main_score = score
        return main_score

    def judge_winner(self, player, dealer):
        """
        勝敗判定

        Parameters
        ----------
        dealer : object
            親
        player : object
            子
        """

        # player, dealer の各スコアで21以下の21に近い方を取得し比較
        player_score_list = [
            player.card_current_score,
            player.card_current_score_sub]
        player_score = self.get_nearest_score(player_score_list)

        dealer_score_list = [
            dealer.card_current_score,
            dealer.card_current_score_sub]
        dealer_score = self.get_nearest_score(dealer_score_list)

        judge_win = ""
        # どちらもバーストはdraw
        if player_score == 0 and dealer_score == 0:
            judge_win = "---draw---"

        if dealer_score < \
                player_score <= 21:
            # dealer < player <= 21の時、playerの勝利
            judge_win = "player win!"
            player.win_count += 1
        elif player_score <= 21 \
                < dealer_score:
            # player が21以下、dealerがバーストはplayerの勝利
            judge_win = "player win!"
            player.win_count += 1
        elif player_score == dealer_score \
                and player_score <= 21:
            # どちらもバーストせず、同じ数字の場合は引き分け
            judge_win = "---draw---"
        else:
            # それ以外の場合は全部playerの負け
            judge_win = "dealer win!"
            dealer.win_count += 1
        # コンソール表示
        print(f"\n/***********/\n/{judge_win}/\n/***********/")

    def display_final_result(
            self,
            player_win_count,
            dealer_win_count,
            total_count):
        """
        勝敗判定

        Parameters
        ----------
        player_win_count : int
            playerの勝利回数
        dealer_win_count : int
            dealerの勝利回数
        total_count : int
            総ゲーム数
        """
        # 総ゲーム数からplayerとdealerの勝利数引いてドローの回数計算
        draw_count = total_count - player_win_count - dealer_win_count
        return f"""\
*-*-*-*-*-*-*-*
total：{total_count}
win：{player_win_count}
lose：{dealer_win_count}
draw：{draw_count}
*-*-*-*-*-*-*-*\
"""

    def check_draw_A(self, person):
        """
        手札にAがある場合はサブスコアも表示

        Parameters
        ----------
        person : object
            player or dealer

        Returns
        --------
        person_sub_score : str
            サブスコア用文字列（手札にAない場合は空文字）
        """
        person_sub_score = ""
        if person.draw_A_flg is True:
            person_sub_score = f", {person.card_current_score_sub}"
        return person_sub_score

    def main(self):
        """
        ブラックジャックのメインゲーム関数
        """

        # 山札セット（セット数を決める）
        deck = stock.Deck()

        total_count = 0
        game_flg = True
        # 残りカードが5枚以上の場合
        while game_flg is True and len(deck.cards) > 5:

            self.player.hands = []
            self.dealer.hands = []

            # ゲーム数+1
            total_count += 1

            # 最初は２枚ずつドロー
            self.player.draw_card(deck, 2)
            self.dealer.draw_card(deck, 2)

            # player初期スコア計算
            self.player.calc_current_score(self.player.hands)
            # A引いてる場合はサブスコアも表示
            player_sub_score = self.check_draw_A(self.player)

            # 初期ドロー時のスコア表示（dealer側の1枚は伏せる）
            print("\n--Game Start--\n")
            first_msg = f"""\
dealer's hands : [{self.dealer.hands[0]}, *-*]
player's hands : {self.player.hands}

players's total_score : {self.player.card_current_score}{player_sub_score}\
            """
            print(f"{first_msg}")

            # playerに hit or stand 決めさせる（stand で player のターンが終了）
            self.player.keep_drawing_card(deck)

            print("\n--Result--\n")

            # dealerスコア計算
            self.dealer.calc_current_score(self.dealer.hands)
            # A引いてる場合はサブスコアも表示
            dealer_sub_score = self.check_draw_A(self.dealer)
            dealer_msg = f"""\
dealer's hands : {self.dealer.hands}
dealer's total_score : {self.dealer.card_current_score}{dealer_sub_score}\
            """
            print(f"{dealer_msg}")

            # dealerの手札の合計が17になるまで引く
            self.dealer.keep_drawing_card(deck)

            # 勝敗判定
            self.judge_winner(self.player, self.dealer)

            print("\n--Game End--\n")

            # ゲームリスタート
            restart_msg = "Qでゲーム終了、それ以外でゲームスタート："
            start_res = input(restart_msg)
            if start_res == 'Q':
                game_flg = False

        # ゲーム回数や勝利回数など計算して表示
        final_score_str = self.display_final_result(
            self.player.win_count, self.dealer.win_count, total_count)
        print(final_score_str)


if __name__ == '__main__':
    game = Game()
    game.main()
