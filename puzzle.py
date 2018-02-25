from queue import PriorityQueue

## state contains board state and the g value
class state:
    g=0
    board = []
    def _init_(self, board, g):
        self.g = g
        self.board = board

class puzzle:
    frontier= PriorityQueue()
    closed = set()

    def _init_(self, board):
        self.intial = frontier.

    def h(self):
        return self.intial

    def f(self):
        print("place")

    def astar(self):
        print("placeholder")

if __name__ == '__main__':
    print("happy camper")
