import unittest

from game_logic.team import Team, White, Black


class TestTeam(unittest.TestCase):
    """Test the team."""

    def test_initialisation(self):
        """Test the constructor."""
        value = 0
        team = Team(value)
        self.assertIsInstance(team, int)
        self.assertEqual(team, value)


class TestWhite(unittest.TestCase):
    """Test the white team."""

    def test_initialisation(self):
        """Test the constructor."""
        team = White()
        self.assertIsInstance(team, int)
        self.assertIsInstance(team, Team)

        self.assertEqual(team, 1)


class TestBlack(unittest.TestCase):
    """Test the white team."""

    def test_initialisation(self):
        """Test the constructor."""
        team = Black()
        self.assertIsInstance(team, int)
        self.assertIsInstance(team, Team)

        self.assertEqual(team, -1)
