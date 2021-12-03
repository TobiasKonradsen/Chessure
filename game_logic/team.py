class Team(int):
    def __new__(cls, value):
        print('new', value)
        return int.__new__(cls, value)


class White(Team):
    def __new__(cls):
        return int.__new__(cls, 1)


class Black(Team):
    def __new__(cls):
        return int.__new__(cls, -1)
