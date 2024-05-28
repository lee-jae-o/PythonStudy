def calculate_win_probability(player_deck, opponent_deck):
    total_outcomes = 0
    favorable_outcomes = 0

    for player_card in player_deck:
        for opponent_card in opponent_deck:
            total_outcomes += 1
            if player_card > opponent_card:
                favorable_outcomes += 1

    win_probability = favorable_outcomes / total_outcomes
    return win_probability

if __name__ == "__main__":
    player_deck = [7, 8, 9, 10, 11, 12, 13, 14]
    opponent_deck = [2, 3, 4, 5, 6, 7, 8, 9]

    win_probability = calculate_win_probability(player_deck, opponent_deck)

    print(f"플레이어가 승리할 확률: {win_probability:.2%}")