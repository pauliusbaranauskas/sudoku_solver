import numpy as np


class Sudoku:
    def __init__(self, sudoku_row_list: list=False):
        if sudoku_row_list is False:
            sudoku_row_list = self.get_empty_matrix()
        self.sudoku = np.array(sudoku_row_list)
        if self.validate_matrix():
            pass

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

    @staticmethod
    def get_square_index(row_id: int, col_id: int):
        """Takes column and row ids and returns square index.

        Args:
            row_id (int): Row id.
            col_id (int): Column id.

        Returns:
            int: Square id.
        """
        return (row_id/3)*3 + col_id/3

    def validate_matrix(self):
        """Checks if sudoku is expected shape.

        Raises:
            ValueError: ValueError if row count is not equal to 9.
            ValueError: ValueError if column count is not equal to 9.
        
        Returns:
            Bool: True if no mistakes were found. Otherwise raises errors.
        """
        rows, cols = self.sudoku.shape
        if rows != 9:
            raise ValueError(f"Incorrect number of rows: {rows}")
        elif cols != 9:
            raise ValueError(f"Incorrect number of columns: {cols}")
        if self.check_duplicates():
            return True

    def check_duplicates(self):
        """Checks if sudoku contains duplicates in any index.
        Raises `ValueError` if duplicate is found in any of the sections.
        Otherwise returns `True`

        Raises:
            ValueError: Returns ValueError when duplicates are in a row.
            ValueError: Returns ValueError when duplicates are in a column.
            ValueError: Returns ValueError when duplicates are in a square.

        Returns:
            Bool: `True` if no duplicates were found. Otherwiser raises `ValueError`.
        """
        for i in range(9):
            if not self.check_list_duplicates(self.sudoku[i, :]):
                raise ValueError(f"Duplicates in row {i}")
            elif not self.check_list_duplicates(self.sudoku[:, i]):
                raise ValueError(f"Duplicates in column {i}")
            elif not self.check_list_duplicates(self.form_square_by_index(i)):
                raise ValueError(f"Duplicates in square {i}")
        return True
    
    @staticmethod
    def check_list_duplicates(row):
        """Checks if list or array contains duplicates.
        Returns `False` if duplicates exists in any sections (Does not specify what digit is duplicated).
        Otherwise returns `True`.

        Arguments:
            row (list/array): List or array with numbers.

        Returns:
            Bool: True if there are no duplicates. False if duplicates were found in any section.
        """
        row = [digit for digit in row if digit is not None]
        if len(row) == len(set(row)):
            return True
        else:
            return False

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
        square_out = self.form_square_by_index(square_id)
        return square_out

    def form_square_by_index(self, square_id):
        """Forms a square by square index.

        Args:
            square_id (int): Square index going top to botom and left to right.

        Returns:
            list: square as a list.
        """
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

        Returns:
            Bool: True if value was inserted.
        """
        if not self.check_if_cell_is_empty(row_id, col_id):
            print(self.sudoku[row_id, col_id])
            raise ValueError("Cell is already occupied")
        else:
            if not self.check_if_digit_in_sections(row_id, col_id, value):
                self.sudoku[row_id, col_id] = value

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
                    inserted = self.insert_value(row_id, col_id, digits[0])
        return inserted

    def loop_one_available_cells(self):
        """Loops through all cells until no cells with one
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
        for row_id in range(9):
            for col_id in range(9):
                if self.sudoku[row_id, col_id] is None:
                    return row_id, col_id

    def check_if_full_sudoku(self):
        """Checks if all cells are filled with numbers.

        Returns:
            Bool: True if all cells are filled with numbers. Otherwise False.
        """
        if self.check_duplicates():
            for row in self.sudoku:
                if None in row:
                    return False
        return True

    @staticmethod
    def get_empty_matrix():
        """Returns matrix of shape 9x9 with None values only.

        Returns:
            np.array: Matrix of shape 9x9 with None values only
        """
        matrix = [[None] * 9] * 9
        matrix = np.array(matrix)
        return matrix

    def check_if_digit_in_sections(self, row_id, col_id, value):
        """Checks if digit is not repeated in row, column or square.
        Returns `False` if digit could be inserted. Otherwise raises `ValueError`.

        Args:
            row_id (int): Row in which digit should be inserted.
            col_id (int): Column in which digit should be inserted.
            value (int): Digit that should be inserted.

        Raises:
            ValueError: `ValueError` if digit already exists in row.
            ValueError: `ValueError` if digit already exists in column.
            ValueError: `ValueError` if digit already exists in square.

        Returns:
            Bool: `False` if digit is not in any of the sections.
        """
        if value in self.sudoku[row_id, :]:
            raise ValueError(f"Value already esists in row {row_id}")
        elif value in self.sudoku[:, col_id]:
            raise ValueError(f"Value already esists in column {col_id}")
        elif value in self.form_square(row_id, col_id):
            raise ValueError(
                f"Value already esists in column {self.get_square_index(row_id, col_id)}")
        else:
            return False


def fill_vague_cells(sudokus):
    """Loops through list of sudoku objects and tries possible values
    Args:
        sudokus(list): list containing already filled cells.

    Returns:
        list: list with sudoku rows.
    """
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
