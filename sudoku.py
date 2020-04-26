import numpy as np

# %%
class Sudoku:
    def __init__(self, sudoku_row_list: list):
        self.sudoku = np.array(sudoku_row_list)
        self.validate_matrix()

    def __str__(self):
        line_separator = "-------------------------"
        sudoku_out = [line_separator]
        for row_num, line in enumerate(self.sudoku):
            if row_num in (3, 6):
                sudoku_out.append(line_separator)
            line_out = ["|"]
            for col_id, digit in enumerate(line):
                if col_id in (3, 6):
                    line_out.append("|")
                if digit is None:
                    digit = " "
                line_out.append(digit)
            line_out.append("|")
            line_out = [str(digit) for digit in line_out]
            line_out = " ".join(line_out)
            sudoku_out.append(line_out)
        sudoku_out.append(line_separator)
        sudoku_out = "\n".join(sudoku_out)
        return sudoku_out

    def get_square_index(self, row_id: int, col_id: int):
        """Takes column and row ids and returns square index.

        Args:
            row_id (int): Row id.
            col_id (int): Column id.

        Returns:
            int: Square id.
        """
        if row_id < 3 and col_id < 3:
            return 0
        elif row_id < 3 and col_id < 6:
            return 1
        elif row_id < 3:
            return 2
        elif row_id < 6 and col_id < 3:
            return 3
        elif row_id < 6 and col_id < 6:
            return 4
        elif row_id < 6:
            return 5
        elif col_id < 3:
            return 6
        elif col_id < 6:
            return 7
        else:
            return 8

    def validate_matrix(self):
        """Checks if sudoku shape is expected.

        Raises:
            ValueError: if row number is not equal to 9.
            ValueError: If column count is not equal to 9.
        """
        rows, cols = self.sudoku.shape
        if rows != 9:
            raise ValueError(f"Incorrect number of rows: {rows}")
        elif cols != 9:
            raise ValueError(f"Incorrect number of columns: {cols}")

    def check_if_digits_in_row(self, row_id: int, digits: list):
        """Goes throught the list of digits and returns list of digits
        that are not present in row.

        Args:
            sudoku (list): Sudoku structure.
            row_id (int): Row index.
            digits (list): Original list of numbers that could be available.

        Returns:
            list: Still available digits.
        """
        row = self.sudoku[row_id, :]
        return [digit for digit in digits if digit not in row]

    def check_if_digits_in_column(self, col_id, digits):
        """Goes throught the list of digits and returns list of digits
        that are not present in column.

        Args:
            col_id (int): column id.
            digits (list): List of digits to look for.

        Returns:
            list: Still available digits.
        """
        col = self.sudoku[:, col_id]
        return [digit for digit in digits if digit not in col]

    def form_square(self, row_id, col_id):
        """Returns elements that are in a square.

        Args:
            row_id (int): Row id.
            col_id (int): Column in.

        Returns:
            list: all elements of a square.
        """
        square_id = self.get_square_index(row_id, col_id)
        if square_id % 3 == 0:
            rows = self.sudoku[:, :3]
        elif square_id % 3 == 1:
            rows = self.sudoku[:, 3:6]
        else:
            rows = self.sudoku[:, 6:]

        if square_id < 3:
            square = rows[:3, :]
        elif square_id < 6:
            square = rows[3:6, :]
        else:
            square = rows[6:9, :]
        square_out = []
        for row in square:
            square_out.extend(row)
        return square_out

    def check_if_digits_in_square(self, row_id, col_id, digits):
        """Goes throught the list of digits and returns list of digits
        that are not present in square.

        Args:
            row_id (int): row id.
            col_id (int): column id.
            digits (list): List of digits to look for.

        Returns:
            list: Still available digits.
        """
        square = self.form_square(row_id, col_id)
        return [digit for digit in digits if digit not in square]

    def check_if_cell_is_empty(self, row_id, col_id):
        """Checks if required cell has digit in it or is it None.

        Args:
            row_id (int): Row id.
            col_id (int): Column id.

        Returns:
            Bool: True if cell is empty (contains None), False if
            digit is present.
        """
        if self.sudoku[row_id, col_id] is None:
            return True
        else:
            return False

    def get_available_digits_for_cell(self, row_id, col_id):
        """Checks what digits in range from 1 to 9 could be used in a cell.

        Args:
            row_id (int): row id.
            col_id (int): Column id.

        Returns:
            list: List of digits that are available.
        """
        if not self.check_if_cell_is_empty(row_id, col_id):
            return []
        digits = list(range(9))
        digits = [digit + 1 for digit in digits]

        digits = self.check_if_digits_in_row(row_id, digits)
        digits = self.check_if_digits_in_column(col_id, digits)
        digits = self.check_if_digits_in_square(row_id, col_id, digits)

        return digits

    def insert_value(self, row_id, col_id, value):
        """Inserts digit to cell.

        Args:
            row_id (int): Row id.
            col_id (int): Column id.
            value (int): Digit to be inserted.

        Raises:
            ValueError: Raises ValueError when there is a digit already.
        """
        if self.check_if_cell_is_empty(row_id, col_id):
            self.sudoku[row_id, col_id] = value
        else:
            print(self.sudoku[row_id, col_id])
            raise ValueError("Cell is already occupied")

    def fill_one_available_cells(self):
        """Runs through all cells once and fills in those that
        have only one value possible.

        Returns:
            Bool: True if at least one value was insterted. Otherwise False.
        """
        inserted = False
        for row_id in range(9):
            for col_id in range(9):
                digits = self.get_available_digits_for_cell(row_id, col_id)
                if len(digits) == 1:
                    self.insert_value(row_id, col_id, *digits)
                    inserted = True
        return inserted

    def loop_one_available_cells(self):
        """Loops through all cells untill no cells with one
        value available are left.
        """
        inserted = True
        while inserted:
            inserted = self.fill_one_available_cells()

    def find_first_empty_cell(self):
        """Finds first empty cell in a sudoku.
        Goes left to right and top to bottom.

        Returns:
            int, int: Column id and row id.
        """
        for row_id, row in enumerate(self.sudoku):
            for col_id, column in enumerate(row):
                if self.sudoku[row_id, col_id] is None:
                    return row_id, col_id

    def check_if_full_sudoku(self):
        """Checks if all cells are filled with numbers.

        Returns:
            Bool: True if all cells are filled with numbers. Otherwise False.
        """
        for row in self.sudoku:
            if None in row:
                return False
        return True

def fill_vague_cells(sudokus):
    while True:
        sudoku = Sudoku(sudokus[-1]["sudoku"].sudoku)
        try:
            row_id, col_id = sudoku.find_first_empty_cell()

        except TypeError:
            break

        digits = sudoku.get_available_digits_for_cell(row_id, col_id)

        while True:
            if len(digits) == 0:
                sudoku = Sudoku(sudokus[-2]["sudoku"].sudoku)
                row_id = sudokus[-1]["row_id"]
                col_id = sudokus[-1]["col_id"]
                digits = sudokus[-1]["digits"]
                sudokus = sudokus[:-1]
            else:
                break

        sudoku.insert_value(row_id, col_id, digits[0])
        sudoku.loop_one_available_cells()

        sudokus.append(
            {
                "sudoku": sudoku,
                "row_id": row_id,
                "col_id": col_id,
                "digits": digits[1:],
            }
        )

        if sudoku.check_if_full_sudoku():
            return sudoku.sudoku

def force_sudoku(empty_sudoku):
    """Runs through all cells and fills them with numbers by checking what
    numbers are available one by one.

    Args:
        empty_sudoku (np.array): array with digits that
        are already available in sudoku.

    Returns:
        np.array: Solved sudoku.
    """
    sudoku = Sudoku(empty_sudoku)
    sudoku.loop_one_available_cells()
    sudokus = [
        {"sudoku": sudoku, "row_id": None, "col_id": None, "digits": None}
    ]
    sudoku_final = fill_vague_cells(sudokus)
    return sudoku_final
