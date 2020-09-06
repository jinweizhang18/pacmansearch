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

def directionHelper(string):
    assert string == ("South" or "North" or "East" or "West")
    if string == "South":
        return Directions.SOUTH
    elif string == "North":
        return Directions.NORTH
    elif string == "East":
        return Directions.EAST
    else:
        return Directions.WEST

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    if problem.isGoalState(problem.getStartState()):
        return []
    closed = []
    closed.append(problem.getStartState())
    fringe = util.Stack() # A fringe of paths, a path is a list of states
    for successor in problem.getSuccessors(problem.getStartState()):
        fringe.push([list(successor)])

    while(1):
        if fringe.isEmpty():
            return None
        curr_path = fringe.pop() #[(A, A->B:4, 4), [B, B->C:0, 4]]
        curr_state = curr_path[len(curr_path) - 1][0]
        #print("curr path:", curr_path, "\ncurr state: ", curr_state, "\n")
        if problem.isGoalState(curr_state):
            actions = []
            for triple in curr_path:
                actions.append(triple[1])
            return actions
        if curr_state not in closed:
            closed.append(curr_state)
            for successor in problem.getSuccessors(curr_state):
                new_path = curr_path + [list(successor)]
                #print("np:", new_path)
                fringe.push(new_path)

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    if problem.isGoalState(problem.getStartState()):
        return []
    closed = []
    closed.append(problem.getStartState())
    fringe = util.Queue() # A fringe of paths, a path is a list of states
    for successor in problem.getSuccessors(problem.getStartState()):
        fringe.push([list(successor)])

    while(1):
        if fringe.isEmpty():
            return None
        curr_path = fringe.pop() #[(A, A->B:4, 4), [B, B->C:0, 4]]
        curr_state = curr_path[len(curr_path) - 1][0]
        #print("curr path:", curr_path, "\ncurr state: ", curr_state, "\n")
        if problem.isGoalState(curr_state):
            actions = []
            for triple in curr_path:
                actions.append(triple[1])
            return actions
        if curr_state not in closed:
            closed.append(curr_state)
            for successor in problem.getSuccessors(curr_state):
                new_path = curr_path + [list(successor)]
                #print("np:", new_path)
                fringe.push(new_path)
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    if problem.isGoalState(problem.getStartState()):
        return []
    closed = []
    closed.append(problem.getStartState())
    fringe = util.PriorityQueue() # A fringe of paths, a path is a list of states
    for successor in problem.getSuccessors(problem.getStartState()):
        #print([list(successor)], list(successor)[2])
        fringe.push([list(successor)], list(successor)[2])

    while(1):
        if fringe.isEmpty():
            return None
        curr_path = fringe.pop() #[(A, A->B:4, 4), [B, B->C:0, 4]]
        curr_state = curr_path[len(curr_path) - 1][0]
        #print("curr path:", curr_path, "\ncurr state: ", curr_state, "\n")
        if problem.isGoalState(curr_state):
            actions = []
            for triple in curr_path:
                actions.append(triple[1])
            return actions
        if curr_state not in closed:
            closed.append(curr_state)
            for successor in problem.getSuccessors(curr_state):
                new_path = curr_path + [list(successor)]
                new_path_cost = list(successor)[2]
                for element in curr_path:
                    new_path_cost += element[2]
                fringe.push(new_path, new_path_cost)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    if problem.isGoalState(problem.getStartState()):
        return []
    closed = []
    closed.append(problem.getStartState())
    fringe = util.PriorityQueue() # A fringe of paths, a path is a list of states
    for successor in problem.getSuccessors(problem.getStartState()):
        #print([list(successor)], list(successor)[2])
        fringe.push([list(successor)], list(successor)[2] + heuristic(list(successor)[0],problem))

    while(1):
        if fringe.isEmpty():
            return None
        curr_path = fringe.pop() #[(A, A->B:4, 4), [B, B->C:0, 4]]
        curr_state = curr_path[len(curr_path) - 1][0]
        #print("curr path:", curr_path, "\ncurr state: ", curr_state, "\n")
        if problem.isGoalState(curr_state):
            actions = []
            for triple in curr_path:
                actions.append(triple[1])
            return actions
        if curr_state not in closed:
            closed.append(curr_state)
            for successor in problem.getSuccessors(curr_state):
                new_path = curr_path + [list(successor)]
                new_path_cost = list(successor)[2] + heuristic(list(successor)[0],problem)
                for element in curr_path:
                    new_path_cost += element[2]
                fringe.push(new_path, new_path_cost)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
