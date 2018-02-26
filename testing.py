# heuristic function counts number of w have to move overband adds them together
import unittest


def astar(self):
    while True:
        tup = self.frontier.get()
        state = tup[0]
        board = state.board
        print(board)
        if (self.h(board) == 0):
            break
        if (board in self.closed):
            continue
        else:
            self.closed.add(board)
            self.next(state)


def h(current):
    result = 0
    count = 0
    for i in current:
        if i == 'b':
            count += 1
        if i == 'w':
            result += count
    return result

class puzzleTestCase(unittest.TestCase):
    """determine if h function is working correctly"""

    def test_is_hsolved_zero(self):
        """Is solved state considered to be zero by heuristic function"""
        self.assertEqual(h(['w', 'w', 'w', 'b', 'b', 'b', '']), 0, msg='wwwbbb_ fails')
        self.assertEqual(h(['b', 'b', 'b', '', 'w', 'w','w']), 9, msg='bbb_www fails')
        self.assertEqual(h(['b', 'b', 'w', 'b', '', 'w', 'w']), 8, msg='bbwb_ww fails')

if __name__ == '__main__':
    unittest.main()
