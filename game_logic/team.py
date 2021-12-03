

class Team(int):
    def __new__(cls, value, *args, **kwargs):
        return int.__new__(cls, value)
    
        
class White(Team):
    def __init__(self):
        super().Team.__init__(1)

    
class Black(Team):
    def __init__(self):
        super().Team.__init__(-1)