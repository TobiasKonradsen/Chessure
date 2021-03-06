class Team(int):
    def __new__(cls, value):
        return int.__new__(cls, value)


class White(Team):
    def __new__(cls):
        return int.__new__(cls, 1)
    
    def __repr__(self):
        return 'White'


class Black(Team):
    def __new__(cls):
        return int.__new__(cls, -1)
    
    def __repr__(self):
        return 'Black'
