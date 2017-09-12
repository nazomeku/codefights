"""Given the total number of rows and columns in the theater (nRows and nCols,
respectively), and the row and column you're sitting in, return the number of
people who sit strictly behind you and in your column or to the left, assuming
all seats are occupied."""


def seats_in_theater(n_cols, n_rows, col, row):
    return (n_rows - row) * (n_cols - col+1)
