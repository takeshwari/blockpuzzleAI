import queue as Q

from babel._compat import cmp

SIZE = 7
## state contains board state and the state's g value
class state:
    g=0
    board = []
    def __init__(self, board, g):
        self.g = g
        self.board = board

    ##for comparing state objects in priority queue
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.g == other.g
        return NotImplemented

    ##for comparing state objects in priority queue
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.g < other.g
        return NotImplemented


class puzzle():
    frontier= Q.PriorityQueue()
    closed = set()

    def __init__(self, board):
        intial = state(board, 0)
        self.frontier.put((self.f(intial), intial))

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
        board, g= current.board, current.g
        space = board.index(" ")
        cost = 1
        print(self.frontier)
        for i in range(1, 4):
            new = board
            if i == 3:
                cost =2
            if(space -i > -1):
                new[space-i], new[i] =  new[i], new[space-i]
                newState = state(new,g + cost )
                ans= self.f(newState)
                self.frontier.put((ans, newState))

            elif (space + i < SIZE):
                new[space + i], new[i] = new[i], new[space + i]
                newState = state(new, g + cost)
                self.frontier.put((self.f(newState), newState))

    ## calculates the f function
    def f(self, state):
        return state.g + self.h(state)

    def astar(self):
        while True:
            tup = self.frontier.get()
            state = tup[1]
            board = state.board
            print(board)
            self.next(state)
            if (self.h(state) == 0):
                break
            elif (tuple(board) in self.closed):
                print(self.closed)
                continue
            else:
                self.closed.add(tuple(board))
                self.next(state)

    print("do we break out?")

if __name__ == '__main__':
    tiles = puzzle(['b', 'b', 'w', 'b', ' ', 'w', 'w'])
    tiles.astar()
