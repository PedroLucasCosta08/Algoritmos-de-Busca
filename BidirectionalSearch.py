def bidirectional_heuristic_search(agent, maze, goal):
    def manhattan_distance(pos, goal):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
    
    def get_neighbors(position):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # up, down, left and right
        neighbors = []
        for dx, dy in directions:
            nx, ny = position[0] + dx, position[1] + dy
            if 0 <= nx < maze.rows and 0 <= ny < maze.columns and maze.grid[nx][ny] == 1: #valid or not
                neighbors.append((nx, ny))                  
        return neighbors
    
    def insert_priority(queue, position, priority):
        queue.append((priority, position))
        queue.sort(key=lambda x: x[0])  # shortest distance first
    
    def reconstruct_path(front_visited, back_visited, meet_point):
        path = []
        
        # meeting point to begning
        current = meet_point
        while current:
            path.append(current)
            current = front_visited.get(current)
        path.reverse()
        
        # meeting point to goal
        current = back_visited.get(meet_point)
        while current:
            path.append(current)
            current = back_visited.get(current)
        
        return path
    start = tuple(agent.current_position)
    goal = tuple(goal)

    front_open = []
    back_open = []
    front_visited = {start: None}
    back_visited = {goal: None}
    
    insert_priority(front_open, start, manhattan_distance(start, goal))
    insert_priority(back_open, goal, manhattan_distance(goal, start))
    
    while front_open and back_open:
        _, current_front = front_open.pop(0)
        if current_front in back_visited:
            return reconstruct_path(front_visited, back_visited, current_front)
        
        for neighbor in get_neighbors(current_front):
            if neighbor not in front_visited:
                front_visited[neighbor] = current_front
                insert_priority(front_open, neighbor, manhattan_distance(neighbor, goal))

        _, current_back = back_open.pop(0)
        if current_back in front_visited:
            return reconstruct_path(front_visited, back_visited, current_back)
        
        for neighbor in get_neighbors(current_back):
            if neighbor not in back_visited:
                back_visited[neighbor] = current_back
                insert_priority(back_open, neighbor, manhattan_distance(neighbor, start))
    
    return None  # didnt find a way