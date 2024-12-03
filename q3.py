"""def count_common_faces(q, queries):
    directions = {
        "top": (-1, 0, 0),
        "down": (1, 0, 0),
        "left": (0, -1, 0),
        "right": (0, 1, 0),
        "front": (0, 0, 1),
        "back": (0, 0, -1)
    }

    # Initialize a 3D array to store cube positions
    cube_grid = [[[None for _ in range(101)] for _ in range(101)] for _ in range(101)]]
    cube_positions = {}

    for query in queries:
        cube_a, cube_b, direction = query.split()
        cube_a, cube_b = int(cube_a), int(cube_b)
        dx, dy, dz = directions[direction]

        # Get the current position of cube_a
        x, y, z = cube_positions.get(cube_a, (0, 0, 0))

        # Calculate the new position of cube_b
        new_x, new_y, new_z = x + dx, y + dy, z + dz

        # Update cube positions in the grid and dictionary
        cube_grid[new_x][new_y][new_z] = cube_b
        cube_positions[cube_b] = (new_x, new_y, new_z)

    # Count common faces by iterating through the grid
    common_faces = 0
    for x in range(101):
        for y in range(101):
            for z in range(101):
                cube = cube_grid[x][y][z]
                if cube:
                    for dx, dy, dz in directions.values():
                        neighbor_x, neighbor_y, neighbor_z = x + dx, y + dy, z + dz
                        if 0 <= neighbor_x < 101 and 0 <= neighbor_y < 101 and 0 <= neighbor_z < 101:
                            neighbor = cube_grid[neighbor_x][neighbor_y][neighbor_z]
                            if neighbor:
                                common_faces += 1

    return common_faces // 2

# Input
q = int(input())
queries = [input().strip() for _ in range(q)]

# Output the result
print(count_common_faces(q, queries))"""


# Function to calculate common cube faces
def count_common_faces(Q, queries):
    # Dictionary to store adjacency information for each cube
    adj = {
        i: {'left': None, 'right': None, 'top': None, 'down': None} for i in range(1, Q+2)
    }

    # Process each query
    for query in queries:
        cubeA, cubeB, direction = query
        if direction == 'right':
            adj[cubeA]['right'] = cubeB
            adj[cubeB]['left'] = cubeA
        elif direction == 'left':
            adj[cubeA]['left'] = cubeB
            adj[cubeB]['right'] = cubeA
        elif direction == 'top':
            adj[cubeA]['top'] = cubeB
            adj[cubeB]['down'] = cubeA
        elif direction == 'down':
            adj[cubeA]['down'] = cubeB
            adj[cubeB]['top'] = cubeA
    
    # Count the number of common faces
    common_faces = 0
    
    # Iterate over each cube and check its adjacent cubes
    for i in range(1, Q+2):
        for direction in ['left', 'right', 'top', 'down']:
            adjacent_cube = adj[i][direction]
            if adjacent_cube is not None:
                common_faces += 1

    return common_faces


# Reading input
Q = int(input())  # number of queries
queries = [input().split() for _ in range(Q)]  # list of queries

# Convert the queries to the appropriate format (cubeA, cubeB, direction)
queries = [(int(query[0]), int(query[1]), query[2]) for query in queries]

# Get the result
result = count_common_faces(Q, queries)

# Print the result
print(result)



