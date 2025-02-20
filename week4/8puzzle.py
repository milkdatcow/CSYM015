class Node:
    def __init__(self, data, level, fval):
        """Initialize the node with the data, level (g), and f-value (f = g + h)."""
        self.data = data
        self.level = level  # g(n): depth in the search tree
        self.fval = fval    # f(n) = g(n) + h(n)

    def generate_child(self):
        """Generate child nodes by moving the blank space in four directions."""
        x, y = self.find(self.data, '_')
        val_list = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]  # left, right, up, down
        children = []
        for new_x, new_y in val_list:
            child = self.shuffle(self.data, x, y, new_x, new_y)
            if child is not None:
                child_node = Node(child, self.level + 1, 0)  # fval will be set later
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        """Move the blank space to the new position if valid."""
        if 0 <= x2 < len(puz) and 0 <= y2 < len(puz):
            temp_puz = self.copy(puz)
            temp_puz[x2][y2], temp_puz[x1][y1] = temp_puz[x1][y1], temp_puz[x2][y2]
            return temp_puz
        return None

    def copy(self, root):
        """Create a deep copy of the puzzle matrix."""
        return [row[:] for row in root]

    def find(self, puz, x):
        """Find the position of the blank space ('_')."""
        for i in range(len(puz)):
            for j in range(len(puz)):
                if puz[i][j] == x:
                    return i, j
        return None  # Shouldn't happen if '_' exists

class Puzzle:
    def __init__(self, size):
        """Initialize the puzzle with size, open list, and closed list."""
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        """Accept puzzle input from the user with basic validation."""
        puz = []
        print(f"Enter {self.n} rows of {self.n} space-separated values (use '_' for blank):")
        for i in range(self.n):
            while True:
                try:
                    row = input(f"Row {i}: ").strip().split()
                    if len(row) == self.n:
                        puz.append(row)
                        break
                    print(f"Invalid: Enter exactly {self.n} values.")
                except Exception:
                    print("Invalid input. Try again.")
        return puz

    def f(self, start, goal):
        """Calculate f(n) = h(n) + g(n)."""
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        """Heuristic: Number of misplaced tiles (excluding blank)."""
        return sum(1 for i in range(self.n) for j in range(self.n)
                   if start[i][j] != goal[i][j] and start[i][j] != '_')

    def process(self):
        """Solve the puzzle using A* search."""
        print("Enter the start state matrix")
        start = self.accept()
        print("Enter the goal state matrix")
        goal = self.accept()

        # Initialize start node
        start_node = Node(start, 0, 0)
        start_node.fval = self.f(start_node, goal)
        self.open.append(start_node)

        while self.open:
            # Get node with lowest f-value
            cur = min(self.open, key=lambda x: x.fval)
            self.open.remove(cur)

            # Print current state
            print("\nCurrent state:")
            for row in cur.data:
                print(" ".join(row))

            # Check if goal is reached
            if self.h(cur.data, goal) == 0:
                print(f"\nGoal reached in {cur.level} moves!")
                break

            # Generate and process children
            for child in cur.generate_child():
                child_state = tuple(map(tuple, child.data))  # Convert to tuple for hashing
                if child_state not in [tuple(map(tuple, n.data)) for n in self.closed]:
                    child.fval = self.f(child, goal)
                    self.open.append(child)

            self.closed.append(cur)

            if not self.open:
                print("No solution exists!")
                break

        else:
            print("No solution exists!")

# Run the puzzle solver for 3x3
if __name__ == "__main__":
    puz = Puzzle(3)
    puz.process()