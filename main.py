import random

def print_maze(maze):
    for row in maze:
        print('+' + '+'.join(['---'] * len(row)) + '+')
        print('| ' + ' | '.join(row) + ' |')
    print('+' + '+'.join(['---'] * len(row)) + '+')

def initialize_maze(size):
    return [[' ' for _ in range(size)] for _ in range(size)]

def place_walls(maze, wall_prob=0.3):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (i == 0 and j == 0) or (i == len(maze) - 1 and j == len(maze[i]) - 1):
                continue  # Skip the start and end points
            if random.random() < wall_prob:
                maze[i][j] = 'X'

def solve_maze_util(maze, x, y, path, visited):
    if not (0 <= x < len(maze) and 0 <= y < len(maze[0])) or maze[x][y] == 'X' or visited[x][y]:
        return False

    path.append((x, y))
    visited[x][y] = True  # Mark this cell as visited

    if x == len(maze) - 1 and y == len(maze[0]) - 1:  # Found the end
        return True

    # Explore neighbors
    if solve_maze_util(maze, x + 1, y, path, visited):  # Move down
        return True
    if solve_maze_util(maze, x, y + 1, path, visited):  # Move right
        return True
    if solve_maze_util(maze, x - 1, y, path, visited):  # Move up
        return True
    if solve_maze_util(maze, x, y - 1, path, visited):  # Move left
        return True

    path.pop()
    visited[x][y] = False
    return False

def solve_maze(maze):
    path = []
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    if not solve_maze_util(maze, 0, 0, path, visited):
        print("No solution exists!")
    else:
        for x, y in path:
            if maze[x][y] != 'S' and maze[x][y] != 'E':
                maze[x][y] = '*'
    return path

def main():
    while True:
        try:
            size = int(input("Enter the size of the maze (n x n): "))
            if size < 1 or size > 10:
                print("Size must be between 1 and 10.")
                continue
        except ValueError:
            print("Please enter a valid integer for maze size.")
            continue

        maze = initialize_maze(size)
        maze[0][0] = 'S'  # Start
        maze[size-1][size-1] = 'E'  # End
        place_walls(maze)
        print("Generated Maze:")
        print_maze(maze)

        choice = input("1. Print the path\n2. Generate another puzzle\n3. Exit the Game\nEnter your choice (1/2/3): ")

        if choice == '1':
            path = solve_maze(maze)
            if path:
                print("Maze with Path:")
                print_maze(maze)
        elif choice == '2':
            continue
        elif choice == '3':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()