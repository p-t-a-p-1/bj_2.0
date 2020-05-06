#!/usr/bin/env python
# coding: UTF-8

# Cardクラス
import card
# リストの要素をシャッフル
from random import shuffle


class Deck:
    """
    カードのマークと数字を出力

    Attributes
    ----------
    deck_set_no : int
        デッキの個数
    """

    def __init__(self, deck_set_count=1):
        """
        Parameters
        ----------
        deck_set_count : int
            デッキの個数
        """

        self.cards = []
        for index in range(deck_set_count):
            # 4つのマーク
            for mark in range(4):
                # 数字（2から13 + 1の14）
                for value in range(2, 15):
                    # cardsに追加
                    self.cards.append(card.Card(mark, value))
        # デッキをシャッフル
        shuffle(self.cards)

    def get_card(self, card_num=1):
        """
        要素を取得しリストから削除

        Parameters
        ----------
        card_num : int
            取得するカードの枚数
        """
        self.card_list = []
        if len(self.cards) == 0:
            # カードが0枚の時は何もしない
            return

        for i in range(card_num):
            self.card_list.append(self.cards.pop())
        return self.card_list


# 2つ分のデッキ
# deck = Deck(2)
# [♦︎-12, ♠︎-3, ♦︎-13, ❤︎-9, ♦︎-3, ♦︎-8, ♠︎-11, ♦︎-13, ♣️-9, ♦︎-11,
#  ♦︎-12, ♠︎-2, ♠︎-8, ❤︎-10, ♦︎-4, ♦︎-9, ♣️-10, ♣️-4, ♦︎-9, ♠︎-6,
#  ♠︎-3, ♣️-12, ♠︎-12, ❤︎-13, ♣️-11, ♣️-8, ♦︎-10, ♦︎-5, ♦︎-7, ❤︎-12,
#  ♣️-8, ♦︎-10, ♣️-10, ♦︎-6, ♠︎-9, ♦︎-5, ❤︎-12, ♠︎-12, ♠︎-10, ♣️-1,
#  ♣️-3, ❤︎-1, ❤︎-9, ❤︎-3, ❤︎-6, ♠︎-8, ♦︎-1, ♠︎-13, ❤︎-3, ♦︎-2, ♣️-1,
#  ♣️-12, ♠︎-7, ❤︎-8, ♣️-5, ♠︎-9, ♣️-4, ♠︎-10, ❤︎-11, ❤︎-4, ♣️-11,
#  ♠︎-4, ♣️-7, ❤︎-7, ❤︎-6, ♣️-3, ♣️-9, ♦︎-2, ♦︎-11, ❤︎-5, ❤︎-4, ♠︎-13,
#  ♠︎-4, ♣️-13, ♠︎-1, ♦︎-1, ♠︎-2, ♦︎-8, ❤︎-8, ♣️-5, ♣️-6, ♠︎-7, ♣️-7,
#  ♠︎-11, ♠︎-6, ♠︎-5, ♦︎-6, ❤︎-5, ♣️-6, ♣️-13, ❤︎-7, ♦︎-7, ❤︎-10, ❤︎-11,
#  ♠︎-5, ❤︎-2, ❤︎-13, ♦︎-3, ♠︎-1, ❤︎-1, ♦︎-4, ♣️-2, ❤︎-2, ♣️-2]
# print(deck.cards)
# カードを5枚引く[♣️-2, ❤︎-2, ♣️-2, ♦︎-4, ❤︎-1]
# print(deck.get_card(5))
