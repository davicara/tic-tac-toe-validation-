import unittest
from unittest.mock import patch
from io import StringIO
from src.main import print_board, is_win, tally_wins


class TestTicTacToe(unittest.TestCase):

    def test_vertical_win(self):
        print("TESTING VERTICAL WIN")
        board = [[' ' for _ in range(3)] for _ in range(3)]
        board[0][0] = 'X'
        board[1][0] = 'X'
        board[2][0] = 'X'
        self.assertTrue(is_win("X", board))

    def test_horizontal_win(self):
        print("TESTING HORIZONTAL WIN")
        board = [[' ' for _ in range(3)] for _ in range(3)]
        board[0][0] = 'X'
        board[0][1] = 'X'
        board[0][2] = 'X'
        self.assertTrue(is_win("X", board))

    def test_diagonal_win(self):
        print("TESTING DIAGONAL WIN")
        board = [[' ' for _ in range(3)] for _ in range(3)]
        board[0][0] = 'X'
        board[1][1] = 'X'
        board[2][2] = 'X'
        self.assertTrue(is_win("X", board))

    def test_board_print(self):
        print("TESTING BOARD PRINTING")
        expected_output = " | | \n-----\n | | \n-----\n | | \n-----\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_board()
            self.assertEqual(fake_out.getvalue(), expected_output)



if __name__ == '__main__':
    unittest.main()
