class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Map to store the original node -> cloned node mapping
        visited = {}

        # Initialize the queue for BFS
        queue = deque([node])
        # Create the clone of the first node
        visited[node] = Node(node.val)

        # BFS traversal
        while queue:
            curr = queue.popleft()

            # Iterate through all the neighbors of the current node
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and add it to the visited map
                    visited[neighbor] = Node(neighbor.val)
                    # Add the neighbor to the queue for further processing
                    queue.append(neighbor)

                # Get the clone of the current node
                cloned_node = visited[curr]

                # Get the clone of the neighbor node
                cloned_neighbor = visited[neighbor]

                # Link the cloned neighbor to the cloned node
                cloned_node.neighbors.append(cloned_neighbor)

        # Return the cloned graph starting point
        return visited[node]
