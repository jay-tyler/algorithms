def pascal(n, i):
    """Get the element value at the nth level and the ith
    index for Pascal's triangle. Levels are 0 at top, and
    increasing number descending; e.g. indexes
    Level 0             0
    Level 1           0   1
    Level 2         0   1   2
    Level 3       0   1   2   3
    etc

    to return values;
    Level 0             1
    Level 1           1   1
    Level 2         1   2   1
    Level 3       1   3   3   1
    etc

    """
    if i > n:
        return 0
    if i in [0, n]:
        return 1
    else:
        sum = (pascal(n - 1, i - 1) + pascal(n - 1, i))
    return sum


def compute_branches(n):
    """For a square grid of n x n, with a robot that can only move
    rightwards or downwards, calculate the number of possible
    paths to get to opposite corner given that the robot starts
    in the top left corner.

     ----- ----- -----
    | X ->|     |     |
    | |   |     |     |
     ----- ----- -----
    |     |     |     |
    |     |     |     |
     ----- ----- -----
    |     |     | O   |
    |     |     |     |
     ----- ----- -----


    This involves calculating the middle element of Pascal's
    triangle at the row corresponding to n-th diagonal row of
    the grid (there are 2n-1 of these diagonal rows for an
    n x n matrix).
    """

    return pascal((2*n - 2), (2*n - 1)//2)
