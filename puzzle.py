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
        ##self.intial = frontier.

    #heuristic function counts number of w have to move overband adds them together
    def h(self, current):
        result = 0
        count = 0
        for i in current.board:
            if i == 'b':
                count += 1
            if i == 'w':
                result += count
        return result

    ## calculates next set of moves and adds them to frontier
    def next(self, current):
        print(self.closed)

    def f(self):
        print("place")

    def astar(self):
        print("placeholder")

if __name__ == '__main__':
    print("happy camper")
