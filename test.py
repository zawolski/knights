class space:
    def __init__(self, num, x_pos, y_pos):
        self.num = num
        self.x = x_pos
        self.y = y_pos
        self.pos = (y_pos, x_pos)

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

    for line in grid:
        out = ""
        for item in line:
            thing = int(item)
            out += f"{thing:03d}" + " "
        print(out)

    for i in range(n ** 2):
        print(f"{i}, {spaces[i].pos}")


make_spiral(9)