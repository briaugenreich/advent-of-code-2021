import math
from functools import reduce

def define_game_boards(input):
    board_count=1
    boards={}
    while input.readline():
        board=[]
        for i in range(5):
            for num in input.readline().split(' '):
                if num:
                    board.append(int(num))
        boards[board_count] = board
        board_count +=1
    # print(boards)
    return boards

def calculate_win(board):
    win = None
    if -1 in board:
        indices = [i for i, x in enumerate(board) if x == -1]
        # print(indices)
        if len(indices) >= 5: # need at least 5 vals
            for i in indices: # todo eliminate ones we know cant be true

                x = math.floor(i/5) * 5
                if x in indices and x+1 in indices and x+2 in indices and x+3 in indices and x+4 in indices:
                    win = board
                    break

                x = i % 5
                if x in indices and x+5 in indices and x+10 in indices and x+15 in indices and x+20 in indices:
                    win = board
                    break
    return win

def calulate_score(board, winning_num):
    score = 0
    scores = [num for num in board if num != -1]
    for s in scores:
        score += s

    print("SCORE:", score, "*", winning_num, "=", score*winning_num)

def play_number(num, board):
    if num in board:
        found_pos = board.index(num)
        board[found_pos] = -1
    return board


def play_to_win(nums, boards):
    winner = False
    round = 0
    while not winner:
        # todo short cut first 5 rounds
        for key, board in boards.items():
            updated_board = play_number(nums[round], board)
            boards[key] = updated_board
            winning_board = calculate_win(board)
            if winning_board:
                calulate_score(winning_board, nums[round])
                winner  = True
                break
        round+=1


def play_to_loose(nums, boards):
    # print("plauing to loose")
    round = 0
    looser = False
    while len(boards) > 1 or not looser:
        # todo short cut first 5 rounds
        board_to_delete = []
        for key, board in boards.items():
            updated_board = play_number(nums[round], board)
            boards[key] = updated_board
            winning_board = calculate_win(board)
            if winning_board:
                if len(boards) == 1:
                    looser = True
                    # print("LAST BOARD TO WIN....", boards)
                    calulate_score(winning_board, nums[round])
                    break
                else:
                    board_to_delete.append(key)
        for b in board_to_delete:
            # print("deleting winning boards", b)
            del boards[b]

        round+=1

# TODO this is silly duplication .... wayyy overly complex... please simplify bri!!
with open('input.txt', 'r') as input_file:
    numbers = [int(num) for num in input_file.readline().split(',')]
    boards=define_game_boards(input_file)
    play_to_win(numbers, boards)

with open('input.txt', 'r') as input_file:
    numbers = [int(num) for num in input_file.readline().split(',')]
    boards=define_game_boards(input_file)
    play_to_loose(numbers, boards)
