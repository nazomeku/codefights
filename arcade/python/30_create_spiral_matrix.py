"""Given the size of the matrix n, your task is to create a spiral matrix."""


def create_spiral_matrix(n):
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    cur_dir = 0
    cur_pos = (n - 1, n - 1)
    res = [[0] * n for i in range(n)]

    for i in range(1, n * n + 1):
        res[cur_pos[0]][cur_pos[1]] = i
        next_pos = cur_pos[0] + dirs[cur_dir][0], cur_pos[1] + dirs[cur_dir][1]
        if not (0 <= next_pos[0] < n and
                0 <= next_pos[1] < n and
                res[next_pos[0]][next_pos[1]] == 0):
            cur_dir = (cur_dir + 1) % 4
            next_pos = cur_pos[0] + dirs[cur_dir][0], cur_pos[1] + dirs[cur_dir][1]
        cur_pos = next_pos

    return res
