# 機能要件

- 初期カードは52枚。引く際にカードの重複は無いようにする
- プレイヤーとディーラーの2人対戦。プレイヤーは実行者、ディーラーは自動的に実行
- 実行開始時、プレイヤーとディーラーはそれぞれ、カードを2枚引く。引いたカードは画面に表示する。ただし、**ディーラーの2枚目のカードは分からないようにする**
- その後、先にプレイヤーがカードを引く。プレイヤーが21を超えていたらバースト、その時点でゲーム終了
- プレイヤーは、カードを引くたびに、次のカードを引くか選択できる
- プレイヤーが引き終えたら、その後ディーラーは、自分の手札が17以上になるまで引き続ける
- プレイヤーとディーラーが引き終えたら勝負。より21に近い方の勝ち
- JとQとKは10として扱う
- Aは1, 11として扱う
- ダブルダウンなし、スプリットなし、サレンダーなし、その他特殊そうなルールなし
- 1回のプログラム実行でゲームを複数回できるように

# 実行例
```
02:01:00 ~/workspace/python/bj_2.0 $ python main.py 

--Game Start--

dealer's hands : [❤︎-J, *-*]
player's hands : [♦︎-3, ♠︎-3]

players's total_score : 6            

Hit(1) or Stand(2) : 1
player draw card is : ♠︎-Q
players's total_score : 16

Hit(1) or Stand(2) : 1
player draw card is : ♠︎-5
players's total_score : 21

--Result--

dealer's hands : [❤︎-J, ♦︎-5]
dealer's total_score : 15            
dealer draw card is : ❤︎-Q
dealer's total_score : 25
dealer burst!!!

/***********/
/player win!/
/***********/

--Game End--

Qでゲーム終了、それ以外でゲームスタート：

--Game Start--

dealer's hands : [♠︎-10, *-*]
player's hands : [♠︎-8, ♦︎-8]

players's total_score : 16            

Hit(1) or Stand(2) : 2

--Result--

dealer's hands : [♠︎-10, ♣️-A]
dealer's total_score : 11, 22            
dealer draw card is : ♣️-5
dealer's total_score : 16, 27
dealer draw card is : ♣️-Q
dealer's total_score : 26, 37
dealer burst!!!

/***********/
/player win!/
/***********/

--Game End--

Qでゲーム終了、それ以外でゲームスタート：

--Game Start--

dealer's hands : [❤︎-K, *-*]
player's hands : [♦︎-A, ♠︎-7]

players's total_score : 8, 19            

Hit(1) or Stand(2) : 2

--Result--

dealer's hands : [❤︎-K, ♠︎-J]
dealer's total_score : 20            

/***********/
/dealer win!/
/***********/

--Game End--

Qでゲーム終了、それ以外でゲームスタート：Q
*-*-*-*-*-*-*-*
total：3
win：2
lose：1
draw：0
*-*-*-*-*-*-*-*
```
