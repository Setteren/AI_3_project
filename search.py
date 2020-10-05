# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from memory_profiler import memory_usage

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

##Helpers
def getCourse(start, end):
    from game import Directions

    [dx, dy] = [end[0] - start[0], end[1] - start[1]]
    direction = None

    if dy == 0 and dx > 0:
        direction = Directions.EAST
    elif dy == 0 and dx < 0:
        direction = Directions.WEST
    elif dx == 0 and dy > 0:
        direction = Directions.NORTH
    elif dx == 0 and dy < 0:
        direction = Directions.SOUTH

    return direction

def recDFS(start, visited, stack_directions, problem):

    if start == problem.goal:
        return True


    visited.append(start)
 
    neighbours = problem.getSuccessors(start)
    for nb in neighbours:
        if nb[0] not in visited:
            if recDFS(nb[0], visited, stack_directions, problem) == True:
                stack_directions.push(nb[1])
                return True
    return False

def showOfChecked(visited):
    import __main__
    __main__.__dict__['_display'].drawExpandedCells(visited)
    
def pathBuilder(goal, explored):
    node = explored[goal]
    pathesP = [goal]
    while not node['prev'] == None:
        pathesP.append(node['prev'])
        node = explored[node['prev']]
    pathesP = pathesP[::-1]
    return pathesP

def reconstructPath(visited, problem):
    start = problem.getStartState()
    [pathesP, neighbours, last] = [[],[], None]
    for elem in visited[::-1]:
        if start in neighbours:
            pathesP.append(start)
            break
        if elem in neighbours or neighbours == []:
                last = elem
                pathesP.append(last)
                neighbours = [x[0] for x in problem.getSuccessors(last)]

    pathesP = pathesP[::-1]
    return pathesP

def getR(pathesP, problem):
    route = []
    start = pathesP[0]
    for pt in pathesP[1:]:
        course = getCourse(start, pt)
        start = pt
        route.append(course)
    return route


def depthFirstSearch(problem, recursive = True):
    visited = []

    start = problem.getStartState()

    route = []

    if recursive:

        stack_directions = util.Stack()

        recDFS(start, visited, stack_directions, problem)

        route = stack_directions.list[::-1]
    else:
        stack = util.Stack()
        stack.push(start)
        while not stack.isEmpty():
            vertex = stack.pop()
            visited.append(vertex)
            if vertex == problem.goal:
                break
            neighbours = problem.getSuccessors(vertex)
            for nb in neighbours:
                if nb[0] not in visited:
                    stack.push(nb[0])

        pathesP = reconstructPath(visited, problem)
        route = getR(pathesP, problem)

    showOfChecked(visited)

    return route

def breadthFirstSearch(problem):
    queue = util.Queue()
    visited = []
    queue.push(problem.getStartState())

    while not queue.isEmpty():
        vertex = queue.pop()
        visited.append(vertex)
        if vertex == problem.goal:
            break
        neighbours = problem.getSuccessors(vertex)
        for nb in neighbours:
            if nb[0] not in visited:
                queue.push(nb[0])

    pathesP = reconstructPath(visited, problem)
    path = getR(pathesP, problem)

    showOfChecked(visited)
    return path
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
