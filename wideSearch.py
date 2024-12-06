import agent as ag
import maze as mz

def wide_search(agent, maze, goal_position):
    visited = []
    queue = [tuple(agent.current_position)]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            agent.set_current_pos(node)
            if agent.reached_objective(goal_position):
                return visited
            else:
                # above                   y                             x
                if maze.valid_or_not(agent.current_position[0] - 1, agent.current_position[1]) and (agent.current_position[0] - 1, agent.current_position[1]) not in visited:
                    queue.append(tuple([agent.current_position[0] - 1, agent.current_position[1]]))
                # left 
                if maze.valid_or_not(agent.current_position[0], agent.current_position[1] - 1) and (agent.current_position[0], agent.current_position[1] - 1) not in visited:
                    queue.append(tuple([agent.current_position[0], agent.current_position[1] - 1]))
                # right
                if maze.valid_or_not(agent.current_position[0], agent.current_position[1] + 1) and (agent.current_position[0], agent.current_position[1] + 1) not in visited:
                    queue.append(tuple([agent.current_position[0], agent.current_position[1] + 1]))
                # down
                if maze.valid_or_not(agent.current_position[0] + 1, agent.current_position[1]) and (agent.current_position[0] + 1, agent.current_position[1]) not in visited:
                    queue.append(tuple([agent.current_position[0] + 1, agent.current_position[1]]))    