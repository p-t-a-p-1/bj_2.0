#!/usr/bin/env python
# coding: UTF-8


class Card:
    """
    カードのマークと数字を出力

    Attributes
    ----------
    card_mark : int
        カードのマーク（♠︎❤︎♦︎♣️）
    card_value : int
        カードの数字
    """

    # マーク
    marks = ["♠︎-", "❤︎-", "♦︎-", "♣️-"]
    # 数字
    values = ([None, None, 2, 3, 4, 5, 6,
               7, 8, 9, 10, 11, 12, 13, 1])

    def __init__(self, card_mark, card_value):
        """
        Parameters
        ----------
        card_mark : int
            カードのマーク（♠︎❤︎♦︎♣️）
        card_value : int
            カードの数字
        """
        self.mark = card_mark
        self.value = card_value

    # オーバーライドしてインスタンスの出力内容を変更
    def __repr__(self):
        return self.marks[self.mark] + str(self.values[self.value])


# Cardクラスからインスタンスを生成（引数にマークと数字）
# reprメソッドで出力内容を変更しているので下記のように出力される
# 通常 → <__main__.Card object at 0x10c949310>
# reprメソッド追加 → ♦︎-4

# card = Card(2, 4)
# print(card)
