from game_logic.position import Position


class SlowMoves(list):
    """A collection of positions."""
    content_type = Position

    def __new__(cls, *args):
        """Return a Moves instance."""
        return super(Moves, cls).__new__(cls, *args)

    def __init__(self, *args):
        """Call list __init__."""
        super().__init__(*args)

    def __len__(self, *args):
        """Use builtin-methods."""
        return super().__len__(*args)

    def __getitem__(self, index):
        super().__getitem__(index)

    def append(self, item):
        """Use builtin-methods."""
        if not isinstance(item, self.content_type):
            raise TypeError(f"Item {item} is not a Position, but a {item.__class__.__name__}")
        super(Moves, self).append(item)


class Moves:
    """A collection of positions."""
    content_type = Position
    l = []

    def __init__(self, *args):
        """Call list __init__."""
        temp = [*args]
        self.l = temp[0]

    def __getitem__(self, index):
        return self.l[index]
    
    def __repr__(self):
        return str(self.l)
        
    def __len__(self, *args):
        """Use builtin-methods."""
        return len(self.l)
    
    def append(self, item):
        """Use builtin-methods."""
        if not isinstance(item, self.content_type):
            raise TypeError(f"Item {item} is not a Position, but a {item.__class__.__name__}")
        self.l.append(item)
