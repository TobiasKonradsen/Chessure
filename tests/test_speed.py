# import unittest
# import time
# from game_logic.moves import Moves as SlowMoves, SlowMoves as Moves

# n = 100_000


# class TestSpeed(unittest.TestCase):

#     def createMoves(self):
#         j = 0
#         for i in range(n):
#             m = Moves([1]*64)
#             j += 1

#     def createSlowMoves(self):
#         j = 0
#         for i in range(n):
#             m = SlowMoves([1]*64)
#             j += 1

#     def indexMoves(self):
#         m = Moves([1]*n)
#         for i in range(n):
#             m[i]

#     def indexSlowMoves(self):
#         m = SlowMoves([1]*n)
#         for i in range(n):
#             m[i]

#     def test_creation(self):
#         start_time = time.time()
#         self.createMoves()
#         print(time.time() - start_time)

#         start_time = time.time()
#         self.indexMoves()
#         print(time.time() - start_time)

#         start_time = time.time()
#         self.createSlowMoves()
#         print(time.time() - start_time)

#         start_time = time.time()
#         self.indexSlowMoves()
#         print(time.time() - start_time)


# if __name__ == "__main__":
#     unittest.main()
