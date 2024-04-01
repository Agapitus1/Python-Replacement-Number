def solution(array, row, column, replace):
    original_value = array[row][column]

    def replacement(r, c):
        if r < 0 or r >= len(array) or c < 0 or c >= len(array[0]) or array[r][c] != original_value:
            return
        array[r][c] = replace
        replacement(r + 1, c)
        replacement(r - 1, c)
        replacement(r, c + 1)
        replacement(r, c - 1)

    replacement(row, column)
    return array
