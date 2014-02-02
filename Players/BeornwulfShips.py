import const
import base_player
from random import randint


class Player(base_player.BasePlayer):

    def __init__(self):
        base_player.BasePlayer.__init__(self)
        self._playerName = "Beornwulf"
        self._playerYear = "1"  # year of study
        self._version = "1.0"  # version of AI
        self._playerDescription = ""

    # Distribute the fleet onto your board
    def deployFleet(self):
        """
        Decide where you want your fleet to be deployed, then return your board.
        The attribute to be modified is _playerBoard. You can see how it is
        defined in the _initBoards method in the file base_player.py
        """
        self._initBoards()
        destroyer = [(0, 0), (0, 1)]
        cruiser = [(0, 0), (0, 1), (0, 2)]
        battleship = [(0, 0), (0, 1), (0, 2), (0, 3)]
        hovercraft = [(0, 0), (0, 1), (1, 1), (-1, 1), (1, 2), (-1, 2)]
        aircraftcarrier = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, 2), (0, 3)]
        fleet = [destroyer, cruiser, battleship, hovercraft, aircraftcarrier]
        boardSquares = [(x, y) for x in range(6) for y in range(6)]
        boardSquares.extend((x, y) for x in range(6, 12) for y in range(12))
        for i in fleet:

        return self._playerBoard

    # Decide what move to make based on current state of opponent's board and
    # print it out
    def chooseMove(self):
        """
        Decide what move to make based on current state of opponent's board and
        return it
        # Completely random strategy
        # Knowledge about opponent's board is completely ignored
        """
        row = randint(0, 11)
        if row < 6:
            # Top half of board, so choose between first and sixth row
            col = randint(0, 5)
        else:
            # Bottom half so choose between first and twelfth row
            col = randint(0, 11)
        # Return move in row (letter) + col (number) grid reference
        # e.g. A3 is represented as 0,2
        return row, col

    def setOutcome(self, entry, row, col):
        """
        entry: the outcome of your shot onto your opponent,
               expected value is const.HIT for hit and const.MISSED for missed.
        row: (int) the board row number (e.g. row A is 0)
        col: (int) the board column (e.g. col 2 is represented by  value 3) so
        A3 case is (0,2)
        """
#        is_valid = False
        if entry == const.HIT:
#            is_valid = True
            Outcome = const.HIT
        elif entry == const.MISSED:
#            is_valid = True
            Outcome = const.MISSED
        else:
            raise Exception("Invalid input!")
        self._opponenBoard[row][col] = Outcome

    def getOpponentMove(self, row, col):
        """ You might like to keep track of where your opponent
        has missed, but here we just acknowledge it. Note case A3 is
        represented as row = 0, col = 2.
        """
        if ((self._playerBoard[row][col] == const.OCCUPIED)
            or (self._playerBoard[row][col] == const.HIT)):
            # They may (stupidly) hit the same square twice so we check
            # for occupied or hit
            self._playerBoard[row][col] = const.HIT
            result = const.HIT
        else:
            # You might like to keep track of where your opponent has missed,
            # but here we just acknowledge it
            result = const.MISSED
        return result


def getPlayer():
    """ MUST NOT be changed, used to get a instance of your class."""
    return Player()