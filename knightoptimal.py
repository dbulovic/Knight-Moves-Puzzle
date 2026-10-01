knight_moves = [[2,1],[2,-1],[1,2],[1,-2],[-1,2],[-1,-2],[-2,1],[-2,-1]]

val1 = 1
val2 = 2
val3 = 3
score_goal = 12

"""Create a 6x6 board with customizable values matching the game pattern."""
# Value pattern for each column (using indices to refer to the three values)
pattern = {
    0: [val1] * 6,                           # column 0: all val1
    1: [val2, val2, val1, val1, val1, val1], # column 1: 2 val2s, 4 val1s
    2: [val2, val2, val2, val2, val1, val1], # column 2: 4 val2s, 2 val1s
    3: [val3, val3, val2, val2, val2, val2], # column 3: 2 val3s, 4 val2s
    4: [val3, val3, val3, val3, val2, val2], # column 4: 4 val3s, 2 val2s
    5: [val3] * 6                            # column 5: all val3s
}
board = []
for row in range(6):
    board_row = [pattern[col][row] for col in range(6)]
    board.append(board_row)  

def next_move(cur_pos, score, visited):
    for move in knight_moves:
        new_pos = [cur_pos[0] + move[0],cur_pos[1] + move[1]]
        if 0 <= new_pos[0] < 6 and 0 <= new_pos[1] < 6:
            if [new_pos[0], new_pos[1]] in visited: continue
            if board[new_pos[0]][new_pos[1]] == board[cur_pos[0]][cur_pos[1]]:
                new_score = score + board[new_pos[0]][new_pos[1]]
            else:
                new_score = score * board[new_pos[0]][new_pos[1]]
            if new_score == score_goal and new_pos[0] == 5 and new_pos[1] == 5:
                print(visited + [[new_pos[0], new_pos[1]]])
                return 0
            elif new_score > score_goal:
                continue
            else:
                new_visited = visited + [[new_pos[0], new_pos[1]]]
                next_move_result = next_move(cur_pos=new_pos, score=new_score, visited=new_visited)
                if next_move_result == 0:
                    return 1
    return 2
                
cur_pos = [0,0]
next_move(cur_pos, val1, [cur_pos])


