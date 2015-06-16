"""
Solution to non code-eval question:
Here is an interview question that I got recently. I thought it was interesting; so I thought I would share... Below is an example table. This is just a short 4 x 4 representation; the data has no bounds & it is not necessary to solve the problem.
So when row=1 & column=1, the returned value is 1. When row=1 & column=2, the returned value is empty (or null). And so on. So If you wanted to know the value at row=987 & column=23, your function would return the value at that cell. Enjoy!

```+------+------+------+------+
|      |      |      |      |
|  1   | null | null | null |
|      |      |      |      |
+---------------------------+
|      |      |      |      |
|  2   |  3   | null | null |
|      |      |      |      |
+---------------------------+
|      |      |      |      |
|  4   |  5   |  6   | null |
|      |      |      |      |
+---------------------------+
|      |      |      |      |
|  7   |  8   |  9   |  10  |
|      |      |      |      |
+------+------+------+------+
"""
import sys


def row_col1(row):
    """Given row number, return value of number in first column."""
    if row == 1:
        return 1
    else:
        return int(row - 1 + row_col1(row-1))


def main(row, column):
    """Given row and column output number."""
    num = int(column) - 1 + row_col1(int(row))
    print num


if __name__ == '__main__':
    row, column = sys.argv[1], sys.argv[2]
    main(row, column)
