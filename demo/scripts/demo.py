#!/usr/bin/env python3
"""
KiCad AI Demo - Main Demo Script
Shows AI routing in action
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from kicad_parser import KiCadPCBParser
from ai_engine import PCBRouter


def run_demo():
    """Run the routing demo"""
    print("=" * 60)
    print("KiCad AI Routing Demo - Spring Break Project")
    print("=" * 60)
    print()
    
    # Step 1: Create a simple router
    print("Step 1: Initializing AI router...")
    router = PCBRouter(board_width=100, board_height=75, grid_resolution=0.5)
    print(f"  Board size: 100mm x 75mm")
    print(f"  Grid resolution: 0.5mm")
    print()
    
    # Step 2: Add some obstacles (simulating existing components)
    print("Step 2: Adding obstacles (components, existing traces)...")
    router.add_obstacle(30, 30, 15, 10)  # Component 1
    router.add_obstacle(60, 40, 20, 15)  # Component 2
    print(f"  Added 2 component obstacles")
    print()
    
    # Step 3: Route a trace
    print("Step 3: Routing trace with AI...")
    start_point = (10, 10)
    end_point = (90, 65)
    print(f"  From: {start_point}")
    print(f"  To: {end_point}")
    
    path = router.route(start_point, end_point, trace_width=0.25)
    
    if path:
        print(f"   Route found with {len(path)} waypoints")
        metrics = router.calculate_cost(path)
        print()
        print("  Routing Metrics:")
        print(f"    Total length: {metrics['length']} mm")
        print(f"    Turns: {metrics['turns']}")
        print(f"    Vias: {metrics['vias']}")
    else:
        print(f"   No route found")
    
    print()
    print("=" * 60)
    print("Demo complete!")
    print()
    print("Next steps:")
    print("  1. Implement full A* pathfinding")
    print("  2. Parse real KiCad PCB files")
    print("  3. Visualize routes with matplotlib")
    print("  4. Add KiCad IPC API integration")
    print("=" * 60)


if __name__ == "__main__":
    run_demo()
