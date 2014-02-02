import const
import base_player
from random import randint, seed

class Player(base_player.BasePlayer):

    
    def __init__(self):
        base_player.BasePlayer.__init__(self)
        self._playerName = "Frank's Awesome Player!!!"  # Can be whatever you want as long as it is a sensible one.
                                                    # No more than 25 characters
        self._playerYear = "7" # indicate your year of study here should range from 1 to 4
        self._version = "3.0"  # enter the version of your solution if you have more than one
        self._playerDescription = "Franks AI - 2D Pattern Match Firing - Fully Random Ship Positioning"
        self.start = True

    def surrounding(self, yPlace, xPlace):
        if self.ourPlacingBoard[yPlace][xPlace] == 0 and ((self.ourPlacingBoard[yPlace+1][xPlace] < 1 and self.ourPlacingBoard[yPlace][xPlace+1] < 1 and self.ourPlacingBoard[yPlace-1][xPlace] < 1 and self.ourPlacingBoard[yPlace][xPlace-1] < 1) or self.forcePlace):
            return True
        else:
            return False
    
    def placeDestroyer(self):
        attemptingPlacement = True
        
        while attemptingPlacement:
            xPlace = randint(0,11)
            yPlace = randint(0,11)
            choice = randint(0,1)
            
            if choice:
                if self.surrounding(yPlace,xPlace) and self.surrounding(yPlace+1,xPlace):
                    attemptingPlacement = False
                    self._playerBoard[yPlace][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace+1][xPlace]=const.OCCUPIED
                    self.ourPlacingBoard[yPlace][xPlace] = 1
                    self.ourPlacingBoard[yPlace+1][xPlace] = 1
            else:
                if self.surrounding(yPlace,xPlace) and self.surrounding(yPlace,xPlace+1):
                    attemptingPlacement = False
                    self._playerBoard[yPlace][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace][xPlace+1]=const.OCCUPIED
                    self.ourPlacingBoard[yPlace][xPlace] = 1
                    self.ourPlacingBoard[yPlace][xPlace+1] = 1
        
    def placeCruiser(self):
        attemptingPlacement = True
        
        while attemptingPlacement:
            xPlace = randint(0,11)
            yPlace = randint(0,11)
            choice = randint(0,1)
            
            if choice:
                if self.surrounding(yPlace,xPlace) and self.surrounding(yPlace,xPlace+1) and self.surrounding(yPlace,xPlace+2):
                    attemptingPlacement = False
                    self._playerBoard[yPlace][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace][xPlace+1]=const.OCCUPIED
                    self._playerBoard[yPlace][xPlace+2]=const.OCCUPIED
                    self.ourPlacingBoard[yPlace][xPlace] = 1
                    self.ourPlacingBoard[yPlace][xPlace+1] = 1
                    self.ourPlacingBoard[yPlace][xPlace+2] = 1
            else:
                if self.surrounding(yPlace,xPlace) and self.surrounding(yPlace+1,xPlace) and self.surrounding(yPlace+2,xPlace):
                    attemptingPlacement = False
                    self._playerBoard[yPlace][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace+1][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace+2][xPlace]=const.OCCUPIED
                    self.ourPlacingBoard[yPlace][xPlace] = 1
                    self.ourPlacingBoard[yPlace+1][xPlace] = 1
                    self.ourPlacingBoard[yPlace+2][xPlace] = 1
        
    def placeBattleship(self):
        attemptingPlacement = True
        
        while attemptingPlacement:
            xPlace = randint(0,11)
            yPlace = randint(0,11)
            choice = randint(0,3)
            
            if choice == 0:
                if self.surrounding(yPlace,xPlace) and self.surrounding(yPlace,xPlace+1) and self.surrounding(yPlace,xPlace+2) and self.surrounding(yPlace,xPlace+3):
                    attemptingPlacement = False
                    self._playerBoard[yPlace][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace][xPlace+1]=const.OCCUPIED
                    self._playerBoard[yPlace][xPlace+2]=const.OCCUPIED
                    self._playerBoard[yPlace][xPlace+3]=const.OCCUPIED
                    self.ourPlacingBoard[yPlace][xPlace] = 1
                    self.ourPlacingBoard[yPlace][xPlace+1] = 1
                    self.ourPlacingBoard[yPlace][xPlace+2] = 1
                    self.ourPlacingBoard[yPlace][xPlace+3] = 1
            if choice == 1:
                 if self.surrounding(yPlace,xPlace) and self.surrounding(yPlace+1,xPlace) and self.surrounding(yPlace+2,xPlace) and self.surrounding(yPlace+3,xPlace):
                     attemptingPlacement = False
                     self._playerBoard[yPlace][xPlace]=const.OCCUPIED
                     self._playerBoard[yPlace+1][xPlace]=const.OCCUPIED
                     self._playerBoard[yPlace+2][xPlace]=const.OCCUPIED
                     self._playerBoard[yPlace+3][xPlace]=const.OCCUPIED
                     self.ourPlacingBoard[yPlace][xPlace] = 1
                     self.ourPlacingBoard[yPlace+1][xPlace] = 1
                     self.ourPlacingBoard[yPlace+2][xPlace] = 1
                     self.ourPlacingBoard[yPlace+3][xPlace] = 1
            if choice == 2:
                xPlace = randint(3,11)
                if self.surrounding(yPlace,xPlace) and self.surrounding(yPlace,xPlace-1) and self.surrounding(yPlace,xPlace-2) and self.surrounding(yPlace,xPlace-3):
                    attemptingPlacement = False
                    self._playerBoard[yPlace][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace][xPlace-1]=const.OCCUPIED
                    self._playerBoard[yPlace][xPlace-2]=const.OCCUPIED
                    self._playerBoard[yPlace][xPlace-3]=const.OCCUPIED
                    self.ourPlacingBoard[yPlace][xPlace] = 1
                    self.ourPlacingBoard[yPlace][xPlace-1] = 1
                    self.ourPlacingBoard[yPlace][xPlace-2] = 1
                    self.ourPlacingBoard[yPlace][xPlace-3] = 1
            if choice == 3:
                yPlace = randint(3,11)
                if self.surrounding(yPlace,xPlace) and self.surrounding(yPlace-1,xPlace) and self.surrounding(yPlace-2,xPlace) and self.surrounding(yPlace-3,xPlace):
                    attemptingPlacement = False
                    self._playerBoard[yPlace][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace-1][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace-2][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace-3][xPlace]=const.OCCUPIED
                    self.ourPlacingBoard[yPlace][xPlace] = 1
                    self.ourPlacingBoard[yPlace-1][xPlace] = 1
                    self.ourPlacingBoard[yPlace-2][xPlace] = 1
                    self.ourPlacingBoard[yPlace-3][xPlace] = 1
        
    def placeHovercraft(self):
        attemptingPlacement = True
        forcePlacement = 0
        
        while attemptingPlacement:
            xPlace = randint(0,11)
            yPlace = randint(0,11)
            choice = randint(0,3)
            forcePlacement = forcePlacement + 1
            
            if forcePlacement > 1000:
                self.forcePlace = True
            
            if choice == 0:
                if self.surrounding(yPlace,xPlace+1) and self.surrounding(yPlace+1,xPlace) and self.surrounding(yPlace+1,xPlace+1) and self.surrounding(yPlace+1,xPlace+2) and self.surrounding(yPlace+2,xPlace) and self.surrounding(yPlace+2,xPlace+2):
                    attemptingPlacement = False
                    self._playerBoard[yPlace][xPlace+1]=const.OCCUPIED
                    self._playerBoard[yPlace+1][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace+1][xPlace+1]=const.OCCUPIED
                    self._playerBoard[yPlace+1][xPlace+2]=const.OCCUPIED
                    self._playerBoard[yPlace+2][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace+2][xPlace+2]=const.OCCUPIED
                    self.ourPlacingBoard[yPlace][xPlace] = 1
                    self.ourPlacingBoard[yPlace+1][xPlace] = 1
                    self.ourPlacingBoard[yPlace+1][xPlace+1] = 1
                    self.ourPlacingBoard[yPlace+1][xPlace+2] = 1
                    self.ourPlacingBoard[yPlace+2][xPlace] = 1
                    self.ourPlacingBoard[yPlace+2][xPlace+2] = 1
            if choice == 1:
                if self.surrounding(yPlace+1,xPlace) and self.surrounding(yPlace,xPlace+1) and self.surrounding(yPlace+1,xPlace+1) and self.surrounding(yPlace+2,xPlace+1) and self.surrounding(yPlace,xPlace+2) and self.surrounding(yPlace+2,xPlace+2):
                    attemptingPlacement = False
                    self._playerBoard[yPlace+1][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace][xPlace+1]=const.OCCUPIED
                    self._playerBoard[yPlace+1][xPlace+1]=const.OCCUPIED
                    self._playerBoard[yPlace+2][xPlace+1]=const.OCCUPIED
                    self._playerBoard[yPlace][xPlace+2]=const.OCCUPIED
                    self._playerBoard[yPlace+2][xPlace+2]=const.OCCUPIED
                    self.ourPlacingBoard[yPlace][xPlace] = 1
                    self.ourPlacingBoard[yPlace][xPlace+1] = 1
                    self.ourPlacingBoard[yPlace+1][xPlace+1] = 1
                    self.ourPlacingBoard[yPlace+2][xPlace+1] = 1
                    self.ourPlacingBoard[yPlace][xPlace+2] = 1
                    self.ourPlacingBoard[yPlace+2][xPlace+2] = 1
            xPlace = randint(2,11)
            yPlace = randint(2,11)
            if choice == 2:
                if self.surrounding(yPlace,xPlace-1) and self.surrounding(yPlace-1,xPlace) and self.surrounding(yPlace-1,xPlace-1) and self.surrounding(yPlace-1,xPlace-2) and self.surrounding(yPlace-2,xPlace) and self.surrounding(yPlace-2,xPlace-2):
                    attemptingPlacement = False
                    self._playerBoard[yPlace][xPlace-1]=const.OCCUPIED
                    self._playerBoard[yPlace-1][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace-1][xPlace-1]=const.OCCUPIED
                    self._playerBoard[yPlace-1][xPlace-2]=const.OCCUPIED
                    self._playerBoard[yPlace-2][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace-2][xPlace-2]=const.OCCUPIED
                    self.ourPlacingBoard[yPlace][xPlace] = 1
                    self.ourPlacingBoard[yPlace-1][xPlace] = 1
                    self.ourPlacingBoard[yPlace-1][xPlace-1] = 1
                    self.ourPlacingBoard[yPlace-1][xPlace-2] = 1
                    self.ourPlacingBoard[yPlace-2][xPlace] = 1
                    self.ourPlacingBoard[yPlace-2][xPlace-2] = 1
            if choice == 3:
                if self.surrounding(yPlace-1,xPlace) and self.surrounding(yPlace,xPlace-1) and self.surrounding(yPlace-1,xPlace-1) and self.surrounding(yPlace-2,xPlace-1) and self.surrounding(yPlace,xPlace-2) and self.surrounding(yPlace-2,xPlace-2):
                    attemptingPlacement = False
                    self._playerBoard[yPlace-1][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace][xPlace-1]=const.OCCUPIED
                    self._playerBoard[yPlace-1][xPlace-1]=const.OCCUPIED
                    self._playerBoard[yPlace-2][xPlace-1]=const.OCCUPIED
                    self._playerBoard[yPlace][xPlace-2]=const.OCCUPIED
                    self._playerBoard[yPlace-2][xPlace-2]=const.OCCUPIED
                    self.ourPlacingBoard[yPlace][xPlace] = 1
                    self.ourPlacingBoard[yPlace][xPlace-1] = 1
                    self.ourPlacingBoard[yPlace-1][xPlace-1] = 1
                    self.ourPlacingBoard[yPlace-2][xPlace-1] = 1
                    self.ourPlacingBoard[yPlace][xPlace-2] = 1
                    self.ourPlacingBoard[yPlace-2][xPlace-2] = 1
        
    def placeAircraftCarrier(self):
        attemptingPlacement = True
        forcePlacement = 0
        
        while attemptingPlacement:
            xPlace = randint(0,11)
            yPlace = randint(0,11)
            choice = randint(0,1)
            
            forcePlacement = forcePlacement + 1
            
            if forcePlacement > 1000:
                self.forcePlace = True
            
            if choice:
                if self.surrounding(yPlace+1,xPlace) and self.surrounding(yPlace+1,xPlace+1) and self.surrounding(yPlace+1,xPlace+2) and self.surrounding(yPlace+1,xPlace+3) and self.surrounding(yPlace,xPlace+3) and self.surrounding(yPlace+2,xPlace+3):
                    attemptingPlacement = False
                    self._playerBoard[yPlace+1][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace+1][xPlace+1]=const.OCCUPIED
                    self._playerBoard[yPlace+1][xPlace+2]=const.OCCUPIED
                    self._playerBoard[yPlace+1][xPlace+3]=const.OCCUPIED
                    self._playerBoard[yPlace][xPlace+3]=const.OCCUPIED
                    self._playerBoard[yPlace+2][xPlace+3]=const.OCCUPIED
                    self.ourPlacingBoard[yPlace+1][xPlace] = 1
                    self.ourPlacingBoard[yPlace+1][xPlace+1] = 1
                    self.ourPlacingBoard[yPlace+1][xPlace+2] = 1
                    self.ourPlacingBoard[yPlace+1][xPlace+3] = 1
                    self.ourPlacingBoard[yPlace][xPlace+3] = 1
                    self.ourPlacingBoard[yPlace+2][xPlace+3] = 1
            else:
                if self.surrounding(yPlace,xPlace+1) and self.surrounding(yPlace+1,xPlace+1) and self.surrounding(yPlace+2,xPlace+1) and self.surrounding(yPlace+3,xPlace+1) and self.surrounding(yPlace+3,xPlace) and self.surrounding(yPlace+3,xPlace+2):
                    attemptingPlacement = False
                    self._playerBoard[yPlace][xPlace+1]=const.OCCUPIED
                    self._playerBoard[yPlace+1][xPlace+1]=const.OCCUPIED
                    self._playerBoard[yPlace+2][xPlace+1]=const.OCCUPIED
                    self._playerBoard[yPlace+3][xPlace+1]=const.OCCUPIED
                    self._playerBoard[yPlace+3][xPlace]=const.OCCUPIED
                    self._playerBoard[yPlace+3][xPlace+2]=const.OCCUPIED
                    self.ourPlacingBoard[yPlace][xPlace+1] = 1
                    self.ourPlacingBoard[yPlace+1][xPlace+1] = 1
                    self.ourPlacingBoard[yPlace+2][xPlace+1] = 1
                    self.ourPlacingBoard[yPlace+3][xPlace+1] = 1
                    self.ourPlacingBoard[yPlace+3][xPlace] = 1
                    self.ourPlacingBoard[yPlace+3][xPlace+2] = 1
    
    
    def perfectMatch(self,gridA,gridB):
        for x in range(7):
            for y in range(7):
                if gridA[y][x] != gridB[y][x]:
                    return False 
        return True
        
    def deDupGrids(self,grids):
        newGrids = []
        for grid in grids:
            present = False
            for includedGrid in newGrids:
                if self.perfectMatch(includedGrid,grid):
                    present = True
                    
            if present == False:
                newGrids.append(grid)
                
        return newGrids
        
    def setWeights(self,grids,weight):
        balancedGrids = []
        for grid in grids:
            balancedGrids.append(self.gridWeight(grid,weight))
            
        return balancedGrids
    
    def gridWeight(self,grid,weight):
        
        newGrid = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
        
        for x in range(7):
            for y in range(7):
                if grid[y][x] != 0:
                    newGrid[y][x] = weight
        
        return newGrid
    
    # Distribute the fleet onto your board
    def deployFleet(self):
        """
        Decide where you want your fleet to be deployed, then return your board.
        The attribute to be modified is _playerBoard. You can see how it is defined
        in the _initBoards method in the file base_player.py
        """
        self._initBoards()
        self.moveCount = 0
        self.debug = False
        
        seed(None)
        
        #Create our own placing board representation
        self.ourPlacingBoard = [[0 for x in range(16)] for x in range(16)]
        
        #Mark playable area
        for x in range(16):
            for y in range(16):
                self.ourPlacingBoard[y][x] = -1
                
        for x in range(12):
            for y in range(12):
                self.ourPlacingBoard[y][x] = 0
        
        #Mark unplacable area
        for x in range(6):
            for y in range(6):
                self.ourPlacingBoard[y][x+6] = -1
        
        
        self.ourFiringBoard = [[0 for x in range(16)] for x in range(16)]
        
        #Mark playable area
        for x in range(16):
            for y in range(16):
                self.ourFiringBoard[y][x] = 1
                
        for x in range(12):
            for y in range(12):
                self.ourFiringBoard[y][x] = 0
        
        #Mark unplacable area
        for x in range(6):
            for y in range(6):
                self.ourFiringBoard[y][x+6] = 1
        
        self.forcePlace = False
        
        # Destroyer (2 squares)
        
        self.placeDestroyer();
        
        # Cruiser (3 squares)
        self.placeCruiser();
        
        # Battleship (4 squares)
        self.placeBattleship();
        
        # Hovercraft (6 squares)
        self.placeHovercraft();
        
        # Aircraft carrier (6 squares)
        self.placeAircraftCarrier();
        
        self.sunkDestroyer = False
        self.sunkCruiser = False
        self.sunkBattleship = False
        self.sunkHovercraft = False
        self.sunkAircraftCarrier = False
        
        self.lastHit = (0,0)
        self.lockedOn = False
        self.currentState = 0
        
        self.mode = 0
        self.hit = False
        self.hitCount = 0
        
        self.countMove = 0
        
        #Create Firing Tables
        destroyerGrid = [
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
                    
        cruiserGrid = [
                [0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
                    
        battleshipGrid = [
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
                
        destroyerGridB = [
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,1,1,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
                    
        cruiserGridB = [
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,1,1,1,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
                    
        battleshipGridB = [
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,1,1,1,1],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
                    
        hovercraftGrid =  [
                [0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0],
                [0,0,0,1,1,1,0],
                [0,0,0,1,0,1,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
                
        hovercraftGridB = [
                [0,0,0,0,0,0,0],
                [0,0,0,1,1,0,0],
                [0,0,0,0,1,1,0],
                [0,0,0,1,1,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
                    
        aircraftGrid = [
                [0,0,0,0,1,0,0],
                [0,0,0,0,1,0,0],
                [0,0,0,0,1,0,0],
                [0,0,0,1,1,1,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
        
        aircraftGridB = [
                [0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,1,1,1],
                [0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
        
        aircraftGridC = [
                [0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0],
                [1,1,1,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
        
        aircraftGridD = [
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,1,1,1,0],
                 [0,0,0,0,1,0,0],
                 [0,0,0,0,1,0,0],
                 [0,0,0,0,1,0,0]]
                 
        aircraftGridE = [
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0],
                [1,1,1,1,0,0,0],
                [1,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
        
        aircraftGridF = [
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1],
                [0,0,0,1,1,1,1],
                [0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
                
        aircraftGridG = [
                [0,0,1,1,1,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
        
        aircraftGridH = [
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,1,1,1,0,0]]   
        
        destroyerGrids = [destroyerGrid,destroyerGridB]
        self.destroyerGridsAll = self.setWeights(self.deDupGrids(self.formGrids(destroyerGrids)),1.0)
        
        cruiserGrids = [cruiserGrid,cruiserGridB]
        self.cruiserGridsAll = self.setWeights(self.deDupGrids(self.formGrids(cruiserGrids)),1.0)
        
        battleshipGrids = [battleshipGrid,battleshipGridB]
        self.battleshipGridsAll = self.setWeights(self.deDupGrids(self.formGrids(battleshipGrids)),1.0)
        
        hovercraftGrids = [hovercraftGrid,hovercraftGridB]
        self.hovercraftGridsAll = self.setWeights(self.deDupGrids(self.formGrids(hovercraftGrids)),1.0)
        
        aircraftGrids = [aircraftGrid,aircraftGridB,aircraftGridC,aircraftGridD,aircraftGridE,aircraftGridF,aircraftGridG,aircraftGridH]
        self.aircraftGridsAll = self.setWeights(self.deDupGrids(self.formGrids(aircraftGrids)),1.0)
        
        self.destroyerAlive = True
        self.cruiserAlive = True
        self.battleshipAlive = True
        self.hovercraftAlive = True
        self.aircraftAlive = True
        
        self.currentHits = 0
        
        self.searchPhase = 0
        self.hits = 0
        
        self.hitsY = []
        self.hitsX = []
        
        self.Ysofar = []
        self.Xsofar = []
        
        self.searching = False
        
        return self._playerBoard
    
    def gridAdd(self, gridA, gridB):
        gridC = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
        
        for x in range(7):
            for y in range(7):
                gridC[y][x] = gridA[y][x] + gridB[y][x]
                
        return gridC
        
    def gridFlipX(self,grid):
        gridC = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
                
        for x in range(7):
            for y in range(7):
                gridC[y][x] = grid[y][6-x]
        
        return gridC
        
    def gridFlipY(self,grid):
        gridC = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
                
        for x in range(7):
            for y in range(7):
                gridC[y][x] = grid[6-y][x]
        
        return gridC
        
    def gridShiftX(self,grid,num):
        gridC = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
                
        for x in range(7):
            for y in range(7):
                gridC[y][x] = grid[y][(x+num)%7]
        
        return gridC
    
    def gridShiftY(self,grid,num):
        gridC = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
                
        for x in range(7):
            for y in range(7):
                gridC[y][x] = grid[(y+num)%7][x]
        
        return gridC
        
    def detectIntersection(self,gridA, gridB):
        for x in range(7):
            for y in range(7):
                if gridA[y][x] == 1 and gridB[y][x] == 1: #Intersection
                    return True
        return False
    
    def detectFireIntersection(self,gridB):
        for item in range(len(self.Ysofar)):
            y = self.Ysofar[item] - self.startY + 3
            x = self.Xsofar[item] - self.startX + 3
            
            if gridB[y][x] == 0:
                return False
                
        return True
    
    def gridMatch(self,localArea, grid):
        for x in range(7):
            for y in range(7):
                if grid[y][x] == 1 and localArea[y][x] != 3: #Mismatch
                    return False
        return True
        
    def formGrids(self,grids):
        moreGrids = []
        for grid in grids:
            shiftedGrids = []
            shiftedGrids.append(grid)
            for shiftX in range(7):
                for shiftY in range(7):
                    newGridXY = self.gridShiftY(self.gridShiftX(grid,shiftX),shiftY)
                    shiftedGrids.append(newGridXY)
            
            for innerGrid in shiftedGrids:
                moreGrids.append(innerGrid)
                moreGrids.append(self.gridFlipX(innerGrid))
                moreGrids.append(self.gridFlipY(innerGrid))
                moreGrids.append(self.gridFlipX(self.gridFlipY(innerGrid)))
        
        filteredGrids = []
        for grid in moreGrids:
            if grid[3][3] == 1:
                filteredGrids.append(grid)
        
        return filteredGrids
        
    
    def fireSystem(self,localarea):        
        firingGrids = []
        
        if self.destroyerAlive:
            for grid in self.destroyerGridsAll:
                firingGrids.append(grid)
                
        if self.cruiserAlive:
            for grid in self.cruiserGridsAll:
                firingGrids.append(grid)
                
        if self.battleshipAlive:
            for grid in self.battleshipGridsAll:
                firingGrids.append(grid)
                
        if self.hovercraftAlive:
            for grid in self.hovercraftGridsAll:
                firingGrids.append(grid)
                
        if self.aircraftAlive:
            for grid in self.aircraftGridsAll:
                firingGrids.append(grid)
        
        firegrid = [
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
        
        for grid in firingGrids:
            if not self.detectIntersection(localarea,grid):
                if self.searching or self.detectFireIntersection(grid):
                    firegrid = self.gridAdd(firegrid,grid)
        
        #Print Firegrid
        if self.debug:
            for line in range(7):
                print firegrid[line]
        
        #Fire in the most likely place
        maxValue = 0
        maxX = -1
        maxY = -1
        for x in range(7):
            for y in range(7):
                if localarea[y][x] == 0 and firegrid[y][x] > maxValue:
                    maxValue = firegrid[y][x]
                    maxY = y
                    maxX = x
        if maxX != -1 and maxY != -1:
            return self.startY+maxY-3,self.startX+maxX-3
        else:
            #We have destroyed a ship, what is it?
            if self.currentHits == 6:
                self.currentHits = 0
                for grid in self.hovercraftGridsAll:
                    if self.gridMatch(localarea,grid):
                        self.hovercraftAlive = False
                        self.lockedOn = False
                        #print "Hover"
                        return 14,14
                
                for grid in self.aircraftGridsAll:
                    if self.gridMatch(localarea,grid):
                        self.aircraftAlive = False
                        self.lockedOn = False
                        #print "Aircraft"
                        return 14,14
            
            if self.currentHits == 4: 
                self.currentHits = 0
                for grid in self.battleshipGridsAll:
                    if self.gridMatch(localarea,grid):
                        self.battleshipAlive = False
                        self.lockedOn = False
                        #print "Battle"
                        return 14,14
            
            if self.currentHits == 3:
                self.currentHits = 0
                for grid in self.cruiserGridsAll:
                    if self.gridMatch(localarea,grid):
                        self.cruiserAlive = False
                        self.lockedOn = False
                        #print "Cruiser"
                        return 14,14
            
            if self.currentHits == 2: 
                self.currentHits = 0       
                for grid in self.destroyerGridsAll:
                    if self.gridMatch(localarea,grid):
                        self.destroyerAlive = False
                        self.lockedOn = False
                        #print "Destroyer"
                        return 14,14
            
            if self.searching == False:
                self.lockedOn = True
                self.searching = True #Got stuck!
                
            if self.searching == True:
                self.searching = False
                self.lockedOn = False
            
            return 14,14
    
    # Decide what move to make based on current state of opponent's board and print it out
    def chooseMove(self):
        """
        """
        seed(None)
        
        if self.debug:
            print "Move: " + str(self.countMove)
            self.countMove = self.countMove + 1
        
        while self.lockedOn:
            localarea = [
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
            for y in range(7):
                for x in range(7):
                    localarea[y][x] = self.ourFiringBoard[self.startY+y-3][self.startX+x-3]
                    if self.startY+y-3 < 0 or self.startX+x-3 < 0:
                        localarea[y][x] = 1 #Out of bounds
                    
            [fireY, fireX] = self.fireSystem(localarea);
            if self.debug:
                print str(self.startY) + "," + str(self.startX)
                print "Fire information  Y: " + str(fireY) + " X: " + str(fireX) + " Status: " + str(self.ourFiringBoard[fireY][fireX])
            if self.ourFiringBoard[fireY][fireX] == 0:
                return fireY, fireX
        
        #Random Fire
        decidingFireMove = True
        timeout = False
        attemptToPlace = 0
        
        while decidingFireMove:
            xPlace = randint(0,11)
            yPlace = randint(0,11)
            attemptToPlace = attemptToPlace + 1 #Emergency Fallback
            if attemptToPlace > 10000:
                timeout = True
            
            if ((xPlace + yPlace) % 2 == 0 or timeout) and self.ourFiringBoard[yPlace][xPlace] == 0:
                return yPlace, xPlace


    def setOutcome(self, entry, row, col):
        """
        entry: the outcome of your shot onto your opponent,
               expected value is const.HIT for hit and const.MISSED for missed.
        row: (int) the board row number (e.g. row A is 0)
        col: (int) the board column (e.g. col 2 is represented by  value 3) so A3 case is (0,2)
        """

        is_valid = False
        if entry == const.HIT:
            is_valid = True
            Outcome = const.HIT
            self.ourFiringBoard[row][col] = 3
                  
            self.lastHit = (row,col)
            self.hit = True
            
            self.currentHits = self.currentHits + 1
            
            self.Ysofar.append(row)
            self.Xsofar.append(col)
            
            if self.lockedOn == False:
                self.lockedOn = True
                self.searching = False
                self.currentHits = 1
                self.currentState = 0
                self.startY = row
                self.startX = col
                
                self.Ysofar = [row]
                self.Xsofar = [col]
                
        elif entry == const.MISSED:
            is_valid = True
            self.hit = False
            self.ourFiringBoard[row][col] = 1
            Outcome = const.MISSED
        else:
            raise Exception("Invalid input!")
        self._opponenBoard[row][col]=Outcome

    def getOpponentMove(self, row, col):
        """ You might like to keep track of where your opponent
        has missed, but here we just acknowledge it. Note case A3 is
        represented as row = 0, col = 2.
        """
        
        if ((self._playerBoard[row][col]==const.OCCUPIED)
            or (self._playerBoard[row][col]==const.HIT)):
            # They may (stupidly) hit the same square twice so we check for occupied or hit
            self._playerBoard[row][col]=const.HIT
            result =const.HIT
        else:
            # You might like to keep track of where your opponent has missed, but here we just acknowledge it
            result = const.MISSED
        return result



def getPlayer():
    """ MUST NOT be changed, used to get a instance of your class."""
    return Player()