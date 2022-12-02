import os
import json

decode_part1 = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

decode_part2 = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Should_lose",
    "Y": "Should_draw",
    "Z": "Should_win"
}

scores = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

def get_score_from_round(opp_move, my_move):
    if opp_move == my_move:
        return 3
    elif opp_move == "Rock":
        if my_move == "Paper":
            return 6
        return 0

    elif opp_move == "Paper":
        if my_move == "Scissors":
            return 6
        return 0

    elif opp_move == "Scissors":
        if my_move == "Rock":
            return 6
        return 0

def what_should_i_play_to_get_output(opp_move, desired_outcome):
    if desired_outcome == "Should_draw":
        return opp_move
    elif desired_outcome == "Should_lose":
        if opp_move == "Rock":
            return "Scissors"
        elif opp_move == "Paper":
            return "Rock"
        elif opp_move == "Scissors":
            return "Paper"
    elif desired_outcome == "Should_win":
        if opp_move == "Rock":
            return "Paper"
        elif opp_move == "Paper":
            return "Scissors"
        elif opp_move == "Scissors":
            return "Rock"

def get_score_for_outcome(outcome):
    if outcome == "Should_win":
        return 6
    elif outcome == "Should_draw":
        return 3
    elif outcome == "Should_lose":
        return 0

total_part1 = 0
total_part2 = 0
# Read each line from the file 'input.txt' and write it to the file 'output.txt'
with open('input.txt', 'r') as input_file:
    for line in input_file:
        opponent_move = decode_part1[line[0]]
        my_move = decode_part1[line[2]]
        desired_outcome = decode_part2[line[2]]

        total_part1 += get_score_from_round(opponent_move, my_move) + scores[my_move]

        what_should_i_play = what_should_i_play_to_get_output(opponent_move, desired_outcome)
        total_part2 += get_score_for_outcome(desired_outcome) + scores[what_should_i_play]

print(total_part1)
print(total_part2)