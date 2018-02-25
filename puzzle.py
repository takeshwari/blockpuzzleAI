from queue import PriorityQueue

SIZE = 7
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
        print("whatever")
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
        board, g= current.element, current.g
        space = board.index(" ")
        cost = 1

        for i in range(1, 4):
            new = board
            if i == 3:
                cost =2
            if(space -i > -1):
                new[space-i], new[i] =  new[i], new[space-i]
                newState = state(new,g + cost )
                self.frontier.put(self.f(newState), newState)
            elif (space + i < SIZE ):
                new[space + i], new[i] = new[i], new[space + i]
                newState = state(new, g + cost)
                self.frontier.put(self.f(newState), newState)

    def f(self, state):
        return state.g + self.h(state)


    def astar(self):
        print("placeholder")

if __name__ == '__main__':
    print("happy camper")
