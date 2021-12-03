from game_logic.position import Position


class Moves(list):
    """A collection of positions."""
    content_type = Position

    def __new__(cls, *args, **kwargs):
        return super(Moves, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        super().__init__()

    def __len__(self, *args):
        return super().__len__(*args)

    def append(self, item):
        if not isinstance(item, self.content_type):
            raise TypeError(f"Item {item} is not a Position, but a {item.__class__.__name__}")
        super(Moves, self).append(item)
