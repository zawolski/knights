import time

class space:
    def __init__(self, num, x_pos, y_pos):
        self.num = num
        self.x = x_pos
        self.y = y_pos
        self.pos = (y_pos, x_pos)
        self.occupant = 0

class piece:
    def __init__(self, name):
        self.name = name
        self.moves = []

class knight(piece):
    def __init__(self):
        self.name = "knight"
        self.moves = [
            (2, 1),
            (-2, 1),
            (2, -1),
            (-2, -1),
            (1, 2),
            (-1, 2),
            (1, -2),
            (-1, -2)
        ]

def make_spiral(n):
    grid = [["99" for _ in range(n)] for _ in range(n)]
    
    x_pos = 0
    y_pos = 0

    x_dir = 1
    y_dir = 1

    cur_num = (n ** 2) - 1
    cur_side = n - 1

    spaces = {}

    grid[0][0] = cur_num
    spaces[cur_num] = space(cur_num, x_pos, y_pos)
    cur_num -= 1

    for i in range(cur_side):
        x_pos += x_dir
        grid[y_pos][x_pos] = cur_num
        spaces[cur_num] = space(cur_num, x_pos, y_pos)
        cur_num -= 1
    x_dir *= -1

    for i in range(cur_side):
        y_pos += y_dir
        grid[y_pos][x_pos] = cur_num
        spaces[cur_num] = space(cur_num, x_pos, y_pos)
        cur_num -= 1
    y_dir *= -1

    for i in range(cur_side):
        x_pos += x_dir
        grid[y_pos][x_pos] = cur_num
        spaces[cur_num] = space(cur_num, x_pos, y_pos)
        cur_num -= 1
    x_dir *= -1

    cur_side -= 1

    while cur_side > 0:
        for i in range(cur_side):
            y_pos += y_dir
            grid[y_pos][x_pos] = cur_num
            spaces[cur_num] = space(cur_num, x_pos, y_pos)
            cur_num -= 1
        y_dir *= -1
        for i in range(cur_side):
            x_pos += x_dir
            grid[y_pos][x_pos] = cur_num
            spaces[cur_num] = space(cur_num, x_pos, y_pos)
            cur_num -= 1
        x_dir *= -1
        cur_side -= 1

    return grid, spaces

    # for line in grid:
    #     out = ""
    #     for item in line:
    #         thing = int(item)
    #         out += f"{thing:03d}" + " "
    #     print(out)

    #for i in range(n ** 2):
    #    print(f"{i}, {spaces[i].pos}")

def check_bounds(n, base, move_list):
    valid_moves = []
    for move in move_list:
        y_pos = base[0] + move[0]
        x_pos = base[1] + move[1]
        if y_pos >= 0 and y_pos < n and x_pos >=0 and x_pos < n:
            valid_moves.append((y_pos, x_pos))
    return valid_moves

def play(n, grid, spaces, players_list):
    player_count = len(players_list)
    smallest_squares = [0] * player_count
    player_num = []
    for i in range(player_count):
        player_num.append(i + 1)
    
    player = 0

    while min(smallest_squares) < n ** 2:
        while smallest_squares[player] < n ** 2:
            if spaces[smallest_squares[player]].occupant != 0:
                smallest_squares[player] += 1
            else:
                visible = check_bounds(n, spaces[smallest_squares[player]].pos, players_list[player].moves)
                valid_flag = 1
                for move in visible:
                    owner = spaces[grid[move[0]][move[1]]].occupant
                    if owner != 0 and owner != player_num[player]:
                        valid_flag = 0
                        break
                if valid_flag == 0:
                    smallest_squares[player] += 1
                else:
                    spaces[smallest_squares[player]].occupant = player_num[player]
                    smallest_squares[player] += 1
                    break
        player = (player + 1) % player_count


def outcome_2_knights(n):
    grid, spaces = make_spiral(n)

    plist = []
    plist.append(knight())
    plist.append(knight())

    play(n, grid, spaces, plist)

    for i in range(n):
        for j in range(n):
            grid[i][j] = 0

    for i in range(n ** 2):
        y = spaces[i].y
        x = spaces[i].x 
        grid[y][x] = spaces[i].occupant

    return grid

def outcome_6_knights(n):
    grid, spaces = make_spiral(n)

    plist = []
    plist.append(knight())
    plist.append(knight())
    plist.append(knight())
    plist.append(knight())
    plist.append(knight())
    plist.append(knight())

    play(n, grid, spaces, plist)

    for i in range(n):
        for j in range(n):
            grid[i][j] = 0

    for i in range(n ** 2):
        y = spaces[i].y
        x = spaces[i].x 
        grid[y][x] = spaces[i].occupant

    return grid

# n = 230
# grid = outcome_2_knights(n)
# # grid, spaces = make_spiral(n)
# # for line in grid:
# #     out = ""
# #     for item in line:
# #         thing = int(item)
# #         out += f"{thing:03d}" + " "
# #     print(out)

# # for i in range(n ** 2):
# #     print(f"{i}, {spaces[i].pos}")

# # print(spaces[0].pos)

# # tknight = knight()
# # print(tknight.moves)

# # print(check_bounds(n, (2,2), tknight.moves))

# # plist = []
# # plist.append(knight())
# # plist.append(knight())
# # # plist.append(knight())
# # # plist.append(knight())

# # play(n, grid, spaces, plist)

# # # for i in range(n ** 2):
# # #     print(f"{i}, {spaces[i].occupant}")

# # # for line in grid:
# # #     out = ""
# # #     for item in line:
# # #         thing = int(item)
# # #         out += f"{thing:02d}" + " "
# # #     print(out)

# # for i in range(n):
# #     for j in range(n):
# #         grid[i][j] = 0

# # for i in range(n ** 2):
# #     y = spaces[i].y
# #     x = spaces[i].x 
# #     grid[y][x] = spaces[i].occupant

# for line in grid:
#     #out = ""
#     for item in line:
#         if int(item) == 0:
#             print(item, end = "")
#         if int(item) == 1:
#             print(f"{'\033[31m'}{item}{'\033[0m'}", end = "")
#         if int(item) == 2:
#             print(f"{'\033[32m'}{item}{'\033[0m'}", end = "")
#         if int(item) == 3:
#             print(f"{'\033[33m'}{item}{'\033[0m'}", end = "")
#         if int(item) == 4:
#             print(f"{'\033[34m'}{item}{'\033[0m'}", end = "")
#     print("")