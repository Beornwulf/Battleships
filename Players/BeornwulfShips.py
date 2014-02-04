import const
import base_player
from random import randint, shuffle


class Player(base_player.BasePlayer):

    def __init__(self):
        base_player.BasePlayer.__init__(self)
        self._playerName = "Beornwulf"
        self._playerYear = "1"  # year of study
        self._version = "1.0"  # version of AI
        self._playerDescription = "Basic Hunter-Killer algorithm."
        self._mode = "hunt"
        self._allSquares = self.initialiseBoard()
        self._targets = self.initialiseHunt()
        self._shots = []
        self._hits = []
        self._priorityTargets = []

    def resetGame(self):
        """
        Resets internal variables and lists between games.
        """
        self._mode = "hunt"
        self._allSquares = self.initialiseBoard()
        self._targets = self.initialiseHunt()
        self._shots = []
        self._hits = []
        self._priorityTargets = []

    def initialiseBoard(self):
        """
        Creates a list of all possible board squares.
        """
        board = [[x, y] for x in range(6) for y in range(6)]
        board.extend([x, y] for x in range(6, 12) for y in range(12))
        return board

    def initialiseHunt(self):
        """
        Create an initial list of targets for the hunt phase.
        Currently a checkerboard pattern.
        """
        hunt_targets = []
        for item in self._allSquares:
            x, y = item
            if (x + y) % 2 == 0:
                hunt_targets.append(item)
        shuffle(hunt_targets)
        #print len(hunt_targets)
        return hunt_targets

    def deployFleet(self):
        """
        Deploy fleet in random positions.
        """
        self.resetGame()
        self._initBoards()
        destroyer = [[0, 0], [0, 1]]
        cruiser = [[0, 0], [0, 1], [0, 2]]
        battleship = [[0, 0], [0, 1], [0, 2], [0, 3]]
        hovercraft = [[0, 0], [0, 1], [1, 1], [-1, 1], [1, 2], [-1, 2]]
        aircraftcarrier = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, 2], [0, 3]]
        fleet = [destroyer, cruiser, battleship, hovercraft, aircraftcarrier]
        boardSquares = [[x, y] for x in range(6) for y in range(6)]
        boardSquares.extend([x, y] for x in range(6, 12) for y in range(12))
        for i in fleet:
            isValid = False
            while isValid is False:
                r = randint(0, (len(boardSquares) - 1))
                keyPoint = boardSquares[r]
                ship = []
                for j in i:
                    square = []
                    square.append(j[0] + keyPoint[0])
                    square.append(j[1] + keyPoint[1])
                    ship.append(square)
                isValid = True
                internalValid = False
                while not internalValid:
                    for square in ship:
                        x, y = square
                        if not square in boardSquares:
                            isValid = False
                        elif self._playerBoard[x][y] == const.OCCUPIED:
                            isValid = False
                        internalValid = True
                if isValid:
                    for square in ship:
                        x, y = square
                        self._playerBoard[x][y] = const.OCCUPIED
        return self._playerBoard

    def chooseMove(self):
        """
        Derermines phase of attack and calls appropriate method.
        Exports target square.
        """
        if self._mode == "hunt":
            target = self.huntMode()
        elif self._mode == "kill":
            target = self.killMode()
        #print len(self._shots), "shots taken"
        #print "shot at:", self._shots
        #print len(self._hits), "hits:", self._hits
        row, col = target
        return row, col

    def huntMode(self):
        """
        Selects a random target from the checkerboard of available targets.
        """
        #print "available targets:", self._targets
        if len(self._targets) == 0:
            for i in self._allSquares:
                if not i in self._shots:
                    self._targets.append(i)
        target = self._targets.pop()
        self._shots.append(target)
        return target

    def killMode(self):
        """
        Once a ship has been found, focuses shots in that area until all squares adjacent to a hit have been targeted.
        Potential improvement: limit killMode to 6 hits in a phase.
        """
        target_list = []
        for i in self._hits:
            a = i[0]
            b = i[1]
            target_list.append([a, b + 1])
            target_list.append([a, b - 1])
            target_list.append([a + 1, b])
            target_list.append([a - 1, b])
        #print "potential priority targets:", target_list
        for i in target_list:
            if i in self._priorityTargets:
                pass
#                print i, "is in _priorityTargets"
            elif i in self._shots:
                pass
#                print i, "is in _shots"
            elif not i in self._allSquares:
                pass
#                print i, "is off the board"
            else:
                self._priorityTargets.append(i)
        if len(self._priorityTargets) == 0:
            self._mode = "hunt"
            target = self.huntMode()
            return target
        else:
            #print "priority targets:", self._priorityTargets
            target = self._priorityTargets.pop()
            self._shots.append(target)
            return target

    def setOutcome(self, entry, row, col):
        """
        entry: the outcome of your shot onto your opponent,
               expected value is const.HIT for hit and const.MISSED for missed.
        row: (int) the board row number (e.g. row A is 0)
        col: (int) the board column (e.g. col 2 is represented by  value 3) so
        A3 case is (0,2)
        """
        if entry == const.HIT:
            shot = [row, col]
            #print "hit"
            Outcome = const.HIT
            self._hits.append(shot)
            #print "hits so far:", self._hits
            self._mode = "kill"
        elif entry == const.MISSED:
            #print "missed"
            Outcome = const.MISSED
        else:
            raise Exception("Invalid input!")
        self._opponenBoard[row][col] = Outcome
        #print "shots taken:", len(self._shots)
        #print "shots hit:", len(self._hits)

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