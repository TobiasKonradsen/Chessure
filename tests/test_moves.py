import unittest

from game_logic.moves import Moves
from game_logic.position import Position


class TestMoves(unittest.TestCase):
    """Test the functionality of the moves collection."""

    def setUp(self):
        self.moves = Moves()

    def test_constructor(self):
        """Test the constructor."""
        self.assertIsInstance(self.moves, Moves)
        self.assertEqual(len(self.moves), 0)

    def test_append(self):
        """Test whether we can append to the moves."""
        with self.assertRaises(TypeError):
            self.moves.append(0)

        position = Position()
        self.moves.append(position)
        self.assertEqual(self.moves[0], position)


if __name__ == "__main__":
    unittest.main()
