import unittest

from game_logic.moves import Moves
from game_logic.position import Position


class TestMoves(unittest.TestCase):
    """Test the functionality of the moves collection."""

    def test_constructor(self):
        """Test the constructor."""
        moves = Moves([])
        self.assertIsInstance(moves, Moves)
        self.assertEqual(len(moves), 0)

    def test_multiple_args_constructor(self):
        """Test the constructor."""
        n = 10
        moves = Moves([None]*n)
        self.assertIsInstance(moves, Moves)
        self.assertEqual(len(moves), n)

    def test_append(self):
        """Test whether we can append to the moves."""
        moves = Moves([])
        with self.assertRaises(TypeError):
            moves.append(0)
        moves = Moves([])
        position = Position()
        print(moves)
        moves.append(position)
        self.assertEqual(moves[0], position)


if __name__ == "__main__":
    unittest.main()
