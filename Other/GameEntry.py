class GameEntry:
    """represents one entry of a list of high scores."""
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)  # '(Bob, 98)'

class Scoreboard:
    """ fixed-length sequence of high scores in non-decreasing order."""
    def __init__(self, capacity=10):
        """ Initialize scoreboard with given maximum capacity."""
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        """ return entry at index k."""
        return self._board[k]

    def __str__(self):
        """ return string representaion of the high score list."""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """ consider adding entry to high scores. """
        score = entry.get_score()
        # answer is yes if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()
        if good:    
            if self._n < len(self._board):  # no score drops from list
                self._n += 1    # so overall number increases
            # shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]   # shift entry from j-1 to j
                j -= 1  # add decrement j
            self._board[j] = entry # when done, add new entry 
        # return self._board

def main():

    mike = GameEntry('Mike', 1105)
    bob = GameEntry('Bob', 750)
    paul = GameEntry('Paul', 720)
    anna = GameEntry('Anna', 660)
    rose = GameEntry('Rose', 590)
    jack = GameEntry('Jack', 510)

    board = Scoreboard()

    board.add(mike)
    board.add(bob)
    board.add(paul)
    board.add(anna)
    board.add(rose)
    board.add(jack)
    
    jill = GameEntry('Jill', 740)
    board.add(jill)

    print(board)


if __name__ == '__main__':
    main()
