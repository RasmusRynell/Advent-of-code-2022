import os
import json

decode_ABC = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}

decode_XYZ_p1 = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

decode_XYZ_p2 = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win"
}

decode_part2 = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win"
}

scores = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

def get_score_for_outcome(outcome):
    if outcome == "Win":
        return 6
    elif outcome == "Draw":
        return 3
    elif outcome == "Lose":
        return 0

def get_score_from_round(opp_move, my_move):
    if opp_move == my_move:
        return get_score_for_outcome("Draw")
    elif opp_move == "Rock":
        if my_move == "Paper":
            return get_score_for_outcome("Win")
        elif my_move == "Scissors":
            return get_score_for_outcome("Lose")
    elif opp_move == "Paper":
        if my_move == "Rock":
            return get_score_for_outcome("Lose")
        elif my_move == "Scissors":
            return get_score_for_outcome("Win")
    elif opp_move == "Scissors":
        if my_move == "Rock":
            return get_score_for_outcome("Win")
        elif my_move == "Paper":
            return get_score_for_outcome("Lose")

def what_should_i_play_to_get_output(opp_move, desired_outcome):
    if desired_outcome == "Draw":
        return opp_move
    elif desired_outcome == "Lose":
        if opp_move == "Rock":
            return "Scissors"
        elif opp_move == "Paper":
            return "Rock"
        elif opp_move == "Scissors":
            return "Paper"
    elif desired_outcome == "Win":
        if opp_move == "Rock":
            return "Paper"
        elif opp_move == "Paper":
            return "Scissors"
        elif opp_move == "Scissors":
            return "Rock"


if __name__ == "__main__":
    total_part1 = 0
    total_part2 = 0
    # Read each line from the file 'input.txt' and write it to the file 'output.txt'
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            opponent_move = decode_ABC[line[0]]
            my_move = decode_XYZ_p1[line[2]]
            desired_outcome = decode_XYZ_p2[line[2]]

            total_part1 += get_score_from_round(opponent_move, my_move) + scores[my_move]

            what_should_i_play = what_should_i_play_to_get_output(opponent_move, desired_outcome)
            total_part2 += get_score_for_outcome(desired_outcome) + scores[what_should_i_play]

    print(f'Part1: {total_part1}')
    print(f'Part2: {total_part2}')