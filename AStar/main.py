import cv2
import numpy as np

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0  # Cost from start to this node
        self.h = 0  # Heuristic (estimated cost from this node to the goal)
        self.f = 0  # Total cost (f = g + h)

    def __eq__(self, other):
        # Compare the position of the nodes for equality
        return self.position == other.position

    def __hash__(self):
        # We need to override __hash__ to make the Node objects hashable, 
        # which is required when using them in sets or as keys in dictionaries
        return hash(self.position)


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed lists (using sets for fast membership checking)
    open_list = set([start_node])
    closed_list = set()

    # Loop until you find the end
    while open_list:

        # Get the current node (node with the lowest f value)
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed_list.add(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children (neighbors of the current node)
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if not (0 <= node_position[0] < len(maze)) or not (0 <= node_position[1] < len(maze[0])):
                continue

            # Make sure walkable terrain (0 means open space, 1 means obstacle)
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append to children list
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list (already evaluated)
            if child in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list and has a higher g value
            if child in open_list and child.g > min(open_list, key=lambda node: node.g).g:
                continue

            # Add the child to the open list
            open_list.add(child)

    return None  # If no path found


def main():
    # Reading the image (in this case, a simple maze image)
    image = cv2.imread('image.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, biner_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)

    # Convert to binary (0 = walkable, 1 = obstacle)
    maze_map = np.array(biner_image) // 255
    print("Maze map:")
    print(maze_map)

    # Define start and end points (these can also be determined from the image)
    start = (0, 0)  # Starting position in the maze
    end = (7, 5)    # Goal position in the maze

    print("Posisi yang diminta ", maze_map[5][5])

    # Call the A* function
    path = astar(maze_map, start, end)
    if path:
        print("Path found:", path)

        # Visualizing the path on the original image
        for i in range(len(path) - 1):
            # Get the current and next point in the path
            start_point = (path[i][1], path[i][0])  # Convert (x, y) to pixel coordinates
            end_point = (path[i+1][1], path[i+1][0])

            # Draw a line between the two points
            cv2.line(image, start_point, end_point, (0, 255, 0), 1)  # Green line with 1-pixel thickness

        # Draw the start and end points as single pixels (1x1)
        cv2.circle(image, (start[1], start[0]), 0, (255, 0, 0), -1)  # Blue circle for start (1-pixel)
        cv2.circle(image, (end[1], end[0]), 0, (0, 0, 255), -1)  # Red circle for end (1-pixel)

        resized_image = cv2.resize(image, (image.shape[1] * 40, image.shape[0] * 40), interpolation=cv2.INTER_NEAREST)

        # Show the image with the path
        cv2.imshow("Pathfinding Result", resized_image)
        cv2.waitKey(0)  # Wait for a key press to close the window
        cv2.destroyAllWindows()
    else:
        print("No path found")

if __name__ == '__main__':
    main()
