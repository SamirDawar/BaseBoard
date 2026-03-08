"""
AI Routing Engine
Implements pathfinding algorithms for PCB trace routing
"""

import numpy as np
from typing import List, Tuple, Optional

class PCBRouter:
    """AI-powered PCB trace routing"""
    
    def __init__(self, board_width, board_height, grid_resolution=0.1):
        """
        Initialize router
        
        Args:
            board_width: Board width in mm
            board_height: Board height in mm
            grid_resolution: Grid size in mm (smaller = more accurate but slower)
        """
        self.width = board_width
        self.height = board_height
        self.resolution = grid_resolution
        
        # Create occupancy grid
        self.grid_w = int(board_width / grid_resolution)
        self.grid_h = int(board_height / grid_resolution)
        self.grid = np.zeros((self.grid_h, self.grid_w), dtype=int)
        
    def add_obstacle(self, x, y, width, height):
        """Mark area as occupied (pads, existing traces, etc.)"""
        x1 = int(x / self.resolution)
        y1 = int(y / self.resolution)
        x2 = int((x + width) / self.resolution)
        y2 = int((y + height) / self.resolution)
        
        self.grid[y1:y2, x1:x2] = 1
    
    def route(self, start: Tuple[float, float], end: Tuple[float, float], 
              trace_width: float = 0.25) -> Optional[List[Tuple[float, float]]]:
        """
        Find route between two points using A* algorithm
        
        Args:
            start: (x, y) starting point in mm
            end: (x, y) ending point in mm
            trace_width: Trace width in mm
            
        Returns:
            List of (x, y) waypoints or None if no route found
        """
        # Convert to grid coordinates
        start_grid = (int(start[0] / self.resolution), int(start[1] / self.resolution))
        end_grid = (int(end[0] / self.resolution), int(end[1] / self.resolution))
        
        # TODO: Implement A* pathfinding
        # For now, return straight line
        return [start, end]
    
    def calculate_cost(self, path: List[Tuple[float, float]]) -> dict:
        """Calculate routing metrics"""
        if not path or len(path) < 2:
            return {"length": 0, "vias": 0, "turns": 0}
        
        # Calculate total length
        length = 0
        turns = 0
        for i in range(len(path) - 1):
            dx = path[i+1][0] - path[i][0]
            dy = path[i+1][1] - path[i][1]
            length += np.sqrt(dx*dx + dy*dy)
            
            # Count direction changes
            if i > 0:
                prev_dx = path[i][0] - path[i-1][0]
                prev_dy = path[i][1] - path[i-1][1]
                if (dx * prev_dx + dy * prev_dy) < 0.99:  # Not same direction
                    turns += 1
        
        return {
            "length": round(length, 2),
            "vias": 0,  # TODO: Calculate layer changes
            "turns": turns
        }


if __name__ == "__main__":
    # Test router
    router = PCBRouter(100, 100)  # 100mm x 100mm board
    
    # Add some obstacles
    router.add_obstacle(40, 40, 20, 20)
    
    # Find route
    path = router.route((10, 10), (90, 90))
    metrics = router.calculate_cost(path)
    
    print(f"Route found: {len(path)} points")
    print(f"Metrics: {metrics}")
