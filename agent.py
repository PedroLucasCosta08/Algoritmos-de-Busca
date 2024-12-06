import deepSearch as ds
import wideSearch as ws
import BidirectionalSearch as bs

class Agent: 
    ## constructor
    def __init__(self, search, starting_position):
        self.search = search
        self.current_position = starting_position
        self.numSteps = 0

    def set_numSteps(self, numsteps):
        self.numSteps = numsteps

    def set_current_pos(self, position):
        self.current_position = position

    def reached_objective(self, objective):
        return self.current_position[0] == objective[0] and self.current_position[1] == objective[1]

    def run(self, maze, goal_position):
        if self.search == 'wide search':
            path = ws.wide_search(self, maze, goal_position)
        if self.search == 'deep search':
            path = ds.deep_search(self, maze, goal_position)
        if self.search == 'bidirectional search':
            path = bs.bidirectional_heuristic_search(self, maze, goal_position)

        return path
    
    