N = 8

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def dfs_queens(board, row):
    if row == N:
        print_solution(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if dfs_queens(board, row + 1):
                return True
            board[row] = -1   # backtrack

    return False


def print_solution(board):
    for r in range(N):
        for c in range(N):
            print("Q" if board[r] == c else ".", end=" ")
        print()


board = [-1] * N
dfs_queens(board, 0)
