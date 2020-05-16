class BlackJack:

    RANKS = (*"A23456789", "10", *"JQK")
    values = list(range(1, 11))  # 1〜10
    values.extend([10, 10, 10])  # JQK
    VALUES = (values)
    # 表示マークとスコアを紐づける
    # {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
    #  '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    #  'J': 10, 'Q': 10, 'K': 10}
    RANK_TO_VALUES = dict(zip(RANKS, VALUES))

    @classmethod
    def calc_current_score(cls, person):
        """
        現在のスコアを計算

        Parameters
        ----------
        person : object
            現在の手札

        Returns
        --------
        card_current_score : int
            現在のスコア
        """
        person.card_current_score = 0
        person.card_current_score_sub = 0
        person.has_A_card = False
        for card in person.hands:
            card_rank = str(card).split("-")[1]
            card_value = cls.RANK_TO_VALUES[card_rank]

            # Aの時も考慮
            person.card_current_score += card_value
            person.card_current_score_sub += card_value
            if card_value == 1:
                if person.has_A_card:
                    # Aが連続した時サブスコアで2重でサブスコア加算されるので+10(+11-1)
                    person.card_current_score_sub += 10
                    print(person.card_current_score_sub)
                    continue
                person.has_A_card = True
                person.card_current_score_sub += 11

    @classmethod
    def is_score_bust(cls, total_score):
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

    @classmethod
    def check_draw_A(cls, person):
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
        if person.has_A_card is True:
            person_sub_score = f", {person.card_current_score_sub}"
        return person_sub_score
