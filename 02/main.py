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

scores_from_moves = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

scores_from_outcomes = {
    "Win": 6,
    "Draw": 3,
    "Lose": 0
}

def get_score_from_round(opp_move, my_move):
    if opp_move == my_move:
        return scores_from_outcomes["Draw"]
    elif opp_move == "Rock":
        if my_move == "Paper":
            return scores_from_outcomes["Win"]
        elif my_move == "Scissors":
            return scores_from_outcomes["Lose"]
    elif opp_move == "Paper":
        if my_move == "Rock":
            return scores_from_outcomes["Lose"]
        elif my_move == "Scissors":
            return scores_from_outcomes["Win"]
    elif opp_move == "Scissors":
        if my_move == "Rock":
            return scores_from_outcomes["Win"]
        elif my_move == "Paper":
            return scores_from_outcomes["Lose"]

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

            total_part1 += get_score_from_round(opponent_move, my_move) + scores_from_moves[my_move]

            what_should_i_play = what_should_i_play_to_get_output(opponent_move, desired_outcome)
            total_part2 += scores_from_outcomes[desired_outcome] + scores_from_moves[what_should_i_play]

    print(f'Part1: {total_part1}')
    print(f'Part2: {total_part2}')